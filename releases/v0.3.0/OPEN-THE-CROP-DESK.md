# CanopyOps crop workspace

See where observations belong, how they changed, and which evidence deserves a closer look. The room and zone schematic, through-date view, measurement plot and observation comparison share your native records with your agent. Understory, Lampblack and Clearspan offer three distinct working environments; see [the skin guide](codex/canopyops/skills/canopyops/workspace/SKINS.md).

Open `Open CanopyOps.cmd` on Windows or `Open CanopyOps.command` on macOS with Python 3.10+. Or ask your agent to “Open CanopyOps.” Follow [the workspace guide](codex/canopyops/skills/canopyops/workspace/WORKSPACE-GUIDE.md) for room exploration, evidence comparison, capture, editing and recovery.

Records live outside the installation in `CANOPYOPS_DATA_HOME`, otherwise `Documents/CanopyOps`. The workspace reads `crop-walk.csv` and room, batch, incident and handoff Markdown files. Imports retain original bytes under `imports`; saves refuse stale hashes and preserve prior content under `history`. Photos keep relative references. Back up the external store separately from the package.

The schematic groups supplied rooms and zones; it does not assert their physical shape or distance. Plots show supplied measurements with compatible provenance, not a continuous sensor stream. Unknown timestamps, absent observations and incomplete measurement context stay visible. Illustrative examples are labeled and unsaved. The generated canopy atmosphere is decoration, not a crop photograph or measurement.

Loopback only: no equipment control, sensor connection or network publication. A narrow host-browser view is supported; a separate network phone is not. macOS and fresh customer-host launches remain unverified. Shortcuts are optional, never silently installed.

The launchers are in `codex/canopyops/skills/canopyops/workspace/` inside this extracted bundle.
