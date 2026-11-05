# Chapter 4 — Architecture

## 4.1 Overview

The architecture begins with a relationship: a person pursues a purpose through
work whose meaning, grounds and consequences must stay understandable as agents
contribute. The environment mediates that relationship. It shapes what
participants can find, what they can do and which differences become visible,
so an environment matters even when it appears to consist only of prompts, files
and ordinary tools.

Root's architectural proposal is to make those mediating means available as
shared, revisable artifacts and operations. Participants can examine a
method, challenge an instruction, repair a query or retire a duty using the same
practices they use to produce applications. This capacity is generative: work
can improve its own means without requiring an orchestration fixed in advance
for every piece of work.

Revision stays within the bounds of authority and evidence. An agent that
discovers a burdensome rule does not thereby gain the right to change the
owner's commitments. A change to a representation does not settle what its
subject means. Root must support adaptation without letting its ability to edit
its own machinery become a claim to define its own purpose.

Three relationships organize the architecture: work and its representation,
responsibility and permission, and a contribution and the result that consumes it.

## 4.2 The Foundational Decision: Current Artifacts and Derived Views

### 4.2.1 The Graph Model

A representation is useful when it makes a relationship available to the next
participant without pretending to replace that participant's assessment. A need
is especially important: it states why one contribution matters to another. A
record that states only that two objects are linked loses the condition that
gives the link its practical meaning. Recording a global completion label can
hide the fact that one consumer's need is met while another's is not.

The convention going forward organizes work around
deliverable localities. `ScopeOfWork.md` holds commitments and acceptance
criteria; `Work/` holds technical reasoning, execution detail and locally kept
working artifacts/outputs, with maturity and issue status explicit; and
`deliverable.yaml` identifies the deliverable and states its needs, with optional
code paths and check references. App and SWBPIPE have adopted `Work/`;
historical `Design/` references retain their source-revision meaning. A consumer
declares what it needs from a supplier, and tools derive the reverse links and
graph views.

The graph represents declared relationships; it is not the work itself. A need
can name a deliverable, an external supplier, a document, a package or an
unresolved target. A condition may require interpretation that no schema check
can perform. Cycles can represent mutual interface development or other
legitimate relationships; their presence alone does not establish an impossible
execution order. Selected planning baselines can be DAGs without requiring every
useful relationship to be a DAG edge.

The current query interface provides `neighborhood`, `impact`, `touches`,
`dag-diff` and `check`. Its results identify their observed basis and show
what is unknown, but they do not mark a deliverable complete or infer acceptance
from a merge. The consumer declarations remain the sources, and no generated
progress register is committed as a competing representation.

### 4.2.2 Why the Artifact Choice Matters

The artifact is a shared object around which disagreement can become specific:
participants can point to a condition, compare a revision, or identify a missing
source. This does not externalize all understanding, but it supplies a subject
stable enough for interpretation and action to continue across time and between
participants.

Plain, versioned artifacts support direct inspection, meaningful diffs, stable
references and recovery of committed versions. They also let agents use ordinary
file and Git tools instead of relying on a separate coordination service. Keeping
the current meaning in the deliverable reduces the number of places that must
be reconciled after a decision.

These are advantages of the chosen arrangement, not properties that only files
have. A database-backed application can also preserve provenance, versions and
attributable decisions. Conversely, a Git repository can contain misleading
claims, incomplete history or inconsistent declarations. A commit identifies
recorded content, but it does not establish that the content is correct, that
the record is complete or that every represented human act is authentic.

Purpose and authorization can arise in the conversation. Applications have
operational state, and domain engines maintain models and results in their own
stores. The grounds needed for a particular use must be accessible and
sufficiently identified. Versioned files serve that requirement for development;
other stores serve their adopted application contracts.

### 4.2.3 Scope and Limits of the Filesystem Commitment

Repository commitments, designs and dependency declarations live in files.
Execution services may hold process state, requests, credentials under their
custodian, caches and recoverable session data. Domain applications own their
canonical models and numerical results. These stores serve different purposes,
and the existence of one does not authorize it to override another.

