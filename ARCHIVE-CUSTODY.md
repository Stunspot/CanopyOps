# CanopyOps v0.1.5 archive custody

CanopyOps keeps one canonical source tree and several independently useful release objects. The objects are deliberately named so a customer or custodian can tell an Augment, plugin, standalone skill, and host upload apart without opening the ZIP.

| Object | Canonical release artifact | Use |
|---|---|---|
| Complete Augment | `release-assets/v0.1.5/CanopyOps-v0.1.5.zip` | Portable full CanopyOps capability tree |
| Codex plugin | `release-assets/v0.1.5/Plugin-CanopyOps-v0.1.5.zip` | Branded Codex plugin, manifest, assets, and bundled skill |
| Standalone skill | `release-assets/v0.1.5/Skill-canopyops--CanopyOps-v0.1.5.zip` | Direct skill installation and subskill custody |
| Claude.ai upload | `claude-ai/canopyops-v0.1.5.zip` | One-top-level-folder Claude.ai upload package |
| Source repository | Git tag `v0.1.5` and its GitHub source archives | Versioned source, documentation, tests, and provenance |

`release-assets/v0.1.5/archive-custody.json` records exact hashes, sizes, member counts, source-tree digests, and extraction-parity results for the governed archives. GitHub release assets and the latest-only convenience backup shelf must match those hashes. Canonical release assets are copied, never moved, to the backup shelf. Older same-family convenience copies may be removed only after the new copies match; unrelated products are untouched.

The standalone skill and Claude.ai upload intentionally carry the same skill content under host-appropriate names. Archive equality does not establish live-host activation.

