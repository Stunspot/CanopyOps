# Read the room, follow the evidence

Open the Windows or macOS launcher in this folder with Python 3.10+, or ask your agent to “Open CanopyOps.” The browser opens on this computer. Your agent and this workspace use the same external files.

## Begin with your room

The room overview groups the observations you have actually supplied. Choose a room, then a zone to narrow the same evidence without losing the room context. The schematic is a visual index of named zones; positions and sizes do not represent a surveyed floor plan. A room without observations is unknown, not healthy.

Use the through-date control to revisit evidence up to the end of a chosen UTC date. The observation trail displays local time, and evidence details retain the original source timestamp; the filter is explicitly labeled UTC. Read each observation's actual timestamp: the newest entry is still a historical observation, not proof of the room's condition now. Entries with unusable or missing timestamps cannot establish a dated trend.

If the store is empty, capture your first observation, import an existing record, or explore the clearly labeled example. Example observations are illustrative, remain separate from your records, and are not saved by exploring them. Choosing Record observation while exploring the example returns to your real records before opening capture.

## Compare what can be compared

Select a measurement series to see discrete supplied readings. Series remain separate when their measurement context differs; units, method, sensor or tool, room and crop context matter. A plotted change is a change in the recorded value, not a diagnosis or an approved response. Do not infer an acceptable band from the shape of a chart.

Select two observations to inspect their evidence together. Compare affected and unaffected zones, or revisit one zone over time. Read timestamp, crop and stage, observer, method, sensor/tool, distribution, condition and any attached photo or record before deciding whether a difference is meaningful. Evidence details preserve the original supplied context.

## Capture the next observation

The crop-walk capture form records a room, observer and observed condition. A numerical measurement also requires its unit, method and sensor/tool. Add zone, crop, stage, distribution, severity, incident reference and other context when available. Attach a PNG, JPEG or WebP photo if useful. Capture preserves observations; it does not infer a cause, approve a target or execute corrective work.

Observations append to `crop-walk.csv` using the native columns. If another writer changed the CSV, reload before retrying. Custom CSV columns remain editable as native text rather than being silently remapped by the capture form.

## Carry the next shift

Open room runbooks, crop plans, incidents and shift handoffs in the record library. When you or your agent write native files directly, use `handoffs/` for the Handoff view and `incidents/` for the Incidents view. Library can find records outside those folders; a filename containing “handoff” alone does not place it in Handoff. Keep working files separate from preserved `history/` and `imports/` material. Read the supplied operational foreground, owner, next action and reopen condition. Use the library’s originals/revisions control to include preserved imports and earlier saves when you need to reconcile an edit. Those preserved files open read-only; Export gives you a working copy. Use the original editor for an explicit change to a current working record. The reading view reflects your text and does not certify its authority.

Save writes the native file after checking the hash from your last read. A changed filename creates a new record. Export preserves the editor's current text, including unsaved edits. Print uses the visible record. If a conflict occurs, export your draft, reopen the current file and reconcile deliberately; a stale save cannot overwrite another writer.

## Choose your working environment

Understory is a rounded botanical environment for spatial orientation. Lampblack is a soot-dark inspection stage for source observations and selected zones. Clearspan is diffused greenhouse daylight across connected schematic bays for room orientation and comparison. They preserve the same controls, evidence and authority boundaries. Theme choice is remembered by this browser. Keyboard focus, reduced motion and narrow screens remain supported.

## Keep the records yours

The default store is `Documents/CanopyOps`; `CANOPYOPS_DATA_HOME` selects another external directory. Imports preserve original bytes under `imports`, prior saved versions live under `history`, and image references point to `photos`. Back up that external store separately. Never place operational records inside an installation or release ZIP.

If startup fails, confirm Python 3.10+ and an accessible external store. The launcher can choose another local port when its normal port is occupied; leave unrelated services running. The workspace does not connect to live sensors or operate equipment. macOS and fresh customer-host launch behavior remain unverified.
