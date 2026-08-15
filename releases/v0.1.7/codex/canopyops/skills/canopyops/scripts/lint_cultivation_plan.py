#!/usr/bin/env python3
"""Lint a CanopyOps Markdown or JSON crop plan for release-critical affordances."""
import argparse
import json
from pathlib import Path


MARKDOWN_CONCERNS = {
    "identity": ["plan id", "facility", "room"],
    "authority": ["owner", "approv"],
    "evidence": ["assumption", "calculation"],
    "operations": ["monitor", "response", "re-plan"],
    "readiness": ["review", "next action"],
}


def lint_markdown(text: str) -> list[str]:
    lower = text.lower()
    return [f"missing {group}: expected one of {terms}" for group, terms in MARKDOWN_CONCERNS.items() if not all(term in lower for term in terms)]


def lint_json(data: dict) -> list[str]:
    required = ["plan_id", "version", "status", "facility_profile", "room", "crop_profiles", "stages", "owner", "review_state"]
    errors = [f"missing required property: {key}" for key in required if key not in data]
    for index, stage in enumerate(data.get("stages", [])):
        for key in ["name", "advance_criteria", "monitoring", "owner"]:
            if key not in stage:
                errors.append(f"stages[{index}] missing {key}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    args = parser.parse_args()
    text = args.plan.read_text(encoding="utf-8-sig")
    errors = lint_json(json.loads(text)) if args.plan.suffix.lower() == ".json" else lint_markdown(text)
    print(json.dumps({"ready": not errors, "findings": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
