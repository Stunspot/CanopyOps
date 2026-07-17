#!/usr/bin/env python3
"""Calculate leaf VPD with explicit air and leaf temperatures."""
import argparse
import json
import math


def saturation_vapor_pressure(temp_c: float) -> float:
    return 0.6108 * math.exp((17.27 * temp_c) / (temp_c + 237.3))


def calculate_vpd(air_temp_c: float, rh_percent: float, leaf_temp_c: float) -> dict:
    if not -50 <= air_temp_c <= 80 or not -50 <= leaf_temp_c <= 80:
        raise ValueError("temperatures must be between -50 and 80 °C")
    if not 0 <= rh_percent <= 100:
        raise ValueError("relative humidity must be between 0 and 100 percent")
    air_svp = saturation_vapor_pressure(air_temp_c)
    leaf_svp = saturation_vapor_pressure(leaf_temp_c)
    actual_vp = air_svp * rh_percent / 100
    return {
        "air_temp_c": air_temp_c,
        "leaf_temp_c": leaf_temp_c,
        "rh_percent": rh_percent,
        "air_svp_kpa": round(air_svp, 4),
        "leaf_svp_kpa": round(leaf_svp, 4),
        "actual_vapor_pressure_kpa": round(actual_vp, 4),
        "leaf_vpd_kpa": round(leaf_svp - actual_vp, 4),
        "formula": "SVP(leaf) - RH/100 * SVP(air), Tetens approximation",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--air-temp-c", type=float, required=True)
    parser.add_argument("--rh-percent", type=float, required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--leaf-temp-c", type=float)
    group.add_argument("--leaf-offset-c", type=float)
    args = parser.parse_args()
    leaf = args.leaf_temp_c if args.leaf_temp_c is not None else args.air_temp_c + args.leaf_offset_c
    result = calculate_vpd(args.air_temp_c, args.rh_percent, leaf)
    result["leaf_temperature_basis"] = "measured" if args.leaf_temp_c is not None else "estimated_from_offset"
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
