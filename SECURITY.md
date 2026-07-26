# Security Policy

## Supported surfaces

Security reports are accepted for both current CanopyOps distribution lines:

- the **repository-native v0.1.5 source and plugin line**;
- the **settled portable v0.1.6 bundle** under `releases/v0.1.6/`.

Read [`RELEASE-STATUS.md`](RELEASE-STATUS.md) and identify the exact artifact before reporting. Earlier public releases remain historical and may not receive fixes.

## Security boundary

CanopyOps is a local skill and package system. The current distributions include no CanopyOps-hosted account, telemetry service, connector, MCP server, hook, equipment integration, or automatic network request.

The selected AI host, model provider, operating system, repository host, storage location, and tools have their own security boundaries. Package presence does not prove safe host configuration.

## What counts as a security concern

Relevant reports include:

- path traversal or unintended file access;
- unsafe archive creation, extraction, or member paths;
- execution of untrusted files or discovered project code;
- command injection or unsafe script arguments;
- exposure of secrets or sensitive cultivation records;
- misleading permission, telemetry, connector, or network behavior;
- cross-package version confusion that selects an unintended skill or plugin;
- a prompt or workflow path that encourages unauthorized external action;
- packaging that silently crosses the documented trust boundary;
- an integrity or checksum failure in the portable bundle.

Operational disagreement, stale horticultural guidance, or incorrect deterministic output may be a bug or source-currency concern rather than a security vulnerability. Use [`SUPPORT.md`](SUPPORT.md) when uncertain.

## Report privately

Use [CanopyOps private vulnerability reporting](https://github.com/Stunspot/CanopyOps/security/advisories/new).

If that route is unavailable, contact Collaborative Dynamics through https://collaborative-dynamics.com and request a private reporting route before sending technical details.

Do not open a public issue containing exploit instructions, credentials, facility security information, personal data, proprietary cultivation records, precise inventory, or unredacted compliance material.

## Include useful evidence

Provide:

- affected distribution line and version;
- exact file, archive, checksum, or installation method;
- host and operating system;
- minimal reproduction using synthetic data;
- expected and observed behavior;
- impact and required preconditions;
- whether the issue has been disclosed elsewhere;
- any safe mitigation already identified.

For portable-bundle integrity concerns, include the computed SHA-256 and the detached checksum value without attaching confidential files.

## Coordinated handling

Collaborative Dynamics may confirm receipt, request a safer reproduction, assess scope, prepare a fix, and coordinate disclosure. No bounty, response deadline, fix commitment, or disclosure embargo is promised unless agreed separately in writing.

A documentation update, package fix, host workaround, or release replacement may each be an appropriate resolution depending on the defect. Security triage does not grant operational authority over a cultivation facility.
