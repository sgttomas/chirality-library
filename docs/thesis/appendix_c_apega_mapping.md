# Appendix C — APEGA Regulatory Mapping

This appendix retains the professional-practice topics used by the thesis's
**2026-07-02 historical mapping**, while revising its account of architectural
support. Its principal source is *Relying on the Work of Others and
Outsourcing*, May 2021, v4.0 [CITE:APEGA_RWO2021], alongside the authentication
and practice-management sources identified in Chapter 6 [CITE:APEGA_Auth]
[CITE:APEGA_PPMP]. Section numbers below refer to that source basis; this
revision has not established that they are still current.

The tables express the author's interpretation and design hypotheses. They
do not certify compliance, establish that AI agents are legally “others,” or
claim regulatory endorsement. The prior firm's practice standard was a source
for the original mapping [CITE:Chirality_PE]; this appendix does not amend that
standard or the firm's practice management plan.

The columns distinguish a professional concern, possible support and evidence
still needed. A mechanism's existence is not proof that the professional
performed the relevant activity. Chapter 6 explains the interpretive limits.

---

[Appendix E](appendix_e_development_history.md#e6-corrections-of-earlier-claims)
records how this candidate practice arrangement evolved. The mapping below
keeps the dated professional topics distinct from the proposed support and the
evidence needed to assess it.

## C.1 Direct Supervision and Control (APEGA §3.1.1)

The historical mapping used supervision and control to examine the
professional's engagement throughout the work. It formerly equated that
engagement with gates and an Agent 0/1/2 hierarchy, but the revised mapping
treats those as implementation choices. Responsibility for purpose, integration and
reserved decisions can remain clear under different staffing arrangements.

### C.1.1 Active Involvement (APEGA §3.1.1.1)

| Topic in the historical mapping | Candidate support | Evidence or limitation to examine |
|---|---|---|
| Directing, monitoring and controlling work throughout its lifespan | The person's objective and authority; an owner continuing through implementation and repairs; visible material findings | Whether direction and intervention actually occurred when needed |
| Establishing scope, duties, responsibilities, authority and limits | Current commitments, contribution roles, the assignment and host permissions | Whether the assignment is adequate and permissions are enforced; the role name alone grants none |
| Maintaining ongoing communication | Conversation, contributor returns, product state and pertinent change records | Whether relevant changes reached the person in time, including after interruptions |
| Identifying competence gaps | Focused examination of results, failure modes and limits; access to suitable expertise | Whether the participant or tool can perform and assess the required work |
| Periodic review | Examination timed to consequential changes and error opportunities | What was examined, by whom or what method, with which findings |

### C.1.2 Responsibility in Decision Making (APEGA §3.1.1.2)

The cited May 2021 source places responsibility for all technical engineering
or geoscience decisions with the licensed professional. It requires the
professional to remain available for questions and for review and approval of
others' decisions; the source does not say only reserved decisions
[CITE:APEGA_RWO2021] (p. 11).

| Topic in the historical mapping | Candidate support | Evidence or limitation to examine |
|---|---|---|
| Considering relevant issues | Current design basis, assumptions, alternatives and material conflicts | Whether important issues were omitted or misunderstood |
| Providing technical direction | An explicit assignment or decision with an identified subject and scope | Whether the decision-maker had the relevant authority and the instruction was applied |
| Availability for questions and review and approval of decisions made by those doing the work | Agent 0 maintains continuity and presents actual choices and consequences | Whether the professional can perform the involvement the source requires; repository reservations do not define its full scope |
| Preserving relevant decisions | Edit the source the decision governs; preserve its reason in an adequate existing change record or required professional record | Whether the act and its scope can be reconstructed; a generated statement cannot create an unperformed decision |

Repository operating rules allow ordinary authorized work to continue without
a new approval at every procedural step, but that arrangement does not narrow
the professional responsibility stated above or displace applicable review,
approval and documentation requirements. A technical engineering or geoscience
decision remains within that responsibility even when the repository treats it
as an operational selection. This historical mapping establishes no new
repository gate.

### C.1.3 Documentation of Due Diligence (APEGA §3.1.1 — Record Keeping Requirement)

| Topic in the historical mapping | Candidate support | Evidence or limitation to examine |
|---|---|---|
| Process described in the practice management plan | The firm's actual maintained practice-system documents | This thesis does not establish their current content or amend them |
| Scope and constraints of agent work | Current instructions, assignment and effective host permissions | Versioned prose is not proof of execution or enforcement |
| Relevant development and review history | Source versions, changes, check results and attributable decisions | Git captures committed material, not every action or conversation |
| Integrity and recoverability of evidence | Stable identification and appropriate retention of relied-upon artifacts | A hash identifies content; it does not establish truth, identity or adequate review by itself |

A record earns its place through a concrete consumer, acceptance requirement
or recovery need. Existing artifacts may serve that purpose. Routine copies,
receipts and handoff chains are not necessary merely because they can be
produced.

---

## C.2 Thorough Review (APEGA §3.1.2)

The historical mapping used thorough review to examine reliability, validity,
technical accuracy and appropriate reliance. The former five-gate REVIEW
protocol was one method for organising this work. Its lifecycle labels and
required registers are not prerequisites in the current repository model.

### C.2.1 Reliability, Accuracy, and Validity (APEGA §3.1.2.1)

| Review topic from the historical mapping | Candidate support | Evidence or limitation to examine |
|---|---|---|
| Scope, including contributed work | ScopeOfWork and actual outputs | Missing work, changed boundaries and intended use |
| Design and operating conditions, risks and mitigations | Current design basis, scenarios and domain analyses | Whether the chosen cases represent the situation and material hazards |
| Assumptions, limitations and caveats | Assumptions beside calculations, source pointers and explicit unknowns | Whether important premises were recognized and tested |
| Suitability for purpose and local conditions | Comparison of input conditions and method limits with the intended use | A source can be correct but inapplicable |
| Health, safety and environmental implications | Hazard analysis and appropriate examination of proposed controls | Labels and checklists do not prove that all hazards were found |
| Integrity and consistency across work products | Dependency queries, revision comparisons and focused interface checks | Undeclared relationships, unit errors and shared mistaken premises |
| Calculations, analyses, evaluations and interpretations | Identified inputs, algorithms, results and relevant checks | What each result establishes, including uncertainty and method limits |
| Materials and construction, inspection, maintenance or operating methods | Domain-specific requirements and design explanation | Practical suitability beyond document completeness |
| Tools and technologies | Benchmarks, oracles, source examination and observed behaviour | Deterministic tools can be wrong; model self-assessment is not independent evidence |
| Interdisciplinary work | Related consumers and appropriately qualified contributors or reviewers | Whether the available expertise covers the actual interfaces |

The criteria for examination are consequence, detectability, the applicable
requirements and the evidence available. A passing schema check does not
justify reliance on numerical meaning. An agent reviewer does not replace a
professional review where one is required. Repeating equivalent checks does
not automatically add independent evidence.

### C.2.2 Adherence to Regulatory Requirements (APEGA §3.1.2.2)

The prior mapping included legislation, practice standards, permits and
contractual approvals. Current work must establish which sources and editions
apply. A prompt instructing an agent to obey a requirement does not verify
compliance with that requirement.

A bounded tool check can help where a requirement has been correctly encoded.
Its output must disclose its scope; the mapping cannot infer that the rest of
the work complies. Conflicts about applicability or reserved commitments need
the appropriate person's decision.

### C.2.3 Adherence to Quality Control and Assurance (APEGA §3.1.2.3)

The prior mapping included adherence to the practice management plan and the
clarity, readability, consistency and completeness of the work. A prescribed
folder or document kit cannot ensure those properties; they must be examined
in the actual work and its use.

Versioned instruction changes, accurate permission enforcement and targeted
checks can support the practice system, but what they cost in attention and
maintenance also matters. Removing unnecessary administration is compatible
with keeping an applicable quality requirement; the requirement and one
historical implementation of it are distinct.

---

## C.3 Authentication (APEGA §3.1 and *Authenticating Professional Work Products*)

The cited authentication context concerns the person's attributable
professional act. The framework reserves that act to the appropriate person
and does not equate it with a repository merge or software lifecycle state.

| Relation to preserve | Candidate support | What it cannot establish alone |
|---|---|---|
| The act concerns identified work | An identified artifact, revision or fingerprint, scope and purpose | Whether that work is correct or fit for purpose |
| The act is attributable and authorized | An appropriate identity and permission mechanism, with faithful capture of the person's action | Whether the person engaged adequately with the work |
| Relevant examination preceded reliance | Actual review grounds, findings and decisions | Completeness merely from a signed checklist or generated summary |
| Later changes remain distinguishable | Source history and comparison of affected content | Whether a prior acceptance applies to changed work without assessing the impact |
| Professional authentication is distinct from development integration | Separate subjects and authority for each act | Professional acceptance from CI success or a merged PR |

A record may report an act, or an authorized interaction may perform an act
under the applicable process. The host can capture that interaction without
becoming the decision-maker. A record written by software does not make the
act agent-originated, and a record's existence does not prove that the act
occurred.

Judgment in this thesis is the person's situated, committed engagement with
the work throughout framing, interpretation and action. Authentication
is one possible expression of that engagement. It does not create knowledge,
make the content true or guarantee the quality of the engagement.

---

## C.4 Definition Mapping

These are working distinctions for this thesis, not substitute statutory
definitions or a report of present registration status.

| Term | Distinction preserved in this analysis |
|---|---|
| Licensed professional | The person whose professional authority and competence must be established for the work |
| Permit holder and Responsible Member | Roles in the cited practice context whose actual obligations and standing require the applicable practice-system sources |
| Professional work product | Technical work considered in relation to its intended reliance; not created by an ISSUED field or by authentication |
| Authentication | The attributable professional act concerning identified work and responsibility; not a machine assessment of truth |
| Validation | A term whose professional meaning must be distinguished from software schema or input validation |
| Direct supervision and control | Actual professional conduct throughout the work; not the existence of a prescribed agent hierarchy |
| Thorough review | Substantive examination of the work and its grounds; not a count of completed gates |
| Due diligence | Appropriate engagement with consequences, grounds and limitations; not the volume of records |
| AI agent | A model acting through instructions, context, tools and permissions within an assignment |
| Agent instruction architecture | One set of means for directing and bounding agent work; not proof of professional conduct or compliance |

---

## C.5 Invariant Cross-Reference

Earlier editions mapped K-* rules to the professional topics above. The table
below retains their historical identity while distinguishing enduring design
concerns from retired mechanisms. It is not a live invariant catalog. Current
repository authority comes from its instructions and applicable product
contracts; the thesis creates no new duties.

| Historical identifiers | Concern that remains useful | Implementation limit or change |
|---|---|---|
| K-AUTH-1, K-AUTH-2, K-BIND-1 | Distinguish authorized human reliance decisions from agent outputs and identify their subjects | Host capture can evidence the person's act; hashes do not establish adequate review or truth |
| K-SEAL-1, K-GHOST-1, K-GATE-1 | Clear assignment, relevant context and reserved decisions | A sealed brief and repeated human launch approval are not universal requirements |
| K-DEP-1, K-DEP-2, K-ID-1 | Discoverable needs, identifiable suppliers and stable references | Current consumer declarations replace old dependency mirrors; missing data remains an explicit unknown |
| K-STATUS-1, K-STALE-1, K-STALE-2 | Understand relevant change and its possible effects | Stored lifecycle state and automatic human triage of every dependency change were retired |
| K-VAL-1 | Know which content and inputs an earlier examination concerned | A later change requires an applicability assessment, not an assertion that every prior act disappeared |
| K-MERGE-1 | Authorized integration and appropriate verification | Git merge is distinct from professional authentication; verification follows consequence |
| K-PROV-1, K-INVENT-1, K-CONFLICT-1, K-CLAIM-1 | Trace material grounds, disclose unknowns and conflicts, avoid overclaiming | No format or instruction guarantees that all gaps or false claims are detected |
| K-WRITE-1, K-WRITE-2 | Constrain actual operations to authorized scope | Scope follows assignment and host enforcement, not a role name alone |
| K-SNAP-1 | Recover relied-upon evidence and identify its version | Routine append-only task snapshots are not required when existing history is adequate |
| K-HIER-1 | Organize work into comprehensible parts | A package/deliverable tree is one representation, not a universal ontology |
| K-AGENTS-1 | Make current instructions and their consumers consistent | Retired catalogs or registries do not acquire authority through historical citation |
| K-DOMAIN-1, K-DOMAIN-2 | Preserve domain semantics and control protected operations | A domain engine is authoritative for its defined operation, not a guarantee of truth about the world |
| K-DOMAIN-3, K-DOMAIN-4 | Distinguish proposal, application, validation and reliance | Authorization follows the actual product contract and assignment; this mapping neither adds nor removes an operation-level approval |

The revision preserves the normative concern for accountable work, proposes
supporting mechanisms and identifies their evidentiary limits. Whether those
mechanisms improve professional examination at an acceptable cost remains a
question for actual practice and evaluation.
