# Chirality Library — Product Requirements Document

**Status:** The owner accepted SCA-20261101-UNDERTAKING-EVALUATION on 2026-11-01, against candidate e157d14910e84cf149f2ead524d585467b18e0f7. The predecessor acceptance below remains historical.
**Revision:** 2026-10-31.  
**Acceptance:** "I approve this PRD." The approved source, before these acceptance
annotations, has SHA-256 `0e9c38d1550ebef5aa933efb4dcddd201f325f3b9a04d6a2c2861d581185e70a`.  
**Owner clarification:** “There is no PEC.” The current §2.3 frozen-product
list reflects this correction; the original acceptance and source identity above
remain historical.

**Downstream use:** Project decomposition, project setup, ScopeOfWork authoring
and consumer-local dependency authoring. Package and deliverable definition
belongs to decomposition; this PRD assigns neither.

## 1. Product outcome

Deliver a maintained Chirality library containing the information, instructions,
tools and execution material needed to use, maintain and develop its own holdings.
A maintainer working under an authorized undertaking must be able to locate the
current basis, pursue the work through the library's methods, verify the result,
reconcile affected holdings and leave the work usable for continued maintenance.

The holdings include principles, publications, roles, workflows, tool-use
instructions, executable tools, formats, reference information and `execution/`.
The library serves the owner's work across projects, embedded agents in products
such as App v4, and other adopters. Consumers retain their own authority, data,
product operation, acceptance and release decisions.

The repository remains usable on its own. An optional thin companion can support
repeated operations where a concrete need warrants it. Existing Git, search,
review, release, validation and scheduling mechanisms are the implementation
baseline; a new application or hosted service is not required.

The selected successor increment adds optional local examination of repository
state change, whether that change justifies the effort under relevant conditions,
and how those conditions can guide more specific local goals and improvement
hypotheses. An undertaking trace supplies evidence of effort and possible means;
activity alone is not the benefit. Repository comparison may span undertakings
or proceed without a complete execution trace where its question permits.

## 2. Objectives and scope

### 2.1 Product objectives

These objectives are the source for decomposition's objective and scope mapping.
Their labels identify PRD intent, not packages or deliverables. A deliverable may
support several objectives, and an objective may require several deliverables.

| Ref | Objective | Required outcome |
|---|---|---|
| O1 | Make maintenance accessible from within the library | A maintainer can enter from a bounded undertaking and find the relevant holdings, instructions, execution work, source basis and unresolved conditions |
| O2 | Maintain the library through its own methods and tools | Additions, revisions, verification, integration and recovery can be carried out using maintained instructions and actual tools; necessary reusable procedure is available in the library |
| O3 | Preserve coherence through changes in understanding and structure | Affected definitions, claims, methods, tools, publications and work records remain consistent with their intended uses, evidence and governing values, or expose the unresolved conflict for decision |
| O4 | Support local progress within the product's wider network | Deliverable localities support objective-directed action, meaningful input/use conditions, evolving understanding and coordinated integration without requiring a complete global graph |
| O5 | Make reuse, change and continuity dependable | Consumers can obtain identified material, inspect consequential changes and choose adoption; maintainers can preserve history, prepare publication and recover unfinished work |

### 2.2 In scope

- Library entry, organization, categorization and directed discovery instructions.
- Optional tool-supported evaluation of repository states, their changes and
  the efforts/means associated with them, including identified comparative cases,
  an inspectable local report and a reusable agent workflow.
- Instructions and tools for maintaining the holdings, including the means of
  revising those maintenance instructions and tools.
- Scope-bounded reconciliation of instructions, executable behavior, shared
  definitions and publication content affected by the work.
- An accepted decomposition and fresh setup of Root's own maintenance execution,
  using the library's existing methods and tools.
- Consumer-local dependency declarations, query use and recoverable working
  material supporting the resulting local goals.
- Procedures for obtaining copies, proposing and integrating changes, occasional
  exclusive maintenance custody, publication preparation and polling for changes.
- Compatibility checks for affected known consuming interfaces.
- The authorized archive transition and preservation of historical references.

