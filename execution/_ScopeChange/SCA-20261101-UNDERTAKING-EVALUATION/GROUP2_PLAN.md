# Exact amendment and propagation plan — Group 2 candidate

**Amendment:** SCA-20261101-UNDERTAKING-EVALUATION  
**Standing:** Group 1 accepted; Group 2 candidate for owner review. No governing
source or accepted pointer has been changed.  
**Predecessor:** `4c2781cd25098fed9f94402afdea21ca726823c1`. Origin was refreshed
and remains at that revision for this preparation.  
**Method:** [current-project scope-change](../../../workflows/scope-change/resources/current-project.md).

## 1. Group 1 decision binding

The owner replied **“Approved.”** after the refinement that repository state change
is what justifies effort under relevant conditions, and that those conditions can
become specific goals and improvement hypotheses. This accepts the change and
impact represented by [the Group 1 document](../SCA-20261101-UNDERTAKING-EVALUATION.md)
at commit `0826802d54cc6133f9efb0634782180a723c1fc5`. The approval is bound to that
reviewed subject; this record does not claim that the owner inspected a hash or
approved the following exact Group 2 text in advance.

The acceptance selects preparation of the exact amendment. It does not implement
the capability, change its acceptance criteria by agent judgment, authorize public
publication of this proposal, or release/adopt a Library successor.

## 2. Exact material for review

- [PRD candidate](candidates/PRD.md): R18, A9, purpose/scope/input and successor-route additions.
- [Decomposition candidate](candidates/PROJECT_DECOMP.md): five packages, eight
  contributions, two new scope items and corresponding coverage/owner mappings.
- [Exact PRD/decomposition diff](amendment.patch): candidate changes against the
  named predecessor; [candidate bindings](candidate-bindings.json) give file hashes.
- [DEL-04-02 contract candidate](candidates/DEL-04-02.ScopeOfWork.md): the precise
  deferred extension after Group 3; [diff](deferred-scope.patch) and
  [bindings](deferred-scope-bindings.json) distinguish its one future source slot.

The candidates are proposal copies. Their repository-relative links are intended
for their governing destinations, not for the temporary candidate directory.
Read the diffs for the exact old/new change. No script has applied either patch.

## 3. Proposed actions and their exact boundaries

| Action | Subject | Candidate application after Group 2 acceptance | Deferred work after Group 3 acceptance |
|---|---|---|---|
| MODIFY | Library PRD | Apply only `docs/PRD.md` from amendment.patch: retain O1–O5/R01–R17/A1–A8; add R18/A9 and identified scope/input/successor-route text | Acceptance-standing annotation below; product fulfillment still unestablished |
| MODIFY | PKG-03 and PKG-04 | Apply their exact inclusion/boundary changes in the decomposition candidate; retain disciplines and IDs | Carry actual assignments through existing roles |
| ADD | SOW-0034 / SOW-0035 | Add the two exact ledger rows and corresponding coverage/mapping changes | Bind real scopes and consumer-local needs after authoring |
| ADD | DEL-03-02 | Add the exact contribution card under PKG-03; no live locality or placeholder scope | Prepare accepted locality, then `scope-of-work INIT` and native need authoring |
| MODIFY | DEL-04-02 | Add SOW-0034 and its exact R18 extension in the decomposition card | Apply deferred contract patch under current-project REVISE, after resolving the source slot and checking the accepted action/revision scope |
| QUALIFY | SOW-0033 / Q-02 | Preserve broad TBD item; exact bounded R18 selection is separated from all unselected tooling | No other bespoke tool, companion or monitoring-service authorization |
| PRESERVE | Existing IDs, accepted snapshots, published editions, unrelated contracts | No writes | Reuse their valid evidence within its original subject; no claimed fulfillment of R18/A9 |

The decomposition also carries forward the already-recorded PRD owner
clarification that there is no PEC: SOW-0030 names frozen App v3 and Runtime,
while its ID, exclusion and preserved historical snapshot retain their standing.
This is a factual consistency correction, not frozen-product reactivation.

The candidate application write boundary is only `docs/PRD.md` and
`execution/_Decomposition/PROJECT_DECOMP.md`, with bytes fixed by the candidate
bindings. The current proposal files may retain decisions and review findings.
No accepted pointer moves before Group 3. A changed predecessor hash requires
inspection and resolution of the affected conflict, not blind patch application.

**DEL-04-02 revision scope:** the exact deferred patch changes its decomposition
basis and SOW references; adds the state-change/effort purpose, OUT-005, CLM-005,
REQ-010/REQ-011, AC-008, VER-008 and one evaluation-matrix row; clarifies existing
utility ownership and the R18 exception to the broader conditional-tooling limit.
OUT-001–004 and AC-001–007 retain their identity and requirements. The book and
formation evidence are preserved. No lifecycle state is introduced or changed.

