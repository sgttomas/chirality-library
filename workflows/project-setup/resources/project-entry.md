# Project entry and standing instructions

A Chirality project repository gives its agents one predictable route in. The
same few surfaces answer the same questions in every project, so an agent, the
owner or another project's Agent 0 can orient without learning a new layout.

Use this convention when standing up a project, revising its entry or standing
instructions, or reviewing its entry arrangement. Preserve a project's accepted
layout until its own authority changes it. Adapt the suggested arrangement to
that project's purpose and accepted basis.

## The surfaces

| Surface | Question it answers | Changes |
| --- | --- | --- |
| `init-prompt.md` | Who am I here, and where do I go next? | Rarely |
| `AGENTS.md` (with `CLAUDE.md` = `@AGENTS.md`) | What authority, boundaries and standing rules apply, what is the current course, and how do I find and carry work? | When authority, a standing rule or the course changes |
| `docs/` | What is the product meant to be? (PRD and companions) | Through the project's commitment process |
| `execution/` | What is each part of the product, and what must it achieve? (`PKG-nn/DEL-nn-nn/`, `_Decomposition/`) | When the product's definition changes |
| `tools/`, `workflows/` | What mechanical checks and local methods exist? | With the tool or method |

The first two are the instruction entry layer: how an agent enters and keeps
operating. There is no `init/` folder and no `loop/LOOP_INIT.md`. The next two
say what the product is; the last row is what an agent works with.

## `init-prompt.md`

A short, reusable prompt the owner sends to start an Agent 0 session. It:

1. resolves `REPO_ROOT` and verifies the checkout's identity (`owner/repo`);
2. reads `AGENTS.md`;
3. resolves the selected Library from `AGENTS.md` (or this repository's own
   source when maintaining the Library) and reads the entry role
   (`agents/AGENT_HELP_HUMAN.md`);
4. names the role and capacity (`HELP_HUMAN` as Agent 0 for this project);
5. ends: “Orient. Briefly report your understanding of the current basis and
   boundaries. Await the owner's steering.”

A project may add its own report subject, such as the Library's consumers. A
project working toward a release target also asks the first report for the path
from the current state to that target, any independent lanes it would open, and
what it needs from the owner to keep the work moving: decisions, credentials and
host conditions.

Keep the prompt free of current status. The owner sends the prompt, then sends
steering separately.

## `AGENTS.md`: standing authority and boundaries

`AGENTS.md` holds standing authority and the route into the work. Use these
sections as a suggested skeleton, adapting their order and headings to the
project's accepted instructions and existing links:

1. **Identity and course.** "This repository owns *X*", the accepted PRD and
   decomposition, and the current standing in a sentence, such as a release
   target linked to where it is defined. *(Local.)*
2. **Where things are** *(optional)*. A short map of local surfaces when the
   layout is not self-evident.
3. **Shared roles and methods.** The Library selection, the role table, and how
   roles and methods load. *(Shared text, plus the local Library selection.)*
4. **Coordination between projects.** One Agent 0 per project, messaging in
   T3 Code, and what a message does and does not carry. *(Shared text.)*
5. **Root relationship.** What Root may and may not do in this repository.
   *(Shared text; Root states the reverse side in its own file.)*
6. **Work and verification.** Deliverable localities, the working cycle, how
   to find the scopes a piece of work concerns (the query commands with a
   worked example; a failed query is not an empty result), and the three
   verification tiers. *(Shared text, plus the local high-consequence list,
   query invocation and anything distinctive in how work is carried here, such
   as platform lanes or a publication route.)*
