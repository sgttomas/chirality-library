# Systems Engineering Design Analysis — Agent Instruction Architecture

A concise systems-engineering analysis; see [Chapter 7](07_se_design_analysis.md)
for the developed argument.

## 1. Architecture & Structural Design

### 1.1 Layered Separation of Concerns

Authority, responsibility and the capability to execute are different things.
The owner sets purpose and reserved decisions, roles describe contributions, and
assignments and hosts establish which effects are permitted. Instructions
request behaviour, while particular tool and host mechanisms can enforce
narrower properties.

### 1.2 Modularity & Encapsulation

Deliverables maintain ScopeOfWork, material in their adopted work locality
(`Work/` in the current App and SWBPIPE repositories), and dependency conditions.
Historical sources retain their original `Design/` paths. These localities are
units of meaning and work, not
necessarily isolated code modules. Shared code and work that spans deliverables require explicit
responsibility for integration rather than compulsory staffing bound to folders.

### 1.3 Interface Contracts

Assignments, dependency conditions, tool schemas and product operations are
interfaces with different semantics. That an input is syntactically valid does
not establish that it is suitable. A strict tool schema is useful without making
every agent assignment a sealed parameter table.

## 2. Configuration Management & Baseline Control

### 2.1 Version Control as a Development Record

Git preserves committed versions and supports comparison and recovery. PRs
explain changes and how they were examined. Neither is a complete event record of
external services, unsaved work or human engagement.

### 2.2 Identifying the Subject of Acceptance

A revision or digest identifies content, but it does not establish truth or a
human act. Applicable product contracts can require specific bindings; ordinary
development follows its current authority rather than inheriting from every
new commit a universal duty to reapprove.

### 2.3 Change Impact

Derived dependency views identify consumers that may be affected, but they do
not mark every consumer stale or establish that a missing edge means
independence.
Meaningful changes are investigated; reserved decisions remain with the owner.

### 2.4 Preservation

Current meaning is edited in place, while committed history and selected tags
preserve earlier versions. Extra records are justified by a concrete consumer,
acceptance requirement or recovery need; immutable run snapshots are not a
general duty.

## 3. Verification & Validation

### 3.1 Decomposition and Integration

The V-model supplies useful questions about how requirements relate to the
examination of the result. It does not uniquely prescribe stages, documents or
separate agents. Implementation and use can expose requirements that need to be
revised through the appropriate authority.

### 3.2 Consequential Checkpoints

Routine reversible work can be inspected, ordinary implementation receives a
focused check, and consequential numerical, persistence, permission or destructive
changes warrant targeted regression checks and independent scrutiny. Passing a
selected check does not constitute professional acceptance.

### 3.3 Coverage Analysis

Coverage measures need a subject. Migration-row accounting, code exercised and
numerical cases establish different bounded facts, and none of them establishes
that the product or its requirements are completely adequate.

### 3.4 Traceability

Traceability is useful when it connects a real question to sources, assumptions,
consumers and checks. Repeating those relationships in multiple registers can
create inconsistent answers without adding useful evidence.

## 4. Safety & Reliability Engineering

### 4.1 Fault Containment

Host permissions and domain-controlled operations can restrict actual effects.
A role label or natural-language instruction alone is not a sandbox. Containment
claims must identify the path enforced and possible paths outside it.

### 4.2 Failure Visibility

Unknown outcomes, refusals and unexecuted work must remain distinguishable from
success where recovery or reliance depends on that distinction. Visibility is
an implementation property to examine, not something that follows from naming
an invariant.

### 4.3 Context Boundaries

A clear assignment and identified sources help establish the basis of a result,
but they cannot erase model priors or guarantee that a sealed brief captures
every relevant condition. Privacy and access limits belong in actual host and
product boundaries.

## 5. Requirements Engineering

### 5.1 Decomposition & Allocation

Decomposition interprets an intention, turning it into workable results and
relationships. Its completeness cannot be proven merely from a flat folder
layout or a populated allocation table.

### 5.2 Requirements Traceability Views

Generate the view needed by the actual consumer. Current ScopeOfWork, work
material and consumer-owned needs provide the primary development sources;
missing mappings remain explicit rather than being counted as absence of impact.

### 5.3 Acceptance Criteria Allocation

The PRD and acceptance criteria constrain development, but they do not compile
into a unique implementation. Re-derivation incorporates prior defects, use and
the owner's interpretation. Its value depends on retaining learning as well as
on producing code.

## 6. Control and Feedback

### 6.1 The Working Loop