**DEL-03-02 authoring boundary:** after Group 3, prepare only
`execution/PKG-03/DEL-03-02/` with accepted ID/name, Work/ and initial native YAML.
INIT authors a substantive ScopeOfWork against the accepted new card and R18/A9:
import/binding, state/condition examination, effort measurement, inspectable local
report, reproducible case/trial-result comparison and direct usage contracts.
Its criteria must establish the card's actual supported first use and error/unknown
handling; they must not invent a reward formula, a specific unavailable API,
a performance threshold or an autonomous observer. Format validation does not
replace examination against the accepted card. Setup does not implement the tools.

## 4. Propagation owners and input/use conditions

These are the named downstream obligations selected by the amendment, not claims
that they have occurred. Use one implementation owner for the combined result;
TASK can author bounded local contributions. Shared files have one editor.

| Receiving contribution / exact owning locations | Work to carry | Condition and examination |
|---|---|---|
| DEL-04-02: `ScopeOfWork.md`, `Work/ReflectiveBasis.md`, `deliverable.yaml` | Apply exact deferred scope; connect new design/evaluation subject from existing Work; author needs after scope | Needs identify the tool's source-bound repository observations, actual result/effort evidence, coverage and limitations for the selected question; do not imply all tools must finish before useful reflection |
| New DEL-03-02: `ScopeOfWork.md`, `Work/`, `deliverable.yaml` | Current setup and INIT; design/import/metric/comparison contract and actual-use basis | Needs identify DEL-04-02's question, state conditions, outcome meanings and comparison basis; named host/export/execution interface and permitted pilot data remain to be established before dependent implementation |
| DEL-04-01: `Work/FormationAndReconciliation.md`, `deliverable.yaml` | Connect activated evaluation to the actual candidate/affected-use evidence where warranted | Reconciliation remains independently usable; evaluation is no automatic merge gate. Preserve seven-locality formation history as its own completed subject |
| DEL-03-01: `Work/ToolBasis.md`, `deliverable.yaml` | Identify reuse of selected existing tools and qualify Q-02's now-selected addition | Existing utility scope stays existing utility scope; source-inspect specific interfaces and actual callers, not a global tool census. No change to its existing acceptance criteria |
| DEL-02-01: `Work/MaintenanceBasis.md`, `deliverable.yaml` | Carry method/tool authoring under existing maintenance means | Use create-workflow for reusable method production; distinguish design/application/code responsibilities. No second maintenance procedure or new approval ceremony |
| DEL-01-01: `Work/DiscoveryBasis.md`, `deliverable.yaml`; owning entry/index when implemented | Make accepted work discoverable at its actual maturity; later connect working capability | No entry claims of implemented support before evidence; use existing catalogs and regenerate derivatives from their sources |
| DEL-05-01: `Work/ConsumerBasis.md`, `deliverable.yaml`; selected README/package guide at delivery | Carry supported interfaces/resources/notices and local/private data boundary into a selected successor candidate | No release, external distribution, consumer installation or adoption selected here; named compatibility claims require exact consuming basis |
| DEL-02-02 | Inspect actual shared-meaning interfaces only if implementation exposes an affected claim | No write allocated now; return a concrete additional change if needed, rather than editing every reference preemptively |

A no-change finding for an existing Work or need declaration requires a brief
reason, not a cosmetic edit or new receipt. The listed existing ScopeOfWork files
other than DEL-04-02 are outside the amendment write boundary. If propagation
reveals a required change to one of their commitments, bring the concrete delta
back to its decision owner. No runtime/code/workflow implementation is performed
by this scope-amendment application; later production remains a selected undertaking.

## 5. Checks before Group 3 acceptance

The applied candidate must match amendment.patch and its hashes. Compare the
entire affected poststate against Group 1 and the exact Group 2 decision. Verify:

- R18/A9 meanings retain the primacy of useful repository state change, relevant
  effort/conditions, local-goal/hypothesis refinement and the evaluation's limits.
- O1–O5 and pre-existing commitments retain their meanings; no benchmark benefit
  is inferred from a merge, positive score, synthetic fixture or prior evidence.
- Ledger contains 35 unique scope IDs: 28 IN, 5 OUT, 2 TBD; five unique package
  homes and eight distinct deliverable cards. New IDs do not replace retired IDs.
- Every IN item has its intended production allocation; card, objective and
  criterion mappings agree, with reciprocal needs preserved as actual uses rather
  than false finish-to-start barriers.
