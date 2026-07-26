# CanopyOps Archive and Distribution Custody

Read [`RELEASE-STATUS.md`](RELEASE-STATUS.md) for the current channel map.

CanopyOps currently preserves two intentionally separate package lines. Their artifacts must remain identifiable without opening a ZIP, and evidence must stay attached to the exact object it examined.

## Distribution map

| Line | Object | Canonical path | Purpose |
|---|---|---|---|
| **Repository-native v0.1.5** | Source skill | `canopyops/` | Canonical repository-native skill tree |
|  | Codex plugin | `plugins/canopyops/` | Branded local/plugin-marketplace installation |
|  | Claude.ai upload | `claude-ai/canopyops-v0.1.5.zip` | Repository-native Claude skill upload |
|  | Complete Augment archive | `release-assets/v0.1.5/CanopyOps-v0.1.5.zip` | Governed v0.1.5 capability archive |
|  | Codex plugin archive | `release-assets/v0.1.5/Plugin-CanopyOps-v0.1.5.zip` | Governed v0.1.5 plugin package |
|  | Standalone skill archive | `release-assets/v0.1.5/Skill-canopyops--CanopyOps-v0.1.5.zip` | Governed v0.1.5 skill package |
|  | OpenAI portal derivative | `release-assets/v0.1.5/Plugin-CanopyOps-v0.1.5-OpenAI-Submission.zip` | Skills-only draft upload; not a replacement for the installable plugin |
| **Portable v0.1.6** | Canonical bundle | `releases/v0.1.6/CanopyOps-v0.1.6.zip` | Self-verifying cross-host package |
|  | Detached checksum | `releases/v0.1.6/CanopyOps-v0.1.6.zip.sha256` | SHA-256 comparison outside the archive |
|  | Package manifest | `releases/v0.1.6/manifest.json` | Source, payload, archive, and package identity |
|  | Release receipt | `releases/v0.1.6/receipt.json` | Canonical/backup copy and checksum custody |
|  | Package docs | `releases/v0.1.6/docs/` | Installation, validation, limitations, evidence, and maintenance |
|  | Convenience backup | `backups/CanopyOps-v0.1.6.zip` | Copy of the canonical bundle, not the canonical source |

## v0.1.5 custody

The v0.1.5 estate records exact hashes, sizes, member counts, source-tree digests, extraction parity, and the deterministic OpenAI submission transform under `release-assets/v0.1.5/`.

The OpenAI submission ZIP is a channel-specific derivative. It does not replace the complete Augment, installable plugin, standalone skill, or Claude archive.

The root `release-manifest.json` is now a **custody router**, not a checksum of current repository HEAD. It points to the package-scoped v0.1.5 custody records, the v0.1.6 package manifest and receipt, the current documentation manifest, and an archived copy of the former repository snapshot at `verification/evidence/release-manifest-v0.1.5-pages-snapshot.json`.

Current living-document consistency is governed by `documentation-manifest.json`, the root test suite, and [`DOCUMENTATION-STATUS.md`](DOCUMENTATION-STATUS.md).

## v0.1.6 custody

The portable v0.1.6 bundle is a settled package with its own self-contained evidence.

Before installation:

```text
python tools/verify_release.py .
```

The verifier checks package structure, manifest relationships, Codex and Claude payloads, archive membership, path safety, and recorded byte identities. See [`releases/v0.1.6/docs/VALIDATION.md`](releases/v0.1.6/docs/VALIDATION.md).

The v0.1.6 package preserves the CanopyOps operating kernel while changing package topology, custody, and verification. It does not inherit new behavioral, field, host-activation, or publication evidence merely because its version number is higher.

## Copy, move, and retention rules

- Canonical release artifacts are copied to backup locations; they are not moved away from canonical custody.
- A backup is accepted only after its hash matches the canonical object.
- Latest-only convenience copies may be replaced only after the new copy verifies.
- Unrelated products and historical release evidence remain untouched.
- Frozen release packages are not edited in place to repair living repository prose.
- A changed package receives a new version, manifest, checksum, and receipt.
- Operational cultivation records never belong inside a release archive or installed skill tree.

## Evidence boundaries

These states remain separate:

1. source file exists;
2. archive exists;
3. checksum matches;
4. archive extracts safely;
5. payload matches its manifest;
6. host installs or imports it;
7. host discovers the skill;
8. invocation reaches the intended workflow;
9. tools execute;
10. behavior meets the requested standard;
11. a human authorizes operational action;
12. the outcome is verified.

Archive custody establishes only the states its records and tools actually observe.

## Historical records

- [`RELEASE-NOTES-v0.1.5.md`](RELEASE-NOTES-v0.1.5.md) describes the v0.1.5 identity and custody release.
- [`VERIFICATION-v0.1.5.md`](VERIFICATION-v0.1.5.md) records v0.1.5 checks at their evidence cutoff.
- [`PLUGIN-DIRECTORY-SUBMISSION-v0.1.5.md`](PLUGIN-DIRECTORY-SUBMISSION-v0.1.5.md) records the v0.1.5 draft-submission state.
- [`releases/v0.1.6/docs/README.md`](releases/v0.1.6/docs/README.md) is the entry point for the portable bundle.

Historical evidence is preserved, not quietly rewritten into a certificate for current HEAD.
