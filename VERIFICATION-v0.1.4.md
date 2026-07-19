# CanopyOps v0.1.4 verification

Verification date: 2026-07-18

This record distinguishes checks that were actually run from behavior that remains untested. Passing a package or documentation check does not establish cultivation-field fitness, legal correctness, host behavior, or accessibility conformance.

## Completed checks

| Check | Result | What it establishes |
|---|---|---|
| Repository deterministic suite | 16 of 16 tests passed | Calculations, record validation, version custody, distribution parity, archive topology, and release-manifest hashes behaved as asserted. |
| Augment Builder package validation | Codex and Claude profiles passed for both standalone and plugin-bundled skill trees | Required structure, metadata, contained resources, JSON, and private-path rules passed the current static profiles. |
| Evaluation-package validation | 8 cases valid at package version `0.1.4` | The canonical evaluation definitions are parseable, version-aligned, and contain their declared indispensable dimensions. This validation did not execute all eight behavioral cases. |
| Distribution parity | Standalone, plugin-bundled, and Claude.ai archive skill trees matched byte-for-byte | The three distributions contain the same CanopyOps skill content. |
| Claude.ai archive inspection | One `canopyops/` top-level folder; portable paths | The supplied ZIP has the intended upload topology. It does not prove Claude.ai activation or script execution. |
| Customer-document Markdown lint | 19 current root documents passed | The checked documents had no heading skips, generic link labels, empty image alternatives, reflow-sensitive directional wording, or unsupported conformance wording detected by the static linter. |
| Local-link inspection | 51 local targets across 115 Markdown files resolved | The inspected repository-local document and image targets existed. External web destinations were not live-tested by this check. |
| Fresh-context Hesperos review | `REVIEW_PASS`; evaluator score 100 | A local Qwen 3.5 reviewer inspected the 13-file customer documentation set for product truth, customer path, safe recovery, accessible structure, and evidence honesty. This is model-review evidence, not representative-user or assistive-technology testing. |

The MIT license text was excluded from the customer-document lint because a legally conventional directional phrase triggers the linter's reflow-language heuristic. The license was not rewritten to satisfy that false positive.

## Inherited behavioral evidence

The operating kernel is unchanged from v0.1.3. The reviewed three-case context-only safety and scope smoke recorded for v0.1.2 remains inherited evidence under its original runtime and prompts. It was not rerun and must not be described as new v0.1.4 behavioral evidence.

## Not established

This release does not establish:

- live Claude.ai upload, enablement, activation, progressive loading, script execution, or persistence;
- live Claude Code execution;
- representative-user or assistive-technology testing;
- formal accessibility conformance;
- cultivation-field fitness or broad behavioral reliability;
- current jurisdiction coverage, legal advice, or regulatory approval;
- equipment integration, direct control, or batch-release authority;
- official OpenAI Plugins Directory appearance.

These remain future evidence obligations, not implied capabilities.