- Historical snapshots remain byte-identical. Successor counts are distinguished
  from earlier formation checks, pending language and case evidence.
- No live DEL-03-02 locality exists before accepted setup; that expected pending
  obligation is not mislabeled implementation completion or audit failure.
- Current SOW format validation on the deferred template establishes representation
  only. Check the substantive delta and revision scope separately.
- A separate reviewer who did not author/apply this amendment examines the complete
  candidate, permissions, evidence, consumer coverage and pending propagation.

The real scope-change operation uses existing current validators and source
comparison; no legacy state/control files or global progress register are created.
If a tool is unavailable, name that unperformed check and use only an adequate
source-reading fallback. Source/format passes do not establish actual product use.

## 6. Exact acceptance-conditional acts after Group 3

Keep the existing `_LATEST_ACCEPTED.md` and all earlier decision evidence unchanged
until the owner accepts the independently examined poststate and its open setup/
production obligations. Then apply only these listed conditional acts:

1. Record the actual Group 3 decision, its reviewed full commit, applicable date
   and accepted remaining obligations in this amendment's review record. Preserve
   the preceding Group 1/2 decision-bearing revisions in Git.
2. In `docs/PRD.md`, replace the three-line amendment-candidate status paragraph
   with: `**Status:** The owner accepted SCA-20261101-UNDERTAKING-EVALUATION on
   <GROUP3_ACCEPTANCE_DATE>, against candidate <GROUP3_REVIEWED_COMMIT>. The
   predecessor acceptance below remains historical.` Use the actual date and
   full reviewed SHA, never inferred acceptance. Preserve every other byte.
3. In `execution/_Decomposition/PROJECT_DECOMP.md`, replace the initial amendment
   status paragraph through `The earlier accepted payload and decisions remain
   unchanged in their snapshot.` with: `**Amendment:**
   SCA-20261101-UNDERTAKING-EVALUATION, accepted by the owner on
   <GROUP3_ACCEPTANCE_DATE> against <GROUP3_REVIEWED_COMMIT>.
   The accepted pointer binds the actual decision and
   exact reviewed source. Earlier accepted payloads and decisions are preserved.`
   Preserve every other byte.
4. Replace `execution/_Decomposition/_LATEST_ACCEPTED.md` with a short pointer
   naming SCA-20261101-UNDERTAKING-EVALUATION, the actual decision/date and exact
   Group 3 reviewed commit, a commit-qualified link to that revision's
   `execution/_Decomposition/PROJECT_DECOMP.md`, the amendment review record and
   preceding Group 3 snapshot. State that only the listed standing annotations
   differ in the applied working copy. Do not rewrite the old snapshot/pointers
   for its Group 1/2 history.
5. Hand accepted scope to current project-setup. For the exact DEL-04-02 deferred
   patch, substitute only `__ACCEPTED_DECOMPOSITION_COMMIT__` with the full Group 3
   reviewed commit, so decomposition_basis names an actual file at that revision.
   Bind its actual final hash in the existing review record. If its predecessor
   scope changed meanwhile, inspect the conflict and reopen only the affected
   decision; do not overwrite it blindly. Then apply current REVISE/VERIFY.
6. Prepare/author the new locality and propagate the bounded Work/need obligations
   in §4. Run current audit-scope-closure on the accepted actions and actual
   results; distinguish amendment acceptance, setup completion, implementation,
   product acceptance and release. The amendment can be accepted with explicitly
   pending implementation; no claim of full production closure follows.

The full reviewed commit and actual acceptance date are the only dynamic standing
slots. They cannot be filled before the actual Group 3 decision. Verify applied
standing text and source references against those bindings after application.
A further substantive edit returns to its affected decision.

## 7. Present decision requested

Accept or return this exact amendment and propagation plan as Group 2. Acceptance
would authorize creating the reviewable PRD/decomposition poststate and obtaining
its independent examination, with accepted pointers and setup still held for
Group 3. It would not authorize implementing the workbench, publishing this local
proposal or releasing a new Library version.

## Preparation checks completed

Candidate hashes match the supplied copies; both patches pass `git apply --check`
against the named predecessor. Governing source hashes remain unchanged. Direct
table checks establish 35 unique scope IDs (28 IN, 5 OUT, 2 TBD), five package
homes, eight unique deliverable cards and complete IN-item allocation. The
DEL-04-02 template validates as SOW_V1 with no issues; its accepted-source slot
remains unresolved pending the actual Group 3 decision. Plan links resolve.
No software behavior, actual benchmark run, implementation closure or independent
Group 3 review is claimed by these preparation checks.
