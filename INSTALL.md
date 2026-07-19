# Install CanopyOps

The release supports four normal installations. Choose one; you do not need all four.

## Before you begin

Keep the downloaded release folder intact. It contains:

- `canopyops/` — the standalone Agent Skill for Codex or Claude Code;
- `claude-ai/canopyops-v0.1.4.zip` — the one-skill upload archive for Claude.ai;
- `plugins/canopyops/` — the branded Codex plugin;
- `.agents/plugins/marketplace.json` — the local Collaborative Dynamics marketplace entry.

Python is optional and no third-party Python packages are required for the bundled utilities.

## Option 1 — Codex plugin

This gives CanopyOps a branded entry in the Codex plugin directory.

1. Download or clone the complete `Stunspot/CanopyOps` repository.
2. Add its GitHub marketplace:

   `codex plugin marketplace add Stunspot/CanopyOps`

3. Install CanopyOps:

   `codex plugin add canopyops@collaborative-dynamics`

4. Start a new Codex task so the installed skill is loaded.

You can alternatively add a downloaded local checkout with `codex plugin marketplace add <absolute-path-to-the-repository>`.

The plugin adds no account, connector, MCP server, hook, telemetry, hosted service, or automatic equipment control.

## Option 2 — Codex standalone skill

Use this when you want the capability without the plugin-directory presentation.

1. Copy the complete `canopyops/` directory to your personal Codex skills directory.
2. On Windows, the resulting path is normally:

   `%USERPROFILE%\.codex\skills\canopyops\SKILL.md`

3. Start a new Codex task.

Preserve every supporting directory beside `SKILL.md`; moving only `SKILL.md` breaks the workflows, persona, templates, references, examples, and scripts.

## Option 3 — Claude.ai custom skill

1. In Claude.ai, open **Customize > Skills**.
2. Select **+**, then **Create skill**, then upload `claude-ai/canopyops-v0.1.4.zip`.
3. Enable the uploaded skill if Claude presents an enable control.
4. Start a new conversation and use the safe discovery request in **Verify discovery safely**.

Claude Skills and code execution must be available for the account. Team and Enterprise organizations may require an owner to enable Skills. The archive contains the complete self-contained skill folder; do not rebuild it by zipping `SKILL.md` alone.

Live Claude.ai upload, enablement, activation, progressive file loading, and script execution have not yet been recorded for v0.1.4. Passing the Claude structural profile establishes package readiness, not live-host behavior.

## Option 4 — Claude Code

For a personal skill available across projects, copy the complete `canopyops/` directory so the resulting path is:

- Windows: `%USERPROFILE%\.claude\skills\canopyops\SKILL.md`
- macOS/Linux: `~/.claude/skills/canopyops/SKILL.md`

For one project only, copy the directory to:

`.claude/skills/canopyops/SKILL.md`

Claude Code can select CanopyOps automatically from its description, or you can invoke it directly with `/canopyops`. If the top-level skills directory did not exist when Claude Code started, restart Claude Code once so it can watch that directory.

Live Claude Code execution has not yet been recorded for v0.1.4; this installation shape is structurally verified against current Agent Skills requirements.

## Verify discovery safely

Start a new task or session and ask:

> Use CanopyOps to outline the evidence you would need before reviewing a fictional late-flower cannabis humidity excursion. Do not diagnose or recommend operational changes yet.

A discovered CanopyOps skill should identify facility context, crop stage, duration, sensor location and method, approved target source and tolerance, observations, prior conditions, and authority before treating the event as an operating decision.

## Python-enabled utilities

Python 3 enables exact VPD, DLI, irrigation, unit-normalization, log-normalization, source-freshness, linting, packaging, and schema-subset checks. CanopyOps should invoke only its bundled scripts against explicit values or user-approved files.

Without Python, it can calculate small cases transparently but must label the result manual or unverified.

## Updating

Replace the complete installed `canopyops/` directory or reinstall the updated plugin. Preserve your own facility and crop records outside the skill directory so an update cannot overwrite them.

## Removing

- Standalone skill: remove the installed `canopyops/` skill directory from the host's skills folder.
- Codex plugin: use the Codex plugin manager or CLI to remove `canopyops@collaborative-dynamics`.

Removing CanopyOps does not delete cultivation artifacts stored elsewhere in your workspace.

## Troubleshooting

- Skill not found: confirm the final path ends in `canopyops/SKILL.md`, then start a new task or session.
- Missing references or templates: reinstall the complete directory rather than a lone `SKILL.md`.
- Script unavailable: confirm Python 3 is available to the host; otherwise use the documented manual fallback.
- Permission prompt: approve only the specific workspace files or bundled scripts needed for the current job.
- Plugin card still shows old copy: reinstall the plugin and open a new Codex task.
- Claude rejects the archive: upload the supplied ZIP unchanged and confirm its top-level folder is `canopyops/` with `SKILL.md` directly inside it.
- Claude Skills are unavailable: check account capabilities or ask the Team or Enterprise organization owner to enable Skills.

For defects and support boundaries, see [SUPPORT.md](SUPPORT.md).