Derived indexes and caches can improve access when their basis and invalidation
behaviour are understood. There is no philosophical requirement to forbid them.
The design concern is whether a reader can identify what a result is based on,
where current meaning is maintained and how divergence is resolved.

Git preserves committed history, but it does not automatically preserve unsaved
work, external services or every input to an analysis. So recovery requirements
must be stated for the operation in question rather than assumed because a
repository is present.

## 4.3 Entity Model and Domain Ontology

### 4.3.1 Project Hierarchy

Root owns shared components in their functional locations: `agents/`,
`workflows/`, `.agents/skills/`, `tools/`, `.github/workflows/` and shared
references. The conversation defines the current work on Root. There is no
standing requirement to generate a product decomposition for every shared edit.

App and SWBPIPE maintain deliverables at their independent repository roots.
The shared convention is:

```text
<project-root>/execution/
└── PKG-nn/
    └── DEL-nn-nn/
        ├── ScopeOfWork.md
        ├── Work/               # locally kept work and outputs; status explicit
        └── deliverable.yaml
```

Packages group deliverables. The flat layout makes navigation predictable, but
it is not a claim that every domain has a naturally flat ontology. An intended
work product is distinct from the folder used to manage it: source code can live
elsewhere, and several deliverables can be relevant to the same code.

Development, examination and acceptance remain distinct activities even when
their artifacts occupy the same deliverable folder. Their meaning comes from the
work, evidence and applicable acts.

### 4.3.2 Stable Identifiers

Package and deliverable identifiers provide references that survive ordinary
text changes and help tools join declarations. In the active layout they follow
`PKG-nn` and `DEL-nn-nn`. A stable identifier does not establish that a
deliverable's meaning is unchanged: a scope revision can preserve identity while
changing a commitment, and that change still requires the appropriate authority.

Code-path mappings express relevance, not exclusive ownership or fulfilment.
An unmapped path produces a partial answer; it is not evidence that the change
has no consumers, nor a reason to start a repository-wide metadata exercise.

### 4.3.3 Deliverable Content and Its Home

The three current artifact types divide responsibility without claiming that
all useful content fits a closed schema:

| Artifact | Purpose | What it does not establish |
|---|---|---|
| `ScopeOfWork.md` | Intended result, commitments and acceptance criteria | That the result exists or is accepted |
| `Work/` | Technical reasoning, execution detail and locally kept working artifacts/outputs; maturity and issue status explicit | That content is suitable, issued or accepted merely because it is here |
| `deliverable.yaml` | Needs, conditions and useful code/check pointers | Completion, suitability or an execution schedule |

A decision changes the text it governs. The PR describes the change, its reason,
checks and unresolved matters; Git retains the earlier text. Sources and
references remain where they help the work rather than in compulsory mirror
files. A record is justified by a concrete consumer, acceptance requirement or
recovery need.

### 4.3.4 Structural and Dependency Views

A concrete traversal starts with an affected project deliverable and its
`neighborhood`. Each need it returns identifies a source file and index. The
agent reads the condition and the relevant supplier material rather than
treating the supplier's presence on main as fulfilment. If the work changes that
condition, the consumer declaration changes; reverse links are derived again. An
`impact` query then selects downstream relationships for investigation. This
sequence keeps one declaration while supporting several useful views.

The package tree supports composition and navigation; the dependency graph
supports investigating inputs and consumers. Neither view alone determines what
can safely proceed. The tool can show that two deliverables have no recorded
dependency, while their implementations still share a file, a memory budget or an
unresolved interface.

`impact` follows declared downstream relationships, including non-gating ones,
and identifies candidates for examination, not an automatic list of invalidated
work. `dag-diff` compares declarations against an identified baseline, but it
does not accept the new graph. Ordinary authorized dependency updates need no new
acceptance ceremony unless they change a reserved commitment or baseline.

### 4.3.5 The Four Structures

The tree, graph, relationship network and attention discussed in Chapter 3 are
complementary perspectives:

- **Tree:** what the work is made of at a useful level of detail.
- **Dependency graph:** which contributions need which inputs and conditions.
- **Relationship network:** sources, decisions, shared concepts and other links
  relevant to interpretation, including those outside execution order.
