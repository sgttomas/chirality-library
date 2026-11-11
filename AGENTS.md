---
name: chirality-library-standing
description: Carry Library work under its standing authority and boundaries.
metadata:
  kind: instruction
  surface: standing
---
# Chirality Library repository instructions

This repository owns the Chirality Library: the shared roles, workflows, tools
and tool-use instructions its products and projects consume. Enter through the
[development entry](#chirality-library-development-entry) below.

<a id="library-and-root"></a>
**Library and Root.** This repository is the Chirality **Library**
(`sgttomas/chirality-library`): reference material for the whole Chirality
Project, namely the roles, workflows, tools and publications used by Root, App,
SWBPIPE and other applications built for the App's agent harness. Chirality
**Root** is the separate private repository `sgttomas/chirality`.
Accepted commitments, decomposition, Work and other records written before
2026-11-05 use "Root" for what is now the Library; read them that way.

## Where work happens

| Scope | Entry | Standing |
|---|---|---|
| Library: shared instructions, workflows, skills, tools and CI | [Development entry](#chirality-library-development-entry) | Work as steered |
| Root: measures and improves agent delivery across projects; hosts shared services | Private `sgttomas/chirality` | Its own instructions; changes nothing here, may open owner-approved issues |
| App v4: independent project | [chirality-app](https://github.com/sgttomas/chirality-app) | Consult its local instructions |
| SWBPIPE: independent project | [SWBPIPE](https://github.com/sgttomas/SWBPIPE) | Consult its local instructions |
| App v3, Runtime | Archived in the private `sgttomas/chirality` Git history (at or before `05d96f3e11`) | Frozen; no development or verification without explicit reactivation |

## Coordination between projects

Session routes are ephemeral; find current sessions by listing T3 threads.

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

Use one coordinator for a shared result, disjoint concurrent writes, and
owners who stay with their work through repairs. Before integration, reconcile
the actual result and verification evidence with affected ScopeOfWork, `Work/`
and dependency conditions in the same PR. The implementation owner carries this
into assignments; Agent 0 checks that the result and declarations agree.
Revise changed meaning and connect necessary work material from what the next
contributor will read. Apply already-authorized decisions without asking again.
Leave unchanged declarations alone and say briefly when no edit was warranted.
Retain historical evidence and identify what remains unverified.

Once integrated, delete the worktrees, branches, build output and scratch this
work created, unless an open review, named consumer or recovery need still uses
them.

## Holding changes and recovery

Before relocating or retiring a holding, inspect relevant uses and establish its
replacement or historical standing, recoverable source and removal authority.
Resume from actual work/operation state and current authority, not history alone.
Silence or elapsed time grants no right to discard work. Procedural coordination
is not enforced exclusion. For interrupted work or exceptional custody, establish
the usable result, open conditions, holder and authorized release/recovery.

## Roles and workflows

| Role | Type | Contribution |
|---|---|---|
| HELP_HUMAN | 0 | Purpose, alignment and continuity with the owner |
| HELPS_HUMANS | 1 | Design workflows, tools and projects with the owner |
| WORKING_ITEMS | 1 | Own implementation, assignments and integration |
| TASK | 2 | Execute one bounded assignment; does not delegate |
| INTERLOCUTOR | 2 | Opt-in second opinion to Agent 0; advises, does not delegate |

The agent working with the owner holds Agent 0’s responsibilities for purpose,
continuity and reserved choices, whatever role it entered through. This grants
no additional host permissions.
Use only the hierarchy the undertaking needs.
Agent 0 delegates a Type 1 role (HELPS_HUMANS or WORKING_ITEMS) to its own
standalone session or thread, never as a child within Agent 0's session or
thread. A Type 1 agent delegates to children within its own session or thread.
A WORKING_ITEMS agent may call in a HELPS_HUMANS agent directly, which like
every Type 1 runs in its own standalone session or thread; other engagements
between Type 1 agents go through Agent 0. Peers do not own one another; Agent 0
keeps them aligned. A Type 2 role runs as a child within the session or
thread of the agent that delegates it, whether Agent 0 or a Type 1; it never
gets a standalone session. Agent 0 gives each Type 1 its full
assignment at the start, including how to reach Agent 0. A Type 1 reports to
Agent 0 by message when it calls in a HELPS_HUMANS agent, reaches a result, has
a PR ready to merge, is blocked or meets a reserved choice, stating the result,
links to its evidence (with the reviewed head SHA for a PR), limits and the next
actor. Agent 0 checks a report against the artifacts it names and reads the
Type 1's session only when a report is missing or disagrees with them. If the
host cannot start a standalone session, Agent 0 tells the owner rather than
nesting the role.
INTERLOCUTOR is opt-in per session. When session steering selects it, Agent 0
starts one INTERLOCUTOR as a child within its own session and continues that
same child by message for the life of the Agent 0 session; a replacement starts
only if it is lost or the owner asks. Agent 0 sends periodic activity summaries
and consults it at least before every PR merge, as
`agents/AGENT_INTERLOCUTOR.md` describes. Its advice changes no owner-reserved
choice, hold or required check.
Load the active role's `agents/AGENT_<ROLE>.md`; other role, workflow and skill
bodies are on demand. Roles, methods and limits come from these
repository files, never from host-side agent definitions, harness configuration
or instruction files kept outside the repository. A dispatched agent's brief is
given in full in the dispatch and refers only to repository files and host facts. Scratch space
holds evidence, outputs and logs, never instructions.

Use `workflows/coordinated-knowledge-work/WORKFLOW.md` when coordinating related
contributions into a usable result. Other methods are indexed in
`workflows/index.json`; load only a selected method and the resources needed for
the stage in hand. Select with `Workflow: <name>` or a source-qualified identity;
retain the selected origin and expose collisions rather than silently switching.
Before creating or revising a reusable workflow, follow `create-workflow`.

# Chirality Library development entry

The [accepted PRD](docs/PRD.md) defines the Library's commitments; the
[accepted decomposition](execution/_Decomposition/_LATEST_ACCEPTED.md)
locates the allocated work.

The Library has published editions and continues maintenance under new steering.
Continue from actual Work, Git and PR state rather than treating earlier gate
decisions, accepted allocation or prepared paths as a current backlog or
fulfilled result.

## Locate the selected work

From the brief's purpose or affected holding, find the relevant ScopeOfWork under
`execution/PKG-nn/DEL-nn-nn/`. Read its `Work/` and `deliverable.yaml`, then the
PRD clauses and sources needed for this slice, without a global state census. Code pointers indicate relevance,
not exclusive ownership. For changes to this entry, begin with the
[discovery scope](execution/PKG-01/DEL-01-01/ScopeOfWork.md) and
[its Work](execution/PKG-01/DEL-01-01/Work/DiscoveryBasis.md).

From the repository root, for example:

```sh
python3 -m tools.deliverables --project . neighborhood DEL-01-01
```

Use the actual selected DEL. The [query guide](tools/deliverables/README.md)
gives the other queries (`impact`, `touches`, `check`, `dag-diff`), their
prerequisites and limits. Examine actual input conditions and evidence; usable
inputs need not await an entire neighboring Deliverable's completion. Keep
unknowns visible while unaffected work continues.

## Deliverables and records

The convention going forward
uses deliverable localities under `execution/PKG-nn/DEL-nn-nn/`:
`ScopeOfWork.md` holds commitments and acceptance criteria; `deliverable.yaml`
holds needs, conditions and code/check pointers.

`Work/` holds the current account: findings with their reasons, working artifacts and outputs. Revise it in place rather than appending history; never rewrite fidelity copies, frozen snapshots or accepted evidence. How the work went (approval quotes, review rounds, retries, run IDs, check results) belongs in the PR description, which states what changed, why, what was checked and what remains open. Cite SHAs or hashes only where they pin something a result relies on. State a fact once and link to it.

Code that runs (implementation, tests, generators, harnesses) lives outside `execution/`, in the project's code locations, and deliverables link to it; `Work/` may keep documentation-only examples that are never run.
Make maturity and issue status explicit. Use
[document metadata](docs/document-metadata.md) for maintained Markdown headers.
The Library maintains its published instruction documents in their Library
source homes. Never hand-maintain derived progress or lifecycle state.

Produce the work and the minimum information needed to review, use or recover
it. A record needs a concrete consumer, acceptance requirement or recovery need.
Save no memories; durable knowledge lives in Chirality.
Quote the owner's words for reserved decisions. Lead owner updates with the result or decision needed.
Use plain prose with spaced identifiers in messages to delegates.
Decisions edit the text they govern, not append registers. No routine receipts, notices, run records or handoff
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
When an owner instruction overrides a standing rule, note the exception in the
PR and ask once whether the standing rule should change.
Model and effort choices come from session steering, not repository doctrine.

### Standing Git grant

For `sgttomas/chirality-library` only, agents may commit, push, open, update and merge PRs
within authorized work after the verification above and required checks pass on
the exact head. The Agent 0 of the session that opened a PR, directly or
through its delegates, merges it after the review its change requires and with
required checks green on the exact head. Delegated agents report a PR ready to
merge and wait for Agent 0 to merge it. Explicit holds and reserved decisions
apply. This grant excludes
protection bypasses, history rewrites, force pushes, permission changes and
releases. Use ordinary Git judgment under the undertaking and these conventions:
`main` is the integration branch; task branches use an author prefix such as
`codex/` or `claude/`. Use a merge commit unless the PR or owning undertaking
selects another strategy within its authority. Preserve unrelated work, stage
only the intended change and retain truthful authorship. Use the host-prepared
checkout when supplied; otherwise isolate only when requested or overlap/risk
warrants it. Inspect the actual diff and affected checks before publishing and
verify the source head before integration. Host permissions still bound every
operation; repository authority cannot expand them.

## Maintain holdings and receive contributions

A consumer request or contributed candidate enters through Library Agent 0.
Establish its purpose, exact source basis, owning locality, affected uses,
bounded writes, decision and review rights, checks and supported return route.
Obtain the required Library content approval before integration. The
contributing project owns its adoption and product work.

Before changing a holding, inspect the uses and required resources the change
affects. Regenerate and check consumed indexes when their owning sources
change; do not hand-edit derived catalogs or invent an index change when
generated bytes stay the same.

The [reconciliation method](workflows/bounded-reconciliation/WORKFLOW.md)
compares results under commitments; [reflect-on-work](workflows/reflect-on-work/WORKFLOW.md)
examines whether that basis or practice still serves the purpose. When a finding
calls purpose, commitments, explanatory framing or the chosen practice into
question, use reflection with the human and Agent 0.

## Examine, publish and coordinate adoption

`tools/run_affected_tests.py` selects tool checks; CI supplies the required
hosted result. The [workflow guide](workflows/README.md) covers metadata and
index checks.

Integration on `main`, publication of an edition and a consumer's adoption are
separate decisions. The [consumer route](README.md#obtain-and-use-the-library)
explains obtaining, source selection, update inspection and release notifications;
[DEL-05-01](execution/PKG-05/DEL-05-01/ScopeOfWork.md) and its Work own
publication preparation and evidence. A consumer records its selected revision;
merging a change here does not update that selection.
Acceptance and release remain owner acts; no publication follows automatically
from the working cycle.
