#!/usr/bin/env python3
"""Create a deterministic ZIP from a CanopyOps package directory."""
import argparse
from pathlib import Path
import zipfile


EXCLUDED_PARTS = {"__pycache__", ".pytest_cache", ".git"}


def package(source: Path, output: Path) -> int:
    files = [p for p in source.rglob("*") if p.is_file() and not any(part in EXCLUDED_PARTS for part in p.parts) and p.resolve() != output.resolve()]
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(files, key=lambda p: p.relative_to(source).as_posix().lower()):
            relative = path.relative_to(source).as_posix()
            info = zipfile.ZipInfo(relative, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    return len(files)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    count = package(args.source.resolve(), args.output.resolve())
    print(f"packaged {count} files to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