- **Attention:** the activity through which a participant selects, relates and
  synthesizes what matters for the question in hand.

Attention is not another mandatory stored graph. Nor must every relationship
be extracted into metadata before work can proceed. A machine-readable link is
useful when a real query needs it; otherwise a clear reference in the relevant
design may suffice. These views assist reckoning and human judgment without
capturing all situated understanding.

## 4.4 Work, Evidence and Acceptance

### 4.4.1 Conditions of Work

Availability, suitability, examination and acceptance concern different
relationships. A supplier may be usable for one consumer while inadequate for
another. A review may cover one revision or purpose, while acceptance identifies
a person's particular commitment. These distinctions guide action through their
actual conditions and evidence. [Appendix E](appendix_e_development_history.md)
records how this representation of work developed.

### 4.4.2 Actions and Authority

The current operating model separates ordinary action from reserved decisions.
Agents can investigate, implement, examine, repair and integrate within the
owner's authorization and the host's permissions. Changes to commitments or
acceptance criteria, releases, risk acceptance and explicit holds remain owner
matters. The repository's standing Git grant permits authorized integration
under its verification conditions, but a merge is not acceptance for
professional reliance.

Human judgment is situated, committed engagement throughout the work. It shapes
purpose, distinctions, evidence and what the person will stand behind. An
acceptance is one expression of that engagement, not its entire content.
Neither a lifecycle transition nor a record can exercise judgment for the person.

### 4.4.3 Stage Gates and Useful Checkpoints

A project can require an accepted baseline, a release decision or another
checkpoint that matters. The purpose, subject and authority of such a checkpoint
must be clear. But those needs do not justify a human gate at every internal
agent handoff or ordinary implementation step.

So the current architecture permits project-specific checkpoints while rejecting
a universal development lifecycle. A tool may enforce objective
preconditions for an operation; passing them is evidence about those conditions,
not permission to claim professional approval.

### 4.4.4 Observable Facts Instead of Stored Progress

The question “what can proceed here?” draws on current conditions, available
inputs, relevant checks, in-flight changes and resource constraints. It is not
answered by a single stored status. A file's presence may establish availability
but say nothing about whether it contains the required interface. A passing
check establishes only the behaviour it exercises under its tested conditions.

Agents assess suitability using these facts and report uncertainty when it
matters. This assessment is part of their reckoning; it does not transfer the
person's accountable judgment to the query tool or agent.

### 4.4.5 Warrant and Revision

A claim's grounds, its examination and the reliance accepted on it can change
independently. A citation can be irrelevant; a reviewed claim can later be
contradicted; an authenticated result can be wrong. Several claims in one
artifact can have different grounds and limits.

The operative questions are what supports the claim, whether that support is
appropriate here, what remains uncertain, and who accepts which reliance.
Answering them requires grounds that can be inspected, not a second obligatory
lifecycle register.

## 4.5 Roles and Responsibility

### 4.5.1 Structural Overview

Roles answer a risk in collective work: a needed responsibility can disappear
between individually completed assignments. Someone must preserve purpose,
someone must make intent concrete, and someone must connect contributions into
a result. Naming those responsibilities makes the gap discussable, but it does
not follow that each needs a separate person or process.

The current role definitions offer four contributions:

| Role | Type | Contribution |
|---|---|---|
| HELP_HUMAN | 0 | Purpose, alignment and continuity with the owner |
| HELPS_HUMANS | 1 | Make intent concrete through design |
| WORKING_ITEMS | 1 | Own implementation, contributors and integration |
| TASK | 2 | Carry one bounded assignment through ordinary repairs; no delegation |

The agent working with the person holds Agent 0's continuity responsibilities,
whatever role it entered through. A session can do substantial work without
delegation. Managers and contributors are engaged when their contribution helps;
the types are not a required staffing chart.

### 4.5.2 Authority Properties

A role describes responsibility, while the assignment and host determine the
available tools and write scope. HELP_HUMAN is not intrinsically read-only.
TASK's no-delegation rule remains a deliberate role boundary, but a TASK can
report to its caller an opportunity to divide work without creating another
hierarchy.

