# Chirality repository instructions

This repository owns the Chirality library: the shared roles, workflows, tools
and tool-use instructions its products and projects consume. Enter through
`execution/_Coordination/LOOP_INIT.md`. The conversation supplies the
undertaking; initialization alone starts none.

Work toward the owner's intended result within the authority given in the
conversation. Roles describe contributions; workflows supply methods. The owner
remains accountable for acceptance and reliance.

## Where work happens

| Scope | Entry | Standing |
|---|---|---|
| Root: shared instructions, workflows, skills, tools and CI | `execution/_Coordination/LOOP_INIT.md` | Work as steered |
| App v4: independent project | [chirality-app](https://github.com/sgttomas/chirality-app) | Development resumed (owner, 2026-10-28); consult its local instructions |
| SWBPIPE: independent project | [SWBPIPE](https://github.com/sgttomas/SWBPIPE) | Active; consult its local instructions |
| App v3, Runtime | [Recovery](projects/FROZEN.md) | Frozen; no development or verification without explicit reactivation |
| `_DomainEngines/` | Owning project's instructions | Write only under a steer for that work |

## Coordination between projects

Chirality Root (`sgttomas/chirality`), App v4 (`sgttomas/chirality-app`) and
SWBPIPE (`sgttomas/SWBPIPE`) each have one top-level Agent 0, working in its own
T3 Code session. When work here needs App v4 or SWBPIPE, such as a shared interface, a
library change a consumer will adopt, a defect found in the other project, or a
shared release gate, this project's Agent 0 messages that project's Agent 0
directly in T3 Code. Read the recipient's session first to confirm that it is
that project's current Agent 0; a retired session is not a route.

A message states what is needed, the revision and files it concerns, and
whether it blocks the sender. The recipient decides and acts within its own
repository and authority. A message carries no owner authority and changes
nothing in another repository. Record an agreed decision by editing the
governing text in the repository that owns it, and take reserved choices to the
owner. Do not message a project the work does not affect.

## Working cycle

1. Take the objective, limits and authorization from the conversation. Do not
   reconstruct a standing backlog from archived plans or records.
2. Locate the affected deliverable or shared Root component. Read its current
   commitments and design; consult the PRD and companions for the requirements
   and interfaces this work involves.
3. Query the relevant inputs, consumers and changes. Read what this slice needs;
   do not perform a global state census. Resolve whether an input meets its
   condition from evidence and judgment, not file existence or merge status.
4. Carry authorized work through implementation, proportionate verification and
   integration. Use one coordinator for a shared result, disjoint concurrent
   writes, and owners who stay with their work through repairs.
5. Before integration, reconcile the actual result and verification evidence with
   the affected ScopeOfWork, `Work/` material and dependency conditions in the
   same PR. The implementation owner carries this into assignments and retains
   responsibility through repairs; Agent 0 checks that the result and declarations
   agree. Revise current descriptions where meaning changed; add new work material
   where needed and connect it from the material the next contributor will read.
   Apply already-authorized decisions without asking again. Leave unchanged
   declarations alone, and say briefly when no edit was warranted. Git preserves
   history; retain historical evidence and identify what remains unverified.
6. Return the usable result, checks, material findings and reserved choices.
   Once the work is integrated, delete the worktrees, branches, build output and
   scratch it created, unless an open review, a named consumer or a recovery need
   still uses them. Stop when the agreed result is established; do not invent
   other closeout work.

## Holding changes and recovery

Before relocating or retiring a holding, inspect relevant uses and establish its
replacement or historical standing, recoverable source and removal authority.
Resume from actual work/operation state and current authority, not history alone.
Silence or elapsed time grants no right to discard work. Procedural coordination
is not enforced exclusion. For interrupted work or exceptional custody, use
[maintenance recovery](docs/MAINTENANCE_RECOVERY.md) to establish the usable result,
open conditions, holder and authorized release/recovery. Publication and update
inspection follow the existing [consumer route](README.md#obtain-and-use-the-library).

## Deliverables and records

The convention going forward
uses deliverable localities under `execution/PKG-nn/DEL-nn-nn/`:
`ScopeOfWork.md` holds commitments and acceptance criteria; `deliverable.yaml`
holds needs, conditions and code/check pointers; `Work/` holds technical
reasoning, execution detail, working artifacts and deliverable outputs kept
locally. Make maturity and issue status explicit. Code and other outputs may
retain their actual product/source homes, referenced from the locality. The
consumer states its needs; tools derive reverse links and graphs.

App v4 and SWBPIPE use `Work/`; their older references to a deliverable's
`Design/` mean its `Work/`. Root's pre-library execution is archived; recovery
is described in [projects/FROZEN.md](projects/FROZEN.md#pre-library-root-execution).
The accepted [Library PRD](docs/PRD.md) and
[final decomposition](execution/_Decomposition/_LATEST_ACCEPTED.md) supply the
basis for the current Root localities. Read the selected ScopeOfWork, Work and
consumer-local needs for their commitments, maturity and unresolved conditions;
setup does not establish product fulfillment or acceptance.

From the repository root, use `python3 -m tools.deliverables --project <project>`,
where `<project>` is the project path such as `.` for a project at repository root, with `neighborhood <DEL>`, `impact <DEL>`, `touches <rev|PR:n>` or
`dag-diff <tag>`. `check` reports structural errors and unresolved references.
See `tools/deliverables/README.md` for arguments and limits. Results are facts
and unknowns, not completion or acceptance claims; code paths indicate relevance,
not exclusive ownership. Never hand-maintain derived progress or lifecycle state.

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
public repository. Required secret and private-term checks still apply.
Model and effort choices come from session steering, not repository doctrine.

### Standing Git grant

For `sgttomas/chirality` only, agents may commit, push, open, update and merge PRs
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

Root's product commitments are in the accepted [Library PRD](docs/PRD.md).
Product commitments live in the project's PRD, named companions and ScopeOfWork.
Its adopted work locality holds the related technical and execution material.
Consult these shared references where applicable:

- [Product boundaries](docs/PRODUCT_BOUNDARIES.md): professional accountability,
  domain ownership, protected writes and human acceptance. Frozen Runtime
  contracts apply only upon explicit reactivation.
- [Agent and workflow runtime](docs/AGENT_WORKFLOW_RUNTIME.md): product interface
  reference, only where adopted by the current product.
- [Compatibility formats](docs/COMPATIBILITY_FORMATS.md): containment and legacy
  formats still consumed by tools.

## Roles and workflows

| Role | Type | Contribution |
|---|---|---|
| HELP_HUMAN | 0 | Purpose, alignment and continuity with the owner |
| HELPS_HUMANS | 1 | Design workflows, tools and projects with the owner |
| WORKING_ITEMS | 1 | Own implementation, assignments and integration |
| TASK | 2 | Execute one bounded assignment; does not delegate |

The agent working with the owner holds Agent 0’s responsibilities for purpose,
continuity and reserved choices, whatever role it entered through. Other roles
are taken up as the work needs them. This grants no additional host permissions.
Use only the hierarchy the undertaking needs.
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
