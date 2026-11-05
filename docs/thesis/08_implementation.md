# Chapter 8 — Evidence and Evaluation

## 8.1 Subject and Evidence Basis

This chapter evaluates the use of Chirality to produce software and carry its
meaning through change. The undertaking joins one developer's purpose, judgment
and steering with agents' investigation, design, implementation, orchestration
and examination. Human direction is foundational to this method and to the
result being evaluated.

The original implementation account retains commit
`a602024416ace9652f61bb2043889c307fd4e09d` (October 10, 2026) as its basis.
The dated extension in §§8.5.3–8.5.5 was examined on October 30. It follows
earlier App behavior through successor definition and redevelopment, incorporates
the October 14–16 native walkthrough, and examines stored SWBPIPE comparison
evidence. Its sources have separate identities:

| Subject | Identified source | What was examined |
|---|---|---|
| Working App v3 and successor investigation | Chirality `2b0572fe049c8ffaa02d61b7dbbc3ae41bc589f6`; preserved investigation in App `032725d32b67e117b8e1fb2b5fa9aa47b30de12e` | Recorded execution, lessons and selected behaviors |
| Accepted successor and realized App v4 behavior | App `032725d32b67e117b8e1fb2b5fa9aa47b30de12e`, with the dated changes cited below | Decomposition, deliverable contracts, implementation changes and native-use records |
| Piping comparison method | SWBPIPE `bc9f7961acee72441ec06c104ed97d4f1c77faa4` | Public pilot design and comparison rules |
| Executed piping comparisons | Owner-held pilot and benchmark run records of October 26–29, inspected October 30 | Stored input/output bindings, selected comparisons and classification arithmetic; no new solver execution |

The extension is a review of identified records and their connecting paths, with
separate agent examination and discussion of the findings. Earlier observations
keep their original scope; the extension does not qualify every later product
revision. [Appendix E](appendix_e_development_history.md) supplies the history.
Unpinned repository links provide navigation; empirical sources below identify
their examined revisions.

Root's principal contribution is normative: purposes, responsibilities, distinctions
and criteria guide work while remaining open to correction. Its tools also make
some relationships operable. The App supplies the chiefly operative perspective;
Piping supplies the chiefly evaluative perspective as an instance of domain
software. Evidence in one perspective can inform another without establishing
its claims. Ontology, epistemology, praxeology and axiology concern all three.

The evaluation distinguishes specification, exercised behaviour and adequacy for
use. A written contract establishes what was required, and a passing check
establishes what its inputs and predicates exercised. Professional adequacy and
human engagement need grounds appropriate to their own subjects.

## 8.2 Authorization and Enforced Boundaries

### 8.2.1 Responsibility and Authorization

The source basis contains four general role files:

| Role | Contribution |
|---|---|
| HELP_HUMAN / Agent 0 | Purpose, alignment and continuity with the person |
| HELPS_HUMANS | Design workflows, tools and projects with the person |
| WORKING_ITEMS | Own implementation, assignments and integration |
| TASK | Execute a bounded assignment without delegation |

These contributions describe responsibility. Human assignment and adopted policy
establish authorization; the host supplies capability and enforces permissions
on its actual paths. One session can carry several contributions. Agent 0's
continuing responsibilities need not imply a separate managerial tier.

### 8.2.2 Exercised Permission Behaviour