No role grants a right to override an explicit hold or make an owner-reserved
decision. Conversely, ordinary refinement of a design within authorized work is
not automatically a reason to escalate. The escalations that are relevant
concern commitments, shared assumptions that matter, interfaces outside the
assignment or a reserved choice.

### 4.5.3 Classification and Capability

Root separates responsibility, method selection and authorization. The role file
states what contribution is being made, the selected workflow supplies a method,
the assignment identifies the authorized work, and the host supplies the actual
capabilities. None can silently stand in for another: a workflow name cannot
grant writes, and a broad host capability cannot widen the assignment.

Type numbers identify responsibilities, not model assignments or levels of
intelligence. Skills and workflows are methods selected for the work. A host's
ability to spawn agents does not itself authorize TASK to delegate, and a
permissive role description cannot expand a read-only host.

The repository resolver represents this distinction when it constructs policy.
Its [implementation](../../tools/workflow_runtime/resolve_workflow.py) explicitly
states that it reports policy rather than acting as a sandbox, so a host must
actually enforce the relevant permissions. App v4's product settings have their
own adopted basis; repository role changes do not silently amend them.

## 4.6 Write Scope and Containment

### 4.6.1 Assignment-Specific Scope

A writing assignment needs a usable boundary: the intended changes, affected
objects and prohibited areas. How precise it must be depends on the operation.
A code change may span source, tests and a design note; it need not fit one
folder merely because the older role catalog assigned folder-based categories.

Missing authorization does not imply unrestricted writes, and explicit read-only
conditions remain in effect. Where a tool accepts paths, normalized containment
and symlink handling are concrete implementation concerns, separate from the
agent's willingness to follow instructions.

### 4.6.2 Shared Work and Protected Objects

Contributors working at the same time should write to separate targets, or one
owner must integrate the shared changes. A read-only review can overlap
production when its basis remains clear. Independence in the dependency graph is
an opportunity to investigate whether work can run concurrently, not proof that
shared writes or resources are absent.

Domain applications add stronger object-level restrictions. The adopted
[product boundaries](../PRODUCT_BOUNDARIES.md) reserve protected domain changes
to the declared engine-controlled path. The engine owns the canonical model
state, but this is authority over storage and operations, not a guarantee of
engineering truth. Applicable proposal, validation and human-acceptance
requirements remain product contracts, and removing repository record duties
does not remove those contracts.

### 4.6.3 What Can Be Enforced

| Mechanism | Bounded contribution | Limit |
|---|---|---|
| Assignment and instructions | State objective, scope and prohibited actions | Following prose is not guaranteed |
| Resolver and schema validation | Reject malformed declarations and some escaping paths | Do not inspect every real effect of an arbitrary command |
| Host permissions | Restrict actions on the enforced execution path | Depend on implementation and coverage of alternative paths |
| Domain operation validation | Check specified model constraints before application | Does not establish all physical or professional adequacy |
| Review and targeted checks | Detect selected errors and assess evidence | Can share assumptions or miss unexamined failures |

This allocation is more precise than saying that instructions themselves create
fault containment. A claim that a property is enforced needs an identified
mechanism, its coverage and appropriate evidence.

### 4.6.4 Fault Containment and Its Costs

Containment can limit the consequences of an error, but path separation alone
does not isolate shared assumptions, resource exhaustion or misleading outputs.
Worktrees reduce some write conflicts, but they do not make integration automatic.
Additional layers can also create stale permissions, waiting and duplicated
state. Their value must be assessed against the failures they address and the
burden they impose.

## 4.7 Commitments, Design Hypotheses and Evidence

### 4.7.1 Three Kinds of Claim

The analysis distinguishes:

1. **Normative commitments:** what responsibility and values the work
   chooses to preserve, such as attributable human acceptance.
2. **Design hypotheses:** how an arrangement is expected to serve those
   commitments, such as identifying the exact subject of an acceptance.
3. **Observed outcomes:** what inspection, tests or use establish about a
   particular implementation and basis.

An acceptance commitment does not prove that a SHA-binding mechanism is sufficient
for it. A successful test of that mechanism does not establish that the person
understood the subject. Appendix A retains the historical identifiers for
comparison and points to adopted product contracts where they still apply.

