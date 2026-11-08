# Project entry and standing instructions

A Chirality project repository gives its agents one predictable route in. The
same few surfaces answer the same questions in every project, so an agent, the
owner or another project's Agent 0 can orient without learning a new layout.
This resource describes those surfaces, what belongs in each, and which text
is shared across projects and which is local.

Use it when standing up a project, when revising a project's entry or standing
instructions, and when reviewing how a project differs from the convention.
It describes a
convention projects have adopted, not an obligation: a project keeps its
accepted layout until its own authority changes it, and reading this resource
moves nothing.

## The surfaces

| Surface | Question it answers | Changes |
| --- | --- | --- |
| `init/init-prompt.md` | Who am I here, and where do I go next? | Rarely |
| `AGENTS.md` (with `CLAUDE.md` = `@AGENTS.md`) | What authority, boundaries and standing rules apply? | When authority or a standing rule changes |
| `loop/LOOP_INIT.md` | What is the current course, and how do I find and carry work? | When the course or the operating route changes |
| `docs/` | What is the product meant to be? (PRD and companions) | Through the project's commitment process |
| `execution/` | What work is allocated, and in what state? (`PKG-nn/DEL-nn-nn/`, `_Decomposition/`, `_Coordination/`, `_ScopeChange/`) | With the work |
| `tools/`, `workflows/` | What mechanical checks and local methods exist? | With the tool or method |

The first three are the instruction entry layer: how an agent enters and keeps operating.
They do not configure or establish host enforcement. The
next two are what it works on; the last row is what it works with. Keep the
entry layer at the top level, separate from the execution record, so "how do I
work here now" is in the same place in every project.

## `init/init-prompt.md`

A short, reusable prompt the owner sends to start an Agent 0 session. It:

1. resolves `REPO_ROOT` and verifies the checkout's identity (`owner/repo`);
2. reads `AGENTS.md`;
3. resolves the selected Library from `AGENTS.md` (or this repository's own
   source when maintaining the Library) and reads the entry role
   (`agents/AGENT_HELP_HUMAN.md`); where the project pins a revision, identifies
   the revision used in its orientation report;
4. names the role and capacity (`HELP_HUMAN` as Agent 0 for this project);
   optionally clarifies that initialization does not select opt-in roles;
5. reads and follows `loop/LOOP_INIT.md`;
6. orients, reports briefly, and awaits the owner's steering.

It ends by stating that initialization selects no undertaking and grants no
commitment, acceptance or release authority. Keep it free of current status;
that belongs in the loop. An optional `init/README.md` tells the owner how to
use it (send the prompt, then send steering separately).

## `AGENTS.md`: standing authority and boundaries

`AGENTS.md` holds what stays true whatever the current course is. Use these
sections as a suggested skeleton, adapting their order and headings to the
project's accepted instructions and existing links:

1. **Identity and entry.** "This repository owns *X*." Enter through
   `loop/LOOP_INIT.md`. The conversation supplies the undertaking;
   initialization starts none. *(Local: the one-line product identity.)*
2. **Where things are** *(optional)*. A short map of local surfaces when the
   layout is not self-evident.
3. **Shared roles and methods.** The Library selection, the role table, and how
   roles and methods load. *(Shared text, plus the local Library selection.)*
4. **Coordination between projects.** One Agent 0 per project, messaging in
   T3 Code, and what a message does and does not carry. *(Shared text.)*
5. **Root relationship.** What Root may and may not do in this repository.
   *(Shared text; Root states the reverse side in its own file.)*
6. **Work and verification.** Deliverable localities, same-change
   reconciliation, deliverable queries, and the three verification tiers.
   *(Shared text, plus the local high-consequence list and query invocation.)*