For each affected area, establish what is already usable, what needs connecting
or repairing, and what is absent. Scope implementation to the required changes
and reuse applicable evidence. This classification belongs in the work, not a
new permanent register.

### 2.3 Boundaries

- Principles, thesis, manuals and courses remain maintained holdings. Their
  authoring work can live in execution; their sources retain their actual homes.
- Root's execution, repository grants and host coordination rules are scoped
  Root holdings. Library consumption does not transfer them to other projects.
- App v4 and SWBPIPE remain independent. Their production adoption and release
  are not prerequisites for accepting a verified library interface.
- App v3 and Runtime remain frozen. Recovery does not reactivate them.
- Private knowledge, consumer operational data and credentials stay outside the
  public library. Public examples and fixtures must be suitable for publication.
- No standing global audit, central relationship graph, subscriber registry,
  automated project management or mandatory companion installation is in scope.
- `plans/` and `_DomainEngines/` were removed from this repository on
  2026-11-04 and remain in the private `sgttomas/chirality` repository.
  Additional archival removals remain subject to the disposition in §5.

## 3. Requirements

The R01–R17 labels are product requirement references. Decomposition will normalize
accepted scope and map it to objectives and deliverables using its own contracts.

### 3.1 Holdings and discovery — O1, O3, O5

**R01 — Entry.** Maintain an explicit starting route to the selected library
basis, applicable role and repository instructions, relevant holdings and current
execution. The undertaking comes from the conversation. Initialization starts
none. The entry must itself be locatable and maintainable through this route.

**R02 — Local meaning.** Organize holdings in recognizable localities. Entries
must supply the purpose, applicability, source standing, relevant inputs/resources,
outputs and limits needed to use the material. Categories and references remain
searchable where the material lives. Distinguish explanation, instruction,
example, proposal and historical source. Preserve required resources and notices
when material is copied or packaged.

**R03 — Directed discovery.** Supply instructions for purposeful file/content
search, following relevant references and querying structured information.
Discovery must preserve source identity and distinguish stated relationships,
inferences, unknowns and search limits. Local views may be incomplete, cyclic
and revised as the inquiry changes. No DAG or globally maintained representation
is required. Existing indexes remain where consumed and are checked or regenerated
from their owning sources; they do not substitute for reading selected material.

### 3.2 Maintenance operations — O2, O3, O5

**R04 — Operational coverage.** The library must contain applicable instructions
for the following operations. Reuse or connect existing methods; the list does
not require one new workflow or tool per operation.

| Operation | Required coverage |
|---|---|
| Add or revise a holding | Purpose, scope, destination, relevant existing material, source identity and checks |
| Organize, relocate or retire | Actual references and consumers, replacements or historical standing, recovery and deletion authority |
| Diagnose and reconcile | Conflicting claims, source meaning and observed behavior; owning material; evidence and repair scope |
| Assess connected change | Relevant inputs, uses and consequences across instructions, tools, publications and execution |
| Review and integrate | Proportionate scrutiny, actual checked revision, findings, owning-text updates and repository change procedure |
| Prepare publication and inspect updates | Version basis, consequential changes, dependencies, limitations and independent adoption |
| Recover or continue | Preserved basis and work, available checks, open conditions and current authority |
| Change the maintenance means | Existing applicable method, proposed replacement, review, adoption and recovery of the previous basis |

**R05 — Actual capabilities.** Tool instructions must describe executable commands
or interfaces, dependencies, outputs, write effects, failure behavior and limits.
Use the selected library's tools for repeatable operations where available. State
unavailable capabilities and permitted fallbacks. Repair a necessary reusable
procedure in its owning material rather than leave it only in a conversation.

**R06 — Self-maintenance.** The entry, roles, maintenance methods, tools and
execution records are subjects of maintenance under these same requirements.
Proposed replacement instructions do not authorize themselves or retroactively
change the basis of their review. Keep a usable selected method and entry until
their replacements are verified and adopted.

### 3.3 Execution and dependencies — O1, O2, O4

