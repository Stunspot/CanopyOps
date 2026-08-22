#!/usr/bin/env python3
"""Build a deterministic CanopyOps portable release from the settled prior line."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import sys
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
RELEASES = REPO / "releases"
OLD_VERSION = "0.1.6"
VERSION = "0.1.7"
SLUG = "canopyops"
TITLE = "CanopyOps"
SUMMARY = "Cannabis cultivation operations guidance with jurisdiction, safety, evidence, and operational boundaries."
SHORT = "🌿 Cannabis health, climate, and yield."
ADVISOR = "🌿 Cannabis health, climate, and yield."
STAMP = (2026, 8, 14, 0, 0, 0)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def zip_tree(archive_path: Path, root: Path, prefix: str = "") -> None:
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.relative_to(root).as_posix()):
            relative = path.relative_to(root).as_posix()
            name = f"{prefix}/{relative}" if prefix else relative
            info = zipfile.ZipInfo(name, STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes())


def load_verifier(path: Path):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("canopyops_portable_verifier", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> int:
    source = RELEASES / f"v{OLD_VERSION}"
    target = RELEASES / f"v{VERSION}"
    if not source.is_dir():
        raise SystemExit(f"missing settled source release: {source}")
    if target.exists():
        if target.resolve().parent != RELEASES.resolve() or target.name != f"v{VERSION}":
            raise SystemExit(f"refusing unsafe target: {target}")
        shutil.rmtree(target)
    shutil.copytree(source, target)

    for generated in [
        target / f"{TITLE}-v{OLD_VERSION}.zip",
        target / f"{TITLE}-v{OLD_VERSION}.zip.sha256",
        target / "receipt.json",
    ]:
        generated.unlink(missing_ok=True)
    (target / "claude" / f"{SLUG}-v{OLD_VERSION}.zip").unlink(missing_ok=True)

    replacements = {
        OLD_VERSION: VERSION,
        "🌿 Cultivation operations advisor.": ADVISOR,
        "🌿 Cultivation operations with safety and evidence.": SHORT,
        "Cultivation operations guidance with jurisdiction, safety, evidence, and operational boundaries.": SUMMARY,
    }
    for path in target.rglob("*"):
        if not path.is_file() or path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".zip"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for old, new in replacements.items():
            text = text.replace(old, new)
        path.write_text(text, encoding="utf-8", newline="\n")

    changelog = target / "codex" / SLUG / "skills" / SLUG / "CHANGELOG.md"
    body = changelog.read_text(encoding="utf-8")
    entry = (
        "## 0.1.7\n\n"
        "- Name cannabis cultivation explicitly in model-visible, UI, and package descriptions.\n"
        "- Preserve the settled v0.1.6 operating method and package topology unchanged.\n"
        "- Add deterministic portable-release construction and renewed custody evidence.\n\n"
    )
    changelog.write_text(body.replace("# Changelog\n\n", "# Changelog\n\n" + entry, 1), encoding="utf-8", newline="\n")

    plugin_path = target / "codex" / SLUG / ".codex-plugin" / "plugin.json"
    plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
    plugin["version"] = VERSION
    plugin["description"] = SUMMARY
    plugin["interface"]["longDescription"] = SUMMARY
    plugin["interface"]["shortDescription"] = SHORT
    dump(plugin_path, plugin)

    skill_root = target / "codex" / SLUG / "skills" / SLUG
    claude_path = target / "claude" / f"{SLUG}-v{VERSION}.zip"
    zip_tree(claude_path, skill_root)

    manifest_path = target / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    family = manifest["family"]
    family.update({"version": VERSION, "backup_filename": f"{TITLE}-v{VERSION}.zip", "summary": SUMMARY, "short_description": SHORT})
    records = []
    for path in sorted((p for p in skill_root.rglob("*") if p.is_file()), key=lambda p: p.relative_to(skill_root).as_posix()):
        data = path.read_bytes()
        records.append({"bytes": len(data), "path": path.relative_to(skill_root).as_posix(), "sha256": digest(data)})
    manifest["source_records"] = [{"files": records, "handle": SLUG}]
    manifest["claude_archives"] = [{"file": f"claude/{claude_path.name}", "handle": SLUG, "sha256": digest(claude_path.read_bytes())}]
    dump(manifest_path, manifest)

    package_receipt = json.loads((target / "package-receipt.json").read_text(encoding="utf-8"))
    package_receipt["version"] = VERSION
    dump(target / "package-receipt.json", package_receipt)

    custody = json.loads((target / "description-custody.json").read_text(encoding="utf-8"))
    custody[SLUG]["model_visible_description"] = ADVISOR
    custody[SLUG]["ui_short_description"] = ADVISOR
    dump(target / "description-custody.json", custody)

    verifier = load_verifier(target / "tools" / "verify_release.py")
    report = verifier.verify(target)
    if not report["ok"]:
        print(json.dumps(report, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    dump(target / "verification-report.json", report)
    shutil.rmtree(target / "tools" / "__pycache__", ignore_errors=True)

    archive_path = target / f"{TITLE}-v{VERSION}.zip"
    staging = target.parent / f".{SLUG}-v{VERSION}-archive"
    if staging.exists():
        shutil.rmtree(staging)
    package_root = staging / f"{SLUG}-v{VERSION}"
    package_root.mkdir(parents=True)
    excluded = {archive_path.name, f"{archive_path.name}.sha256", "receipt.json"}
    for path in target.rglob("*"):
        if not path.is_file() or path.relative_to(target).as_posix().split("/", 1)[0] in excluded:
            continue
        relative = path.relative_to(target)
        destination = package_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
    zip_tree(archive_path, staging)
    shutil.rmtree(staging)

    archive_hash = digest(archive_path.read_bytes())
    (target / f"{archive_path.name}.sha256").write_text(f"{archive_hash}  {archive_path.name}\n", encoding="utf-8", newline="\n")
    with zipfile.ZipFile(archive_path) as archive:
        member_count = len(archive.namelist())
    receipt = {
        "backup": None,
        "backup_checksum": None,
        "backup_sha256": None,
        "canonical_checksum": f"{archive_path.name}.sha256",
        "canonical_zip": archive_path.name,
        "canonical_zip_member_count": member_count,
        "canonical_zip_sha256": archive_hash,
        "copy_not_move_verified": False,
        "family": SLUG,
        "schema": "cd-settled-family-build-receipt/v1",
        "status": "canonical-built-backup-pending",
        "version": VERSION,
    }
    dump(target / "receipt.json", receipt)
    print(json.dumps({"archive": str(archive_path), "sha256": archive_hash, "members": member_count}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
