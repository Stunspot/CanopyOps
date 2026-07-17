# Security Policy

## Supported release

Security fixes are considered for the current v0.1.1 release line. Older prototype snapshots are retained as development evidence and are not supported public distributions.

## What counts as a security concern

Relevant reports include:

- path traversal or unintended file access;
- unsafe archive creation or extraction;
- execution of untrusted files or discovered project code;
- command injection or unsafe script arguments;
- exposure of secrets or sensitive cultivation records;
- misleading permission, telemetry, connector, or network behavior;
- a prompt or workflow path that encourages unauthorized external action;
- packaging that silently crosses the documented trust boundary.

CanopyOps v0.1.1 contains no hosted service, account, telemetry, connector, MCP server, hook, or automatic network request.

## Report privately

Use [CanopyOps private vulnerability reporting](https://github.com/Stunspot/CanopyOps/security/advisories/new). If that route is unavailable, contact Collaborative Dynamics through https://collaborative-dynamics.com and request a private reporting route before sending technical details.

Do not open a public issue containing exploit instructions, credentials, facility security information, personal data, proprietary cultivation records, or other sensitive material.

## What to include

- affected version and file;
- host and operating system;
- minimal reproduction using synthetic data;
- impact and required preconditions;
- whether the issue has been disclosed elsewhere;
- any safe mitigation already identified.

## Coordinated handling

Collaborative Dynamics may confirm receipt, request a safer reproduction, assess scope, prepare a fix, and coordinate disclosure. No bounty, response deadline, or disclosure embargo is promised unless agreed separately in writing.