**R07 — Local goals.** Decomposition must define bounded contributions to the
product objectives. Each resulting deliverable must have a meaningful intended
improvement, scope, expected outputs and evidence for evaluating its result.
Objectives do not prescribe package boundaries; source directories and activities
are not automatically deliverables. Shared material can be relevant to several
contributions without creating conflicting ownership of the same change.

**R08 — Work locality.** Setup must materialize the accepted deliverables under
`execution/PKG-nn/DEL-nn-nn/` with:

- `ScopeOfWork.md`: the local goal, accepted scope/objective references, output
  definitions, boundaries, acceptance criteria and verification methods.
- `deliverable.yaml`: actual consumer-local needs and conditions, plus useful
  source, code and check references.
- `Work/`: current reasoning, evidence, alternatives, consequential attempts,
  unresolved conditions and locally retained outputs, with maturity explicit.

Code, publications and reusable instructions retain their maintained homes,
referenced from the locality. Leave unchanged declarations alone.

**R09 — Meaningful dependencies.** A need must identify the input, its intended
use/condition, the relevant case or trigger, and its source or unresolved binding.
Author local needs after scope exists, using accepted decomposition inputs,
ScopeOfWork, relevant work material and sources. Preserve distinct conditions
between the same endpoints, preliminary versus final use, reciprocal relationships
and technical holds. Do not infer whole-deliverable finish-to-start constraints
or supplier commitments from a dependency. Assess suitability from evidence;
file presence, merge status and structural checks are insufficient.

**R10 — Local progress and integration.** A locality must support choosing an
authorized action from the goal, current evidence and actual input conditions,
examining its effect and revising the route. Refine work and understood dependency
neighborhoods as knowledge develops. Continue unaffected work when a particular
condition remains unresolved. Changes to commitments, acceptance criteria or
reserved decisions return to the owner. Check local results against affected
uses; one integration owner retains the broader purpose for related contributions.

Queries derive relevant relationships from owning declarations and report source
basis, scope, unknowns and partial coverage. Do not maintain a second manual
progress graph. An inquiry may reveal that a goal or partition needs revision;
return that finding through the applicable authority rather than optimize local
completion at the expense of the product.

### 3.4 Coherence and verification — O2, O3, O4

**R11 — Coherence under revision.** Review affected holdings against their
ontology, epistemology, praxeology and axiology: their definitions and relationships,
warranted claims, described actions and governing values. Record consequential
reasoning in the owning work. These perspectives do not require four separate
reports or approvals. Bound the holdings, relationships and uncertainty being
examined; expand inquiry where needed without silently expanding the commitment
to change every connected item.

A change in a distinction, evidence, method or goal must be appraised for its
consequences in the other affected perspectives. Reconcile operating guidance
and publications that describe it, or identify the retained edition's earlier
basis. Preserve historical identities and scoped adopted contracts. Distinguish
library definitions from product-specific runtime policy and enforcement.

**R12 — Evidence and continuity.** Verify the actual candidate in proportion to
the change. Numerical meaning, persistence, permissions and destructive operations
require focused regression checks and independent scrutiny. Content review,
behavior tests and consumer-interface checks establish different claims. Reuse
applicable evidence; report missing evidence as unverified.

Unfinished work must be recoverable from its locality and actual review record:
source basis, usable result, checks, unresolved conditions and next needed action.
Keep at most one replaceable recovery note where those records are insufficient.
A past record does not authorize restarting work or create a standing backlog.

### 3.5 Use and change management — O3, O5

**R13 — Independent consumption.** Consumers may consult, invoke or copy selected
material through ordinary files, Git, archives and documented interfaces. They
retain required resources, applicable licenses and the actual source basis.
Git is not required merely to read the library; tools declare their own real
dependencies. Local adaptations remain distinguishable from shared and packaged
sources. Check affected named consumer interfaces at an explicit basis; provide
a supported path or coordinated adapter before an incompatible change.

**R14 — Check-in and custody.** Maintainers review and integrate contributions
within their grants. For an operation that requires exclusive custody, identify
the holder, affected item, reserved operation and release/recovery condition.
Use an existing locking or coordination mechanism with honest enforcement limits.
Readers normally retain the last checked-in material. Resolve interrupted custody
through its authorized maintainer; elapsed time does not authorize discarding work.

