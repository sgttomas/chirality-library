---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-01
package_id: PKG-05
decomposition_basis: execution/_Decomposition/checkpoint_snapshots/GROUP3-20261101T011431Z/PROJECT_DECOMP.md@fd847ac9ac68250b2f35d2e9c0087c16e86b510a
project_scope_refs: [SOW-0019, SOW-0020, SOW-0022, SOW-0023, SOW-0025, SOW-0026]
package_objective_refs: [OBJ-002, OBJ-003, OBJ-005]
---

# Obtain, qualify and inspect identified library material

## Purpose and Objective Traceability

DEL-05-01 supplies a usable route for independent consumers to obtain and use
identified library material, qualify a named interface, inspect consequential
changes and choose adoption. Maintainers use that route to prepare publication
and preserve recovery through ordinary repository facilities. The accepted
identity is DEL-05-01_consumer-use-guide in PKG-05, Independent reuse and
publication. There is no separate DEL-05-02 or edition/history product.

| Accepted scope | Intended contribution | Objective trace |
|---|---|---|
| SOW-0019 | Obtain, consult, invoke or copy identified material with its resources, notices and adaptation distinctions | OBJ-005 / PRD O5 |
| SOW-0020 | Qualify an affected named interface at a maintained consumer basis; preserve a supported route before incompatible change | OBJ-003, OBJ-005 / PRD O3, O5 |
| SOW-0022 | Prepare an identifiable candidate from verified sources, preserving publication and adoption authority | OBJ-003, OBJ-005 / PRD O3, O5 |
| SOW-0023 | Explain meaningful changes and exercise inspection against a prior basis | OBJ-003, OBJ-005 / PRD O3, O5 |
| SOW-0025 | Keep ordinary use independent of private inputs and hidden environments; screen public artifacts | OBJ-002, OBJ-005 / PRD O2, O5 |
| SOW-0026 | Preserve documented historical routes and original consumer pins without restarting old work | OBJ-003, OBJ-005 / PRD O3, O5 |

The governing source is `docs/PRD.md`, especially R13, R15–R17 and A6–A7,
read with the accepted decomposition's vocabulary, ledger, DEL-05-01 card,
§8.1 formation obligations, §9 interfaces and §10 qualifications. The snapshot
path is in frontmatter; its `DECISION.md` supplies acceptance and setup authority,
and `ACCEPTED_MANIFEST.csv` binds the accepted payload and handoff. The payload's
pre-decision submission status is historical. Its relative links resolve from
`execution/_Decomposition/PROJECT_DECOMP.md`.

The current undertaking develops and examines obtaining/use and change-inspection
guidance under Agent 0, with a bounded Type 2 contribution exercising the selected
App reader. Initial setup alone did not establish these results. The linked Work
binds actual source/consumer revisions, the copied package and comparison evidence.
The owner approved this content for integration in PR #1784; no product acceptance,
publication, automatic adoption or permanent contributor appointment is inferred.

The initial source assessment and continuation conditions are in [Work/ConsumerBasis.md](Work/ConsumerBasis.md). Consumer-local needs are now declared in `deliverable.yaml`; their presence establishes no satisfaction claim.

## Deliverable Definition — Ontology

The selected basis is the identified source actually governing use. A newer
publication examined is distinct from that basis and from an adopted revision.
A publication candidate is concrete identified material prepared from verified
maintained sources in its intended delivery form; it is not a version proposal
or a Git log alone. Proposed, integrated, published, examined and adopted describe
different acts and must not be conflated. A local adaptation is distinguishable
from its shared or packaged source. A named compatibility claim is limited to
its consumer, interface, use case, maintained contract/fixtures and revisions.

Expected outputs are functional results; existing holdings and applicable checked
evidence may supply part or all of them. No file is required merely to populate
the locality. Source publications remain at their maintained homes. Review
accounts stay in actual PR descriptions and ordinary release notes; technical
reasoning and locally retained evidence belong in `execution/PKG-05/DEL-05-01/Work/`.
`deliverable.yaml` carries initial needs and useful source/check pointers.

