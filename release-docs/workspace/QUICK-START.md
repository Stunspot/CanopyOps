# Your first useful CanopyOps session

Extract `CanopyOps-v0.3.0.zip` into a new folder. From the extracted release root, run `python tools/verify_release.py .` and require `"ok": true` with no findings. Then install the [Codex skill](INSTALL-CODEX.md) or [Claude skill](INSTALL-CLAUDE.md) if you want agent guidance.

## Open the crop workspace

With Python 3.10+ available, open `Open CanopyOps.cmd` on Windows or `Open CanopyOps.command` on macOS inside `codex/canopyops/skills/canopyops/workspace/`. A local agent can also respond to “Open CanopyOps.” The browser opens on this computer's loopback address. macOS launch behavior has not been verified here.

Your records live in `Documents/CanopyOps`, or an external directory selected with `CANOPYOPS_DATA_HOME`. Capture one real observation or import a native record. If you want to inspect the experience first, explore the labeled example; it is separate from your store. Choosing Record observation returns to your real store before opening capture.

Choose a room and zone, revisit observations through the end of a UTC date, and open their evidence. Compare compatible measurement series or two observations. Open the record library for room plans, incidents and handoffs. The [workspace guide](../codex/canopyops/skills/canopyops/workspace/WORKSPACE-GUIDE.md) explains the controls and conflict recovery.

## Ask for cultivation reasoning

In a fresh task, invoke CanopyOps with: “Assess this cultivation decision and its safe next steps.” Supply jurisdiction, room and crop/stage, your decision or symptom, timestamped observations, measurement units/method/location, recent changes and facility constraints. CanopyOps distinguishes evidence from assumptions and identifies the next consequential step with its authority boundary.

If the wrong package opens, check its location and version before changing files. If a save reports a changed record, export your draft and reconcile with the current file. See [support](SUPPORT.md) for recovery.
