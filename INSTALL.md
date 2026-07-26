# Install CanopyOps

CanopyOps currently has two separate distribution lines. Read [`RELEASE-STATUS.md`](RELEASE-STATUS.md) first, choose one route, and keep that package intact.

## Before you begin

- Use a fresh directory for downloads and extraction.
- Store real facility and crop records outside the installed skill or plugin directory.
- Confirm that your chosen workspace backup or version-history process covers those records.
- Use fictional or sanitized information for the first invocation.
- Do not mix files from v0.1.5 and v0.1.6.

Python 3 is optional for ordinary reasoning. It is required for the deterministic utilities and the v0.1.6 portable verifier. The bundled repository-native utilities use only the Python standard library.

## Route A — repository-native v0.1.5 Codex plugin

Use this route for the shortest direct GitHub installation:

```text
codex plugin marketplace add Stunspot/CanopyOps
codex plugin add canopyops@collaborative-dynamics
```

Then start a fresh Codex task so discovery is tested without stale task state.

This route uses:

- `plugins/canopyops/` — the branded Codex plugin;
- `canopyops/` — the canonical repository-native skill tree;
- `.agents/plugins/marketplace.json` — the local marketplace entry.

The plugin adds no account, connector, MCP server, hook, telemetry, hosted service, or automatic equipment control. Command availability still depends on the installed Codex build and workspace policy.

## Route B — portable v0.1.6 Codex package

Use this route when you want a self-verifying portable bundle rather than the repository-native marketplace path.

1. Download [`releases/v0.1.6/CanopyOps-v0.1.6.zip`](releases/v0.1.6/CanopyOps-v0.1.6.zip) and its [detached checksum](releases/v0.1.6/CanopyOps-v0.1.6.zip.sha256).
2. Extract the archive into a new directory.
3. Open a terminal at the extracted release root.
4. Run:

   ```text
   python tools/verify_release.py .
   ```

5. Continue only when the verifier exits `0`, reports `"ok": true`, and returns no findings.
6. Follow [`releases/v0.1.6/docs/INSTALL-CODEX.md`](releases/v0.1.6/docs/INSTALL-CODEX.md).

The portable package expects a Codex build that supports local plugin import or a configured local plugin source directory. Select the complete extracted `codex/canopyops/` directory; do not select its parent or copy individual files out of it.

Static package verification does not prove that the host loaded the plugin, discovered its skill, invoked the intended route, or executed tools successfully.

## Route C — standalone Codex skill

Use the repository-native v0.1.5 skill without the plugin presentation:

1. Copy the complete `canopyops/` directory to your personal Codex skills directory.
2. On Windows, the resulting path is normally:

   ```text
   %USERPROFILE%\.codex\skills\canopyops\SKILL.md
   ```

3. Start a fresh Codex task.

Keep every supporting directory beside `SKILL.md`. Copying only the entry file breaks the persona, workflows, templates, references, examples, adapters, evaluations, and scripts.

## Route D — Claude.ai custom skill

Two packaged uploads are available:

- repository-native v0.1.5: `claude-ai/canopyops-v0.1.5.zip`;
- portable v0.1.6: extract the portable bundle and use `claude/canopyops-v0.1.6.zip`.

For the current Claude interface:

1. Enable **Code execution and file creation** for the account or organization.
2. Open **Customize → Skills**.
3. Select **+ → Create skill → Upload a skill**.
4. Upload one supplied ZIP unchanged.
5. Enable the uploaded skill if Claude presents a toggle.
6. Start a fresh conversation.

Anthropic’s current instructions are at:

- https://support.claude.com/en/articles/12512180-use-skills-in-claude
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

Live Claude.ai upload, activation, progressive file loading, and script execution are not claimed as current CanopyOps evidence. A structurally valid ZIP is not proof of host behavior.

## Route E — Claude Code

For a personal repository-native skill, copy the complete `canopyops/` directory to:

- Windows: `%USERPROFILE%\.claude\skills\canopyops\SKILL.md`
- macOS/Linux: `~/.claude/skills/canopyops/SKILL.md`

