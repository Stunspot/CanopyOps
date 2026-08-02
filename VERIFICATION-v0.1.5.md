# CanopyOps v0.1.5 Verification

Verification date: **July 20, 2026**

> **Historical evidence record:** This document applies to the frozen v0.1.5 release candidate and the exact evidence named below. It does not certify later repository documentation, the GitHub Pages site, or the separate portable v0.1.6 package. See [`RELEASE-STATUS.md`](RELEASE-STATUS.md) and [`DOCUMENTATION-STATUS.md`](DOCUMENTATION-STATUS.md).

This record distinguishes checks actually run from behavior that remained untested. Passing package, archive, plugin-listing, or documentation checks did not establish cultivation-field fitness, legal correctness, live-host behavior, or accessibility conformance.

## Completed checks

| Check | Result | What it establishes |
|---|---|---|
| Repository deterministic suite | **18 of 18 tests passed** on the frozen release candidate | Calculations, record validation, version custody, canonical/plugin/Claude parity, customer-document reachability, release-manifest hashes, and OpenAI submission reproducibility behaved as asserted in that snapshot |
| Augment Builder profiles | Bundle, canonical Codex, plugin-bundled Codex, and Claude profiles passed | Required structure, metadata, contained resources, JSON, and private-path rules passed the then-current static profiles |
| Plugin-readiness audit | 1 skill; 0 errors; 0 warnings | The v0.1.5 manifest, HTTPS customer links, listing metadata, skill entry point, and version-bound PNG assets satisfied the deterministic publication preflight |
| Distribution parity | Canonical, plugin-bundled, and Claude.ai skill trees matched | Every supported v0.1.5 distribution carried the same CanopyOps operating skill; this did not prove host activation |
| Governed release archives | Complete Augment, Codex plugin, and standalone skill archives built and extracted byte-for-byte | `release-assets/v0.1.5/archive-custody.json` records source-tree and archive hashes, byte sizes, member counts, and extraction parity |
| OpenAI submission archive | Deterministic 76-member skills-only ZIP reproduced byte-for-byte | `release-assets/v0.1.5/openai-submission-custody.json` records the channel transform, archive hash, manifest hashes, and POSIX member paths |
| OpenAI draft creation | Listing, three prompts, one skill, and three capability tags saved under the verified Collaborative Dynamics Inc business identity; the skill passed automated scanning | Draft creation and scan success were observed; owner attestations, review submission, approval, publication, and discoverability were not |
| Listing-asset inspection | Canopy-grid icon inspected at 1024 and 32 pixels | The mark remained recognizable at listing size and used shape and contrast, rather than color alone; this was visual inspection, not accessibility conformance testing |
| Customer-document checks | 21 declared customer documents and tracked repository-local Markdown links passed deterministic validation | The v0.1.5 release identity and local navigation were coherent at the review cutoff; external destinations, representative users, and assistive technologies were not tested |

## Documentation review custody

This page records checks performed against other release artifacts; it is not the evidence source for its own statements.

The repository test output, Builder profile results, plugin-readiness audit, archived v0.1.5 repository manifest, archive-custody ledger, and retained reviewer records provide evidence outside this prose summary.

The independent Hesperos review covered the 20-document pre-draft corpus. The subsequently added Plugins Directory packet was included in the 21-document deterministic inventory but did not receive a new independent accessibility review. The current review record is retained in `documentation-review.json` as a historical snapshot.

## Inherited behavioral evidence

The operating kernel was unchanged from v0.1.4. The reviewed three-case context-only safety and scope smoke retained from v0.1.2 remained inherited evidence under its original runtime and prompts. It was not rerun and was not new v0.1.5 behavioral evidence.

## Not established

This release did not establish:

- fresh Codex marketplace installation, plugin discovery, task activation, live resource loading, or script execution under customer permissions;
- live Claude.ai upload, enablement, activation, progressive loading, script execution, or persistence;
- broad repeated-model behavior, cultivation-field fitness, or production reliability;
- current jurisdiction coverage, legal advice, regulatory approval, or compliance certification;
- equipment integration, direct control, batch-release authority, or customer outcomes;
- browser, keyboard, screen-reader, localization, representative-user, or formal accessibility-conformance testing;
- owner policy attestations, submission for review, approval, public Directory appearance, or discoverability.

## Current verification routes

- Current repository suite: `python -m unittest discover -s tests -v`
- Portable v0.1.6 verifier: extract the bundle, then run `python tools/verify_release.py .`
- Current release map: [`RELEASE-STATUS.md`](RELEASE-STATUS.md)

Those later routes produce their own evidence. They do not retroactively alter this v0.1.5 record.
