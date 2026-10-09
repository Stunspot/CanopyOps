# Open or install CanopyOps

Use the current **v0.3.0 portable crop workspace and skills**. A plugin is not required. Older native plugin and portable releases keep their historical identity; do not combine their files with this release.

## Verify the portable bundle

Download [CanopyOps-v0.3.0.zip](releases/v0.3.0/CanopyOps-v0.3.0.zip) and its [checksum](releases/v0.3.0/CanopyOps-v0.3.0.zip.sha256). Extract to a new directory. With Python 3.10+ available, open a terminal at the extracted release root and run:

```text
python tools/verify_release.py .
```

Continue when the command exits zero and reports `"ok": true` with no findings. If it fails, preserve any working records, obtain the canonical bundle and extract a fresh copy. Static verification checks package integrity; it does not prove host discovery or useful cultivation behavior.

## Open the crop desk

Inside the extracted bundle, open the launcher in `codex/canopyops/skills/canopyops/workspace/`. That path is the current payload location; it does not require plugin installation. The launcher opens a browser on this computer. Alternatively, run:

```text
python codex/canopyops/skills/canopyops/workspace/desk.py
```

Your records belong outside the extracted or installed product. The default is `Documents/CanopyOps`; `CANOPYOPS_DATA_HOME` selects another external store. Start with fictional data and confirm the desk shows your records or its empty-state capture action. See [the workspace guide](canopyops/workspace/WORKSPACE-GUIDE.md).

If startup fails, check Python 3.10+ and access to the external store. Leave unrelated services running; the launcher can select another local port. A browser opening alone is not a completed crop-work session.

## Add the Codex skill

Copy the complete extracted `codex/canopyops/skills/canopyops/` directory into your personal skill directory, keeping all its supporting folders beside `SKILL.md`. Current Codex manual user skills normally live at `~/.agents/skills/canopyops/`; use the host's actual configured skill location when different. The owner's existing `.codex/skills/canopyops/` is a maintained legacy installation, not a new-user prerequisite.

Open a fresh task, confirm CanopyOps is discoverable, then ask it to perform one [first job](START-HERE.md). If the host does not discover it, check the configured skill location and the complete directory layout. If discovery succeeds but invocation fails, retain the error and package identity for support; do not call the installation healthy from copied files alone.

## Use Claude

The complete bundle contains `claude/canopyops-v0.3.0.zip` for its documented custom-skill route. Follow the [package's Claude guide](releases/v0.3.0/docs/INSTALL-CLAUDE.md) and the controls exposed by your host. The local Python crop desk can also be opened independently. Upload, discovery, invocation and successful work are separate observations; fresh Claude activation remains unverified here.

## Update and return

Locate the active skill before changing it. Back up its current payload; preserve unknown local additions and keep the external record store untouched. Replace corresponding maintained product files, then start a fresh task to check discovery. Open the same external store to recover observations, handoffs, originals and revisions. Back up that store separately from the product.

Historical plugin custody and older release evidence are described in [release status](RELEASE-STATUS.md) and [archive custody](ARCHIVE-CUSTODY.md). Existing installations are not automatically removed or disabled by this guidance.
