# Chirality Library repository instructions

This repository owns the Chirality Library: the shared roles, workflows, tools
and tool-use instructions its products and projects consume. Enter through
`loop/LOOP_INIT.md`.

Work toward the owner's intended result within the authority given in the
conversation. Roles describe contributions; workflows supply methods. The owner
remains accountable for acceptance and reliance.

<a id="library-and-root"></a>
**Library and Root.** This repository is the Chirality **Library**
(`sgttomas/chirality-library`): reference material for the whole Chirality
Project, namely the roles, workflows, tools and publications used by Root, App,
SWBPIPE and other applications built for the App's agent harness. Chirality
**Root** is the separate private repository `sgttomas/chirality`. It measures
how agents deliver work across the Chirality projects and improves it, and hosts
what is best delivered as a shared service. Its agents read session telemetry
read-only, segregated by repository, and the owner reviews every finding. Root
never changes another project's files, branches or PRs; its only action in
another repository is opening a GitHub issue for an owner-approved finding,
with content cleared for publication. Routine adherence checks of this
project's deliverables are run by this project's own Agent 0 through a Library
workflow. Root's `main` was rebuilt on 2026-11-04; earlier monorepo content,
including what this repository calls archived or preserved there, is
recoverable only from Root's Git history at or before commit `05d96f3e11`.
Accepted commitments, decomposition, Work and other records written before
2026-11-05 use "Root" for what is now the Library; read them that way. Mapping of DEL-04-02 and exact holding ownership
between the two remains open; this naming does not move them.

## Where work happens

