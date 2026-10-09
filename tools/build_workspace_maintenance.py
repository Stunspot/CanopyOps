#!/usr/bin/env python3
"""Create a separate maintenance candidate from the accepted current workspace."""
from __future__ import annotations
import argparse
import importlib.util
import json
import shutil
from pathlib import Path
import build_workspace_release as kit

REPO = Path(__file__).resolve().parents[1]
BASELINE = REPO / "releases" / "v0.3.0"
CANDIDATES = REPO / "release-candidates"


def target_path(value: str) -> Path:
    target = Path(value).resolve()
    if target.parent != CANDIDATES.resolve() or target.name in {"", ".", ".."}:
        raise ValueError("Output must be a new direct child of release-candidates")
    if target.exists() or target.is_symlink():
        raise ValueError("Output already exists; preserve it and choose a new candidate")
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        target = target_path(args.output)
    except ValueError as error:
        parser.error(str(error))
    if not BASELINE.is_dir():
        parser.error("Accepted current v0.3.0 payload is missing")
    # Never delete or reconstruct the accepted release from an older version.
    target.parent.mkdir(exist_ok=True)
    shutil.copytree(BASELINE, target, ignore=shutil.ignore_patterns(
        "CanopyOps-v0.3.0.zip", "CanopyOps-v0.3.0.zip.sha256", "receipt.json",
        "verification-report.json", "__pycache__", "*.pyc", "*.pyo"))
    skill = target / "codex/canopyops/skills/canopyops"
    shutil.copy2(REPO / "canopyops/workspace/WORKSPACE-GUIDE.md", skill / "workspace/WORKSPACE-GUIDE.md")
    for topic in ("INSTALL-CODEX.md", "QUICK-START.md", "MAINTAINER-GUIDE.md", "PROVENANCE.md"):
        shutil.copy2(REPO / "release-docs/workspace" / topic, target / "docs" / topic)
    shutil.copy2(REPO / "delivery-sidecars/CanopyOps v0.3.0 Extra.md", target / "delivery-sidecars/CanopyOps v0.3.0 Extra.md")
    # Container metadata is preserved for compatibility; installation uses the complete skill.
    claude = target / "claude/canopyops-v0.3.0.zip"
    kit.zip_tree(claude, skill)
    manifest = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
    manifest["source_records"] = [{"handle": "canopyops", "files": kit.file_records(skill)}]
    manifest["claude_archives"] = [{"handle": "canopyops", "file": "claude/" + claude.name, "sha256": kit.digest(claude)}]
    manifest["delivery_sidecars"] = {"path": "delivery-sidecars", "files": kit.file_records(target / "delivery-sidecars")}
    manifest["current_delivery"] = "Portable crop workspace and complete skills; plugin installation is not required."
    kit.dump(target / "manifest.json", manifest)
    verifier = kit.verifier_at(target / "tools/verify_release.py")
    report = verifier.verify(target)
    if not report["ok"]:
        print(json.dumps(report, indent=2))
        return 1
    kit.dump(target / "verification-report.json", report)
    archive = target.parent / (target.name + "-CanopyOps-v0.3.0.zip")
    if archive.exists():
        raise SystemExit("Candidate archive exists; refusing replacement")
    kit.zip_tree(archive, target, "canopyops-v0.3.0")
    checksum = kit.digest(archive)
    archive.with_suffix(archive.suffix + ".sha256").write_text(
        checksum + "  " + archive.name + "\n", encoding="utf-8", newline="\n")
    kit.dump(target / "maintenance-build-receipt.json", {
        "baseline": "accepted portable v0.3.0", "version": "0.3.0",
        "archive": str(archive), "sha256": checksum,
        "claim": "Static candidate package; no installation, activation or field outcome claim."})
    print(json.dumps({"archive": str(archive), "sha256": checksum, "verification": report}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
