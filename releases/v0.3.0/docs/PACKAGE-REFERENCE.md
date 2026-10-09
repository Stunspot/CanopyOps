# CanopyOps: package reference

The outer `canopyops-v0.3.0` directory contains `codex/canopyops/`, the Claude skill ZIP under `claude/`, these thirteen guides under `docs/`, `tools/verify_release.py`, manifests and static verification records. `OPEN-THE-CROP-DESK.md` links to the workspace entry path. The three customer sidecars live under `delivery-sidecars/` as a convenience; they are not runtime skill files.

The Codex payload's `skills/canopyops/workspace/` contains the local Python server, HTML, JavaScript, styles, decorative artwork, launchers and workspace guides. The Claude ZIP contains the same skill files. Operational records are excluded.

The canonical archive is `CanopyOps-v0.3.0.zip`. Its detached `receipt.json` and `.sha256` file live beside it because an archive cannot contain its own final digest. [manifest.json](../manifest.json) binds the skill files and nested Claude archive. [verification-report.json](../verification-report.json) records a fresh static check; [package-receipt.json](../package-receipt.json) describes its claim boundary.
