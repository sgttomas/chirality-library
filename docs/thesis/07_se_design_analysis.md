# Chapter 7 — Systems Engineering Design Analysis

## 7.1 Introduction and Method

Systems engineering offers methods for architecture, configuration management,
verification, safety, requirements, control, formal analysis and human factors
[CITE:INCOSE2023]. Their value depends on the problems they help resolve.

The analysis uses repository instructions, the
[deliverable CLI](../../tools/deliverables/README.md) and
[CI selection](../CI_SELECTION.md) at the stated source basis.
[Appendix E](appendix_e_development_history.md) retains the developmental
comparisons. A rule as specified needs evidence of its actual operation.

Instructions are not formal verification. A completed checklist does not
establish complete review coverage, and several controls may share the same
failure. Each mechanism needs evidence appropriate to the claim made for it.

## 7.2 Architecture and Structural Design

### 7.2.1 Layered Separation of Concerns

The current arrangement separates three concerns without prescribing one physical
layout for every application:

- **Authority:** what the person has authorized and what remains reserved.
- **Responsibility:** who maintains purpose, produces a contribution and integrates
  the result.
- **Information and execution:** where current meaning is maintained, what tools
  reveal, and what the host actually permits.

HELP_HUMAN may write within its assignment and host permissions. Agent 0 can
carry work directly, and TASK remains a bounded executor that does not delegate.
The arrangement of roles serves the responsibilities of the work, while the
assignment a person gives and adopted policy establish authorization.

Where the line falls between instructions and product content also depends on
context. Repository instructions can be changed through authorized work in
Root; they are not universally immutable. An application's bundled instructions
have an adopted product basis and must not be silently changed merely because a
repository role file changed.

### 7.2.2 Modularity and Encapsulation

A deliverable folder is a useful unit for maintaining commitments, design and
needs, but it need not contain all implementation files or represent an isolated
module. Shared code can serve multiple deliverables, and one contributor can own
a coherent undertaking across several folders.

So modularity is assessed by the burden of change and integration,
not by folder count alone. A clear local condition may reduce the investigation
needed; an artificial boundary may instead require several synchronized edits.
Concurrent writes that do not overlap help integration, but they do not
establish that the contributors' assumptions are compatible. One participant
retains responsibility for the shared result.

### 7.2.3 Interface Contracts

The current development interfaces include the assignment, ScopeOfWork, technical
design, consumer-owned dependency conditions and executable tool contracts.
Machines can check them to different degrees: YAML syntax and path containment
are checkable, but whether an input meets a condition can require
interpretation.

