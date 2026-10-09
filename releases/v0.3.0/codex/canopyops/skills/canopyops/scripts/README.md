# Deterministic utilities

These Python 3 utilities use only the standard library. Run each with `--help` for arguments.

- `calculate_vpd.py`: leaf VPD from air temperature, RH, and measured leaf temperature or an explicit offset.
- `calculate_dli.py`: DLI from averaged PPFD and photoperiod.
- `calculate_irrigation.py`: delivered, drainage, retained, and per-plant/event metrics.
- `normalize_units.py`: common temperature, volume, and pressure conversions.
- `normalize_logs.py`: timezone-aware CSV normalization into UTC and canonical units.
- `validate_record.py`: validation against the bundled JSON Schema subset.
- `lint_cultivation_plan.py`: release-critical plan affordance checks.
- `check_source_freshness.py`: source review-age flags; not a legal-validity check.
- `package_deliverables.py`: deterministic ZIP assembly.

Exact arithmetic does not make inputs representative, targets authoritative, or recommendations approved. Preserve the emitted interpretation limits with downstream use.