- **OUT-001** — Obtaining, copying, version-selection and use guidance in `README.md` and the selected existing tool/workflow/reference guides, linking applicable resources, notices, dependencies, limitations and source/adaptation distinctions. Trace: SOW-0019, SOW-0025; OBJ-002, OBJ-005.
- **OUT-002** — Bounded named-consumer qualification evidence, retained in this locality's `Work/` or referenced actual review/maintained fixture homes, identifying supported use and any unresolved incompatibility. Public evidence uses cleared material; private source evidence remains with its custodian. Trace: SOW-0020, SOW-0025; OBJ-003, OBJ-005.
- **OUT-003** — A real identifiable publication candidate prepared from verified maintained sources through ordinary review/publication facilities, with a proposed version/edition label, source revision, delivery-form checks, notices, dependencies, limitations and recovery route. It retains the selected holding's source/output home; no parallel history product is established. Trace: SOW-0022, SOW-0025; OBJ-003, OBJ-005.
- **OUT-004** — Usable update-inspection guidance in the existing consumer guides, a meaningful change account in actual PR descriptions/publication notes, and evidence of applying the guidance to OUT-003 against an identified prior basis. Trace: SOW-0023, SOW-0025; OBJ-003, OBJ-005.
- **OUT-005** — Preserved commit/edition recovery routes in `projects/FROZEN.md`, `docs/alignment-manual/README.md` and the selected holding's existing references, with byte verification for historical content actually relied upon. Original consumer pins, including the App's historical SWBPIPE source identity, retain their meaning. Trace: SOW-0026; OBJ-003, OBJ-005.