[PR #1223](https://github.com/sgttomas/chirality/pull/1223) couples the
HELP_HUMAN authorization interpretation with resolver boundary tests. The resolver
retains authorized write targets while denying unauthorized targets and respecting
a read-only host. Tests cover absent authorization and escaping targets, including
symlink escapes. This supports the resolver behaviour under the examined conditions.

That result does not establish containment of every command, host or App entry
point. An instruction, a tested path predicate and an operating-system sandbox
have different coverage. App v4's role configuration remains a product contract.
The [workflow resolver contract](../../tools/workflow_runtime/README.md) defines
its own operations; a claim about broader containment requires evidence about
broader paths.

## 8.3 Access to Relevant Meaning

### 8.3.1 Current Sources and Queries

On this chapter's identified source basis, active project deliverables maintain
commitments and acceptance criteria in `ScopeOfWork.md`, useful technical
reasoning in `Design/`, and consumer-owned
needs and conditions in `deliverable.yaml`. The
[Root entry](../../execution/_Coordination/LOOP_INIT.md) locates the shared
component and affected consumers; an active project entry locates product
commitments. The authorized work directs the inquiry. Current shared locality
naming is governed by Root `AGENTS.md`: `Work/` is the convention going forward.
App and SWBPIPE adopted `Work/` by the October 30 extension basis. Historical
`Design/` paths below locate the original evidence; the rename does not change
what those observations established.

The [deliverable CLI](../../tools/deliverables/README.md) exposes
`neighborhood`, `impact`, `touches`, `dag-diff` and `check`. It reports source
locations and its observed basis, including working-tree changes. Code mappings
indicate relevance, not exclusive ownership. Missing mappings leave a partial
answer rather than proving that there are no consumers.

`check` rejects malformed data and invalid or escaping identities and paths.
Unresolved suppliers, planned paths and cycles are reported distinctly. Mutual
or non-gating relationships can legitimately form cycles. The checker does not
establish that an input is suitable; an agent must examine the input's condition
and actual contents within the assignment.

### 8.3.2 Preservation of Meaning Through Transformation

[App v4 PR #1213](https://github.com/sgttomas/chirality/pull/1213) and
[Piping PR #1216](https://github.com/sgttomas/chirality/pull/1216) provide bounded
evidence about preservation of dependency conditions. Source-row accounting and
comparison with identified graph bases detect omitted or changed declarations.
Independent examination of meanings complements those mechanical checks.

This supports preservation on the examined basis, but it establishes neither
that the source declarations captured every real dependency nor that any
supplier met its consumer's condition. Several distinct conditions between the
same pair of deliverables must remain understandable; reducing them to one
readiness label would lose part of the relationship.

### 8.3.3 Method Selection and Actual Consumers

Methods are indexed in `workflows/index.json` and selected as needed. The resolver
specifies ordered selection, explicit resources and source identities. Missing
or escaping selected resources fail resolution; omitted resources are not read.
Returned hashes identify the inputs read by the resolver, but they do not
establish that the host delivered them to an agent or that the agent applied the
method.

The [workflow index builder](../../tools/validation/build_workflow_index.py)
connects package metadata to the catalog; an adopted App bundle is a separate
consumer. The useful evidence concerns the saved source, selected identity,
affected consumer and checked connection. Updating a shared source alone cannot
establish adoption by each product.

## 8.4 Production, Examination and Integration

### 8.4.1 Continuing Ownership

The [coordinated-knowledge-work workflow](../../workflows/coordinated-knowledge-work/WORKFLOW.md)
organizes purpose, integration, contributions and scrutiny. Owners continue
through ordinary repairs. Independent work can continue while an unrelated
branch is unresolved; shared writes, interfaces, resources and review capacity
can require coordination. A missing declared edge cannot prove independence.

The implementation supplies a usable method, not proof that every undertaking
retains intent or reaches integration. Continuity draws on current artifacts,
conversation, tool queries and Git history, with recovery support where needed.
Recovery requires evidence from an actual continuation: a preserved conversation
alone does not establish that work resumed without loss or duplicated action.

### 8.4.2 Selected Checks and Reuse

The [CI selection reference](../CI_SELECTION.md) defines `harness` as the required
aggregate result for repository checks and selected active-product workflows.
Unrelated jobs can be skipped explicitly. A selected job that fails, is cancelled
or is missing must prevent the aggregate from passing. Selection and failure
propagation are distinct properties requiring examination.

[PR #1214](https://github.com/sgttomas/chirality/pull/1214) supplies recorded
checks of that selection. Applicable prior passes can be reused, with the explicit
qualification that no new tests executed. A build cache is not a prior test result;
manual runs can obtain fresh evidence. Reuse depends on applicability to the
candidate and concern, rather than the mere existence of a green result.

The repository selects targeted regression checks and independent scrutiny for
numerical meaning, persistence, permissions and destructive operations. Routine
reversible work can be inspected or exercised directly. This selection principle
makes consequence and detectability relevant; it cannot establish that every
important behaviour was selected or that the checks cover it adequately.

### 8.4.3 Evidence at Connecting Paths

The integration reviews recorded in [Appendix E](appendix_e_development_history.md)
identified live technical references among intended removals. Repair needed both
relocation and consumer updates. A passing test of the generated product did not
establish that the next invocation of the generator would remain usable. The
connecting path, rather than the isolated component, was the subject requiring
examination.

[App PR #1240](https://github.com/sgttomas/chirality/pull/1240) supplies a different
witness: actual native interaction exposed role-header accumulation and input
autocorrection defects, followed by repair. This supports exercising the assembled
application, but it does not establish general usability or the absence of other
defects. The appropriate finding concerned product behaviour and prompted product
repair.

Agents can do extensive reckoning on such evidence: inference, criticism,
comparison, investigation and authorized action. Human judgment sets and revises
the purpose of the work and what the person can stand behind throughout.
Independent agent scrutiny can improve the grounds without performing that
person's act of reliance.

## 8.5 App and Domain-Software Evidence

### 8.5.1 Operative Perspective: The App

The [App PRD](https://github.com/sgttomas/chirality/blob/a602024416ace9652f61bb2043889c307fd4e09d/projects/chirality-app-v4/docs/PRD.md) and
[architecture](https://github.com/sgttomas/chirality/blob/a602024416ace9652f61bb2043889c307fd4e09d/projects/chirality-app-v4/docs/ARCHITECTURE.md) define the
application-specific inquiry. Conversations, request cards, workflow authoring,
trial runs and inspection of returned work supply operative paths through which
intent and methods can be tried and revised.

The [host-integration contract](https://github.com/sgttomas/chirality/blob/a602024416ace9652f61bb2043889c307fd4e09d/projects/chirality-app-v4/docs/HOST_INTEGRATION.md)
proposes making application capabilities discoverable. A common catalog does not
establish correct domain behaviour, good interfaces, recovery or every transport
adapter.
[PR #1244](https://github.com/sgttomas/chirality/pull/1244) assigns file and record
writes, supplier interaction and capture of human acts to the Rust host, while
the web view presents and sends human-initiated requests. This ruling is a product
commitment; its text alone does not establish that all paths conform to it.

An accepted act and substantive engagement remain different claims. Capturing a
human action can support attribution and identify its subject, but it cannot
establish that the person understood the consequences or performed adequate
professional examination.

#### Workflow trials must test the intended instructions

A trial is useful only if its relationship to later use is understood. Earlier
attachment-based trials supplied instructions differently from a registered
workflow run. A successful trial could therefore depend on context or wording
that would not be present when the workflow was used.

The [App's workflow design](https://github.com/sgttomas/chirality/blob/a602024416ace9652f61bb2043889c307fd4e09d/projects/chirality-app-v4/execution/PKG-02/DEL-02-02/Design/WORKSPACE_AND_REGISTRATION.md)
made this difference explicit. At the identified evidence basis, preparation
snapshots the draft and compares trial text with the text used for a registered
run. A trial label and its own references identify the different activity.
Changed draft content must not silently become a different trial. These checks
concern what was supplied. They do not establish that the agent followed the
instructions or that the method was suitable.

Trying a method in its authoring conversation can use helpful context. Trying
it in a fresh conversation can expose assumptions left out of the instructions.
Neither is always preferable. The author must know which question the trial
examines. Native examination of both trial routes remained incomplete at the
identified basis.

#### An interrupted turn does not prove that its command stopped

The [October 10 native App observation](https://github.com/sgttomas/chirality/blob/a602024416ace9652f61bb2043889c307fd4e09d/projects/chirality-app-v4/execution/PKG-01/DEL-01-02/Design/NATIVE_WITNESS_2026-10-10.md)
recorded an interrupted turn running `sleep 90`. The live turn ended as
interrupted, but later supplier history showed that the command completed with
exit zero after about ninety seconds. The App retained these observations
separately. It did not establish that interrupting a turn stopped the command.

This matters before retrying work that can change files or affect another
system. A correct turn-status label can still leave the person without the
information needed to act. Recovery must examine the operation's actual outcome,
including uncertainty about whether it completed, rather than infer that outcome
from the conversation state. This is a bounded observation of that configuration,
not a claim about every later App or supplier version.

### 8.5.2 Evaluative Perspective: Piping

The [Piping PRD](https://github.com/sgttomas/chirality/blob/a602024416ace9652f61bb2043889c307fd4e09d/projects/chirality-piping/docs/PRD.md) distinguishes
physical models, analytical models, analysis runs, comparison and handoff. These
objects need domain definitions, numerical implementation and evidence. The cases below examine limits of the software operations and calculations.

Operation validation, numerical verification and engineering adequacy answer
different questions. Operation validation examines whether a proposed change
satisfies the engine's defined conditions. Numerical verification examines
calculation against an appropriate reference or method. Engineering adequacy
concerns whether physical intent, model assumptions, cases, alternatives and
results support the proposed use. Passing the first cannot establish the others.

The [illustrative support-arrangement revision](WORKED_EXAMPLE.md) links those
questions to practical alternatives and the person's choice and revision. It is
an illustration, not measured evidence. Piping is one instance of domain software;
its numerical results do not establish economical transfer to all domains.

#### Missing inputs must remain visible

The [solver-boundary tests](https://github.com/sgttomas/chirality/blob/a602024416ace9652f61bb2043889c307fd4e09d/projects/chirality-piping/tests/test_analytical_solver_boundary_adapter.py)
examine missing properties, unrecognized loads and invalid orientations. An
unknown property must not become an unexplained default merely to make a solve
possible. The agent can help locate a source or propose an assumption, but its
basis and proposed use must remain available for examination. These tests cover
an internal path; they do not establish every graphical or agent entry path.

#### Tests must reach the implementation used for the work

The [operation-engine decision](https://github.com/sgttomas/chirality/blob/a602024416ace9652f61bb2043889c307fd4e09d/projects/chirality-piping/docs/architecture/adr/ADR-0001_operation_seam_engine_unification.md)
describes a native Rust engine and an earlier separate TypeScript implementation.
Testing each did not establish that both applied the same validation or produced
the same model. Replacing the browser implementation with a WebAssembly build of
the Rust engine removed that source of divergence. It did not prove the engine
correct: both entry paths could still share a defect.

This case distinguishes consistency between entry paths from numerical
verification and engineering adequacy. Each needs evidence about its own subject.
A common interface alone cannot establish those results.

#### A numerical repair has a defined scope

The [curved-element numerical account](https://github.com/sgttomas/chirality/blob/a602024416ace9652f61bb2043889c307fd4e09d/projects/chirality-piping/execution/PKG-04/DEL-04-01/Design/curved-numerical-integrity.md)
describes cancellation in small-angle expressions and repairs using a stable
half-angle form, explicit geometry and scaled inversion. Short-arc tests compare
with high-precision references and examine rigid motion and coordinate changes.

The local repair does not remove ill-conditioning caused by a short, stiff bend
beside longer, softer elements in the assembled system. Some cases remain
sensitive or are refused. Reporting that limit is more informative than treating
a passing local test as evidence for the whole solve. The account also records
removal of tests for a proposed mutation found equivalent under the relevant
conditions. Test count is not a substitute for a meaningful distinction between
correct and defective behavior. These are findings in the cited source, not
numerical examinations newly performed for this manuscript.

### 8.5.3 Longitudinal Redevelopment and Retained Learning

The App case supplies substantial evidence of preserved meaning and useful
evolution across redevelopment. Its observation unit is the complete path from
an earlier working behavior, through interpretation and accepted successor
commitments, to behavior in the rebuilt application. The developer directs the
undertaking and its consequential choices; agents carry the production and
examination through the deliverables.

| Stage | Evidence | Finding |
|---|---|---|
| Working predecessor | [v3 execution record](https://github.com/sgttomas/chirality/blob/2b0572fe049c8ffaa02d61b7dbbc3ae41bc589f6/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/spike/EVIDENCE.md), September 12 | Native planning, real tool execution, conversational workflow creation, reuse/refinement, interruption and relaunch were exercised. A failed refinement path was repaired and exercised successfully. |
| Abstraction for a successor | [Investigation record](https://github.com/sgttomas/chirality-app/blob/032725d32b67e117b8e1fb2b5fa9aa47b30de12e/conceptual/WORKING_RECORD.md) and [exemplars and lessons](https://github.com/sgttomas/chirality-app/blob/032725d32b67e117b8e1fb2b5fa9aa47b30de12e/conceptual/EXEMPLARS_AND_LESSONS.md), September 25 | Existing behavior, requirements, failures and unrealized intentions were distinguished. Useful relationships were selected for preservation while obsolete runtime mechanisms were reconsidered. |
| Accepted production basis | [Composite acceptance](https://github.com/sgttomas/chirality/blob/cea76c2f469350d237c5d579b765113f7569f0e5/projects/chirality-app-v4/execution/_Coordination/Acceptances/APP-V4-BASIS-20260926/ACCEPTANCE.md), [final decomposition decision](https://github.com/sgttomas/chirality-app/blob/032725d32b67e117b8e1fb2b5fa9aa47b30de12e/execution/_Decomposition/checkpoint_snapshots/GROUP3-20260928T001055Z/DECISION.md) and [DEL-02-02](https://github.com/sgttomas/chirality-app/blob/032725d32b67e117b8e1fb2b5fa9aa47b30de12e/execution/PKG-02/DEL-02-02/ScopeOfWork.md) | The successor basis became 11 packages and 41 deliverables, with explicit ownership of the complete create–trial–review–register–reuse–refine experience. The counts identify the subject; they are not outcome measures. |
| Realized successor behavior | [Native walkthrough](https://github.com/sgttomas/chirality-app/blob/032725d32b67e117b8e1fb2b5fa9aa47b30de12e/execution/PKG-02/DEL-02-02/Work/NATIVE_WALKTHROUGH_2026-10-14.md), October 14–16 | Four registered revisions remained in one lineage. The workflow was tried, reviewed, registered, reused on new inputs and continued after relaunch. Summary and source-line-reference outputs were added while earlier reports remained compatible. |
| Feedback into production | App changes [08c67c4b](https://github.com/sgttomas/chirality-app/commit/08c67c4bf2dbb33b587931282d21681151b7b6e1), [e1a8e3e7](https://github.com/sgttomas/chirality-app/commit/e1a8e3e7c5e3aac7107f66700ab11abb1bf00083) and [687c78ea](https://github.com/sgttomas/chirality-app/commit/687c78ead04d70cbf2d4bea0a3dec732a9c27829) | Revised trial intent reached requirements, acceptance/verification criteria and Work design; native findings reached implementation and tests; later declaration findings reached supplied guidance and its checks. |

What persisted was a set of meanings and relationships: the person directs and
accepts; the agent contributes; a draft differs from a registered workflow; a
workflow revision differs from its execution; source and content identity matter;
an observed result differs from an attributed human act. Storage, supplier
hosting, interfaces and some categories changed. This is preservation through
re-expression, with functional evolution, rather than a requirement to reproduce
every earlier mechanism.

The walkthrough records actual limitations alongside the successful sequence.
It used debug candidates; part of its earlier activity was reconstructed from
session history and persisted artifacts. New guidance reached one installed
App through the owner's explicit restore, and some child-instruction observations
were unavailable. These observations identify product behavior and repair needs. The evidence
supports the observed continuity and extensions, without claiming automatic
preservation of every behavior or qualification of every later build.

Human direction, examination and correction are constitutive of this
undertaking. They connect its purpose to what is built and to what experience
changes next.

The development method was itself revised in use. The [October 4 direction](https://github.com/sgttomas/chirality/blob/24e9117b9c2d9d10f57642da4eef0d13c90bb166/projects/chirality-app-v4/execution/_Coordination/AgentRuns/APP-V4-GRAPH-CLOSURE-20261004/OWNER_DECISIONS.md)
redirected dependency rewording toward a coupled contract core, a working
skeleton and subsequent parallel implementation. The deliverable basis remained,
while the means of carrying it out changed in response to purpose. This is a
recorded instance of the framework improving its own means through human
judgment and agent reckoning.

### 8.5.4 Dated Engineering Comparison Evidence

The October 30 extension also examined SWBPIPE's owner-held CAEPIPE comparison
records. The [pilot design](https://github.com/sgttomas/SWBPIPE/blob/bc9f7961acee72441ec06c104ed97d4f1c77faa4/execution/PKG-17/DEL-17-05/Work/caepipe-correlation-pilot.md)
identifies invented inputs, independent analytical witnesses, unit and sign
mapping, comparison tolerances and a deliberately injected fault. Selected
quantities in the force-loaded cantilever, anchored thermal and longer-span
cantilever cases agreed with CAEPIPE within the declared pilot tolerances.
The injected fault produced discrepancies that the comparison detected.

The examination checked stored input and output identities and independently
recalculated the recorded pilot tolerance classifications. Raw external-tool
outputs and detailed comparisons remain in the owner's private evidence
collection; the public design identifies the method, not a public reproduction
of those results. This account reports the examined case findings and their
scope. It reports no fresh solver execution or general equivalence between the
programs. The larger exploratory set includes discrepancies and unresolved
findings; its existence is not a claim that every case agreed.

These observations add external numerical evidence to the development case.
Agreement on identified quantities supports the implementation under those
conditions, while the detected fault shows that the comparison can distinguish
a real difference. Neither result establishes professional adequacy or code
compliance. Investigation of differences, like successful comparison, supplies
material for the next engineering and software decision.

### 8.5.5 Forms of Transfer

| Transfer | Evidence and standing in this case |
|---|---|
| Development method across products | The App and SWBPIPE use shared roles, methods and deliverable contracts to produce distinct applications. Their implementation and examination records demonstrate that use. |
| Product meaning across time | The App trace in §8.5.3 demonstrates preserved distinctions and useful behavior through successor definition and redevelopment, with recorded extensions and repairs. |
| Agent capability embedded in a domain product | The [current App–SWBPIPE integration account](https://github.com/sgttomas/chirality-app/blob/032725d32b67e117b8e1fb2b5fa9aa47b30de12e/execution/PKG-09/DEL-09-06/Work/SWBPIPE_CODEX_INTEGRATION.md) identifies implemented contributions and remaining connected evidence. A complete product journey remains to be established. |
| Use by additional practitioners and organizations | A further empirical setting, in which participants bring their own purpose, judgment and steering. Its outcomes and adaptation costs have not been examined here. |

These transfers have different subjects. An unfinished embedded-agent journey
does not undo observed use of the development method or the App's temporal
continuity. Conversely, those achievements do not establish the remaining
runtime integration. The distinction makes both the attained results and the
next questions explicit.

## 8.6 Assessment and Remaining Questions

| Claim | Relevant evidence at the basis | Limit or remaining question |
|---|---|---|
| Authorized paths are distinguished | Resolver tests and assignment/policy interpretation | Coverage of each host and actual entry path |
| Dependency meanings are preserved in the examined transformation | Source accounting, graph comparison and independent examination | Missing original declarations and present input suitability |
| Methods can be selected from explicit sources | Resolver operations, resource boundaries and source identities | Delivery, interpretation and adoption by actual consumers |
| Integration can detect failures beyond component checks | Reference/consumer findings and native-use repair | Common assumptions and interactions outside the examinations |
| Human acts can have identified subjects | Product commitments and attributable decisions where captured | Competence, understanding and substantive engagement |
| Product meaning survives specification-led redevelopment | Predecessor execution, successor investigation, accepted deliverables and native v4 use (§8.5.3) | The identified behaviors and revisions; preservation of every behavior is not inferred |
| Experience changes the product and the production method | Traced trial/guidance repairs and the October 4 development correction | Particular observed improvements; no isolated causal estimate for each mechanism |
| Selected piping quantities agree with an external solver | Stored comparisons, analytical witnesses, identity checks and fault detection (§8.5.4) | Declared cases/tolerances; private raw evidence; broader findings remain |
| The development method transfers useful means | App and SWBPIPE production/examination records (§8.5.5) | Wider settings, adaptation costs and embedded-agent product integration are distinct subjects |

The combined evidence demonstrates useful production, correction and retained
meaning in this longitudinal case. Repository instructions, role files, selected
methods, deliverable sources and the query CLI are in use; the relevant Git and
CI paths have been exercised. More substantively, the App's selected meanings
and behaviors reached a redeveloped implementation and were extended in use.
[PR #1238](https://github.com/sgttomas/chirality/pull/1238) provides the accepted
manuals describing that working model, but their existence does not imply that
the whole system is fully validated.

Evaluation must include applicable obligations, uncertain premises, negotiable
preferences and control costs separately. Required conditions retain their
standing; attention, delay, maintenance, false alarms and the consequences of
missed errors matter in choosing how to meet them. More records or checks need to
make a concrete contribution to the work; fewer controls need evidence that their
functions are unnecessary or adequately served elsewhere. No universal scalar or
mandated process resolves this assessment.

The most useful further investigations concern connecting paths: whether a fresh
participant finds a governing condition and its supplier; whether a method change
reaches its adopted consumer; whether a reviewer receives the candidate and actual
basis; and whether work can continue reliably after an interruption. Their
outcomes must concern usable work, errors that matter and total effort, including
owner attention. These research questions create no product commitments or
standing implementation backlog.

Comparative productivity, comparative error detection, professional suitability
for a particular deployment and sustained adoption across further settings
remain separate questions. The observations do not isolate the contribution of
each mechanism from changing model capabilities, accumulated knowledge or task
mix. Human purpose, judgment and steering are foundational parts of the method
whose local efficacy is observed. Activity counts cannot establish the broader
comparisons, but the executed and traced results establish more than activity.

## 8.7 Summary

The development record supplies substantial longitudinal case evidence for a
human-directed, agent-executed method that produces working software, carries
core product meaning through redevelopment, and supports functional extension
and correction. Sources, methods, relationships, authorization and continuing
ownership connect these observed production and examination paths. Each finding
retains its actual subject, source basis and checked path.

App and Piping expose operative and evaluative questions that Root alone cannot
answer. Their findings can revise the shared means through iterative feedback.
Accountable human judgment remains situated engagement throughout that
relationship; neither implementation traces nor passing checks establish it on
the person's behalf.