For one project only, use:

```text
.claude/skills/canopyops/SKILL.md
```

For the portable v0.1.6 line, follow [`releases/v0.1.6/docs/INSTALL-CLAUDE.md`](releases/v0.1.6/docs/INSTALL-CLAUDE.md) and use the skill tree supplied by that package.

Claude Code may select CanopyOps from its description, or you may invoke `/canopyops`. If the skills directory did not exist when Claude Code started, restart once after installation.

## Verify discovery safely

Start a fresh task or conversation and ask:

> Use CanopyOps to outline the evidence you would need before reviewing a fictional late-flower cannabis humidity excursion. Do not diagnose or recommend operational changes yet.

A discovered CanopyOps skill should identify facility context, crop stage, duration, sensor location and method, approved-target source and tolerance, observations, prior conditions, equipment state, and accountable authority before treating the event as an operating decision.

Record these states separately:

1. package present;
2. static verification passed;
3. host discovered the skill;
4. explicit invocation reached CanopyOps;
5. referenced resources loaded;
6. deterministic tools executed;
7. output met the requested evidence and authority boundary.

## Python-enabled utilities

The repository-native line includes deterministic scripts for VPD, DLI, irrigation, unit normalization, log normalization, source freshness, plan linting, schema-subset validation, and packaging.

CanopyOps should invoke only bundled scripts against explicit values or user-approved files. Without Python, it may show small calculations transparently, but must label them manual or unverified.

## Updating

1. Preserve all operational records outside the installation tree.
2. Identify the installed distribution and version.
3. Replace the complete matching package; do not overlay v0.1.6 files onto v0.1.5 or vice versa.
4. Start a fresh task.
5. repeat the safe discovery check.
6. Re-run the appropriate deterministic verifier.

For the repository-native line, reinstall the plugin or replace the complete `canopyops/` directory. For the portable line, extract the new archive into a new directory and verify it before switching.

## Removing

- Repository-native standalone skill: remove the installed `canopyops/` directory.
- Repository-native plugin: use the Codex plugin manager or CLI to remove `canopyops@collaborative-dynamics`.
- Claude.ai: disable or delete the uploaded skill under **Customize → Skills**.
- Claude Code: remove the installed `canopyops/` skill directory.
- Portable local plugin: remove it through the host’s supported plugin controls, then archive or delete the extracted package according to your own retention policy.

Removing CanopyOps does not delete cultivation artifacts stored elsewhere.

## Recover from overwrite or data loss

CanopyOps does not back up facility or crop records.

If an update overwrote records stored inside the installation tree:

1. stop before another update or reinstall;
2. preserve the remaining files and exact error state;
3. restore from the approved workspace backup or version history;
4. move every recovered record outside the installation tree;
5. retry only after confirming the records are separate from the package.

If no backup exists, preserve what remains and use the organization’s approved data-recovery process. Do not ask CanopyOps to invent operational records from memory.

## Troubleshooting

- **Skill not found:** confirm the final path ends in `canopyops/SKILL.md`, then start a fresh task.
- **Plugin not found:** confirm the complete plugin directory and the installed distribution line.
- **Missing references or templates:** reinstall the complete package rather than a lone `SKILL.md`.
- **Portable verifier fails:** discard the extracted copy, verify the detached checksum, and extract again.
- **Script unavailable:** confirm Python 3 is available; otherwise use the documented manual fallback.
- **Permission prompt:** approve only the specific workspace files or bundled scripts needed for the current job.
- **Claude rejects the ZIP:** upload a supplied archive unchanged and verify its top-level skill folder.
- **Old copy still appears:** remove or disable stale duplicates, restart the host, and record which version is selected.
- **Directory listing is absent:** local GitHub installation and OpenAI Plugin Directory publication are separate states. See [`PLUGIN-DIRECTORY-SUBMISSION-v0.1.5.md`](PLUGIN-DIRECTORY-SUBMISSION-v0.1.5.md).

For defects and support boundaries, see [`SUPPORT.md`](SUPPORT.md).
