#!/usr/bin/env python3
"""Build a deterministic SHA-256 manifest for a CanopyOps repository release."""
import argparse
import hashlib
import json
from pathlib import Path


EXCLUDED_PARTS = {".git", "__pycache__", ".pytest_cache", "release-assets"}
MANIFEST_NAME = "release-manifest.json"


def build_manifest(root: Path, version: str) -> dict:
    files = []
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix().lower()):
        if not path.is_file() or any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        relative = path.relative_to(root).as_posix()
        if relative == MANIFEST_NAME:
            continue
        data = path.read_bytes()
        files.append(
            {
                "path": relative,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    return {
        "format": "cd-public-release-manifest/v1",
        "product": "CanopyOps",
        "version": version,
        "generated_on": "2026-07-20",
        "hash_algorithm": "sha256",
        "files": files,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    output = root / MANIFEST_NAME
    output.write_text(json.dumps(build_manifest(root, args.version), indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
