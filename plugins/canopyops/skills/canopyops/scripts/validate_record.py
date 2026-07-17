#!/usr/bin/env python3
"""Validate CanopyOps JSON records against the bundled schema subset."""
import argparse
from datetime import date, datetime
import json
from pathlib import Path


TYPE_MAP = {"object": dict, "array": list, "string": str, "number": (int, float), "integer": int, "boolean": bool, "null": type(None)}


def _matches_type(value, expected) -> bool:
    types = expected if isinstance(expected, list) else [expected]
    return any(isinstance(value, TYPE_MAP[t]) and not (t in {"number", "integer"} and isinstance(value, bool)) for t in types)


def validate(value, schema: dict, path: str = "$") -> list[str]:
    errors = []
    expected = schema.get("type")
    if expected and not _matches_type(value, expected):
        return [f"{path}: expected {expected}, got {type(value).__name__}"]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} is not one of {schema['enum']}")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: string is shorter than minLength")
        fmt = schema.get("format")
        try:
            if fmt == "date": date.fromisoformat(value)
            elif fmt == "date-time": datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            errors.append(f"{path}: invalid {fmt}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required property {key!r}")
        if len(value) < schema.get("minProperties", 0):
            errors.append(f"{path}: object has fewer than minProperties")
        for key, child in value.items():
            if key in schema.get("properties", {}):
                errors.extend(validate(child, schema["properties"][key], f"{path}.{key}"))
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: array has fewer than minItems")
        if "items" in schema:
            for index, child in enumerate(value):
                errors.extend(validate(child, schema["items"], f"{path}[{index}]"))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("schema", type=Path)
    args = parser.parse_args()
    record = json.loads(args.record.read_text(encoding="utf-8-sig"))
    schema = json.loads(args.schema.read_text(encoding="utf-8-sig"))
    errors = validate(record, schema)
    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
