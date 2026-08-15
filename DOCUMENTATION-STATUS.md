# CanopyOps Documentation Status

Last substantive documentation remediation: **August 14, 2026**

## Status

The living repository documentation and GitHub Pages source now form one explicit customer journey:

- **v0.1.5** remains the repository-native source and plugin line.
- **v0.1.7** remains the separate settled portable bundle with static package evidence.
- Frozen package bytes and historical release records were preserved.
- README, Pages, installation, examples, safety, privacy, security, support, archive custody, and evidence pages agree on those boundaries.
- Three public visual roles use separate files, compositions, and aspect ratios: a 1500×600 README operations banner, a 1600×900 Pages environment hero, and a 1731×909 text-bearing social card.

The canonical version and platform map remains [`RELEASE-STATUS.md`](RELEASE-STATUS.md).

## Current customer journey

| User moment | Canonical surface |
|---|---|
| Understand the product and fit | [`README.md`](README.md) and the [project site](https://stunspot.github.io/CanopyOps/) |
| Choose the correct distribution | [`RELEASE-STATUS.md`](RELEASE-STATUS.md) |
| Install, verify discovery, update, remove, or recover | [`INSTALL.md`](INSTALL.md) |
| Reach first value | [`START-HERE.md`](START-HERE.md), [`JUDGE-QUICKSTART.md`](JUDGE-QUICKSTART.md), and [`EXAMPLE-TOUR.md`](EXAMPLE-TOUR.md) |
| Understand capabilities and boundaries | [`FAQ.md`](FAQ.md) and [`SAFETY-AND-SCOPE.md`](SAFETY-AND-SCOPE.md) |
| Understand privacy, network, storage, and security | [`DATA-AND-PRIVACY.md`](DATA-AND-PRIVACY.md) and [`SECURITY.md`](SECURITY.md) |
| Get help or contribute | [`SUPPORT.md`](SUPPORT.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Inspect rights and terms | [`LICENSE.md`](LICENSE.md), [`TERMS-OF-USE.md`](TERMS-OF-USE.md), and [`TRADEMARKS.md`](TRADEMARKS.md) |
| Inspect package and publication evidence | [`ARCHIVE-CUSTODY.md`](ARCHIVE-CUSTODY.md), [`VERIFICATION-v0.1.5.md`](VERIFICATION-v0.1.5.md), and the v0.1.7 package docs |

## Material repairs in this pass

- Rebuilt Pages from a polished but partial narrative into a complete installation-to-removal customer journey.
- Added host-specific installation and discovery verification, first-success guidance, representative inputs and outputs, configuration truth, troubleshooting, recovery, cleanup, privacy, security, support, rights, and evidence limits.
- Removed the mobile rule that hid four primary navigation links.
- Replaced README reuse of the Pages hero with a role-specific operations banner.
- Replaced the generic corporate-slide social card with original image-generated cultivation artwork carrying the exact product title and identifying line, then wired it to Open Graph and X/Twitter metadata.
- Corrected the current deterministic-suite count from 20 to 21.
- Corrected archive custody so an absent `backups/` path is not presented as a repository object; the frozen v0.1.7 receipt remains unchanged and explicitly scoped to packaging-stage custody.

## Verification

Run from the repository root:

```text
python -m unittest discover -s tests -v
```

The current suite contains **21 tests**. It covers calculations, record validation, package parity, repository-native version custody, portable-bundle custody, the historical release-manifest boundary, customer-document reachability, the canonical release story, and Pages-local assets.

Run the settled portable verifier from `releases/v0.1.7/`:

```text
python tools/verify_release.py .
```

A successful static check proves only the states it observes. It does not prove fresh-host installation, discovery, invocation, tool execution, field fitness, legal correctness, regulatory currency, or customer outcomes.

## Review custody

The current documentation review receipt is [`documentation-review.json`](documentation-review.json). The separate accessibility result is [`documentation-accessibility-review.json`](documentation-accessibility-review.json). Each record binds its verdict to the exact governed scope declared in `documentation-manifest.json`; any later change to a governed current document, site source, or visual invalidates that receipt and requires review again. Historical records are reviewed for context but remain outside the living-content fingerprint.

Historical v0.1.5 review and verification evidence remains retained under `verification/evidence/` and is not relabeled as current evidence.

## Still not established

This documentation work does not establish:

- cultivation-field fitness or production reliability;
- jurisdictional currency or legal correctness;
- live Codex, Claude.ai, or Claude Code behavior for every supported route;
- OpenAI Plugin Directory review, approval, publication, or discoverability;
- representative-user usability, localization, formal accessibility conformance, or exhaustive browser compatibility;
- equipment integration, direct control, pesticide authority, batch release, or customer outcomes.

Those boundaries are product truth, not missing decoration.