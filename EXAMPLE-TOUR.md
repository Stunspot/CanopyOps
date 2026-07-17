# Example Tour

CanopyOps includes four demonstrations built around different operating decisions. They are teaching cases, not claims about a real facility, cultivar, product, or jurisdiction.

## 1. New room crop plan

**Situation:** A cultivation team has a fixture map, HVAC and dehumidification specifications, irrigation layout, facility profile, and vendor cultivar description—but not a single approved plan hiding in those inputs.

**What CanopyOps demonstrates:**

- separates facility limits from desired targets;
- treats vendor cultivar claims as provisional rather than agronomic fact;
- exposes missing source, tolerance, stage, and approval information;
- builds a crop plan with assumptions, decision owners, risks, and verification gates.

**Why it matters:** A room plan is not merely a table of setpoints. It is a chain of assumptions and authorities that must survive contact with the actual crop and facility.

[Read the complete new-room crop-plan demonstration](canopyops/examples/new-room-crop-plan.md).

## 2. Late-flower humidity incident

**Situation:** A late-flower room experiences an overnight humidity excursion with incomplete sensor and response information.

**What CanopyOps demonstrates:**

- reconstructs the event without claiming missing measurements;
- distinguishes immediate reversible containment from cause-specific correction;
- preserves disease, equipment, airflow, sensor, and operating explanations until evidence discriminates among them;
- produces an incident record with authority, owner, and reopen conditions.

**Why it matters:** The useful result is not “humidity bad.” It is a defensible next state: what is known, what is at risk, what is safe to do now, and what evidence controls the next decision.

[Read the complete late-flower humidity demonstration](canopyops/examples/late-flower-humidity-incident.md).

## 3. Rising runoff EC diagnosis

**Situation:** Runoff EC is rising, but a single number cannot distinguish feed concentration, dryback, sampling method, irrigation distribution, substrate behavior, or plant demand.

**What CanopyOps demonstrates:**

- keeps influent, runoff, substrate, timing, and method conceptually separate;
- checks units and comparisons before interpreting direction;
- asks for the smallest discriminating measurements;
- avoids prescribing a flush or recipe change before the evidence supports one.

**Why it matters:** Crop steering language can make a weak inference sound technical. CanopyOps makes the measurement chain visible before recommending a correction.

[Read the complete runoff-EC demonstration](canopyops/examples/high-runoff-ec-diagnosis.md).

## 4. Harvest-readiness review

**Situation:** A team needs to decide whether a cannabis batch is ready to harvest while quality observations, timing, operational capacity, and unresolved holds remain mixed together.

**What CanopyOps demonstrates:**

- separates measured evidence from interpretation;
- retains unresolved quality and compliance holds;
- distinguishes harvest recommendation from batch-release authority;
- creates a review artifact another accountable person can challenge.

**Why it matters:** “Looks ready” and “authorized for the next irreversible step” are different statements. The review keeps them different.

[Read the complete harvest-readiness demonstration](canopyops/examples/harvest-readiness-review.md).

## Try the pattern on your own case

Give CanopyOps the smallest complete evidence bundle you have and name the decision you need. Ask it to begin with a provisional reading, preserve competing explanations, and produce the relevant operating artifact.

For installation and starter requests, see [START-HERE.md](START-HERE.md).

