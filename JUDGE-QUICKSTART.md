# CanopyOps Judge Quickstart

This path uses fictional data, requires no cultivation facility, and takes about five minutes. It demonstrates installation, deterministic machinery, and the authority-bounded operating behavior.

## 1. Install the branded Codex plugin

~~~text
codex plugin marketplace add Stunspot/CanopyOps
codex plugin add canopyops@collaborative-dynamics
~~~

Start a new Codex task after installation.

No account, API key, connector, MCP server, hosted service, telemetry, or cultivation equipment is required.

## 2. Run the fictional incident

Paste this into the new task:

> Use CanopyOps for a fictional, licensed cannabis cultivation facility. A late-flower room held 27 C and 78% RH for 42 minutes overnight. One wall sensor recorded the excursion; its calibration status and exact canopy position are unknown. The active room target is 25 C and no more than 60% RH, but I have not supplied the approved source or tolerance. The crop lead says to increase dehumidification immediately. Build a provisional incident workup and incident record. Preserve competing explanations, distinguish reversible containment from cause-specific correction, identify the evidence that would change the next decision, and do not claim that any setting was approved or changed.

## 3. What to look for

A useful result should:

- classify supplied facts and expose missing measurement context;
- avoid treating one sensor as proof of whole-room conditions;
- preserve plausible sensor, spatial, equipment, load, and control explanations;
- separate reversible containment from cause-specific correction;
- refuse to claim that a controller change was approved or executed;
- identify the target source, tolerance, sensor calibration/location, corroborating sensors, crop observations, controller trend, and equipment state as decision-relevant evidence;
- produce an incident record with owner, authority, follow-up, verification, and status fields;
- close provisionally or awaiting authority rather than declaring the incident solved.

The exact prose may vary. The custody of evidence and authority should not.

## 4. Run the deterministic suite

From the repository root:

~~~text
python -m unittest discover -s tests -v
~~~

Expected result:

~~~text
Ran 12 tests

OK
~~~

The suite uses only Python's standard library and exercises:

- leaf-temperature-aware VPD;
- input rejection;
- DLI and irrigation arithmetic;
- unit conversion;
- valid and invalid schema records;
- plan-template linting;
- source freshness;
- timezone-required log normalization;
- required package surfaces;
- all bundled JSON schemas.

## 5. Inspect one deterministic calculation

~~~text
python canopyops/scripts/calculate_vpd.py --air-temp-c 27 --rh-percent 78 --leaf-temp-c 26
~~~

The output includes the supplied air, leaf, and RH values; intermediate vapor-pressure values; leaf VPD; the formula basis; and whether leaf temperature was measured or estimated. CanopyOps does not silently substitute air temperature for leaf temperature.

## Other supported paths

- Standalone Codex SKILL: copy **canopyops/** to the personal Codex skills directory.
- Claude Code: structurally compatible personal or project Agent Skill; live host execution is not claimed.
- Fileless chat: documented degraded mode without deterministic scripts or persistent artifacts.

See [INSTALL.md](INSTALL.md) for exact paths, updating, removal, and troubleshooting.

## Safety

All data above are fictional. Do not use this quickstart to operate equipment. CanopyOps is advisory decision support and does not authorize pesticides, legal interpretations, batch release, alarm bypass, occupied-space CO2 work, extraction, or direct actuator commands.
