# Built with Codex and GPT-5.6

CanopyOps is Collaborative Dynamics' OpenAI Build Week entry in **Work & Productivity**. It is an evidence-bounded operations and compliance Augment for lawful cannabis cultivation teams.

The project demonstrates two things at once:

1. A useful vertical Agent capability for a real, highly regulated agricultural audience.
2. Codex with GPT-5.6 performing product-scale synthesis from compact human direction, not merely producing code fragments.

## Origin

CanopyOps was conceived and built on July 17, 2026, during the official submission period. The initiating direction in Codex was compact: make the CanopyOps SKILL in the Augment lab.

From that direction, the working Augment emerged in roughly an hour. Public packaging, branding, licensing, safety review, release hardening, and publication continued afterward.

The /feedback Codex Session ID for the core project task is supplied in the Devpost submission.

## What was built

CanopyOps turns facility data, crop observations, logs, and constraints into defensible work products for lawful cannabis cultivation:

- crop and room plans;
- environmental, irrigation, root-zone, pest, disease, and quality incident workups;
- VPD, DLI, irrigation, runoff, dryback, and unit calculations;
- harvest-readiness reviews;
- compliance-verification briefs;
- incident reports, CAPA, risk registers, runbooks, crop walks, and shift handoffs.

It preserves an explicit custody chain among observed facts, measurements, assumptions, calculations, interpretations, recommendations, approvals, and execution. It does not operate controllers or acquire legal, pesticide, safety, or batch-release authority by sounding confident.

## The machinery

CanopyOps is an Augment, not a lone prompt.

| Surface | Responsibility |
|---|---|
| **canopyops/SKILL.md** | Recognizes the job, establishes the operating contract, activates Ella, and routes work. |
| **canopyops/personas/ella-greenfield-v2.md** | Supplies cultivation judgment and field-facing interaction style. |
| Five operating workflows | Handle planning, incidents, environment/root zone, harvest/quality, and compliance/operations. |
| Independent review workflow | Challenges evidence custody, authority, safety, and release status. |
| Nine Python utilities | Perform reproducible calculations, normalization, linting, freshness checks, schema validation, and packaging. |
| Twelve templates and six schemas | Preserve consequential operating state in readable and machine-checkable forms. |
| Behavioral evaluations | Test transfer, sparse evidence, contradictions, authority boundaries, and degraded operation. |
| Host adapters | Preserve the capability across Codex, Claude Code, chat, and bot environments. |
| Codex plugin | Provides branded installation and Agent-Skills discovery. |

Python utilities use only the standard library. The core reasoning layer remains available without Python, but CanopyOps labels manual calculations and unavailable deterministic checks honestly.

## How Codex and GPT-5.6 contributed

Codex with GPT-5.6:

- inspected the Augment-building system, source materials, persona, research corpus, and package conventions;
- designed the responsibility topology and runtime routing;
- authored workflows, operational templates, schemas, adapters, examples, and customer documentation;
- implemented deterministic Python utilities;
- generated evaluation cases and exercised bounded safety and scope behavior;
- validated paths, package structure, plugin metadata, archives, and installation;
- diagnosed and repaired packaging and host-integration problems;
- prepared licensing, branding, public-repository, and publication surfaces;
- added this public deterministic test suite, cross-platform verification, and judge quickstart.

This was iterative collaboration. Codex proposed and executed changes, reported boundaries, and produced evidence. Stun accepted, rejected, redirected, and refined the product throughout.

## Decisions that remained human

Stun, acting for Collaborative Dynamics:

- chose the product and audience;
- supplied the cultivation persona and source corpus;
- set the distinction between an Augment and its technical components;
- set the lawful-market, human-authority, and no-controller boundaries;
- determined that the product should remain useful to both commercial cultivators and less formal growers without becoming unserious;
- directed the evidence-custody and evaluation philosophy;
- chose the branding, licensing, attribution, and trademark posture;
- approved public release and the final claims.

Codex did not independently authorize publication, legal posture, operational actions, or contest entry.

## Evidence

The public repository provides three levels of evidence:

1. **Deterministic:** run **python -m unittest discover -s tests -v**. The 16 tests cover calculations, invalid inputs, unit and timestamp normalization, schema validation, template linting, source freshness, required package surfaces, schema parsing, version custody, distribution parity, archive topology, and release-manifest integrity.
2. **Installable:** install the branded plugin directly from this repository using the two commands in [INSTALL.md](INSTALL.md).
3. **Behavioral:** run the fictional late-flower incident in [JUDGE-QUICKSTART.md](JUDGE-QUICKSTART.md) and inspect whether CanopyOps preserves alternatives, authority, reversible containment, and an auditable record.

The release also records structural validation, plugin validation, archive round trips, a clean public installation, and a bounded three-case context-only safety/scope smoke.

## Judging map

### Technological implementation

Codex created and connected routing, deterministic programs, schemas, operational artifacts, behavioral evaluations, packaging invariants, plugin metadata, installation paths, and public verification. The capability is inspectable and runnable.

### Design

CanopyOps presents one coherent operating system from installation through evidence intake, analysis, decision support, record creation, review, and handoff. It includes onboarding, examples, safety boundaries, privacy guidance, support policy, licensing, and branded distribution.

### Potential impact

Cultivation teams routinely make consequential decisions from incomplete sensor data, crop observations, handwritten notes, vendor claims, and shifting regulations. CanopyOps turns that ambiguity into accountable evidence, explicit unknowns, named authority, and reusable records.

### Quality of the idea

The novelty is not “AI knows cannabis.” It is an AI capability designed as a governed operating institution: persona-led judgment, deterministic custody where exactness matters, explicit authority boundaries, operational memory, adversarial review, and honest release gates.

## Limits

CanopyOps is not field-validated, legal advice, medical advice, a pesticide authority, a batch-release authority, or an equipment controller. The public evidence does not establish universal behavioral reliability, current jurisdiction coverage, live Claude Code execution, or integration with cultivation hardware.

Those limitations are part of the design. A regulated-operations Agent that cannot say what it has not established is a liability wearing a chatbot hat.