| Scope | Entry | Standing |
|---|---|---|
| Library: shared instructions, workflows, skills, tools and CI | `loop/LOOP_INIT.md` | Work as steered |
| Root: measures and improves agent delivery across projects; hosts shared services | Private `sgttomas/chirality` | Its own instructions; changes nothing here, may open owner-approved issues |
| App v4: independent project | [chirality-app](https://github.com/sgttomas/chirality-app) | Consult its local instructions |
| SWBPIPE: independent project | [SWBPIPE](https://github.com/sgttomas/SWBPIPE) | Consult its local instructions |
| App v3, Runtime | Archived in the private `sgttomas/chirality` Git history (at or before `05d96f3e11`) | Frozen; no development or verification without explicit reactivation |

## Coordination between projects

The Chirality Library (`sgttomas/chirality-library`), Chirality Root (private
`sgttomas/chirality`), App v4 (`sgttomas/chirality-app`) and SWBPIPE
(`sgttomas/SWBPIPE`) each have one top-level Agent 0, working in its own
T3 Code session. When work here needs Root, App v4 or SWBPIPE, such as a shared interface, a
library change a consumer will adopt, a defect found in the other project, or a
shared release gate, this project's Agent 0 messages that project's Agent 0
directly in T3 Code. Read the recipient's session first to confirm that it is
that project's current Agent 0; a retired session is not a route.

A message states what is needed, the revision and files it concerns, and
whether it blocks the sender. The recipient decides and acts within its own
repository and authority. A message carries no owner authority and changes
nothing in another repository. Record an agreed decision by editing the
governing text in the repository that owns it, and take reserved choices to the
owner. Do not message a project the work does not affect. Root may also open a
GitHub issue here for an owner-approved finding; this project decides how to
act on it, as with a message.

## Working cycle

Follow [the operating entry](loop/LOOP_INIT.md) to locate and carry the selected
work. Use one coordinator for a shared result, disjoint concurrent writes, and
owners who stay with their work through repairs. Before integration, reconcile
the actual result and verification evidence with affected ScopeOfWork, `Work/`
and dependency conditions in the same PR. The implementation owner carries this
into assignments; Agent 0 checks that the result and declarations agree.
Revise changed meaning and connect necessary work material from what the next
contributor will read. Apply already-authorized decisions without asking again.
Leave unchanged declarations alone and say briefly when no edit was warranted.
Retain historical evidence and identify what remains unverified.

Return the usable result, checks, material findings and reserved choices. Once
integrated, delete the worktrees, branches, build output and scratch this work
created, unless an open review, named consumer or recovery need still uses them.
Stop when the agreed result is established; do not invent other closeout work.

## Holding changes and recovery

Before relocating or retiring a holding, inspect relevant uses and establish its
replacement or historical standing, recoverable source and removal authority.
Resume from actual work/operation state and current authority, not history alone.
Silence or elapsed time grants no right to discard work. Procedural coordination
is not enforced exclusion. For interrupted work or exceptional custody, establish
the usable result, open conditions, holder and authorized release/recovery. Publication and update
inspection follow the existing [consumer route](README.md#obtain-and-use-the-library).

## Deliverables and records

The convention going forward
uses deliverable localities under `execution/PKG-nn/DEL-nn-nn/`:
`ScopeOfWork.md` holds commitments and acceptance criteria; `deliverable.yaml`
holds needs, conditions and code/check pointers; `Work/` holds technical
reasoning, execution detail, working artifacts and deliverable outputs kept
locally. Make maturity and issue status explicit. Code and other outputs may
retain their actual product/source homes, referenced from the locality. For
agent instructions bundled with an application, maintain the source in the named
deliverable's `Work/`, generate the shipped copy from it, and list both in
`deliverable.yaml`. The Library maintains its published instruction documents in
their Library source homes. The consumer states its needs; tools derive reverse links and graphs.

App v4 and SWBPIPE use `Work/`; their older references to a deliverable's
`Design/` mean its `Work/`. Pre-library execution is recoverable from the
private Root repository's Git history (`sgttomas/chirality`, at or before
`05d96f3e11`).
The accepted [Library PRD](docs/PRD.md) and
[final decomposition](execution/_Decomposition/_LATEST_ACCEPTED.md) supply the
basis for the current Library localities. Read the selected ScopeOfWork, Work and
consumer-local needs for their commitments, maturity and unresolved conditions;
setup does not establish product fulfillment or acceptance.

The operating entry gives query usage; the [query guide](tools/deliverables/README.md)
defines arguments, prerequisites and limits. Results are facts and unknowns,
not completion or acceptance claims; code paths indicate relevance, not exclusive
ownership. Never hand-maintain derived progress or lifecycle state.

Produce the work and the minimum information needed to review, use or recover
it. A record needs a concrete consumer, acceptance requirement or recovery need.
The PR states what changed, why, what was checked and what remains open; quote
the owner's words for reserved decisions. Decisions edit the text they govern,
not append registers. No routine receipts, notices, run records or handoff
chains. Keep one replaceable recovery note only where continuity needs it.

## Verification and authority

- Routine, reversible changes: inspect or exercise the result.
- Ordinary implementation: run a focused check.
- Numerical meaning, persistence, permissions or destructive operations: use
  targeted regression checks and independent scrutiny by a separate agent.
- Releases: check the actual product; release remains an owner act.

Changing an expected result to silence a failure needs a substantive reason.
Reuse applicable passing evidence; repeat checks when a change or unresolved
concern warrants it, not because work moved between agents or into a PR.

Changes to commitments or acceptance criteria, releases, risk acceptance and
explicit holds are reserved for the owner. Present an unresolved reserved choice
with its consequence. Otherwise continue authorized work; uncertainty alone does
not require another approval. Keep credentials and private data out of this
public repository. Required credential checks still apply.
Model and effort choices come from session steering, not repository doctrine.

### Standing Git grant

For `sgttomas/chirality-library` only, agents may commit, push, open, update and merge PRs
within authorized work after the verification above and required checks pass on
the exact head. Explicit holds and reserved decisions apply. This grant excludes
protection bypasses, history rewrites, force pushes, permission changes and
releases. Use ordinary Git judgment under the undertaking and these conventions:
`main` is the integration branch; task branches use an author prefix such as
`codex/` or `claude/`. Use a merge commit unless the PR or owning undertaking
selects another strategy within its authority. Preserve unrelated work, stage
only the intended change and retain truthful authorship. Use the host-prepared
checkout when supplied; otherwise isolate only when requested or overlap/risk
warrants it. Inspect the actual diff and affected checks before publishing and
verify the source head before integration. The PR carries the reason, checked
revision, findings and open matters; a separate Git workflow or receipt is not
required. Cleanup follows the working cycle above. Host permissions still bound
every operation; repository authority cannot expand them.

## Current contracts

The Library's product commitments are in the accepted [Library PRD](docs/PRD.md).
Product commitments live in the project's PRD, named companions and ScopeOfWork.
Its adopted work locality holds the related technical and execution material.

## Roles and workflows

| Role | Type | Contribution |
|---|---|---|
| HELP_HUMAN | 0 | Purpose, alignment and continuity with the owner |
| HELPS_HUMANS | 1 | Design workflows, tools and projects with the owner |
| WORKING_ITEMS | 1 | Own implementation, assignments and integration |
| TASK | 2 | Execute one bounded assignment; does not delegate |
| INTERLOCUTOR | 2 | Opt-in second opinion to Agent 0; advises, does not delegate |

The agent working with the owner holds Agent 0’s responsibilities for purpose,
continuity and reserved choices, whatever role it entered through. Other roles
are taken up as the work needs them. This grants no additional host permissions.
Use only the hierarchy the undertaking needs.
INTERLOCUTOR is opt-in per session. Agent 0 delegates it only when session
steering selects it; Agent 0 then shares periodic activity summaries and
relevant prior feedback and consults it at least before every PR merge, as
`agents/AGENT_INTERLOCUTOR.md` describes. Its advice requires no sign-off and
carries no veto; Agent 0 keeps its decisions and the owner keeps reserved
choices. Sessions that do not select it have no consultation step.
Load the active role's `agents/AGENT_<ROLE>.md`; other role, workflow and skill
bodies are on demand. Keep ownership of integration and route returns through
the host's actual mechanisms. Roles, methods and limits come from these
repository files, never from host-side agent definitions, harness configuration
or instruction files kept outside the repository. A dispatched agent's brief is
given in full in the dispatch and refers only to repository files and host facts. Scratch space
holds evidence, outputs, logs and at most one recovery note, never instructions.

Use `workflows/coordinated-knowledge-work/WORKFLOW.md` when coordinating related
contributions into a usable result. Other methods are indexed in
`workflows/index.json`; load only a selected method and the resources needed for
the stage in hand. Select with `Workflow: <name>` or a source-qualified identity;
retain the selected origin and expose collisions rather than silently switching.
Before creating or revising a reusable workflow, follow `create-workflow`.
Product discovery and registration mechanics live in the interface reference.
