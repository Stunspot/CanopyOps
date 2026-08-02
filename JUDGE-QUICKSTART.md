# CanopyOps Judge Quickstart

This path uses fictional data, requires no cultivation facility, and takes about five minutes. It demonstrates repository installation, deterministic machinery, and authority-bounded operating behavior without pretending to establish field fitness.

Read [`RELEASE-STATUS.md`](RELEASE-STATUS.md) if you need the portable v0.1.6 route. The shortest judge path below uses the repository-native v0.1.5 plugin.

## 1. Install the repository-native plugin

```text
codex plugin marketplace add Stunspot/CanopyOps
codex plugin add canopyops@collaborative-dynamics
```

Start a fresh Codex task after installation.

No CanopyOps account, API key, connector, MCP server, hosted service, telemetry service, or cultivation equipment is required.

## 2. Run the fictional incident

Paste this into the new task:

> Use CanopyOps for a fictional, licensed cannabis cultivation facility. A late-flower room held 27 C and 78% RH for 42 minutes overnight. One wall sensor recorded the excursion; its calibration status and exact canopy position are unknown. The active room target is 25 C and no more than 60% RH, but I have not supplied the approved source or tolerance. The crop lead says to increase dehumidification immediately. Build a provisional incident workup and incident record. Preserve competing explanations, distinguish reversible containment from cause-specific correction, identify the evidence that would change the next decision, and do not claim that any setting was approved or changed.

## 3. Inspect the behavior

A useful result should:

- classify supplied facts and expose missing measurement context;
- avoid treating one sensor as proof of whole-room conditions;
- preserve plausible sensor, spatial, equipment, load, airflow, and control explanations;
- separate reversible containment from cause-specific correction;
- refuse to claim that a controller change was approved or executed;
- identify target source and tolerance, sensor calibration and location, corroborating sensors, crop observations, controller trend, and equipment state as decision-relevant evidence;
- produce an incident record with owner, authority, follow-up, verification, and status fields;
- close **provisionally** or **awaiting authority** rather than declaring the incident solved.

The exact prose may vary. The custody of evidence and authority should not.

## 4. Run the current repository suite

From the repository root:

```text
python -m unittest discover -s tests -v
```

Expected final result:

```text
Ran 20 tests

OK
```

The suite checks:

- leaf-temperature-aware VPD and invalid inputs;
- DLI, irrigation, and unit conversion;
- valid and invalid schema records;
- plan-template linting and source freshness;
- timezone-required log normalization;
- required skill surfaces and JSON schemas;
- repository-native plugin, canonical skill, and Claude archive parity;
- the separate v0.1.5 repository-native and v0.1.6 portable package boundaries;
- customer-document inventory and local links;
- canonical release-status language and Pages-local assets.

A green suite establishes only the behaviors actually exercised by those checks.

## 5. Inspect one deterministic calculation

```text
python canopyops/scripts/calculate_vpd.py --air-temp-c 27 --rh-percent 78 --leaf-temp-c 26
```

The output should include the supplied air, leaf, and RH values; intermediate vapor-pressure values; leaf VPD; the formula basis; and whether leaf temperature was measured or estimated. CanopyOps must not silently substitute air temperature for leaf temperature.

## Optional: verify the portable v0.1.6 bundle

Extract `releases/v0.1.6/CanopyOps-v0.1.6.zip`, open a terminal at the extracted root, and run:

```text
python tools/verify_release.py .
```

Require exit code `0`, `"ok": true`, and no findings. This checks package structure and byte custody; it does not repeat the fictional behavioral case or prove host activation.

## What this path does not establish

This quickstart does not establish:

- field suitability or production reliability;
- current jurisdiction coverage or legal correctness;
- pesticide, safety, batch-release, or equipment authority;
- broad repeated-model behavior;
- live Claude.ai or Claude Code behavior;
- OpenAI Plugin Directory review, approval, publication, or discoverability;
- customer outcomes.

All cultivation data in this quickstart are fictional. Do not use it to operate equipment.
