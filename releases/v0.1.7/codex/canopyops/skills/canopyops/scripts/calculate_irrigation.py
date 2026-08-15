#!/usr/bin/env python3
"""Calculate transparent irrigation and drainage summary metrics."""
import argparse
import json


def calculate(delivered_l: float, drainage_l: float, plant_count: int, events: int) -> dict:
    if delivered_l <= 0 or drainage_l < 0:
        raise ValueError("delivered volume must be positive and drainage non-negative")
    if drainage_l > delivered_l:
        raise ValueError("drainage cannot exceed delivered volume for this bounded calculation")
    if plant_count <= 0 or events <= 0:
        raise ValueError("plant count and events must be positive")
    return {
        "delivered_l": delivered_l,
        "drainage_l": drainage_l,
        "retained_l": round(delivered_l - drainage_l, 4),
        "drainage_percent": round(drainage_l / delivered_l * 100, 4),
        "delivered_ml_per_plant": round(delivered_l * 1000 / plant_count, 4),
        "drainage_ml_per_plant": round(drainage_l * 1000 / plant_count, 4),
        "delivered_ml_per_plant_per_event": round(delivered_l * 1000 / plant_count / events, 4),
        "plant_count": plant_count,
        "events": events,
        "interpretation_limit": "Totals do not establish distribution, root-zone state, or an appropriate drainage target."
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--delivered-l", type=float, required=True)
    parser.add_argument("--drainage-l", type=float, required=True)
    parser.add_argument("--plants", type=int, required=True)
    parser.add_argument("--events", type=int, default=1)
    args = parser.parse_args()
    print(json.dumps(calculate(args.delivered_l, args.drainage_l, args.plants, args.events), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
