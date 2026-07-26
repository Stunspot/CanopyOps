# CanopyOps Documentation Status

Last editorial reconciliation: **July 25, 2026**

## Status

The living repository documentation has been reconciled around one explicit release story:

- **v0.1.5** is the repository-native source and plugin line.
- **v0.1.6** is a separate settled portable bundle with static package evidence.
- Historical verification, review, and Plugins Directory records remain historical and retain their original scope.
- The GitHub Pages site, root README, onboarding, installation, FAQ, privacy, security, support, archive, and evidence documents now point to [`RELEASE-STATUS.md`](RELEASE-STATUS.md) instead of implying one undifferentiated “current version.”

## Current customer journey

| User moment | Canonical document |
|---|---|
| Understand the product | [`README.md`](README.md) |
| Choose the correct distribution | [`RELEASE-STATUS.md`](RELEASE-STATUS.md) |
| Reach first value | [`START-HERE.md`](START-HERE.md) |
| Install or remove it | [`INSTALL.md`](INSTALL.md) |
| Run a fictional judge path | [`JUDGE-QUICKSTART.md`](JUDGE-QUICKSTART.md) |
| Understand normal use | [`FAQ.md`](FAQ.md) and [`SAFETY-AND-SCOPE.md`](SAFETY-AND-SCOPE.md) |
| Handle privacy or security | [`DATA-AND-PRIVACY.md`](DATA-AND-PRIVACY.md) and [`SECURITY.md`](SECURITY.md) |
| Report or recover from a problem | [`SUPPORT.md`](SUPPORT.md) |
| Inspect release and archive evidence | [`VERIFICATION-v0.1.5.md`](VERIFICATION-v0.1.5.md), [`ARCHIVE-CUSTODY.md`](ARCHIVE-CUSTODY.md), and the v0.1.6 package docs |

## What was repaired

- Reordered the README around audience, jobs, first value, outputs, status, installation, evidence, and provenance.
- Replaced vague “the release” language with channel-specific version and artifact names.
- Corrected the judge path so its expected test count matches the current suite.
- Added current official OpenAI and Anthropic platform references without treating external platform documentation as proof of CanopyOps availability.
- Marked v0.1.5 release notes, verification, Plugins Directory custody, and the prior Hesperos review as historical records rather than current-HEAD certificates.
- Added deterministic checks for the release-status contract, customer-document inventory, local Markdown links, Pages assets, and package-line separation.
- Preserved frozen v0.1.6 package bytes and their detached evidence instead of rewriting a settled archive to make the prose look tidy.
- Replaced the misleading root all-tree checksum role with a small `release-manifest.json` custody router and archived the former v0.1.5 repository snapshot intact.

## Verification

Run from the repository root:

```text
python -m unittest discover -s tests -v
```

The current suite contains **20 tests**. The checks cover calculations, record validation, package parity, repository-native version custody, portable-bundle custody, the historical release-manifest boundary, customer-document reachability, the canonical release story, and Pages-local assets.

The GitHub Actions result is the execution evidence. This page does not self-certify a run merely because the command is printed here.

## Review custody

The prior Hesperos review remains valid for the exact v0.1.5 document snapshot it examined. Its record is retained in [`documentation-review.json`](documentation-review.json) and under `verification/evidence/`.

That review did **not** cover the later Pages site, the v0.1.6 portable estate, or this reconciliation. The current pass is a maintainer/editorial reconciliation with deterministic checks, not a falsely relabeled independent fresh-context review.

## Still not established

This documentation work does not establish:

- cultivation-field fitness or production reliability;
- jurisdictional currency or legal correctness;
- live Codex, Claude.ai, or Claude Code behavior for every supported path;
- OpenAI Plugin Directory review, approval, publication, or discoverability;
- representative-user usability, localization, browser compatibility, keyboard testing, screen-reader testing, or formal accessibility conformance;
- equipment integration, direct control, pesticide authority, batch release, or customer outcomes.

Those boundaries are product truth, not missing decoration.