**R15 — Publication.** The owner publishes named versions from verified source
revisions; these are the downstream default. Consumers may explicitly follow
`main` for development. A merge is not an owner release. Published material must
retain source identity, applicable notices, dependencies and known limitations.
Commit-pinned history and publication editions must remain recoverable through
their documented routes. Adoption stays with the consumer.

**R16 — Change inspection.** Existing review descriptions and publication notes
must explain affected holdings, the old/new basis, the reason and difference in
meaning or use, and known migration consequences. Provide a polling/inspection
procedure using existing release and diff facilities. Consumer interests and
impact inquiry stay local. Distinguish the basis in use from publications examined;
failed or partial checks must not claim no change or imply adoption. Scheduling,
external delivery and unattended operation need their actual configuration and
authority. No new notice register is required.

**R17 — Existing foundations and public boundary.** The repository must remain
usable without a companion. Add bespoke tooling only for a demonstrated gap in
these operations. Ordinary library use must not depend on undisclosed sibling
checkouts, dated run directories, private source inputs or credentials. Private
consumer evidence stays local; public fixtures and summaries must be cleared.
Required credential checks apply to public changes.

### 3.6 Work and repository-change evaluation — O2, O3, O4, O5

**R18 — Evaluate useful state change and its means.** Supply an optional local
capability to select an evaluation question, bind before/after repository bases
and relevant conditions, examine the resulting change against its grounds and
intended use, and relate the result to observed effort without invented attribution.
Distinguish commitments, representations, implementation, observed behavior,
evidence, uncertainty and accepted/issued standing. A commit, merge, file count
or completion claim alone does not establish improvement. Repository comparison
shall not require a complete host trace when its selected claim can be supported
without one.

Make it possible to derive more specific local goals from conditions of useful
state change and to examine hypotheses about methods, tools, context and
coordination that might establish those conditions more effectively. Bind actual
outcomes, affected uses, relevant total effort and the cost of evaluation itself.
Preserve the preceding basis when goals or criteria change. Retention, reframing,
negative findings and a supported conclusion that evidence is insufficient are
valid returns; a faster variant or positive numerical score is not mandatory.

The initial capability shall provide one actual supported record-import route,
evidence-linked local inspection, identified case preparation and a supported
route for collecting/comparing baseline and variant trial results. Use the selected
host's execution mechanism rather than commission a new agent runtime. Bind the
host/export and invocation contracts, permitted data, project, task family and
outcome examination before dependent implementation or claims. Demonstrate actual
use as well as labelled fixtures for failures, missing evidence and variability.
State observed coverage and unsupported cases; a synthetic record alone cannot
qualify the promised real route.

Human judgment shapes purpose and relevant consequences throughout. Software
collects and calculates; bounded agent work investigates meanings and returns
supported findings. Keep the evaluation's own categories, grounds and burden open
to examination. A profile-specific score requires its explicit rubric and grounds;
there is no universal reward or automatic change to commitments. Activation does
not authorize all project observation, new host permissions, public data egress,
a mandatory merge gate, a permanent observer, a global project manager or automatic
model training/adoption. Existing standalone, privacy and consumer boundaries apply.

## 4. Acceptance criteria

The criteria below evaluate product requirements. They do not define deliverables
or require a separate project for each test. Select substantive authorized
maintenance cases; one case can establish several criteria. Reuse relevant prior
evidence and distinguish walkthroughs, synthetic cases and actual observed work.

