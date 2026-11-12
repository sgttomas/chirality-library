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
Accepted commitments, decomposition and other records written before
2026-11-05 use "Root" for what is now the Library; read them that way.

## Where work happens

| Scope | Entry | Standing |
|---|---|---|
| Library: shared instructions, workflows, skills, tools and CI | [Development entry](#chirality-library-development-entry) | Work as steered |
| Root: measures and improves agent delivery across projects; hosts shared services | Private `sgttomas/chirality` | Its own instructions; its Agent 0 and agents working under its assignment may change files here within owner-authorised work, through a PR under these instructions; may open owner-approved issues |
| App v4: independent project | [chirality-app](https://github.com/sgttomas/chirality-app) | Consult its local instructions |
| SWBPIPE: independent project | [SWBPIPE](https://github.com/sgttomas/SWBPIPE) | Consult its local instructions |
| App v3, Runtime | Archived in the private `sgttomas/chirality` Git history (at or before `05d96f3e11`) | Frozen; no development or verification without explicit reactivation |

## How the work is organised

- A **package** (`execution/PKG-nn/`) groups related deliverables; the
  decomposition names each package and what it covers.
- A **deliverable** (`execution/PKG-nn/DEL-nn-nn/`) is one identifiable,
  composable part of the product.
- Its **scope of work** (`ScopeOfWork.md`) states what the part must achieve,
  under what conditions, and what would show that it is adequate. The scope
  leads. Code is measured against it, and where the two disagree, the
  difference is either the work to do or a finding to report.
- Its **needs** (`deliverable.yaml`) state what it relies on: the source
  (another deliverable, a document, an outside party, or one not yet known),
  what the input must provide for this use, and when that applies. A need
  describes what this part consumes; it commits no one to supply it.
- Its **code paths** (the same file) point to the code, tests and other
  artifacts that bear on it. They show relevance, not exclusive ownership, and
  an empty list means none are declared. Keep them accurate.

A locality is its `ScopeOfWork.md` and `deliverable.yaml`; it has no `Work/`
folder. Code, tests, schemas,
fixtures and validation references live in the project's code locations, not
under `execution/`.

There are two ways in, and neither proves you have found everything:

- From a purpose: find the part in the deliverable cards of the
  [decomposition](execution/_Decomposition/PROJECT_DECOMP.md#8-deliverables-and-formation-obligations),
  whose numeric prefixes name the localities, open its scope, then ask what
  surrounds it.
- From changes already committed: ask which deliverables they bear on.

```sh
<query> neighborhood DEL-nn-nn    # its declared inputs, and the deliverables that consume it
<query> touches HEAD              # deliverables whose locality or code paths match that one commit
<query> touches main...HEAD       # the same for a whole branch
```

Read the scope and its needs, then the code. An input can be used when its
need's condition is met; it does not wait for the whole neighbour to be
finished. The queries show what is declared, not whether an input is fit for
your use: read the condition. A query that fails is not an empty answer: read
the files and say the check was unavailable.

Correct a scope's description only when the thing being made has materially
changed or the description is materially wrong, and correct a need the work
showed to be wrong, missing or no longer applicable in the same pull request. A changed commitment or criterion
is the owner's, unless an explicit delegation covers it. If a criterion looks wrong, cannot be met or no longer serves its purpose, and
no explicit delegation covers it, do not change it, weaken its check or build around it: say what you found and
what you would change, and carry on with what it does not affect; the other
criteria stay in force. Treat an
assumption you were given that turns out false the same way, taking it and its
consequence to whoever integrates your work.

`<query>` is `python3 -m tools.deliverables --project .`, run from the
repository root of this checkout with Python 3, PyYAML, Git and a resolvable
`HEAD`. The [query guide](tools/deliverables/README.md) gives the other
queries (`impact`, `check`, `dag-diff`), their prerequisites and limits.

## How agents are organised

- **Agent 0** has the perspective of the whole project: its purpose, the
  choices the owner has reserved, and how the undertakings in progress fit
  together. Where the owner works with one agent and no other holds that
  perspective, that agent does, whatever role it entered through.
- A **Type 1** agent has the perspective of the locality of its assignment:
  the deliverables it concerns, what they need and who relies on them. It
  works in a new thread of its own, at the same level as Agent 0's thread and
  any other Type 1 thread, so that the owner can start one or work with it
  directly, as with Agent 0; that does not change its type. Type 1 agents are
  peers: none owns another's work, and Agent 0 keeps them aligned.
- A **Type 2** agent has one bounded assignment and deliberately limited
  means. It is a child of the agent that delegated it, reports back to that
  agent and starts no other agent.

Two words are kept apart here and in every assignment: a Type 1 is **started
in a new thread**, and a Type 2 is **delegated** as a child. What either is
given is its **assignment**.

How much of the work to give to other agents, and to how many, is the judgment
of the agent holding it. Agent 0 may start a Type 1 in a new thread or
delegate to Type 2 agents. A Type 1 may delegate to Type 2 agents or start
another Type 1 in a new thread. Any agent may message any other; assignments
and returns usually follow the line of assignment, which is what lets an
assigner examine a result and Agent 0 keep the undertakings aligned. A script
suits mechanical work; it does not replace an agent that holds an assignment
and answers for a result. If the host cannot start a new thread, Agent 0 tells
the owner; it does not run a Type 1 as a child.

**An assignment travels whole.** It gives the role to load, what is wanted and
why, what it rests on, what may be read and written, who integrates the
result, how it will be reviewed, which choices are not the assignee's, and how
to reach the assigner.

**A return leads with the result.** It links the evidence (for a pull request,
the reviewed head), states its limits and names who acts next. The assigner
checks it against the artifacts, and reads the assignee's session only when a
return is missing or disagrees with them. A Type 1 also tells its assigner as
it goes: when it starts another Type 1, is blocked, meets a reserved choice
or has a pull request ready. When the owner's steering changes an
undertaking's scope or how it fits with other work, it tells Agent 0 and
whoever integrates the affected work. Whoever owns a result owns its repair.

**An independent review** is made by an agent that did not write the work and
examines the artifacts and what governs them directly, not the author's
account. It says what it read and what it did not. Each review is a fresh
reviewer: a view of the work as it stands at that moment. One reading is
enough when it answers the question. When a matter takes more rounds, give
the next reviewer the earlier findings and what was done about them. Aim to
resolve within two rounds, continue past three only while still converging,
and stop at six. Unresolved findings return to whoever integrates the work,
to decide within its authority; ending the rounds waives no required check or
reserved choice.

**The INTERLOCUTOR** advises Agent 0 on direction in a session the owner opts
in; it is never an entry or default role. Agent 0 keeps the same one as
its child through the session, continued by message; a replacement starts only
if it is lost or the owner asks. It is worth most early: bring it a
consequential proposal while its advice can still change it, and carry on with
unaffected work while it answers. It also carries the continuity that a fresh
reviewer does not. In each review round it examines the findings and the
proposed response against the undertaking's purpose and the earlier rounds,
before the response is settled. That includes rounds a Type 1 runs: the
reviewer's return and the Type 1's proposed response reach it through Agent 0,
or directly where the assignment says so. Tell it how the work develops, and
consult it before a merge. Agent 0 keeps the decision; the advice needs no
sign-off and changes no reserved choice, hold or required check. It does not
replace independent review.

Each agent loads its own role text once, at the start of its session, from the
selected Library: `agents/AGENT_<ROLE>.md`.

| Relationship | Role text |
| --- | --- |
| Agent 0 | `HELP_HUMAN` |
| Type 1 | `WORKING_ITEMS`, `HELPS_HUMANS` |
| Type 2 | `TASK`, `INTERLOCUTOR` |

Which models and effort serve in each relationship comes from the owner's
steering for the session, never from a file.

## Roles and workflows

The Library is its own source and selects no edition: here the selected
Library is this repository at the revision checked out, and each role text is
read from its `agents/`. Roles, methods and limits come from these repository
files, never from host-side agent definitions, harness configuration or
instruction files kept outside the repository. Holding Agent 0's
responsibilities, or any role, grants no additional host permissions. Other
role, workflow and skill bodies are on demand. An assignment refers only to
repository files and host facts. Scratch space holds evidence, outputs and
logs, never instructions.

Use `workflows/coordinated-knowledge-work/WORKFLOW.md` when coordinating related
contributions into a usable result. Other methods are indexed in
`workflows/index.json`; load only a selected method and the resources needed for
the stage in hand. Select with `Workflow: <name>` or a source-qualified identity;
retain the selected origin and expose collisions rather than silently switching.
Before creating or revising a reusable workflow, follow `create-workflow`.

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

[How the work is organised](#how-the-work-is-organised) gives the way from a
purpose to a scope, and when a scope, a need or a criterion is corrected or
taken to the owner; the [scope method](workflows/scope-of-work/WORKFLOW.md#what-a-scope-says)
says what a scope's six parts hold. Describe the change at a high level in the
PR. The session ends there and discovery starts anew next session.

Use one coordinator for a shared result and disjoint concurrent writes. The
implementation owner carries the cycle into assignments; Agent 0 checks that
the result and declarations agree. Apply already-authorized decisions without
asking again.

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

# Chirality Library development entry

The [accepted PRD](docs/PRD.md) defines the Library's commitments; the
[accepted decomposition](execution/_Decomposition/_LATEST_ACCEPTED.md)
locates the allocated work.

The Library has published editions and continues maintenance under new steering.
Continue from actual code, Git and PR state rather than treating earlier gate
decisions, accepted allocation or prepared paths as a current backlog or
fulfilled result.

## Locate the selected work

[How the work is organised](#how-the-work-is-organised) gives the two ways in
and the queries. With the scope and its needs, read the PRD clauses and
sources needed for this slice, without a global state census. Keep unknowns
visible while unaffected work continues. For changes to this entry, begin with
the [discovery scope](execution/PKG-01/DEL-01-01/ScopeOfWork.md); from the
repository root,

```sh
python3 -m tools.deliverables --project . neighborhood DEL-01-01
```

shows its declared inputs and the deliverables that consume it.

## Deliverables and records

Keep check pointers accurate, as code paths are.

Never rewrite frozen snapshots
or accepted evidence. State a fact once and link to it. Use
[document metadata](docs/document-metadata.md) for maintained Markdown headers.
The Library maintains its published instruction documents in their Library
source homes. Never hand-maintain derived progress or lifecycle state.

Produce the work and the minimum information needed to review, use or recover
it. A record needs a concrete consumer, acceptance requirement or recovery need.
Save no memories; durable knowledge lives in Chirality.
Quote the owner's words for reserved decisions in the PR. Lead owner updates with the result or decision needed.
Use plain prose with spaced identifiers in assignments and messages to other agents.
Decisions edit the text they govern, not append registers. No receipts, notices, run records, accounts of
the work, recovery notes or handoff chains.

## Verification and authority

- Routine, reversible changes: inspect or exercise the result.
- Ordinary implementation: run a focused check.
- Numerical meaning, persistence, permissions or destructive operations: use
  targeted regression checks and independent scrutiny by a separate agent.
- Releases: check the actual product; release remains an owner act.

Never change an expected result merely to silence a failure.
Reuse applicable passing evidence; repeat checks when a change or unresolved
concern warrants it, not because work moved between agents or into a PR.

Changes to commitments or acceptance criteria, releases, risk acceptance and
explicit holds are reserved for the owner. Present an unresolved reserved choice
with its consequence. Otherwise continue authorized work; uncertainty alone does
not require another approval. Keep credentials and private data out of this
public repository. Required credential checks still apply.
When an owner instruction overrides a standing rule, note the exception in the
PR and ask once whether the standing rule should change.

### Standing Git grant

For `sgttomas/chirality-library` only, agents may commit, push, open, update and merge PRs
within authorized work after the verification above and required checks pass on
the exact head. The Agent 0 of the session that opened a PR, directly or
through agents working under its assignment, merges it after the review its change requires and with
required checks green on the exact head. Agents working under that Agent 0's assignment report a PR ready to
merge and wait for that Agent 0 to merge it. A Type 1 the owner started
directly reports its PR ready to this project's Agent 0; where the owner works
with it alone and no Agent 0 holds the project, it holds that perspective and
merges under this grant. Explicit holds and reserved decisions
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
[DEL-05-01](execution/PKG-05/DEL-05-01/ScopeOfWork.md) owns
publication preparation. A consumer records its selected revision;
merging a change here does not update that selection.
Acceptance and release remain owner acts; no publication follows automatically
from the working cycle.
