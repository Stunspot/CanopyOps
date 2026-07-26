# CanopyOps Data and Privacy

Read [`RELEASE-STATUS.md`](RELEASE-STATUS.md) for the current distribution map.

## Package behavior

The repository-native v0.1.5 line and the settled portable v0.1.6 bundle include no CanopyOps account, telemetry, analytics service, hosted service, connector, MCP server, hook, or automatic network request.

Collaborative Dynamics does not receive cultivation records, facility data, prompts, or generated outputs through the CanopyOps package itself.

The GitHub Pages site is static documentation. It uses no JavaScript, tracking code, analytics, remote fonts, account system, or facility connection.

## Host and tool behavior

Data entered while using CanopyOps is handled by the AI host, model provider, repository host, operating system, storage location, and any tools the user chooses to invoke. Their terms, privacy controls, retention rules, synchronization behavior, and network access govern that processing.

Before providing real operational data, confirm that the selected environment is approved for:

- confidential facility and crop information;
- employee, customer, patient, or vendor information;
- licence, compliance, seed-to-sale, laboratory, or inventory records;
- security controls and facility access details;
- proprietary recipes, SOPs, trade secrets, and commercial plans.

Do not assume that a local-looking interface means data remain local.

## Local artifacts

CanopyOps can write Markdown, CSV, JSON, and other workspace artifacts when the user asks it to. Those files remain wherever the user or host places them.

The package does not independently upload, synchronize, back up, delete, encrypt, or transmit those artifacts. Users must select an approved storage location, access policy, retention period, and backup process.

Store operational records outside the installed skill or plugin directory so updates and removal do not overwrite them.

## Photos, logs, and source documents

Use the minimum data needed for the decision. Remove or redact:

- names and personal identifiers;
- facility addresses and access details;
- credentials, API keys, and licence numbers;
- precise security layouts;
- unrelated inventory and commercial information;
- copyrighted third-party material not needed for analysis.

A public GitHub issue is never an appropriate place for confidential operational evidence. Use synthetic or sanitized reproductions under [`SUPPORT.md`](SUPPORT.md).

## Release boundary

This statement covers the CanopyOps package lines described in [`RELEASE-STATUS.md`](RELEASE-STATUS.md) as distributed on July 25, 2026.

A future connector, hosted service, telemetry system, equipment integration, synchronization feature, or different data path requires a new privacy review and an updated statement before release.