### 4.7.2 Assurance and the Limits of Layering

Examination is justified by the claim that matters to a consumer. Its purpose is
to expose a mistake that matters or establish a missing ground, not to certify
that work has passed through enough reviewers. A contribution can be consistent
with its test suite and still inherit a mistaken premise shared by every test
author. The basis of agreement sometimes needs examination more than another
instance of agreement does.

Instructions, deterministic checks, host enforcement and human examination can
complement one another, but they can also share the same mistaken premise.
Merely counting layers gives no assurance that one failure cannot compromise the
result.

Verification is chosen according to consequence and detectability. Routine
reversible changes can be inspected; ordinary implementation receives a focused
check; numerical meaning, persistence, permissions and destructive operations
justify targeted regression checks and independent scrutiny. The repository's
required `harness` result combines the checks selected for the candidate.
Passing CI is bounded evidence for integration, not a certificate of product
correctness.

The cost of control belongs in this assessment. Repeated records and checks can
consume the attention needed for substantive examination. Conversely, a cheap
numerical oracle that consistently passes can remain valuable because it detects
a failure that matters and would otherwise stay silent.

## 4.8 Coordination and Continuing Ownership

The relationship developed in the
[introduction](INTRODUCTION.md#iteration-as-learning) has an architectural
consequence: a correction must reach its actual consumer. A revised method needs
an adoption path into the App; an engineering finding needs a path back to the
relevant model, operation or design criterion. Root's sources and queries support
that investigation, while the receiving application owns its operations and
checks. A shared source establishes neither adoption nor domain adequacy.

The [illustrative support-arrangement revision](WORKED_EXAMPLE.md) follows that
relationship across physical intent, operation, calculation, alternatives and
choice. It supplies no measured numerical result or proof of implementation.

### 4.8.1 Contributions Rather Than a Spawning Chart

Ownership through repair connects production to consequences. An author who
leaves at the first return can shift interpretive work onto a reviewer or
coordinator without making that shift visible. Continuing ownership preserves
context while another perspective examines the result. The relevant division is
between contribution and scrutiny, not necessarily between every production step.

The [coordinated-knowledge-work workflow](../../workflows/coordinated-knowledge-work/WORKFLOW.md)
organizes purpose, integration, production and independent examination. An agent
can carry several responsibilities when the work permits. Separate contributors
are useful for parallel lines of work, different expertise or independent
scrutiny; creating the largest possible agent tree is not itself an outcome.

Independent work need not wait behind an unresolved branch, but shared writes,
resource limits, review capacity and integration costs can still justify
sequencing. These are properties of the work, not universal serial or parallel
defaults.

### 4.8.2 Continuity and Recovery

Continuity concerns whether what remains to be done is understandable.
Transcribing everything cannot guarantee it: a large history may leave the next
participant unable to identify the current question. A current source and a
precise unresolved condition can preserve more useful continuity than a
chronology of every action.

Continuity comes mainly from current artifacts, the conversation, tool queries
and the existing change history. A replaceable recovery note is useful when
those sources do not suffice across an interruption. It is not a routine second
work graph or a record of every action.

A participant who resumes the work does not gain the earlier participant's whole
situated understanding by reading a file. Recovery must be tested against an
actual task: can the participant identify the current objective, basis,
unresolved matters and next authorized action without repeating or losing work
that matters?

### 4.8.3 The Working Cycle

Consider a change to a reusable workflow. The producer locates its package and
actual consumers, follows `create-workflow`, edits the method and rebuilds the
workflow index when its consumed metadata changes. An affected App bundle is
updated only where the product actually adopts the changed source. Examination
then follows that connecting path. Merely posting a notice neither updates the
consumer nor establishes what it will execute.

The same principle governs review. A reviewer needs the actual candidate, the
applicable source basis and the existing evidence. A stale synopsis, a prior
preview or an inherited statement that a test passed cannot replace inspecting
the claim at issue. A source correction reaches the governed text and the
affected implementation, while valid unrelated evidence remains usable.

The current repository cycle is to establish the objective and authorization,
locate affected artifacts, query inputs and consumers, do and examine the work,
update current meaning where necessary, and return the usable result. Ownership
continues through ordinary repairs and integration. The agent stops when the
agreed result is established rather than inventing administrative closeout.

The cycle can proceed under standing authority and does not require a human
confirmation at each iteration. An unresolved owner-reserved decision pauses the
affected action, while independent authorized work can continue.

### 4.8.4 App Exemplar and Domain Application

Root produces and revises reusable meanings and methods. The App expresses
Chirality inside an application: workflow authoring lets people develop, try,
inspect and improve methods through the human–agent relationship. It provides
a first exemplar whose subject is close to Root's own work, but that does not
make Root the App's executable runtime or oblige every product to adopt the same
process arrangement.

SWBPIPE is an instance of the approach in a particular category of application.
Physical and analytical models, operations, numerical results and
engineering interpretation introduce meanings that a general authoring App
cannot supply. Human and agent entry points are intended to reach common domain
operations. Their correctness belongs to the application, not to Root's method
library.

So the transfer preserves selected relationships rather than a complete software
topology. The [App case](08_implementation.md#851-operative-perspective-the-app)
examines hosting and workflow authoring; the
[engineering case](08_implementation.md#852-evaluative-perspective-piping) examines
piping-domain instantiation. A shared kernel gives them an orientation, but it
does not discharge either application's evidence obligations.

Successive App versions illustrate how an application is re-derived from a
current PRD. Requirements constrain the result, while prior implementation,
failures, useful interactions and supplier changes inform the design. Root helps
make those sources accessible, but it does not mechanically compile them into
one correct application. Earlier
Apps, Runtime and PEC remain recoverable through
[projects/FROZEN.md](../../projects/FROZEN.md), without current development duties.

## 4.9 Assignment and Result Interfaces

### 4.9.1 The Assignment

An assignment can be the conversation. It needs enough purpose, context,
boundaries and expected result for its recipient to act. Reusable tools may need
strict schemas, but that does not make every agent brief a fixed parameter table.
The current repository requires a dispatched brief to be given in full in the
dispatch and to refer to repository sources, avoiding hidden instruction sets in
scratch space or host-side persona files.

Identical inputs do not guarantee equivalent model outputs, so repeatability
claims must identify the actual execution and assessment conditions. Missing
information is handled according to how much it matters: report a real blocker,
investigate an uncertainty that can be resolved, and continue unaffected work.

### 4.9.2 The Result

A return gives the result location, checks, material findings and unresolved
choices. Contributors inspect returns through the host's actual completion
mechanism. A separate return file, receipt or tool-root snapshot is not a general
requirement.

Some outputs need durable records: an accepted artifact, numerical evidence,
recoverable operation outcome or release package. Their form follows the
consumer's need. Machine-generated execution history can be useful for debugging
and recovery without requiring agents to duplicate it in authored summaries.

### 4.9.3 Historical Preservation and Current Meaning

Current documents are edited in place when their meaning changes. Git preserves
committed versions, while selected tags identify baselines and recovery points.
A tag that records an owner decision must accurately identify that decision, but
creating the tag is not the decision itself.

What is retained depends on the actual consumer, acceptance or recovery need.
Identifying the version that was relied on and recovering an interrupted action
are different needs and may require different mechanisms. [Appendix E](appendix_e_development_history.md)
records the snapshot convention used during development.

## 4.10 Summary

The Root architecture joins current artifacts, selective access to methods,
bounded tools, continuing ownership and appropriate examination. Its immediate
result is a usable environment for producing work and for revising that
environment itself. The architecture keeps need, availability, suitability,
execution, outcome and acceptance distinct without requiring a separate status
system to stand for each.

The four perspectives become practical questions along these paths: what object
or commitment changes, what supports the change, how it reaches its consumer,
and whether its benefits justify its consequences and costs. Agent reckoning
can carry out substantial work within this arrangement; human judgment remains
situated commitment throughout the work.

The App and SWBPIPE test different receiving contexts. Root's success does not
establish their usability, numerical adequacy or professional suitability.
Likewise, a productive application does not prove every shared procedure useful.
The relationship supports mutual examination while leaving each claim with its
actual subject and evidence.