- **CLM-001** — Current inspected holdings provide reusable pieces, not an exercised end-to-end consumer route: `README.md` distinguishes the shared library and independent products; `LICENSE.md` supplies the repository MIT notice subject to component-specific licenses; `tools/workflow_runtime/README.md` explains selected resource resolution and host enforcement limits; `docs/alignment-manual/README.md` distinguishes discovery links, resolved editions, source revisions and rendering checks. Their existence establishes neither named compatibility nor A7 satisfaction.
- **CLM-002** — Accepted decomposition §9 allocates navigation meaning to `DEL-01-01`, general maintenance/review/recovery and custody procedures to `DEL-02-01`, scoped shared-reference/publication meaning clarification to `DEL-02-02`, actual tool behavior and separately justified adapter implementation to `DEL-03-01`, reconciliation practice and initial setup/needs formation coverage to `DEL-04-01`, and reflective examination/decomposition formation coverage to `DEL-04-02`. Each local implementation owner keeps its own commitments, Work and needs (§8.1); Agent 0 integrates related changes with one shared-file editor. This deliverable supplies obtaining/version/use conditions, not those neighboring contributions.
- **CLM-003** — `AGENTS.md` and PRD §§2.3, 3.5 and 5 reserve Root product acceptance, protected baseline/commitment changes, risk acceptance, releases and additional archival disposition to the owner. Consumers retain their own authority, operational data, adaptations, adoption and product release. Root Agent 0 coordinates affected independent projects through their current Agent 0 under actual authorization; a message transfers no authority. Frozen App v3 and Runtime require explicit owner reactivation. Private evidence remains with its owning consumer/custodian; public clearance is required before use in public fixtures. PRD R16 requires actual operator configuration and authority for scheduling, external delivery or unattended operation.
- **CLM-004** — `projects/FROZEN.md` documents the completed pre-library transition at `archive/pre-library-execution-2026-10-31`, commit `f80f1510fb50799764720303b86c36da64b75d19`, and the frozen-product recovery routes. The accepted decomposition carries the original consumer-pin preservation obligation; pin-specific content is still to be selected for actual reliance. This is a documented recovery basis, not a claim that this author inspected archived bytes or that external historical dependencies remain available. Accepted SOW-0026 requires preservation, not another removal or restored backlog.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — OUT-001 shall provide independent documented routes appropriate to consulting, invoking or copying selected material through ordinary files, Git, archives or documented interfaces. Reading alone shall require no Git installation; selected executable tools shall disclose their real dependencies. Identify source revision/edition, required resources, applicable notices and licenses, limitations and local adaptations; ordinary use shall not depend on undisclosed sibling checkouts, dated run directories, private inputs or credentials. Basis: CLM-001; PRD R13, R17.
- **REQ-002** — OUT-002 shall test the actual selected interface/use claim against a named consumer's maintained contract or fixtures at an exact revision, with the candidate basis explicit. Generic demonstrations and Root component tests do not establish named compatibility. Before an incompatible interface change, establish a supported path or coordinated adapter under the relevant authority; an unresolved path remains a hold on that change, not on unrelated guide work. Basis: accepted SOW-0020; PRD A6.
- **REQ-003** — OUT-003 shall identify the real candidate, proposed version/edition label, verified source revision and actual delivery form, retain resources/notices/dependencies/known limitations, and make commit-pinned history and editions recoverable. Named owner publications are the downstream default; following main is an explicit development selection. Integration does not confer publication standing. Basis: PRD R15, A7; CLM-003.
- **REQ-004** — OUT-004 shall explain affected holdings, old/new bases, reason, difference in meaning or use and known migration consequences in actual review/publication material. Exercise the documented procedure with existing release/diff facilities against the actual prior basis; distinguish selected basis, publications examined and adoption. Failed or partial inspection shall expose its limits and shall not report no change. Interests remain consumer-local. Basis: PRD R16, A7.
- **REQ-005** — OUT-005 shall retain historical identities and routes, verifying selected historical bytes before reliance and reusing applicable preservation evidence with its limits. Recovery shall not reinstate old commitments, lifecycle state or frozen development. Basis: CLM-004; PRD R12, R15; SOW-0026.
- **REQ-006** — Public guidance, candidate material and retained public evidence shall pass maintained credential and private-term checks at the actual candidate basis, declaring unavailable screening coverage. Public fixtures/summaries require clearance; private operational data stays local. Basis: SOW-0025; PRD R17; CLM-003.
- **REQ-007** — This deliverable shall perform no act owned by another deliverable: navigation design owned by `DEL-01-01`, general maintenance/review/custody procedure production owned by `DEL-02-01`, shared-meaning reconciliation owned by `DEL-02-02`, tool or adapter implementation owned by `DEL-03-01`, reconciliation/setup/needs practice owned by `DEL-04-01`, or reflective/decomposition practice owned by `DEL-04-02`, as allocated in CLM-002. Coordinated application and affected-use review do not transfer ownership. This deliverable retains its own local contract, Work and needs responsibility through future production and repairs.
- **REQ-008** — Excluded acts and their decision owners are those in CLM-003: Root release, product acceptance, risk acceptance and protected baseline/commitment changes belong to the Root owner; consumer operational changes, adoption and product release belong to that consumer's owners; external project coordination belongs to the relevant Agent 0 under actual authority; frozen reactivation and additional archival removal need the Root owner's explicit decision; private-source disclosure requires its custodian's clearance; scheduling/external delivery/unattended operation requires the responsible operator's actual configuration and authority. This contract authoring executes none of them. No blanket prohibition assigns these acts to a sibling deliverable or makes them acceptance prerequisites.

The criteria below express the accepted production commitments. Passing schema or
setup checks cannot satisfy them. Completion requires the applicable concrete
evidence, with unresolved criteria reported as unverified; risk or changed
commitment decisions cannot be substituted by an author weakening a criterion.

