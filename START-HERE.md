# Start Here

CanopyOps helps an AI agent reason about and document lawful cannabis cultivation operations. Begin with one bounded decision, not your entire facility.

## 1. Choose the correct distribution

Read [`RELEASE-STATUS.md`](RELEASE-STATUS.md) before installing.

- Choose the **repository-native v0.1.5 plugin** for the shortest direct GitHub/Codex route.
- Choose the **settled portable v0.1.6 bundle** when you want a self-verifying archive with package-specific Codex and Claude instructions.
- If CanopyOps is already available in your host, skip installation and continue below.

Do not combine files from v0.1.5 and v0.1.6. Package identity, installation, discovery, invocation, and healthy behavior are separate observations.

## 2. Pick one first job

Good first jobs include:

- review one room and crop before a new run;
- investigate one humidity, irrigation, runoff, EC, pH, pest, disease, or crop-quality event;
- check one DLI, VPD, irrigation-volume, or unit-conversion calculation;
- review one batch’s harvest-readiness evidence;
- turn one proposed change into a compliance-verification brief;
- convert one messy handoff into a traceable operating record.

For installation, use [`INSTALL.md`](INSTALL.md).

## 3. Run a fictional ten-minute case

Use fictional or non-sensitive information the first time:

> Review a fictional late-flower cannabis room after an overnight humidity excursion. The room held [temperature] and [relative humidity] for approximately [duration]. The crop is at [stage], and the approved room target is [target, source, and tolerance if known]. Begin with a provisional reading, list the missing facts that would change the next decision, distinguish reversible containment from cause-specific correction, and draft an incident record with owner and verification fields. Do not claim that any action was approved or executed.

CanopyOps should:

1. reflect what it believes happened;
2. separate observed, measured, calculated, assumed, interpreted, and recommended information;
3. ask only for facts that change the next consequential judgment;
4. preserve plausible alternatives rather than leaping to one diagnosis;
5. produce a usable record with authority, owner, follow-up, and verification fields;
6. close with a status rather than declaring the matter solved.

## 4. Bring useful evidence

Partial information is acceptable. Helpful inputs include:

- facility, room, crop, and cultivar profiles;
- environmental or irrigation logs with timestamps and time zones;
- sensor location, calibration, and measurement method;
- crop-stage and symptom observations;
- photos, lab results, crop-walk notes, and prior incidents;
- approved targets with source, scope, tolerance, and owner;
- current SOPs, labels, jurisdiction sources, and equipment documentation;
- the decision you are actually trying to make.

Do not include employee, patient, customer, security, licence, or trade-secret information unless the selected host and workspace are approved for it. See [`DATA-AND-PRIVACY.md`](DATA-AND-PRIVACY.md).

## 5. Read the status, not just the prose

CanopyOps closes work with one of these states:

- **Provisional** — useful analysis exists, but material facts remain uncertain.
- **Ready for review** — the artifact is coherent enough for an accountable person to examine.
- **Awaiting authority** — the evidence supports a proposal, but approval is still required.
- **Blocked** — the next responsible step depends on unavailable evidence, capability, or authority.
- **Verified for stated use** — a named verification condition was actually satisfied for the stated scope.

“Recommended” never means “approved,” and “approved” never means “executed.”

## 6. Continue through the relevant route

- Planning a room or run: ask for a crop plan and facility-constraint review.
- Investigating a problem: ask for an incident workup and reversible containment options.
- Checking numbers: provide values, units, time basis, measurement method, and target source.
- Preparing harvest: ask for a readiness review with holds and release authority kept separate.
- Changing an SOP, product, setpoint, pesticide/PGR program, or compliance record: ask for a verification brief before requesting a recommendation.

Explore the complete worked cases in [`EXAMPLE-TOUR.md`](EXAMPLE-TOUR.md).

## Stop and use the real emergency path

If an occupied active CO2 or life-safety alarm exists, follow the facility emergency or evacuation procedure and use qualified response. CanopyOps is not an emergency controller, alarm authority, or substitute for trained responders.