For products, the relevant interfaces are meaningful application operations and
supplier protocols. [App v4's architecture](https://github.com/sgttomas/chirality-app/blob/main/docs/ARCHITECTURE.md)
keeps native supplier capabilities and distinguishes common semantics from a
shared service topology. [SWBPIPE's PRD](https://github.com/sgttomas/SWBPIPE/blob/main/docs/PRD.md)
requires model changes to pass through the domain engine. These are concrete
design choices whose implementation and usefulness must be examined separately.

## 7.3 Configuration Management and Baseline Control

### 7.3.1 Version Control as a Development Record

Git identifies committed versions, supports comparison and preserves recoverable
history while those objects remain available. PRs supply the reasons for a
change and the evidence from its verification. Current documents are edited in
place rather than copied into a new run folder after every action.

Git records committed content. Unsaved changes, external inputs, host state and
a person's actual engagement require their own evidence where relevant. The
configuration needed to reproduce or examine a particular result must be
identified and recoverable.

### 7.3.2 Identifying the Subject of Acceptance

A commit or content digest can identify the subject of a decision. That can
keep a reader from confusing an accepted revision with a later one, but it does
not establish that the named person made the decision or understood its subject.

What an acceptance means also includes its scope and purpose. A SHA-binding
contract applies where an adopted product requires it; this analysis does not
amend that contract. For ordinary development, a changed commit does not itself
require the owner to approve every unchanged commitment again. The
current authority and the consequences of the change determine what must be
examined or decided.

### 7.3.3 Change Impact and Staleness

A dependency query can reveal affected consumers, but it cannot conclude that
every consumer is invalid merely because an upstream file changed. A change to
the implementation may preserve the required interface, while a small change of
wording may alter a critical condition.

So the active model returns relationships and observable facts rather than
propagating a maintained stale flag. Agents investigate relevant effects within
their assignments. Changes to a reserved commitment, acceptance or risk go to
the owner. This preserves useful impact analysis without requiring a person to
triage every transitive edge.

### 7.3.4 Preservation Without Routine Copies

Git recovery and selected tags preserve committed versions. Retaining anything
more is justified by what the consumer needs, including evidence that is relied
on and uncertain operation outcomes.
[Appendix E](appendix_e_development_history.md) records the development of this
policy.

Some evidence must still be preserved: a relied-upon analysis basis, a release
package or the outcome needed to recover an interrupted operation. The
requirements for retaining such evidence follow that use. Neither universal
snapshots nor universal deletion is an adequate policy.

## 7.4 Verification and Validation

### 7.4.1 Decomposition and Integration

The V-model is useful as a reminder to connect requirements with the evidence
needed to examine the integrated result [CITE:INCOSE2023]. It does not require
that all design proceed down a completed hierarchy before implementation begins,
or that every upward integration step become a separate human gate.

A current ScopeOfWork identifies intended results and acceptance criteria.
Implementation, use and review can reveal inadequate assumptions or missing
requirements. Authorized refinements update the relevant design, while changes
to reserved commitments require the owner to decide. This feedback makes the
relationship iterative rather than a one-way derivation.

### 7.4.2 Checkpoints by Consequence

The current verification rule is proportionate to consequences: reversible
work can be inspected; ordinary implementation receives a focused check; and
numerical meaning, persistence, permissions and destructive operations require
targeted regression checks and independent scrutiny. Releases remain acts of the
owner and need checks of the actual product.

This is a principle for selecting checks, not an exemption from evidence. The
repository's required `harness` result fails when a selected product path fails
or does not report as required. Passing it still does not establish that every
important behaviour was selected or adequately tested. Which checks are selected
and how they behave are themselves implementation concerns.

### 7.4.3 Coverage and What It Measures

Coverage needs a stated subject. Lines exercised, requirements linked, dependency
rows migrated and numerical cases checked measure different things, and none of
them is a complete measure of whether the product is adequate.

When dependency declarations are transformed, source-row accounting and
comparison with an identified graph basis can detect relations that were lost or
altered. An independent examination of their meanings adds evidence that
the conditions were preserved. Neither examination establishes that the original
declarations captured every real dependency. Chapter 8 evaluates the bounded
case evidence.

Whether a check survives depends on the consequential failures it can detect,
its cost and overlap, and whether failure would otherwise become visible in
time. A low recent failure rate is not by itself a reason to remove a cheap
numerical oracle. Repeated checks of unchanged applicable inputs are not
inherently more informative because they occur in another session.

### 7.4.4 Traceability for an Actual Question

Useful traceability lets a participant move from a claim or proposed change to
its relevant source, assumptions, consumers and checks. It need not be represented
three times in a ledger, a dependency row and a context mirror.

The current artifact model puts each condition where it is used and derives
reverse links. A source pointer helps inspection, but it does not validate the
inference. Where a question cannot be answered from the declarations, the gap is
reported and investigated. The architecture cannot promise complete traceability
merely because every populated field conforms to a schema.

## 7.5 Safety and Reliability Engineering

### 7.5.1 Fault Containment

Host permissions and domain-operation boundaries can reduce the effects of
mistakes. The assurance they give concerns the actual execution paths they
govern. An
instruction to remain in a folder is different from a path check, and a path check
is different from a sandbox restricting the effects of arbitrary commands.

The [workflow resolver](../../tools/workflow_runtime/resolve_workflow.py)
constructs policy and rejects invalid declarations; it explicitly is not a
sandbox. That distinction keeps a narrow test result from being presented as a
complete argument for containment. Safety analysis must consider unsafe
interactions as well as component failures [CITE:Leveson2011].

### 7.5.2 Failure Visibility

An unknown outcome, missing input or contradicted claim must remain
distinguishable from success. Visibility depends on detecting and reporting the
condition; an instruction to expose uncertainty does not guarantee it. Product
operations also need to distinguish refusal, non-execution, successful
application and lost acknowledgement when those distinctions affect recovery.

A failure can be harmless in one context and matter in another: a missing
optional reference can permit a partial query, while a missing numerical input
may require refusal. The response follows what the condition means, not a
universal rule that every unknown either blocks everything or can be ignored.

### 7.5.3 Context Boundaries

An identified input basis makes examination possible, but a closed brief cannot
remove the priors a model has learned or establish that the agent used only
intended information. A claim of complete context isolation requires an
execution mechanism and evidence that goes beyond checking that metadata is
present.

The current repository supplies the full assignment in the dispatch, keeps
instructions in repository sources, and retrieves additional material according
to the task. Privacy and access limits remain enforceable host or product
boundaries. Task context can change as relevant discoveries are made, without a
new routine ceremony to seal it.

## 7.6 Requirements Engineering

### 7.6.1 Decomposition and Allocation

Decomposition makes a large intention workable by identifying results, boundaries
and connections. It is an interpretation of source requirements, not proof that
the source was exhaustive or that every resulting partition is natural.

Stable identifiers and a predictable folder layout help agents locate the work.
Acceptance criteria belong to the current commitment; code paths identify
relevant implementation. Neither a flat layout nor a one-to-one allocation rule
is a universal requirement for every domain.

### 7.6.2 Traceability Views

A requirements-to-deliverables view can be generated when an actual review needs
it. Its value lies in answering whether a commitment has an implementation and
a suitable basis for examination. A maintained matrix is justified when its
consumer requires it; otherwise direct references and queries can provide the
same useful navigation with fewer things to keep synchronized.

Missing mappings remain visible. Tool output should not make a partial mapping
look like a claim of completeness.

### 7.6.3 Acceptance Criteria and Re-Derivation

A PRD does not compile deterministically into an application; it leaves design
choices that must be informed by the owner, supplier capabilities, prior defects
and actual use. App v4 supplies an operative setting in which purposes, selected
useful behaviours and actual supplier interfaces must become working application
paths.

A new implementation should be assessed for the learning it retains as well as
for its speed. If it repeatedly loses valuable behaviour or rediscovers earlier
failures, its derivation from the PRD has not preserved enough of the work's
knowledge. Changes to criteria remain the owner's attributable decisions;
evidence from implementation can motivate those decisions without making them
automatically.

## 7.7 Control and Feedback

### 7.7.1 The Working Loop

Reading the work as a feedback loop remains useful: establish an objective, act,
inspect the result, compare it with what is needed and correct. The actor need
not change at each step. Sustained ownership keeps an agent with the ordinary
repairs and integration that make its contribution usable.

This is an analogy to control, not a demonstrated control-theoretic model with
proven convergence. The objectives, available information and even the relevant
state description can change as work reveals new conditions.

### 7.7.2 Observables and Objectives

Useful observations include whether an operation applied, which check ran, what
an input contains and which consumers declare a need. The objective is a usable
result under the applicable conditions. A progress label measures only the
classification asserted; it does not establish that result.

Completed work needs evidence tied to its actual purpose. The owner
must be able to understand what was achieved, what remains uncertain and what
reliance is being proposed. A dashboard can assist that understanding but cannot
replace it.

### 7.7.3 Feedback Across Contributors and Sessions

A contributor can continue independent work while a related branch is unresolved.
Coordination becomes necessary where results affect shared assumptions, interfaces
or writes. The host's completion mechanism delivers returns, and the integrating
participant examines them and settles how they relate to the whole.

Conversation and current artifacts support continuity. Recovery is a
practical property to test after an interruption, not a guarantee that a handoff
file supplies. A replacement participant may need to re-establish context even
when the preserved facts are accurate.

### 7.7.4 Authority and Stopping

Human authority does not imply that confirmation is required at every control
cycle. Standing authorization permits ordinary work to continue. An explicit
hold or reserved choice stops the affected action. Completing the agreed result
is also a stopping condition; agents should not invent records to prolong
closeout.

Judgment remains the person's situated, committed engagement throughout the work.
The agent's planning, evaluation and adaptive action are reckoning within the
assigned authority. A stronger capacity for reckoning can change what
supervision is suitable without itself transferring judgment.

## 7.8 Specification and Formal Methods

### 7.8.1 Stated Properties and Their Grounds

A value commitment, a procedure and a property of a tool each require a
different argument. A named rule needs precise scope and an actual enforcement
mechanism before it can support a formal claim. Adopted product contracts apply
through their current sources. [Appendix A](appendix_a_invariant_catalog.md)
preserves the catalogs as a developmental comparison.

### 7.8.2 Preconditions and Postconditions

Executable tools can check explicit preconditions and report well-defined
outcomes. The deliverable checker, for example, tells malformed metadata apart
from relationships that are well formed but unresolved. So a successful
structural check means something narrower than “all needs are met.”

Agent assignments can state expected results and conditions, but stating them in
prose does not give stochastic execution guaranteed postconditions. The
resulting work must be inspected or tested as appropriate. A claim of formal
proof would need a specified model, assumptions and an actual proof, not a table
of intended behaviours.

### 7.8.3 Types and Interpretive Limits

Types reduce ambiguity at particular interfaces. The active YAML schema rejects
invalid identities and malformed fields while preserving unresolved suppliers.
Legacy formats can remain documented for adopted consumers without defining
current development behaviour.

The older labels `FACT`, `ASSUMPTION`, `PROPOSAL` and `TBD` are useful distinctions
in some reviews; they are not an exhaustive, mutually exclusive ontology of every
claim. A proposal can contain supported facts and untested assumptions. Checking
a label's spelling cannot establish that its classification is appropriate.

The exact legacy `FindingSeverity` enum remains in the standalone
[SE companion, §7.3](SE_Design_Analysis.md#73-the-type-system) because the
compatibility-format reference still cites it. Retaining that interface does not
reinstate the older review gates.

### 7.8.4 State Machines Where They Fit

Product request, persistence and operation protocols benefit from explicit
state machines when their transitions and failure outcomes faithfully represent
the behaviour controlled. A deliverable's claims, dependencies and accepted
uses can vary independently. A state machine's scope follows the operation it
models; it does not supply a universal model of work.

## 7.9 Human Factors and Decision Authority

### 7.9.1 Responsibility Allocation

The person retains judgment and reserved commitments. Agent 0 maintains purpose
and continuity in the interaction; managers and executors are opportunities for
useful contributions. TASK's rule against delegating provides a particular
boundary once that role is selected. None of this requires the owner to
personally repeat every implementation decision or review every reversible edit.

An agent can help frame an ambiguous choice, but the framing is itself something
to examine. A choice reduced to two options is not necessarily easier to
judge well if it conceals relevant alternatives or assumptions.

### 7.9.2 Cognitive Load and Attention

A clear source, a concise return or explicitly stated uncertainty can reduce the
investigation needed, while repeated registers, notices and status mirrors can
increase it. Labels do not remove the need to examine how reliable a claim is,
and an immutable record can still be wrong or distracting.

Attention is a scarce part of professional work. Information should be
sufficient to review, use or recover the result, with detail accessible when
needed. The value of this arrangement must be assessed in actual use, including
by someone other than its author.

### 7.9.3 Proportionate Rigor

Rigor concerns whether an examination is adequate for its consequences, not the
number of forms or test runs. Numerical meaning warrants stronger evidence than
a reversible wording change. A routine change can come to matter when it alters
executable configuration or an embedded source.

Evaluating a control includes its cost: execution time, maintenance, attention,
false alarms and lost opportunities to do substantive work.
Removing a control is justified when its useful function is unnecessary or
adequately served elsewhere, not merely because it is inconvenient.

## 7.10 Cross-Cutting Patterns

### 7.10.1 Tree, Graph, Network and Attention

Composition, dependency and relevance are distinct views of the work. Attention
selects and relates them in a particular inquiry. A schema can support these
activities without exhaustively representing the world or a person's knowledge.
The graph can reveal opportunities for parallel work while leaving questions
about shared writes, resources and interpretation unresolved.

### 7.10.2 Local Meaning and Derived Views

Consumer-owned needs let an agent examine a relevant neighbourhood without a
census of global state. A generated answer avoids maintaining a second authored
graph, but it is only as fresh as the declarations it read. Stale or incomplete
declarations still yield stale or incomplete answers.

So the maintenance responsibility is to update current meaning when it changes
and to leave unchanged declarations alone. No storage arrangement removes that
responsibility.

### 7.10.3 Evidence and Its Limitations

Sources, checks and independent examination make grounds inspectable, but they
do not guarantee that every unsupported claim can be discovered or that a cited
source warrants the conclusion. Shared errors in models, fixtures and
expectations can survive several apparent layers of verification.

SWBPIPE makes this limitation concrete: a result can pass software validation
without becoming professional engineering approval. Similarly, recovery of an
App workflow cannot be inferred solely from a recovered conversation. Each claim
requires evidence about its own subject.

### 7.10.4 Complementary Controls

Controls are complementary when they address distinct failure modes or provide
independent evidence. Writing the same assumption into instructions, a schema
and a test may create repetition without independence. The assurance argument
must identify what each control checks and what remains outside it.

So the architecture supports a bounded argument about failures, not a blanket
claim that no single failure can compromise system integrity.

## 7.11 Assessment

### 7.11.1 What SE Contributes

The disciplines provide useful ways to ask whether boundaries are clear,
configurations identifiable, interfaces coherent, evidence appropriate, failures
recoverable and human attention well directed. They are resources for design and
criticism. Implementing a named artifact for each discipline does not establish
their value.

<a id="7112-a-revisable-relationship-to-the-four-pillars"></a>

### 7.11.2 A Revisable Relationship to the Four Perspectives

| Perspective | SE questions it motivates | What remains contingent |
|---|---|---|
| Ontology | Which objects, identities and relationships need to be distinguished? | Folder layout, schemas and storage topology |
| Epistemology | What supports a claim and how can its limits be examined? | Checks, source bindings and evidence formats |
| Praxeology | How do contributions become a usable result through action and correction? | Staffing, workflow stages and coordination mechanisms |
| Axiology | Whose purposes and responsibilities matter, and what costs are acceptable? | Decision interfaces and proportionate controls |

These questions constrain one another: a recovery failure can reveal a missing
distinction between outcomes, a new risk can change the examination needed, and
excessive procedure can consume the attention that sound judgment requires. The
framework holds together through such correction, not through permanent
commitment to one architecture.

Applicable obligations and constraints, uncertain premises, negotiable preferences
and control costs require distinct treatment. A missing physical input concerns
the grounds of the calculation. A mandated review concerns an applicable
obligation. A preference for a simpler interface and the attention cost of a
control concern available design choices. Agents can compare consequences and
alternatives; the person judges the arrangement in its situation. No universal
score or compulsory sequence resolves these questions.

### 7.11.3 Bounded Conclusion

Chapter 8 traces an inspectable arrangement in use: useful predecessor behavior
and governing distinctions become successor commitments and deliverables, then
working behavior in the redeveloped App. Findings change the product and its
production method. Human purpose, judgment and steering are foundational to
those observed results.

The evidence supports useful production and temporal continuity in this case.
Comparative safety, productivity and economical transfer to further settings
require their own comparisons. Systems engineering helps examine these claims;
it does not certify the quality of human judgment or settle the philosophical
capacities of all future machines.
