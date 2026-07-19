# CanopyOps v0.1.4 release notes

Release date: 2026-07-18

CanopyOps v0.1.4 is a documentation-custody and release-integrity patch. It preserves the v0.1.3 operating kernel while bringing customer documentation, evaluation metadata, distribution copies, and release evidence under one current version boundary.

## What changed

- Updated installation, privacy, security, FAQ, and release-status documentation to describe the current package and all three distribution forms.
- Advanced the canonical evaluation manifest and case files to package version `0.1.4`.
- Added regression checks for version custody, standalone/plugin/archive parity, archive topology, and release-manifest hashes.
- Added a reproducible SHA-256 release manifest and rebuilt the Claude.ai archive from the canonical skill tree.

## Verification

- The standalone `canopyops/` tree passes the current Augment Builder Codex and Claude profiles.
- The plugin-bundled skill and Claude.ai archive match the standalone tree byte-for-byte.
- The Claude.ai ZIP uses portable paths and contains exactly one top-level `canopyops/` folder.
- The canonical evaluation package validates at version `0.1.4`.
- The deterministic repository test suite, accessible-Markdown lint, local-link check, and release-manifest verification pass.

See [VERIFICATION-v0.1.4.md](VERIFICATION-v0.1.4.md) for the exact checks, results, reviewer disposition, and untested boundaries.

## Evidence boundary

The operating kernel is unchanged, so the reviewed three-case context-only safety/scope smoke recorded for v0.1.2 remains inherited evidence rather than a new behavioral run. Live Claude.ai upload, enablement, activation, progressive resource loading, script execution, and persistence were not exercised for v0.1.4. Live Claude Code execution, field use, equipment integration, current jurisdiction coverage, representative-user testing, and formal accessibility or legal assessment also remain unverified. Structural compatibility and static documentation checks are not live-host, field-fitness, or accessibility-conformance claims.

## License

The existing CanopyOps licensing and trademark terms are unchanged. CanopyOps remains free and publicly available under the terms described in [LICENSE.md](LICENSE.md) and [TRADEMARKS.md](TRADEMARKS.md).