| Ref | Acceptance criterion and evidence | Requirements | Objectives |
|---|---|---|---|
| A1 | From the entry and a bounded brief, locate the relevant holdings, method, source basis and execution work, including unresolved conditions. Verify directed discovery and source distinctions without relying on a complete central graph. | R01–R03 | O1 |
| A2 | Carry an actual instruction or tool change through preparation, review and integration using maintained library methods. Establish usable commands/resources and make any necessary reusable procedural repair available in its owning material. | R04–R06 | O2 |
| A3 | For accepted and set-up scope, trace a local goal to product objectives and demonstrate action selected from evidence and an actual input/use condition. Show how a finding changes the route or understanding, with affected neighboring uses examined. | R07–R10 | O4 |
| A4 | Resolve a scoped inconsistency across relevant holdings, including publication content where affected. Verify the owning changes, their warrant, their use and their consistency with governing values; preserve historical qualifications. | R11–R12 | O2, O3 |
| A5 | Revise a maintenance instruction, entry or supporting tool under the existing basis. Verify both the resulting holding and the means used to maintain it; preserve the preceding basis and actual adoption authority. | R06, R11–R12 | O1, O2, O3 |
| A6 | Obtain and use identified material through a documented consumer path. Test claimed compatibility against a named consumer's maintained contract or fixtures at a specified revision. Confirm notices, required resources and source identity. | R13, R17 | O5 |
| A7 | Prepare an identifiable publication candidate and meaningful change account; exercise the documented change-inspection procedure against a prior basis. Distinguish proposed, integrated, published, examined and adopted material. Actual release is an owner act. | R15–R17 | O3, O5 |
| A8 | Recover real retained work or a labelled recovery case from its locality and review record. Establish the usable basis and remaining conditions; where custody applies, verify release/recovery and its actual enforcement boundary. | R08, R12, R14 | O4, O5 |
| A9 | On a named project/task family, demonstrate an actual supported host-record route, identified repository before/after examination and baseline/variant comparison. Trace a useful state condition through a local goal or improvement hypothesis to the examined state change and relevant effort. Establish faithful data binding, meaningful outcome examination, comparability and limits; expose missing/malformed evidence and unsupported attribution. Return a warranted conclusion without requiring a positive improvement. The recipient can inspect findings and their grounds. | R05, R11–R13, R17–R18 | O2, O3, O4, O5 |

A repaired output alone does not establish that its maintenance procedure is
available in the library. A walkthrough does not establish executable behavior.
A generic demonstration does not establish compatibility with a named consumer.
Test the claim actually made. Consumer adoption and release remain independent;
compatibility checks may use an isolated environment.

The undertaking is complete when accepted objective/scope coverage is established,
the required maintenance paths work, and scoped findings are resolved or explicitly
dispositioned by the owner with their consequences. Check how the local results
fit together. New needs outside the commitment are returned with their relevance;
they do not create an unlimited audit or standing maintenance obligation.

## 5. Reserved choices

**PRD acceptance:** the owner has accepted the objectives, scope, requirements
and criteria. Decomposition, its deliverables and later implementation results
retain their applicable review and acceptance requirements.

**Additional archival scope:** the recommendation is to archive only the old
execution selected by the owner. The owner later disposed of `plans/` and
`_DomainEngines/`; they were removed from this repository on 2026-11-04 and
remain in the private `sgttomas/chirality` repository. Classification as
historical does not authorize removal.
Principles, thesis, manuals and courses remain library holdings. Existing indexes
are retained or deliberately migrated according to actual consumer needs.

No additional decision on a hosting platform, global graph schema or compulsory
companion is required to proceed with this proposal after acceptance.

**Selected additional tooling:** SCA-20261101-UNDERTAKING-EVALUATION selects
only the R18/A9 capability. The owner accepted its audited poststate and listed
corrections on 2026-11-01 against `e157d14910e84cf149f2ead524d585467b18e0f7`.
Setup and product implementation remain separately examined obligations. Other
bespoke tooling and companions remain conditional. This does not reopen or
invalidate an earlier accepted edition or authorize a successor release.

## 6. Inputs, dependency considerations and downstream use

### 6.1 Input basis

| Input | Intended use and condition |
|---|---|
| Owner steering and this PRD | Accepted scope and objectives for decomposition; unresolved scope remains explicit |
| `AGENTS.md`, active role instructions and Root entry | Current authority and maintenance route; remain usable until replacements are checked and adopted |
| Existing workflows and tools | Reuse for decomposition, setup, authoring, review, queries and publication; inspect the selected method's actual applicability and dependencies |
| Maintained holdings and their references | Source basis for affected changes; preserve meanings, editions, required resources and identified consumer uses |
| Consumer inventory and actual consumer contracts | Locate affected interfaces and provenance; inventory is bounded evidence, not a current global census or an adoption instruction |
| Relevant execution and review evidence | Reuse applicable findings and checks; historical plans create no backlog or new authority |
| R18 evaluation inputs | Identified repository states, available host records and permitted data, actual tool/execution interface, selected question and outcome/comparison basis; unknown coverage stays explicit |
| Pre-removal source history | Recovery and historical consumer pins; verify reachability and selected bytes before relying on the archive |