- **AC-001** — An obtaining/use case follows OUT-001 at an identified source basis, obtains and uses selected material through its documented path, retains notices/resources and demonstrates the stated source/adaptation distinctions and real dependencies without hidden private or sibling inputs. Reading guidance supports ordinary file use without Git. Verified by VER-001; contributes to PRD A6, not its named-compatibility portion.
- **AC-002** — OUT-002 binds the named consumer, maintained contract/fixtures, exact consumer and candidate revisions and selected use; observed results substantiate the claimed compatibility, with supported path or coordinated adapter evidenced before any incompatible change and unresolved results explicitly held. Verified by VER-002; required for the named-compatibility portion of PRD A6.
- **AC-003** — OUT-003 is a concrete identifiable candidate from verified maintained sources with proposed version/edition label, actual delivery-form checks, source identity, notices, dependencies, limitations and recoverable revision/edition route. Proposed, integrated and published standing is accurate, and owner release is not claimed. Verified by VER-003; contributes to PRD A7.
- **AC-004** — OUT-004's actual review/publication account identifies affected holdings, old/new bases, reason, changed meaning/use and migration consequences sufficiently to inform the selected consumer use. Verified by VER-004; contributes to PRD A7.
- **AC-005** — The documented inspection procedure is exercised for OUT-003 against the identified prior basis using existing release/diff facilities; evidence distinguishes the basis in use from material examined and adoption, and any failed/partial result exposes its limits rather than claiming no change. Verified by VER-005; required for PRD A7.
- **AC-006** — OUT-005 preserves the selected recovery and original-pin routes; historical bytes actually relied upon are checked at their identified source, with unavailable dependencies or unexamined history explicit and no reinstated old work. Verified by VER-006.
- **AC-007** — Public artifacts for OUT-001 through OUT-005 satisfy REQ-006 at the examined basis, with cleared evidence and accurate screening limits. Verified by VER-007.
- **AC-008** — Outputs preserve the act/owner distinctions in REQ-007 and REQ-008, contain no parallel edition/history or notice-register obligation, and make no consumer adoption, owner release or product-completion claim from setup alone. Verified by VER-008.

Input and use conditions for later consumer-local need authoring follow. These
are not supplier appointments or whole-deliverable sequencing gates; preliminary
document review and final qualification have distinct conditions.

| Input / source | Use and trigger | Suitability condition / unresolved binding |
|---|---|---|
| Selected holdings, guides, licenses and resource manifests at their maintained homes | Draft obtaining/use guidance; final exercise when making a use claim | Identify actual exported surface and revision; inspect required resources and applicable component notices. CLM-001 is a starting set, not a mandatory bundle of every Root holding. |
| Named consumer contract/fixtures | Claim compatibility or select an incompatible interface change | Exact maintained source and revision plus authorized access/cleared evidence required; the selected App reader case is bound in TBD-001 and Work. No consumer adoption follows from it. |
| Verified candidate sources and ordinary review/publication facilities | Prepare candidate and make A7 claims | Bind actual version label, source revision, delivery form, verification and prior comparison basis; the selected source/edition case is bound in TBD-002 and Work. A merged revision alone is insufficient. |
| Existing maintenance and reconciliation methods | Authorized preparation, review, source reconciliation and integration | Read applicable current methods and evidence from DEL-02-01 and DEL-04-01; do not await whole-deliverable completion or infer new supplier obligations. |
| Navigation and shared-meaning material | Guide wording or applicability change affects shared README/reference/publication sources | Coordinate navigation use with DEL-01-01 and scoped meaning with DEL-02-02 through Agent 0 and one shared-file editor; preserve adopted contracts and earlier editions. |
| Actual tool/interface behavior and supported compatibility route | Guidance invokes a tool or proposed change is incompatible | Use documented commands, dependencies and checks from selected sources; any demonstrated implementation gap returns to DEL-03-01 under Q-02, not an assumed adapter. |
| Historical pins/editions and documented recovery routes | Rely on particular historical content | Identify original pin/path and verify selected bytes before reliance; retain unrelated history without a global audit. CLM-004 supplies the documented starting route. |

- **TBD-001** — Q-04 is bound for the selected capture/declaration/content-identity claim: App `366e7a6656d807142e7bdeda0ccf99c37d7227b1` reader and maintained contracts, with Root `1357d706ea77497903976bf159f3880bea4d1360` coordinated-knowledge-work package, as identified and exercised in Work/ConsumerBasis.md. Other consumer operations or source revisions remain outside that evidence. Independent examination found no blockers; the owner approved the presented content for integration. The test does not imply adoption or full product acceptance.
- **TBD-002** — Q-05 retains the examined F-02/manual candidate and comparison in Work/ConsumerBasis.md. The broader owner-approved source-delivery subject is the complete library source candidate at `7c334bf5cb529a814e0f96f68bc8d9500b15cdd5`, compared with `547e7d7f833f9bec351f7a034bddd7c1a37db15a`; owning Work records archive identity, notices and selected operation evidence. The owner approved the content and exact archive candidate in PR #1787; no library version tag, publication or release is selected.
- **TBD-003** — Q-01 retains additional archival disposition of `plans/`, `_DomainEngines/` and other unselected removals with the owner. Q-02 retains bespoke tooling as contingent on a demonstrated gap and actual authorization; no adapter, companion or service is commissioned. These qualifications do not block unaffected guidance or source-preservation work.