Purpose, action, examination, correction and integration can remain with one
agent or involve contributors. Ownership continues through ordinary repairs.
This is a useful description of feedback, not a proof of convergence.

### 6.2 Feedback Across Contributions

Independent work can proceed while another branch is unresolved. Shared writes,
resource limits and integration costs may justify doing work in sequence.
Recovery from an interruption must be assessed through an actual attempt to
continue.

### 6.3 Authority and Stopping

Standing authority permits ordinary progress; a reserved decision stops the
affected action. Human judgment shapes the work throughout. Completing the
agreed result stops work without a compulsory closeout packet.

## 7. Specification and Formal Methods

### 7.1 Invariant Systems

A stated value, procedure and tool property each require different grounds. A
named rule needs defined scope, an enforcement mechanism and evidence of its
operation. Current adopted contracts are consulted in their current homes;
[Appendix A](appendix_a_invariant_catalog.md) retains the catalog comparison.

### 7.2 Preconditions and Postconditions

Executable checks can enforce explicit input conditions and produce bounded
results. Assignments written in prose do not guarantee postconditions for
stochastic agents. Formal proof would require a model, assumptions and a proof
of the stated property.

### 7.3 The Type System

Types can make distinctions at an interface checkable while leaving open whether
the meaning is adequate. The following **legacy review-format vocabulary** is
retained exactly because
[Compatibility formats §10.6](../COMPATIBILITY_FORMATS.md#106-review-finding-severity)
cites this section:

```text
FindingSeverity : CRITICAL | MAJOR | MINOR | OBSERVATION
```

These values classify review findings about deliverable content for consumers of
that format. They are distinct from historical governance-verifier severities
(`BLOCK`, `REVIEW`, `WARN`, `INFO`, `NOT_APPLICABLE`) and the former agent-conformance
rubric. Preserving them does not require every current review to use the
legacy format or reinstate its lifecycle gates. No enum value itself establishes
the technical severity of a finding.

Likewise, `FACT`, `ASSUMPTION`, `PROPOSAL` and `TBD` can support a review without
exhaustively or exclusively classifying all claims. Correct spelling of a label
is not evidence that its interpretation is correct.

### 7.4 State Machines

Product request, persistence and operation protocols can benefit from explicit
state machines that are faithful to their actual transitions and outcomes. Work,
evidence and acceptance are related in several ways that can vary
independently.

## 8. Human Factors & Decision Authority

### 8.1 Responsibility Allocation

Agent 0 holds purpose and continuity with the person. Other roles are used as the
work needs them; TASK does not delegate. Agents can do substantial reckoning
within authority. Increased agent capability does not transfer the person's
situated, committed judgment.

### 8.2 Cognitive Load

Clear current artifacts and concise returns can reduce the investigation needed.
Labels, registers and records can also obscure relevant questions. Their cost
includes the attention that people and agents need to maintain and interpret
them.

### 8.3 Proportionate Rigor

Rigor concerns adequate examination of consequential failures. The number of
controls is not a useful substitute. A control earns its place through the
failures it addresses, its cost and the limits of alternative feedback.

## 9. Cross-Cutting Patterns

### 9.1 Tree, Graph, Network and Attention

Composition, dependency and relevance are views of the work. Attention
relates them for a purpose. They need not be four separately maintained datasets.

### 9.2 Local Meaning with Derived Views

Consumer declarations support queries on demand without a competing authored
graph, but a fresh query is still only as adequate as the declarations it reads.

### 9.3 Evidence and Its Limits

Provenance enables examination but does not validate an inference. Independent
review is valuable where assumptions and consequences warrant it; several checks
can still share an error.

### 9.4 Complementary Controls

A control contributes assurance only within its actual coverage. Several layers
do not prove that no single failure can compromise a result.

## 10. Assessment

The longitudinal case demonstrates useful production and preserved product
meaning through specification-led redevelopment, with functional extension and
correction. Human purpose, judgment and steering are foundational to this
arrangement. Chapter 8 traces the result through identified sources, deliverables,
implementation and native use. Comparative productivity, recovery beyond the
examined cases and outcomes in additional settings remain distinct empirical
questions. [Appendix E](appendix_e_development_history.md) preserves the history.

### 10.1 The Revisable Relationship

Ontology, epistemology, praxeology and axiology supply enduring questions, and
architecture supplies responses that can be revised. An SE analysis should show
how a response addresses those questions, what it costs and what evidence
supports it. It should not treat an understandable design as proof of
accountable practice.
