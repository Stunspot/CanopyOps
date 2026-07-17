# Start Here

CanopyOps helps an AI agent reason and document work for legal cannabis cultivation. You do not need to understand its internal files, schemas, or scripts to begin.

## Choose a first job

Start with one bounded situation—not your entire operation.

Good first jobs include:

- review one room and cultivar before a new run;
- investigate one humidity, irrigation, runoff, EC, pH, pest, or crop-quality event;
- check one DLI, VPD, irrigation-volume, or unit-conversion calculation;
- review one batch's harvest-readiness evidence;
- turn one proposed change into a compliance-verification brief;
- convert one messy handoff into a traceable operating record.

For installation, follow [INSTALL.md](INSTALL.md). If CanopyOps is already available in your agent, continue below.

## Your ten-minute first run

Use fictional or non-sensitive information the first time. Paste this starter request and replace the bracketed facts you know:

> Review a fictional late-flower cannabis room after an overnight humidity excursion. The room held [temperature] and [relative humidity] for approximately [duration]. The crop is at [stage], and the approved room target is [target, source, and tolerance if known]. Begin with a provisional reading, list the missing facts that would change the next decision, distinguish reversible containment from cause-specific correction, and draft an incident record with owner and verification fields. Do not claim that any action was approved or executed.

CanopyOps should:

1. reflect what it believes happened;
2. separate observed, measured, assumed, calculated, interpreted, and recommended information;
3. ask only for facts that change the next consequential judgment;
4. preserve plausible alternatives rather than leaping to one diagnosis;
5. produce a usable record with authority and follow-up fields.

## Bring useful evidence

You can begin with partial information. Helpful inputs include:

- facility, room, crop, and cultivar profiles;
- environmental or irrigation logs with timestamps and time zones;
- sensor location, calibration, and measurement method;
- crop-stage and symptom observations;
- photos, lab results, crop-walk notes, and prior incidents;
- approved targets with source, scope, tolerance, and owner;
- current SOPs, labels, jurisdiction sources, and equipment documentation;
- the decision you are actually trying to make.

Do not include employee, patient, customer, security, license, or trade-secret information unless your chosen host and workspace are approved for it.

## Read the status, not just the prose

CanopyOps closes work with one of these states:

- **Provisional:** useful analysis exists, but material facts remain uncertain.
- **Ready for review:** the artifact is coherent enough for an accountable person to examine.
- **Awaiting authority:** the evidence supports a proposal, but approval is still required.
- **Blocked:** the next responsible step depends on unavailable evidence, capability, or authority.
- **Verified for stated use:** a named verification condition was actually satisfied for the stated scope.

“Recommended” never means “approved,” and “approved” never means “executed.”

## Pick the next path

- Planning a room or run: ask for a crop plan and facility constraint review.
- Investigating a problem: ask for an incident workup and reversible containment options.
- Checking numbers: provide values, units, time basis, measurement method, and target source.
- Preparing harvest: ask for a readiness review with holds and release authority kept separate.
- Changing an SOP, product, setpoint, pesticide/PGR program, or compliance record: ask for a verification brief before asking for a recommendation.

Explore the complete worked cases in [EXAMPLE-TOUR.md](EXAMPLE-TOUR.md).

## Stop and use the real emergency path

If an occupied active CO2 or life-safety alarm exists, follow the facility emergency or evacuation procedure and qualified response. CanopyOps is not an emergency controller, alarm authority, or substitute for trained responders.

