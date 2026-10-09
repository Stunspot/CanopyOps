# Install the CanopyOps skill in Codex

## Verify and copy

Use an extracted `CanopyOps-v0.3.0.zip` bundle and Python 3.10+. From the release root, run `python tools/verify_release.py .`; require exit zero, `"ok": true` and no findings. A plugin is not required.

Copy the complete `codex/canopyops/skills/canopyops/` directory into the host's configured personal skill directory. Current manual user skills normally use `~/.agents/skills/canopyops/`; an existing owner-maintained legacy location may differ. Keep every supporting directory beside `SKILL.md`.

Open a fresh task, confirm CanopyOps is discoverable, then use the [quick start](QUICK-START.md). Verify discovery and actual invocation separately. Copying files alone proves neither.

## Open the workspace

Run the launcher in the skill's `workspace/` folder, or `python workspace/desk.py` from the installed skill directory. Keep operational records outside the installation. The default store is `Documents/CanopyOps`; `CANOPYOPS_DATA_HOME` selects another external directory. Read the [workspace guide](../codex/canopyops/skills/canopyops/workspace/WORKSPACE-GUIDE.md).

## Recover or update

If package verification fails, preserve working records and extract a fresh canonical bundle. If discovery fails, check the actual skill directory and complete supporting files. If invocation fails after discovery, retain the error and [support information](SUPPORT.md).

Before an update, locate and back up the active payload. Preserve unknown local additions and leave the external record store untouched. Replace corresponding maintained files, open a fresh task and check discovery. Reopen the same store to return to saved work. Existing historical plugin installations are not automatically removed or disabled.

Package integrity, discovery, invocation and useful work are different checks. Fresh customer-host and live Claude activation remain unverified.
