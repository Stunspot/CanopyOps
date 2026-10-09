![A cultivation operations desk with review charts, environmental instruments, tagged samples, and a controlled crop room beyond.](docs/assets/canopyops-readme-hero.png)

# CanopyOps

**Evidence-bounded cultivation operations for lawful cannabis teams.**

CanopyOps is an installable AI skill for cannabis cultivation that turns room data, crop observations, logs, and facility constraints into reviewable crop plans, incident workups, transparent calculations, harvest-readiness reviews, CAPA, runbooks, and operating records—while keeping evidence, uncertainty, ownership, and human authority visible.

**[Open the project site →](https://stunspot.github.io/CanopyOps/)** · **[Start here](START-HERE.md)** · **[Install](INSTALL.md)** · **[Choose the correct release](RELEASE-STATUS.md)**

## What CanopyOps does

- **Plans rooms and crops** from facility limits, crop stage, cultivar information, measurement methods, targets, labor, and unresolved decisions.
- **Works incidents without pet theories** by preserving competing explanations and separating reversible containment from cause-specific correction.
- **Calculates transparently** across VPD, DLI, irrigation, runoff, dryback, EC, pH, and normalized units.
- **Reviews harvest and quality evidence** without confusing schedule pressure, interpretation, holds, recommendation, and release authority.
- **Produces operating memory** through incident reports, CAPA, risk registers, room runbooks, crop walks, drying logs, cultivation decisions, and shift handoffs.

## Open the crop workspace

The v0.3.0 portable workspace keeps supplied observations in room, zone and time context. Compare compatible measurements and pairs of observations without losing their timestamps, methods and evidence. Understory, Lampblack and Clearspan offer three distinct environments. Open the launcher in the packaged `workspace/` folder with Python 3.10+, or ask your installed CanopyOps agent to open it. Read [the workspace guide](canopyops/workspace/WORKSPACE-GUIDE.md).

## Why it is different

CanopyOps does not flatten every sentence into “the AI says so.” It preserves nine distinct states:

`observed → measured → calculated → assumed → interpreted → recommended → approved → executed → verified`

A supplied target remains a **comparison value** until its source, crop stage, scope, tolerance, measurement method, and accountable approval establish an **active target**. A recommendation never becomes authorization merely because it sounds polished.

Facility SOPs, emergency procedures, current approved labels, current jurisdiction sources, qualified laboratory evidence, equipment documentation, and accountable humans govern and override model output.

## Try it in five minutes

Install CanopyOps, start a fresh task, and use fictional or sanitized data:

> Use CanopyOps for a fictional licensed cultivation facility. A late-flower room held 27 C and 78% RH for 42 minutes overnight. One wall sensor recorded the excursion; its calibration status and exact canopy position are unknown. The active target is 25 C and no more than 60% RH, but I have not supplied the approved source or tolerance. Build a provisional incident workup and incident record. Preserve competing explanations, distinguish reversible containment from cause-specific correction, identify the evidence that would change the next decision, and do not claim that any setting was approved or changed.

A useful result should expose missing measurement context, avoid treating one sensor as whole-room proof, preserve plausible alternatives, propose only bounded next steps, and end with an explicit status such as **provisional** or **awaiting authority**.

The complete path is in [`JUDGE-QUICKSTART.md`](JUDGE-QUICKSTART.md).

## Current delivery

**v0.3.0 portable crop workspace and maintained skills** are the current CanopyOps delivery. Open the local desk with Python 3.10+, or install the contained skill in your host. A plugin is not required. Start with [installation](INSTALL.md), [the first job](START-HERE.md) and [the workspace guide](canopyops/workspace/WORKSPACE-GUIDE.md).

The repository-native v0.1.5 plugin and older portable bundles remain historical material with their original provenance. Their packaging is not a current repair obligation. Read [release status](RELEASE-STATUS.md) for publication boundaries and evidence limits.

## What it produces

CanopyOps works primarily in readable Markdown, CSV, and JSON. Included templates cover:

- facility and crop profiles;
- crop plans and room runbooks;
- incident reports and CAPA;
- cultivation decisions and compliance-verification briefs;
- risk registers, crop walks, drying logs, and shift handoffs;
- harvest-readiness reviews with explicit holds and authority.

See [`EXAMPLE-TOUR.md`](EXAMPLE-TOUR.md) for four complete fictional demonstrations.

## Evidence and limitations

The repository includes a **21-test deterministic suite** covering calculations, validation, package parity, version custody, documentation reachability, release-story consistency, and Pages-local assets. The historical v0.1.5 verification record documents the checks executed against that release candidate. The v0.3.0 workspace bundle carries its own freshly generated portable verifier report. Older test/review records remain attached to the releases they examined.

These are different claims:

- a file exists;
- a package validates;
- a host discovers the skill;
- an invocation reaches the intended workflow;
- the tools are healthy;
- the behavior is useful;
- a cultivation decision is correct;
- a human is authorized to act.

CanopyOps does not collapse them. No field pilot, broad reliability guarantee, current jurisdiction coverage, legal opinion, pesticide authorization, batch-release authority, direct equipment control, or customer outcome is claimed.

- [Current release and platform status](RELEASE-STATUS.md)
- [Current documentation status](DOCUMENTATION-STATUS.md)
- [v0.1.5 verification record](VERIFICATION-v0.1.5.md)
- [Safety and scope](SAFETY-AND-SCOPE.md)
- [Data and privacy](DATA-AND-PRIVACY.md)
- [Security](SECURITY.md)

## Built with Codex and GPT-5.6 during OpenAI Build Week

CanopyOps was conceived and built on July 17, 2026, during the OpenAI Build Week submission period. Stun supplied the product intent, source material, Ella Greenfield persona, domain and authority boundaries, evaluation philosophy, and release judgment. Codex with GPT-5.6 turned that direction into the routed skill, deterministic utilities, schemas, templates, evaluations, host adapters, documentation, licensing, packaging, verification, and public repository.

The initial working Augment emerged in roughly an hour; public packaging, branding, hardening, documentation, and release custody continued afterward. Read [`BUILD-WEEK.md`](BUILD-WEEK.md) for the architecture, provenance, and human/AI responsibility split.

## Repository map

- [`canopyops/`](canopyops/) — shared cultivation source with current portable-workspace authoring under `workspace/`; the branded native plugin remains separately versioned.
- [`plugins/canopyops/`](plugins/canopyops/) — branded repository-native Codex plugin.
- [`claude-ai/`](claude-ai/) — repository-native Claude.ai upload archives.
- [`releases/v0.3.0/`](releases/v0.3.0/) — current portable crop workspace, checksums, manifest, receipt and docs. Older versioned releases retain their historical custody.
- [`tests/`](tests/) — deterministic repository checks.
- [`docs/`](docs/) — GitHub Pages source and the three governed role-specific raster assets.
- [`verification/`](verification/) — retained evidence and review custody.
- [`release-assets/v0.1.5/`](release-assets/v0.1.5/) — governed v0.1.5 release objects and custody records.

## License, identity, and support

CanopyOps is a Collaborative Dynamics Augment created by Sam Walker (stunspot), with the Ella Greenfield cultivation persona operating inside an evidence-bounded lawful-market system.

The authentic unmodified authored Augment uses `CC-BY-ND-4.0`; Python scripts, tests, and machine-readable schemas use MIT. Names and marks remain governed by the trademark policy.

- [License](LICENSE.md)
- [Attribution](ATTRIBUTION.md)
- [Trademark policy](TRADEMARKS.md)
- [Support](SUPPORT.md)
- [Contributing](CONTRIBUTING.md)
