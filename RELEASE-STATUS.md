# CanopyOps Release Status

Last reconciled: **July 25, 2026**

## Canonical answer

CanopyOps currently has **two intentionally separate distribution lines**. They carry the same cultivation-operations method, but they are packaged, verified, and installed differently.

| Distribution line | Version | Use it when | Evidence boundary |
|---|---:|---|---|
| **Repository-native source and plugin** | **v0.1.5** | You want the direct GitHub marketplace commands, the root `canopyops/` skill tree, the branded `plugins/canopyops/` plugin, or the root Claude upload ZIP. | The root test suite, v0.1.5 verification record, archive-custody ledger, and Plugins Directory draft packet apply to this line at their stated dates and scopes. |
| **Settled portable bundle** | **v0.1.6** | You want one self-verifying ZIP with Codex and Claude payloads, detached checksums, a package manifest, a portable verifier, and package-specific installation guides. | The bundle establishes static package structure, byte parity, archive membership, and documented custody. It does **not** establish host activation, invocation quality, field fitness, publication, or customer outcomes. |

Do not mix files from the two lines. A version number identifies a package boundary; it is not evidence that a host installed, loaded, or successfully used that package.

## Recommended routes

### Direct GitHub installation

Use the **v0.1.5 repository-native plugin**:

```text
codex plugin marketplace add Stunspot/CanopyOps
codex plugin add canopyops@collaborative-dynamics
```

Then start a fresh Codex task. This is the shortest repository-native route documented by this project.

### Portable or offline verification

Use the **v0.1.6 settled bundle**:

- [`releases/v0.1.6/CanopyOps-v0.1.6.zip`](releases/v0.1.6/CanopyOps-v0.1.6.zip)
- [`releases/v0.1.6/CanopyOps-v0.1.6.zip.sha256`](releases/v0.1.6/CanopyOps-v0.1.6.zip.sha256)
- [`releases/v0.1.6/docs/README.md`](releases/v0.1.6/docs/README.md)

Extract it into a new directory and run:

```text
python tools/verify_release.py .
```

Require exit code `0`, `"ok": true`, and an empty findings list before attempting installation.

### Claude.ai or Claude Code

The repository-native v0.1.5 line includes `claude-ai/canopyops-v0.1.5.zip`. The portable v0.1.6 bundle includes `claude/canopyops-v0.1.6.zip` and package-specific Claude instructions. Both are packaged skill surfaces; neither is presented here as proof of a successful live upload or runtime invocation.

Current Claude skill setup is documented by Anthropic at:

- https://support.claude.com/en/articles/12512180-use-skills-in-claude
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

## Current public-state ledger

| Surface | Current documented state |
|---|---|
| **GitHub repository** | Public and installable through the repository-native route, subject to the user’s Codex build and workspace controls. |
| **GitHub Pages** | Live documentation site. Publication proves only that the static site deployed. |
| **OpenAI Plugin Directory** | A v0.1.5 skills-only draft was created and scanned on July 20, 2026. Owner attestations, review submission, approval, publication, and discoverability were not recorded. The historical packet is [`PLUGIN-DIRECTORY-SUBMISSION-v0.1.5.md`](PLUGIN-DIRECTORY-SUBMISSION-v0.1.5.md). |
| **Claude.ai** | Upload archives are packaged. Live upload, enablement, invocation, resource loading, and script execution are not recorded as current evidence. |
| **Claude Code** | Skill layouts and adapters are packaged. Live runtime execution is not recorded as current evidence. |
| **Cultivation operations** | No field pilot, regulatory approval, legal opinion, pesticide authorization, batch-release authority, equipment integration, or production reliability claim is made. |

OpenAI’s current public explanation of Plugins in ChatGPT and Codex is available at https://help.openai.com/en/articles/20001256-plugins-in-codex. Directory visibility or a draft record must not be confused with public availability.

## Evidence map

- Root repository behavior and v0.1.5 release evidence: [`VERIFICATION-v0.1.5.md`](VERIFICATION-v0.1.5.md)
- Root archive and distribution custody: [`ARCHIVE-CUSTODY.md`](ARCHIVE-CUSTODY.md)
- Manifest router for artifact-scoped evidence: [`release-manifest.json`](release-manifest.json)
- Portable v0.1.6 validation: [`releases/v0.1.6/docs/VALIDATION.md`](releases/v0.1.6/docs/VALIDATION.md)
- Current documentation scope: [`DOCUMENTATION-STATUS.md`](DOCUMENTATION-STATUS.md)
- Product safety and authority boundary: [`SAFETY-AND-SCOPE.md`](SAFETY-AND-SCOPE.md)

## Maintenance rule

A future release may unify these distribution lines. Until that happens, every customer-facing document must preserve the distinction above. Historical evidence remains attached to the exact artifact and date it examined; it is never silently promoted to a newer package or to live-host behavior.
