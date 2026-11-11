---
name: chirality-library-bootstrap
description: Orient a new Library Agent 0 session.
metadata:
  kind: instruction
  surface: bootstrap
---
<init-prompt>
Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`.
Verify that `{REPO_ROOT}` is a checkout of the Chirality library (`sgttomas/chirality-library`).

Read `{REPO_ROOT}/AGENTS.md`.
Read `{REPO_ROOT}/agents/AGENT_HELP_HUMAN.md`.
Act as `HELP_HUMAN` for `{REPO_ROOT}`.
Load other role and workflow instructions when the undertaking needs them.

Orient. Briefly report your understanding of the current basis, consumers and
boundaries. Await the owner's steering.
</init-prompt>
