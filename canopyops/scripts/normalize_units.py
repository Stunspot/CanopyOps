#!/usr/bin/env python3
"""Normalize common CanopyOps quantities without external dependencies."""
import argparse
import json


ALIASES = {"c": "c", "°c": "c", "f": "f", "°f": "f", "l": "l", "liter": "l", "liters": "l", "ml": "ml", "gal": "us_gal", "gallon": "us_gal", "gallons": "us_gal", "us_gal": "us_gal", "kpa": "kpa", "pa": "pa"}


def normalize(value: float, source: str, target: str) -> float:
    source, target = ALIASES.get(source.lower(), source.lower()), ALIASES.get(target.lower(), target.lower())
    if source == target:
        return value
    conversions = {
        ("f", "c"): lambda x: (x - 32) * 5 / 9,
        ("c", "f"): lambda x: x * 9 / 5 + 32,
        ("ml", "l"): lambda x: x / 1000,
        ("l", "ml"): lambda x: x * 1000,
        ("us_gal", "l"): lambda x: x * 3.785411784,
        ("l", "us_gal"): lambda x: x / 3.785411784,
        ("pa", "kpa"): lambda x: x / 1000,
        ("kpa", "pa"): lambda x: x * 1000,
    }
    if (source, target) not in conversions:
        raise ValueError(f"unsupported conversion: {source} to {target}")
    return conversions[(source, target)](value)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("value", type=float)
    parser.add_argument("from_unit")
    parser.add_argument("to_unit")
    args = parser.parse_args()
    result = normalize(args.value, args.from_unit, args.to_unit)
    print(json.dumps({"input": args.value, "from_unit": args.from_unit, "to_unit": args.to_unit, "result": round(result, 6)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