The initial compatibility questions included Root-specific versus reusable
instruction scope in the former runtime-interface, product-boundary and
compatibility-format references (removed on 2026-11-04; retained in the private
`sgttomas/chirality` repository); publication source/edition bindings; and the
deliverables format and queries consumed by the products and private planning.
These identify relevant inputs, not preassigned work packages.

The current deliverables CLI requires Git, HEAD and its declared dependencies.
Preserve actual live-metadata selection and project-root reference semantics.
A file-only query interface or namespace adapter is bounded implementation work
only where a selected consumer need requires it; its availability is not assumed.

### 6.2 Decomposition and setup contract

Use the Root library's `project-decomp`, then `project-setup` on the accepted
decomposition. `scope-of-work` initializes objective-grounded local contracts;
`dependency-extract` authors actual consumer-local needs after scope exists.
`construct-local-work-graph` supports subsequent inquiry and sequencing.

Decomposition normalizes accepted scope, vocabulary, objectives and open questions;
proposes cohesive packages and bounded deliverables with anticipated artifacts;
and checks coverage, ownership, interfaces and boundaries through its applicable
review and acceptance stages. It assigns the package, deliverable and formal
scope/objective identities. This PRD's O/R/A references remain source references.

Carry needed inputs with the responsible consuming deliverable, intended use and
condition, case/trigger and source location. Leave unknown bindings explicit.
Do not convert a general interface into every possible producer/consumer edge
or invent producer commitments. Setup materializes accepted localities and
ScopeOfWork contracts, then authors their local needs from actual scope and
work material. Reverse links and inquiry-specific graphs are derived on demand.

### 6.3 Required order

1. Obtain owner acceptance of the PRD.
2. Tag the verified complete pre-removal main tree before removal. Proposed tag:
   `archive/pre-library-execution-<actual-date>`. Remove accepted archive paths
   in one reviewed PR, retain/rewrite the operational entry and add recovery
   instructions. Repair removal-caused references/checks and preserve original
   consumer-pinned history, including App's historical SWBPIPE source bytes.
   Integrate after required checks and independent scrutiny.
3. Decompose the accepted scope using the selected library workflow. Obtain its
   applicable decisions and independent audit before decomposition acceptance.
4. Set up the accepted decomposition and authorized scope with Chirality's own
   preparation and authoring tools. Verify their current locality assumptions
   before use. Create `execution/PKG-nn/DEL-nn-nn/` with `ScopeOfWork.md`,
   `deliverable.yaml` and `Work/`; author actual needs after local scope exists.
   Run `python3 -m tools.deliverables --project . check` and inspect relevant
   neighborhoods. Structural checks do not decide input suitability.
5. Execute and integrate the resulting authorized work using the library's roles,
   methods and tools; verify §4 and return the result for acceptance. Necessary
   method/tool repairs remain explicit bounded work. Do not silently adopt
   historical scaffold, lifecycle or record requirements that conflict with the
   current instructions and selected project basis.

This acceptance supplies the basis for the ordered transition above. Subsequent
decomposition, setup, implementation acceptance and release retain their actual
authority requirements. Recovery does not reactivate frozen work. Private material
remains local; public material uses cleared requirements and consumer evidence.

### 6.4 Successor scope amendment

For SCA-20261101-UNDERTAKING-EVALUATION, use the current-project scope-change
route to preserve the predecessor and identify the exact PRD, decomposition and
contract changes. Materialize new localities only after amendment poststate
acceptance. Author new scopes before their native needs; reconcile affected
existing sources within accepted boundaries. Initial archival removal and
seven-locality formation are historical acts, not new work selected by this
increment. Product fulfillment, owner acceptance, publication and independent
consumer adoption remain subsequent, separately identified acts.
