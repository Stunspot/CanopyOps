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
    try: target = target_path(args.output)
    except ValueError as error: parser.error(str(error))
    if not BASELINE.is_dir(): parser.error("Accepted current v0.3.0 payload is missing")
    version="0.3.1"
    shutil.copytree(BASELINE,target,ignore=shutil.ignore_patterns("CanopyOps-v0.3.0.zip","CanopyOps-v0.3.0.zip.sha256","receipt.json","verification-report.json","__pycache__","*.pyc","*.pyo"))
    skill=target/"codex/canopyops/skills/canopyops"
    # Preserve all accepted runtime bodies except the finite authored desk additions.
    for name in ["desk.py","index.html","README.md","WORKSPACE-GUIDE.md","create_entry.py","canopyops-icon.png","canopyops.ico","canopyops.icns"]:
        shutil.copy2(REPO/"canopyops/workspace"/name,skill/"workspace"/name)
    for topic in ("INSTALL-CODEX.md","QUICK-START.md","MAINTAINER-GUIDE.md","PROVENANCE.md","PACKAGE-REFERENCE.md","SUPPORT.md","README.md"):
        shutil.copy2(REPO/"release-docs/workspace"/topic,target/"docs"/topic)
    for p in (target/"docs").glob("*.md"):
        raw=p.read_bytes().replace(b"v0.3.0.zip",b"v0.3.1.zip").replace(b"releases/v0.3.0",b"releases/v0.3.1")
        p.write_bytes(raw)
    # Current optional entry procedure is a bounded addition; old cultivation evidence stays unchanged.
    p=target/"OPEN-THE-CROP-DESK.md"
    raw=(REPO/"canopyops/workspace/README.md").read_bytes().replace(b"(SKINS.md)",b"(codex/canopyops/skills/canopyops/workspace/SKINS.md)").replace(b"(WORKSPACE-GUIDE.md)",b"(codex/canopyops/skills/canopyops/workspace/WORKSPACE-GUIDE.md)")
    p.write_bytes(raw+b"\nThe installed desk is under `codex/canopyops/skills/canopyops/workspace/`.\n")
    for name in ("CanopyOps v0.3.0.md","CanopyOps v0.3.0 Extra.md"):
        oldpath=target/"delivery-sidecars"/name
        if oldpath.exists():oldpath.unlink()
    for name in ("CanopyOps.png","CanopyOps v0.3.1.md","CanopyOps v0.3.1 Extra.md"):
        shutil.copy2(REPO/"delivery-sidecars"/name,target/"delivery-sidecars"/name)
    plugin_path=target/"codex/canopyops/.codex-plugin/plugin.json"
    plugin=json.loads(plugin_path.read_text(encoding="utf-8"));plugin["version"]=version;kit.dump(plugin_path,plugin)
    # This metadata preserves the existing container only; no historical plugin packaging/activation.
    kit.dump(target/"release-decision.json",{"schema":"cd-release-treatment/v1","product":"canopyops","baseline_version":"0.3.0","baseline_sha256":"223d23b8adc3aa6595b86db7624e9e3d16bfd676eddb0b61063766335237e26f","target_version":version,"kind":"update","effect":"expanded_workflow","reason":"Owner-required increment adds browser/nativeicons and explicit external-store desktopentry; accepted cultivation/store/launchbehavior preserved."})
    notes=target/"RELEASE-NOTES-v0.3.1.md";notes.write_bytes(b"# CanopyOps0.3.1\n\nAdds product icons and optional no-clobber desktopentries through the existing Python desk with an explicit external record store. Accepted cultivation intelligence, measurements, history/conflict protection, themes and original artwork remain unchanged. NativeWindows entry and portableMac construction passed; nativeMac launch remains unobserved. Historical plugin delivery remains excluded.\n")
    oldclaude=target/"claude/canopyops-v0.3.0.zip"
    if oldclaude.exists():oldclaude.unlink()
    claude=target/"claude/canopyops-v0.3.1.zip";kit.zip_tree(claude,skill)
    manifest=json.loads((target/"manifest.json").read_text(encoding="utf-8"));manifest["family"]["version"]=version;manifest["family"]["backup_filename"]="CanopyOps-v0.3.1.zip";manifest["source_records"]=[{"handle":"canopyops","files":kit.file_records(skill)}];manifest["claude_archives"]=[{"handle":"canopyops","file":"claude/"+claude.name,"sha256":kit.digest(claude)}];manifest["delivery_sidecars"]={"path":"delivery-sidecars","files":kit.file_records(target/"delivery-sidecars")};manifest["current_delivery"]="Portable cropworkspace and completeskill; historicalplugin installation is not required.";kit.dump(target/"manifest.json",manifest)
    receipt_path=target/"package-receipt.json"
    receipt=json.loads(receipt_path.read_text(encoding="utf-8"));receipt["version"]=version;kit.dump(receipt_path,receipt)
    verifier=kit.verifier_at(target/"tools/verify_release.py");report=verifier.verify(target)
    if not report["ok"]:print(json.dumps(report,indent=2));return 1
    kit.dump(target/"verification-report.json",report)
    archive=target.parent/(target.name+"-CanopyOps-v0.3.1.zip")
    if archive.exists():raise SystemExit("Candidate archive exists; preserve it")
    kit.zip_tree(archive,target,"canopyops-v0.3.1");checksum=kit.digest(archive)
    archive.with_suffix(archive.suffix+".sha256").write_text(checksum+"  "+archive.name+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({"archive":str(archive),"sha256":checksum,"verification":report},indent=2));return 0


if __name__ == "__main__":
    raise SystemExit(main())
