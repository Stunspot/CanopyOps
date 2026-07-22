#!/usr/bin/env python3
"""Normalize CSV headers, timestamps, and common temperature/volume fields."""
import argparse
import csv
from datetime import datetime, timezone
from pathlib import Path

from normalize_units import normalize


HEADER_ALIASES = {
    "time": "timestamp", "datetime": "timestamp", "date_time": "timestamp",
    "temp_f": "temperature_f", "temp_c": "temperature_c", "temperature": "temperature_c",
    "humidity": "rh_percent", "rh": "rh_percent", "relative_humidity": "rh_percent",
    "volume_gal": "volume_us_gal", "gallons": "volume_us_gal", "liters": "volume_l",
}


def iso_timestamp(value: str) -> str:
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        raise ValueError(f"timestamp lacks timezone: {value}")
    return parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_row(row: dict) -> dict:
    renamed = {HEADER_ALIASES.get(k.strip().lower(), k.strip().lower()): v.strip() for k, v in row.items()}
    if renamed.get("timestamp"):
        renamed["timestamp"] = iso_timestamp(renamed["timestamp"])
    if renamed.get("temperature_f"):
        renamed["temperature_c"] = f"{normalize(float(renamed.pop('temperature_f')), 'f', 'c'):.4f}"
    if renamed.get("volume_us_gal"):
        renamed["volume_l"] = f"{normalize(float(renamed.pop('volume_us_gal')), 'us_gal', 'l'):.4f}"
    return renamed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()
    with args.input_csv.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [normalize_row(row) for row in csv.DictReader(handle)]
    if not rows:
        raise ValueError("input CSV has no data rows")
    fieldnames = sorted({key for row in rows for key in row})
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"normalized {len(rows)} rows to {args.output_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