## Production and Verification Method — Praxeology

For a later authorized production undertaking, select a bounded material/use case
and classify its existing guidance as usable, needing connection/repair or absent.
Reuse applicable content and evidence with their exact source limits. Connect the
obtaining/version/inspection route in existing guides, coordinate shared-file
changes, and retain necessary reasoning and candidate-bound evidence in Work or
actual review material. If changing a reusable workflow, use `create-workflow` at
that time. Do not invent a new workflow merely to express these outputs.

Resolve claim-specific inputs before asserting compatibility or A7 fulfillment.
Prepare the selected candidate, meaningful account and inspection application
through ordinary Git/PR/release facilities under the existing maintenance basis.
Inspect the actual delivered form and preserve publication source homes. Reconcile
changed meaning and evidence with this contract, Work and needs in the same PR;
leave unchanged declarations alone. Human acceptance/release remain separate.

- **VER-001** — Exercise the selected documented acquisition/use path and inspect the obtained material, required resources/notices, source identity and adaptations. Check file-reading instructions without requiring Git and exercise invoked tools with their declared dependencies. Record the actual environment assumptions, basis, steps, result and limits; a walkthrough proves only the claims it exercises.
- **VER-002** — At the explicit consumer and candidate revisions, run the selected maintained contract/fixture checks or direct interface exercise appropriate to the claim. Inspect results and any supported path/adapter evidence, report failures and unsupported cases, and keep private details at their authorized home. A generic example cannot replace these inputs; do not execute this method while Q-04 is unresolved.
- **VER-003** — Inspect the real candidate against its verified source revision and proposed label, applicable checks and actual delivery form. Check resources/notices, dependencies, limitations, recovery identity and declared standing. For a rendered publication, check source/output correspondence and its actual intended reading/delivery form; do not assume a particular format or renderer before selection.
- **VER-004** — Compare the actual PR/publication account with the identified old/new holdings and their uses. Review reason, meaning/use differences and migration consequences against the changes, distinguishing known consequences from unknowns; a commit list alone is insufficient.
- **VER-005** — Follow the documented release/diff inspection procedure for the identified candidate and prior basis. Inspect the resulting comparison and local interpretation, including selected versus examined basis and any failed/partial result. Retain only evidence needed to show the procedure was exercised and its limits; perform no adoption, scheduled job or external delivery as a side effect.
- **VER-006** — Inspect documented recovery references and verify the selected historical bytes/pin actually used against its identified Git/edition basis. Reuse relevant prior preservation evidence where still applicable, identify unavailable dependencies and unexamined history, and check that guidance does not reactivate or migrate an archived backlog.
- **VER-007** — Screen actual public changed artifacts and retained evidence through maintained credential and private-term APIs with available authorized terms. Record candidate identity, coverage and findings without exposing secrets/terms; state if hosted terms were unavailable. Review fixture clearance and ordinary-use instructions for hidden private prerequisites.
- **VER-008** — Review each excluded act against CLM-002 and CLM-003 and its actual owner; inspect output language for authority transfers, implied adoption/release, parallel registers/products or setup-as-fulfillment claims. Check affected interfaces with Agent 0 under authorized coordination, not by assuming a library change binds consumers.

## Governing Values and Decisions — Axiology

