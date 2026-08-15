#!/usr/bin/env python3
"""Flag source records whose access date exceeds a supplied review interval."""
import argparse
from datetime import date
import json
from pathlib import Path


def check(records: list[dict], today: date, default_max_age: int) -> list[dict]:
    results = []
    for record in records:
        accessed = date.fromisoformat(record["accessed_at"])
        age = (today - accessed).days
        limit = int(record.get("max_age_days", default_max_age))
        results.append({
            "identifier": record.get("identifier", record.get("url", "unnamed")),
            "accessed_at": accessed.isoformat(),
            "age_days": age,
            "max_age_days": limit,
            "status": "review-due" if age > limit else "within-review-window",
            "note": "Freshness status does not establish continuing validity or applicability."
        })
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("records", type=Path, help="JSON array containing accessed_at and optional max_age_days")
    parser.add_argument("--today", default=date.today().isoformat())
    parser.add_argument("--default-max-age", type=int, default=30)
    args = parser.parse_args()
    records = json.loads(args.records.read_text(encoding="utf-8-sig"))
    results = check(records, date.fromisoformat(args.today), args.default_max_age)
    print(json.dumps({"results": results, "review_due": sum(r["status"] == "review-due" for r in results)}, indent=2))
    return 1 if any(r["status"] == "review-due" for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