7. **Standing Git grant and Git conventions.** *(Shared text, scoped to this
   repository, with the owner's grant quoted.)*
8. **Local boundaries.** Holds, private data, IP, hardware, release
   reservations and other limits that apply only here. *(Local.)*

Within a project, `AGENTS.md` and the loop do not repeat each other. A rule
lives in one of them, and the other links to it where a reader needs it.

### Shared text

Sections 3–7 carry shared substance. The selected Library's
[`AGENTS.md`](../../../AGENTS.md) is the reference wording, not an authority
grant to a consumer. Preserve its source identity and any relied-on section
anchors when adapting names, scope and arrangement. A change to shared wording
here is a proposal for affected projects, not an automatic update: use the
Library review route, then let each project Agent 0 decide adoption under its
own authority. For shared rules, the selected reference wording governs where
this summary differs; local authority remains with the project. The substance
each section carries:

- **Shared roles and methods.** The Library location on this workspace and,
  elsewhere, an owner-selected checkout or release archive of
  `sgttomas/chirality-library`. A path does not identify an edition: a project
  that relies on particular Library content pins an edition or revision and
  records the revision actually used with dependent results; changing the
  selection is a deliberate edit. The role table (HELP_HUMAN 0, HELPS_HUMANS 1,
  WORKING_ITEMS 1, TASK 2, and INTERLOCUTOR 2 where adopted, opt-in per
  session). The owner-facing agent holds Agent 0's responsibilities whatever
  role it entered through. Load the active role file; other roles and methods
  on demand. Use `coordinated-knowledge-work` for related contributions,
  `workflows/index.json` to select others, `create-workflow` before authoring a
  reusable method. Retain source identity and expose collisions. Roles grant no
  host permissions; model and effort come from session steering. Give a
  dispatched agent its brief in full in the dispatch, referring only to
  repository files and host facts. The selected coordination method supplies
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
  repository; the owner reviews every finding; Root changes no files, branches
  or PRs here and may only open an issue for an owner-approved finding cleared
  for publication. Routine adherence checks of this project's deliverables are
  run by this project's Agent 0 through a Library workflow.
- **Work and verification.** `execution/PKG-nn/DEL-nn-nn/` holds
  `ScopeOfWork.md` (commitments), `deliverable.yaml` (needs and pointers) and
  `Work/` (reasoning, detail, outputs). Reconcile changed meaning and
  dependency conditions in the same change; leave unchanged declarations
  alone. Verification is proportionate: routine reversible changes are
  inspected; ordinary implementation gets a focused check; high-consequence
  changes get targeted regression checks and independent scrutiny by a separate
  agent. Never change an expected result merely to silence a failure. Owner
  reservations (commitments, acceptance criteria, risk acceptance, holds,
  releases) and settings/protection changes are presented to the owner.
- **Standing Git grant.** Quote the owner's words granting it. "For
  `owner/repo` only, agents may commit, push, open, update and merge PRs within
  authorized work after the verification above and required checks pass on the
  exact head. Explicit holds and reserved decisions apply. This grant excludes
  protection bypasses, history rewrites, force pushes, permission changes and
  releases." Conventions: `main` integrates; author-prefixed task branches;
  merge commits unless chosen otherwise; stage only the intended change and keep
  truthful authorship; the PR states what changed, why, what was checked and
  what remains open, quoting the owner for reserved decisions, with no separate
  receipts. Use the host-prepared checkout when supplied; otherwise isolate
  only when requested or overlap/risk warrants it. Inspect the actual diff and
  affected checks before publishing and verify the source head before integration.
  After merge, remove the worktrees, branches, build output and scratch the work
  created unless an open review, named consumer or recovery need still uses them.

A project's grant comes from the owner for that repository. Agents do not
write a grant for themselves by copying this text; they record one the owner
has given.

### Local content

Each project fills these in for itself: the product identity; the
high-consequence list for its verification tier (for example numerical
meaning, measure definitions, persistence, permissions, destructive
operations); its query invocation; its governance overlap paths; and its local
boundaries. Owner delegations that extend authority (for example a standing
delegation to decide wording or scope within limits) are standing authority and
belong in `AGENTS.md`, quoted with their dates.

## `loop/LOOP_INIT.md`: current course and operating route

The loop is where an initialized Agent 0 learns what the project is doing now
and how work is found and carried. Typical parts:

1. **Course and basis.** One paragraph: the product, the accepted PRD and
   decomposition, and the current standing in a sentence (for example a release
   target, or "edition N is published; work comes from new steering"). Link
   to the record that holds the detail instead of narrating gate history.
2. **Locate the selected work.** From the steering to the owning
   `DEL-nn-nn`: its `ScopeOfWork.md`, `Work/`, `deliverable.yaml`, then the PRD
   clauses this slice needs. Give the query commands with a worked example. A
   failed query is not an empty result.
3. **Select methods.** How to resolve Library workflows from this project,
   retaining qualified source identity and exposing collisions with local methods.
   Do not infer a different selection from a matching name.
4. **Carry it through.** Agent 0 and implementation-owner responsibilities,
   ordering constraints, reconciliation in the same PR, check selection and the
   hosted merge check.
5. **Project-specific cycle.** What is distinctive here: a release climb,
   platform lanes, a review rule, a publication route, how contributions from
   other projects enter.

Keep it as short as its content allows. Status that changes weekly belongs in a
coordination record the loop links to (for example
`execution/_Coordination/CURRENT_EXECUTION_BASIS.md`), not in the loop or in
`AGENTS.md`. Git and accepted snapshots preserve earlier loops; an archive
folder needs a named consumer.

## Checking a project

When reviewing a project that has selected this convention, examine the
following. A difference is an observation to assess against that project's
accepted basis, not an automatic defect or authority to migrate it:

- `init/init-prompt.md` covers the bootstrap shape above, including its
  conditional steps, and leads to `loop/LOOP_INIT.md`;
- `CLAUDE.md` contains only `@AGENTS.md`;
- `AGENTS.md` covers the standing subjects above under the project's authority,
  retaining the selected shared meaning and identifying local adaptations;
- standing authority, including any Git grant and owner delegations, is in
  `AGENTS.md` with the owner's words, and nothing in the loop grants authority;
- neither `AGENTS.md` nor the loop narrates session or gate history;
- the loop's commands work from the stated working directory with their stated
  prerequisites, and links resolve from the containing document. Distinguish
  inspection or a constructed walkthrough from an observed execution result.

Report differences to the project's Agent 0 as observations; the project
decides what to change.