- **AX-001** — Preserve human accountability and consumer choice. A test implements verification; it creates no acceptance condition or authority. Root grants, execution records and host/runtime policy do not transfer by copying library material. PRD §§1, 2.3 and R13–R16 govern.
- **AX-002** — Preserve source identity, truthful maturity and inspectable warrant. Distinguish evidence of content, executable behavior and named compatibility; retain failed/partial results and unresolved conditions without claiming no change. Historical sources remain evidence, not current instructions or a backlog.
- **AX-003** — Use ordinary facilities and the minimum maintained artifacts required for use and review. Removing the separate DEL-05-02 does not waive R15/R16/A7. Avoid a second notice/history register, compulsory companion, global census or automated management obligation. Existing applicable holdings may fully supply an output.
- **AX-004** — The Group 3 owner decision states: “I accept this decomposition as the basis for project setup.” Its setup authority permits this source-grounded INIT contract, with no lifecycle source or status touch. Product implementation, expanded commitments, human acceptance and release are separate acts. Q-01/Q-02 and claim-specific Q-04/Q-05 remain qualified, and Q-03 assignments remain future decisions. Substantive ambiguity is returned as CONFLICT with its consequence; it is not resolved by weakening a criterion.

## Output and Evaluation Matrix

Each row's verification set applies to its single acceptance criterion. Repeated
output references express different evidence claims, not additional artifacts.

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | OBJ-002, OBJ-005 | REQ-001, CLM-001 | AC-001 | VER-001 | Identified obtaining/use case, resources/notices, real dependency and adaptation observations |
| OUT-002 | OBJ-003, OBJ-005 | REQ-002 | AC-002 | VER-002 | Named maintained consumer contract/fixture basis and actual compatibility/path results; Q-04 unresolved at setup |
| OUT-003 | OBJ-003, OBJ-005 | REQ-003 | AC-003 | VER-003 | Real candidate identity, source and actual delivery-form evidence; Q-05 unresolved at setup |
| OUT-004 | OBJ-003, OBJ-005 | REQ-004 | AC-004 | VER-004 | Actual old/new account, meaning/use and migration appraisal |
| OUT-004 | OBJ-003, OBJ-005 | REQ-004 | AC-005 | VER-005 | Exercised inspection against prior basis, selected/examined distinction and honest partial/failure limits |
| OUT-005 | OBJ-003, OBJ-005 | REQ-005, CLM-004 | AC-006 | VER-006 | Selected historical-byte verification and preserved recovery/pin routes with reliance limits |
| OUT-001 | OBJ-002, OBJ-003, OBJ-005 | REQ-006, CLM-003 | AC-007 | VER-007 | Public-boundary screening and cleared evidence with actual coverage limits |
| OUT-002 | OBJ-002, OBJ-003, OBJ-005 | REQ-006, CLM-003 | AC-007 | VER-007 | Public-boundary screening and cleared evidence with actual coverage limits |
| OUT-003 | OBJ-002, OBJ-003, OBJ-005 | REQ-006, CLM-003 | AC-007 | VER-007 | Public-boundary screening and cleared evidence with actual coverage limits |
| OUT-004 | OBJ-002, OBJ-003, OBJ-005 | REQ-006, CLM-003 | AC-007 | VER-007 | Public-boundary screening and cleared evidence with actual coverage limits |
| OUT-005 | OBJ-002, OBJ-003, OBJ-005 | REQ-006, CLM-003 | AC-007 | VER-007 | Public-boundary screening and cleared evidence with actual coverage limits |
| OUT-001 | OBJ-002, OBJ-003, OBJ-005 | REQ-007, REQ-008, CLM-002, CLM-003 | AC-008 | VER-008 | One-for-one excluded-act/owner review and truthful authority/standing statements |
| OUT-002 | OBJ-002, OBJ-003, OBJ-005 | REQ-007, REQ-008, CLM-002, CLM-003 | AC-008 | VER-008 | One-for-one excluded-act/owner review and truthful authority/standing statements |
| OUT-003 | OBJ-002, OBJ-003, OBJ-005 | REQ-007, REQ-008, CLM-002, CLM-003 | AC-008 | VER-008 | One-for-one excluded-act/owner review and truthful authority/standing statements |
| OUT-004 | OBJ-002, OBJ-003, OBJ-005 | REQ-007, REQ-008, CLM-002, CLM-003 | AC-008 | VER-008 | One-for-one excluded-act/owner review and truthful authority/standing statements |
| OUT-005 | OBJ-002, OBJ-003, OBJ-005 | REQ-007, REQ-008, CLM-002, CLM-003 | AC-008 | VER-008 | One-for-one excluded-act/owner review and truthful authority/standing statements |