7. **Standing Git grant and Git conventions.** *(Shared text, scoped to this
   repository, with the owner's grant quoted.)*
8. **Local boundaries.** Holds, private data, IP, hardware, release
   reservations and other limits that apply only here. *(Local.)*

### Shared text

This resource is the single source of shared wording for project `AGENTS.md`
and `init-prompt.md`, including the Library's own entry documents. Record an optional reconciliation basis using
[document metadata](../../../docs/document-metadata.md#library-derivation)
after the corresponding comparison has been completed.

Preserve source identity and relied-on section anchors when adapting names,
scope and arrangement. Apply grants, delegations and reservations from the
project's own instructions. Submit shared-wording changes through Library
review and coordinate adoption with each affected project's Agent 0. Follow the
[consumer route](../../../README.md#obtain-and-use-the-library) and
[Discovery and reliance](../../../docs/alignment-manual/README.md#discovery-and-reliance)
for adoption and source distinctions.

- **Shared roles and methods.** The Library location on this workspace and,
  elsewhere, an owner-selected checkout or release archive of
  `sgttomas/chirality-library`. Identify the Library edition or tracked line the
  project relies on and record the resolved revision with dependent results.
  Choose pinning or tracking under the project's authority; a checkout path alone
  identifies neither. Use the role table (HELP_HUMAN 0, HELPS_HUMANS 1,
  WORKING_ITEMS 1, TASK 2, INTERLOCUTOR 2) and the selected source's exact
  [`agents/AGENT_INTERLOCUTOR.md`](../../../agents/AGENT_INTERLOCUTOR.md)
  for INTERLOCUTOR instructions. When session steering selects it, Agent 0
  starts one INTERLOCUTOR as a child within its own session and continues that
  same child by message for the life of the Agent 0 session; a replacement
  starts only if it is lost or the owner asks. The owner-facing agent holds Agent 0's
  responsibilities whatever role it entered through. Load the active role file; other roles and methods
  on demand. Use `coordinated-knowledge-work` for related contributions,
  `workflows/index.json` to select others, `create-workflow` before authoring a
  reusable method. Retain source identity and expose collisions. Roles grant no
  host permissions; model and effort come from session steering. Give a
  dispatched agent its brief in full in the dispatch, referring only to
  repository files and host facts. Use plain prose with spaced identifiers in
  messages to delegates. Lead owner updates with the result or decision needed.
  The selected coordination method supplies
  the assignment contents, including objective, basis, writes, integration
  ownership and review/decision rights.
- **Coordination between projects.** Each project has one top-level Agent 0 in
  its own T3 Code session. When work needs another project, this Agent 0
  messages that one directly, after reading its session to confirm it is
  current. A message states the need, the revision and files, and whether it
  blocks. The recipient decides within its own authority; a message carries no
  owner authority and changes nothing elsewhere. Agreed decisions are recorded
  by editing the governing text where it lives; reserved choices go to the
  owner. Do not message a project the work does not affect.
- **Root relationship.** Root reads session telemetry read-only, segregated by
  repository: session metadata in any repository, to attribute sessions, and
  message and tool content only for the repositories a query selects. The owner
  reviews every finding before it reaches this project. Root's Agent 0 and its delegates may change
  this project's files within work the owner has authorised, through a PR here
  under these instructions, this project's checks and its Git grant, and tell
  this project's Agent 0. What Root writes in a public repository is cleared
  for publication first. Root may also open an issue for an owner-approved
  finding cleared for publication. Routine adherence checks of this project's deliverables are
  run by this project's Agent 0 through a Library workflow.
- **Work and verification.** There is the work, which is the code, and what
  expresses its goal, which is the scopes of work. A deliverable is a
  composable part of the product with an identity and a scope. Its locality
  `execution/PKG-nn/DEL-nn-nn/` is `ScopeOfWork.md` (what is intended, under
  what conditions, and what would establish that it is adequate) and
  `deliverable.yaml` (needs and accurate `code_paths`). Code, tests, schemas,
  fixtures and validation references live in the project's code locations.

  Start with what you are trying to accomplish. Read the scopes you think
  relevant and what you find along the way. Plan. Implement and learn.
  Reconcile a scope only if the thing being made, or its description within the
  six parts, materially changed; correct a need the work showed to be wrong,
  missing or no longer applicable in the same change. Describe the change at a
  high level in the PR. The session ends there and discovery starts anew next
  session.

  If you conclude that a criterion is wrong, cannot be met or no longer serves
  its purpose, do not change it, weaken its check or build around it. Say what
  you found and what you would change. Decide it only within an explicit
  delegation; otherwise it goes to the owner. The other criteria stay in force.

  Verification is proportionate: routine reversible changes are
  inspected; ordinary implementation gets a focused check; high-consequence
  changes get targeted regression checks and independent scrutiny by a separate
  agent. Never change an expected result merely to silence a failure. Owner
  reservations (commitments, acceptance criteria, risk acceptance, holds,
  releases) apply subject to applicable, unrevoked owner delegations recorded in
  the project, within their scope and conditions. Present remaining reserved
  decisions and settings/protection changes to the owner. When an owner
  instruction overrides a standing rule, note the exception in the PR and ask
  once whether the standing rule should change.
- **What the repository keeps.** Produce the work and the minimum information
  needed to review, use or recover it. A record needs a concrete consumer,
  acceptance requirement or recovery need. Decisions edit the text they govern,
  not append registers. No receipts, notices, run records, accounts of the
  work, recovery notes or handoff chains; never hand-maintain derived progress
  or lifecycle state. Roles and methods
  come from repository files, never host-side agent definitions or harness
  configuration. Session routes are ephemeral: find current sessions by listing
  T3 threads. Agents save no memories; durable knowledge lives in Chirality.
  Scratch holds evidence, outputs and logs, never instructions. Once work is
  integrated, delete its scratch, worktrees, branches and build output unless an
  open review, named consumer or recovery need still uses them.
- **Standing Git grant.** Record the owner's actual repository-scoped grant with their words; never write one by copying.

### Packaged product instructions

For an application that bundles agent instructions with its product, assign
those instructions to a named deliverable. Maintain canonical runtime assets in
the product's source locations. List the actual maintained and shipped paths in
`deliverable.yaml`. For generated copies, identify the maintained source and
generator.

For example, SWBPIPE DEL-16-06's canonical catalog is
`apps/desktop/src-tauri/resources/agent-capability-catalog.json`.
`tools/agent_catalog_resource.py` validates that resource against its witness
pin; the deliverable's scope governs its requirements.
Keep product build, test and CI independent of a sibling Library checkout.

The Library publishes the documents themselves for consumers to read and
identifies its edition; maintain its published documents in their Library source
homes.

### Local content

Each project fills these in for itself: the product identity; the
high-consequence list for its verification tier (for example numerical
meaning, measure definitions, persistence, permissions, destructive
operations); its query invocation; its governance overlap paths; and its local
boundaries. Owner delegations that extend authority (for example a standing
delegation to decide wording or scope within limits) are standing authority and
belong in `AGENTS.md`, with the owner's wording. When relocating an existing
delegation, preserve its scope, conditions, reservations and owner wording.

## Checking a project

When reviewing a project that has selected this convention, examine the
following. A difference is an observation to assess against that project's
accepted basis. Preserve that basis until the project authorizes a change:

- a root `init-prompt.md` covers the bootstrap steps above; there is no `init/`
  folder or `loop/LOOP_INIT.md`;
- `CLAUDE.md` contains only `@AGENTS.md`;
- `AGENTS.md` covers the standing subjects above under the project's authority,
  retaining the selected shared meaning and identifying local adaptations;
- standing authority, including any Git grant and owner delegations, is in
  `AGENTS.md` with the owner's words; relocated delegations retain their scope,
  conditions and reservations;
- `AGENTS.md` narrates no session or gate history and carries no status;
- its commands work from the stated working directory with their stated
  prerequisites, and links resolve from the containing document. Distinguish
  inspection or a constructed walkthrough from an observed execution result.

Report differences to the project's Agent 0 as observations; the project
decides what to change.
