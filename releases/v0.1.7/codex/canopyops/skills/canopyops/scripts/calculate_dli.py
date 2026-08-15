#!/usr/bin/env python3
"""Calculate DLI from constant or averaged PPFD and photoperiod."""
import argparse
import json


def calculate_dli(ppfd_umol_m2_s: float, photoperiod_hours: float) -> float:
    if ppfd_umol_m2_s < 0:
        raise ValueError("PPFD cannot be negative")
    if not 0 < photoperiod_hours <= 24:
        raise ValueError("photoperiod must be greater than 0 and no more than 24 hours")
    return ppfd_umol_m2_s * photoperiod_hours * 3600 / 1_000_000


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ppfd", type=float, required=True, help="Average PPFD in µmol/m²/s")
    parser.add_argument("--hours", type=float, required=True)
    args = parser.parse_args()
    result = calculate_dli(args.ppfd, args.hours)
    print(json.dumps({
        "ppfd_umol_m2_s": args.ppfd,
        "photoperiod_hours": args.hours,
        "dli_mol_m2_day": round(result, 4),
        "formula": "PPFD * hours * 3600 / 1,000,000",
        "interpretation_limit": "Represents the supplied average PPFD; does not establish canopy uniformity or schedule variation."
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
