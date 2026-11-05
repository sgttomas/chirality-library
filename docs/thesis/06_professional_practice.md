# Chapter 6 — Professional Practice Integration

---

## 6.1 Introduction

Using agents in professional work raises questions about supervision,
competence, examination, documentation and reliance. The Alberta engineering
setting attaches concrete obligations to these questions.

**Scope of the regulatory analysis.** The mapping retains the source editions
and interpretation used in the thesis as of **2026-07-02**. This analysis
reassesses the architectural argument; it does not establish whether those
regulatory sources are current, amend the firm's practice management plan or
certify legal compliance. The mapping is the author's interpretation, not a
determination or endorsement by APEGA. Appendix C sets out in detail how the
review topics relate to the proposed support.

---

## 6.2 Regulatory Framework

### 6.2.1 Governing Legislation and Standards

The analysis situates the work under Alberta's *Engineering and
Geoscience Professions Act*, its *General Regulation* and three APEGA practice
standards:

- *Relying on the Work of Others and Outsourcing*, May 2021, v4.0
  [CITE:APEGA_RWO2021];
- *Authenticating Professional Work Products*, November 2024, v8.6
  [CITE:APEGA_Auth];
- *Professional Practice Management Plan*, November 2022, v1.1
  [CITE:APEGA_PPMP].

The cited editions supply the section references below. Their
applicability, and whether they are current, must be established for
actual work.

The firm's *Professional Engineering with Agentic AI in Regulated Practice*
is maintained in its quality management system [CITE:Chirality_PE].

### 6.2.2 Professional Work Products and Reliance

In the cited practice context, a professional work product (PWP) concerns
technical information on which others rely to make decisions or take action.
Its character is not created by a repository status field. Nor does an
unauthenticated work product become a PWP only when someone authenticates it.

The relevant distinctions are the work's content, purpose, intended reliance,
state of examination and applicable professional acts. A draft can contain
technical information that matters. A completed software change has its own
subject of acceptance and need not be an authenticated engineering work
product.

Git integration, an owner accepting a development slice and professional
authentication are different acts, and the subject and authority of each must
be identified separately.

### 6.2.3 Applicability to AI-Assisted Work

The dated source basis includes APEGA's *Guidance for Registrants Regarding
the Use of Artificial Intelligence Tools*, updated March 23, 2026
[CITE:APEGA_AI2026]. The interpretation reads that guidance as placing responsibility for
appropriate use and examination of AI results with the registrant, while
comparing AI results to those of other technical tools.

The thesis proposed using the supervision and review topics from the
reliance standard to structure AI-assisted practice. That proposal remains
useful as a design inquiry, but it does not settle whether an AI agent is an
“other” in the standard's legal meaning. Being able to map a mechanism to a
professional concern establishes neither direct legal applicability nor
sufficient performance of the obligation.

---

## 6.3 The Central Argument: AI Agents as "Others"

### 6.3.1 Structure of the Argument

The argument is:

1. Professional use of agent-produced work raises concrete questions about
   scope, competence, evidence, examination and responsibility.
2. The cited supervision and review topics offer a disciplined way to examine
   those questions.
3. Agent instructions, tools and records can support some of the required
   activities, subject to their actual operation and limitations.
4. The architecture cannot establish that the professional performed those
   activities adequately or that the arrangement satisfies applicable law.

This argument supports a candidate practice arrangement without depending on
a settled classification of the agent as a worker or tool.

<a id="632-why-the-framework-applies-directly-not-by-analogy"></a>
### 6.3.2 Direct Application and Analogy: An Interpretive Limit

The “others” interpretation offers a conservative candidate position. The
alternative treats AI as a technical tool whose results the professional must
be competent to assess. Neither interpretation can be settled simply by
calling the system an agent or by observing that it performs complicated
work.

Classifying AI as a tool does not imply that casual review is adequate, and
an analogy to a worker does not prove that extra records or approvals improve
protection. The appropriate examination depends on the work's consequences,
the kinds of error that are possible and the applicable professional
requirements.

Agents can interpret requirements, compare alternatives, criticize designs
and take authorized action. In the thesis's terminology, this is
sophisticated **reckoning**. **Judgment** is the person's situated, committed
and world-involving answerability for the work. The distinction does not
restrict agents to clerical production, nor does it make their legal
classification follow from their capability.

### 6.3.3 The Technology Provider Distinction

A model supplier, the host application, the agent's assignment and the
professional work are separate things to examine. A supplier's claims about
capability do not establish that a particular output is suitable for
reliance. Likewise, an instruction framework does not make the supplier's
component safe by definition.

In practice, the agent system includes the model, instructions, context,
tools, permissions and execution environment, and investigating a failure may
require examining any of these. A model update can change behaviour; a tool
can return wrong units; a permission defect can allow an unintended
operation.

The thesis allocates accountable professional commitment to the person using
the work. It makes no general legal determination here about the liabilities
of suppliers or firms, and the architecture's responsibility model cannot
settle those questions.

---

## 6.4 Direct Supervision and Control

### 6.4.1 The APEGA Standard

The mapping uses §3.1.1 of the cited reliance standard to examine
active involvement, responsibility in decision making and documentation.
These topics direct attention to what the professional does throughout the
work, but they do not demonstrate that a particular number of agents, levels
or approval stops is necessary.

Chirality contributes proposed support for that conduct. Actual supervision
cannot be inferred from a passed validator, an available dashboard or an
instruction telling an agent to ask when it is uncertain.

### 6.4.2 Active Involvement (APEGA §3.1.1.1)

Five topics organize this inquiry:

| Topic | Proposed support | What still requires examination |
|---|---|---|
| Direct, monitor and control the work | An objective and authority from the person; visible material findings and opportunities to intervene | Whether the person remains meaningfully engaged at the required points |
| Establish scope, duties, responsibilities, authority and limits | Current commitments, role responsibilities, assignment boundaries and host permissions | Whether scope and permissions fit the work and are actually enforced |
| Maintain ongoing communication | Conversation, actual contributor returns and relevant product state | Whether important changes reached the person in time |
| Identify competence gaps | Examine results and failure modes; obtain suitable expertise or a different method | Whether the available participants and tools can address the problem |
| Conduct periodic review | Review at points where errors or changes have material consequences | Whether the examination covered the relevant risks and work |

Agent 0 maintains continuity; managers and bounded contributors are used
where they serve the work. Roles do not grant permissions. Write access
follows the assignment and host limits, and TASK does not delegate in the
repository's chosen role framework. That arrangement is one current
implementation, not something deduced from the professional topics above.

### 6.4.3 Responsibility in Decision Making (APEGA §3.1.1.2)

In the cited May 2021 standard, §3.1.1.2 assigns the licensed professional
responsibility for **all technical engineering or geoscience decisions**
related to the work. It also requires consideration and documentation of
relevant issues, technical direction with attention to applicable requirements,
and availability to answer questions and review and approve decisions made by
those doing the work [CITE:APEGA_RWO2021] (p. 11). The source does not limit
these obligations to a repository's reserved decisions.

The repository separately permits standing authorization for investigation,
implementation and repair. Ordinary action need not return to the owner
merely because a procedural stage has changed, but changes to reserved
commitments, acceptance criteria, reliance purposes or risk decisions require
the appropriate person. These are repository arrangements, not a narrower
interpretation of the cited professional obligation. Where that obligation
applies, operational selections and standing authorization remain subject to
it; calling a choice ordinary implementation does not remove professional
responsibility for a technical engineering or geoscience decision.

An agent can present a choice and its consequences, resolve an implementation
question within actual authority, or apply an already-authorized decision
without pretending to exercise the person's judgment. The required professional
involvement must still be established for the actual practice context.

The decision changes the artifact it governs. Its reason and scope are
preserved where the work needs them, using the existing change record when
that record is adequate. Removing an administrative ledger does not remove an
actual professional documentation requirement.

### 6.4.4 Documentation of Due Diligence

Documentation should let a relevant reader reconstruct what was directed,
examined and relied upon. The amount and form depend on the practice context
and applicable requirements. Current source documents, identified outputs,
captured conversation and version history may supply that evidence; a special
record is justified where these are insufficient.

Git preserves committed content and its changes, but it does not
automatically capture every conversation, action, input, human decision or
external event. Nor does a versioned instruction prove that it was followed.
A claim about practice must state what its evidence actually covers.

The person can perform an authorized act through a host that captures the
result. A machine-written record of that act is not an acceptance that
originated with the machine. Conversely, a generated statement that approval
occurred cannot create an approval that never happened.

---

## 6.5 Thorough Review and Authentication

### 6.5.1 Applicability

The mapping uses §3.1.2 of the cited reliance standard to organize the
examination that comes before professional reliance. Review in this sense is
more than format checking: it examines whether the work and its grounds
support the intended purpose.

No mandatory lifecycle for claims follows. Cited, reviewed and authenticated
identify different relationships; they are not increasing truth values. The
appropriate review must consider material claims that labels or dependency
metadata may have missed.

### 6.5.2 Reliability, Accuracy, and Validity (APEGA §3.1.2.1)

Review addresses the following subjects in relation to the work's intended
use. Who carries out the review, and when, depends on the required
competence, consequences and grounds.

| Review subject from the historical mapping | Application to agent-assisted work |
|---|---|
| Scope, including contributed work | Examine the intended result, contribution boundaries and omissions |
| Design and operational conditions, risks and mitigations | Examine loads, operating cases, environmental conditions and failure consequences |
| Assumptions, limitations and caveats | Test material premises; make unresolved limits visible at the point of use |
| Intended purpose and local conditions | Assess whether the analysis and inputs apply to the actual situation |
| Health, safety and environment | Examine relevant hazards and whether proposed controls address them |
| Integrity and consistency across work products | Check units, interfaces, revisions and consequential dependencies |
| Calculations, analyses, evaluations and interpretations | Inspect actual inputs, transformations, outputs and their claimed meaning |
| Materials and methods for construction, inspection, maintenance or operation | Examine domain-specific suitability beyond document completeness |
| Tools and technologies | Assess algorithms, software behaviour, model limitations and the validity of the checks themselves |
| Interdisciplinary work | Obtain appropriate examination where no one participant covers the relevant expertise |

An agent can discover discrepancies, prepare a focused comparison and carry
repairs through the authorized work. Independent scrutiny is particularly
valuable where contributors may share an undetected premise. It can involve
another competent person, another agent or a different technical method as
appropriate to the claim; an agent reviewer does not substitute for a
required professional reviewer.

### 6.5.3 Adherence to Regulatory Requirements (APEGA §3.1.2.2)

The historical mapping included legislation, practice standards and
project-specific approvals or permits. Current work must identify its
applicable requirements and authoritative source editions. An instruction
to obey them is behavioural guidance, not a compliance check. A checker can
establish a bounded property only if its rule correctly represents the
applicable requirement and its coverage is adequate.

### 6.5.4 Adherence to Quality Control and Assurance (APEGA §3.1.2.3)

The mapping also included the practice management plan and the clarity,
consistency and completeness of work. No document kit can ensure these
properties by its presence. A short current basis can be clearer than a
complete set of contradictory templates.

A changed repository procedure does not automatically amend an external
practice obligation. The responsible person must address any applicable
practice-system requirement in its actual home. This chapter neither adds
such an obligation nor declares it discharged.

### 6.5.5 Authentication

The cited authentication discussion concerns a professional act relating a
person to identified work and responsibility for its use. This framework
reserves that act to the appropriate person; a PR merge, a successful analysis
or a generated receipt does not perform it.

Content addressing can identify the bytes associated with the act, but
reliable attribution, scope and purpose remain separately necessary. A
fingerprint alone proves neither who approved the work nor whether the
examination was adequate. These limits apply whether the person types the
record or an authorized host interaction captures it.

A later change leaves the historical act attached to its original subject.
Whether a prior acceptance remains applicable to changed work requires
assessing the affected content and reliance conditions. A universal rule
that any repository edit voids all earlier acceptance is not warranted.

Authentication does not create knowledge, establish truth or exhaust
judgment. The person's committed engagement also shapes purpose, framing,
interpretation and action before this particular act occurs.

---

## 6.6 Professional Obligations

This section states the framework's adopted commitments. Their legal
application remains subject to the historical-source and interpretive limits
in §6.1; software does not guarantee their fulfilment.

### 6.6.1 Public Welfare as First Constraint

The framework puts public safety and the protection of people, property and
the environment ahead of schedule or convenience. Material hazards require
appropriate examination and decision. A severity label can help direct
attention, but it cannot guarantee that hazards were found or effectively
controlled.

Delay, excessive paperwork and the diversion of expert attention also have
consequences, and their costs belong in the design assessment. Removing a
low-value check can improve practice when it frees attention for an important
failure mode; removing a numerical oracle can worsen it when wrong results
would otherwise remain plausible.

### 6.6.2 Responsible Charge Remains Human

Chirality places accountable professional commitment with the person. Agents
may perform extensive reckoning and act within the authority granted to them,
but they do not thereby acquire the person's responsibility or authority to
authenticate. This is the framework's allocation for the systems examined here,
not a metaphysical proof about every possible future machine.

Judgment is exercised throughout the work. Reducing it to the final
signature would make an unattended approval ritual appear sufficient. A
person's decision needs engagement with what the work means and what they
will stand behind; a record can serve as evidence of an act but cannot
guarantee that engagement.

### 6.6.3 Competence Includes Tool Competence

The professional needs a defensible basis for assessing the tools and work
used for the intended purpose. This includes knowing what a check establishes,
where a model or calculation may fail and when further expertise is needed,
but it does not mean that every computation must be repeated manually.

Useful evidence can include analytical solutions, validated benchmarks,
independent methods, input inspection and observed behaviour. Competence
cannot be inferred from having a checklist, tool catalog or instruction file.
The architecture can make evidence accessible, but the person must be able to
understand its relevance and limits.

### 6.6.4 Evidence Over Plausibility

Material claims need suitable grounds. An extracted number must not quietly
become an inferred estimate; an accepted assumption must not be presented as
an observation. A source citation needs to support the actual claim, and a
passing test needs a stated scope.

This is a commitment implemented through instructions, useful data structures
and focused checks. It is not proof that invention or omission cannot occur.

### 6.6.5 Hierarchy of Authority

Authority, evidential strength and task responsibility are different orders.
An applicable law or contract constrains action; it is not a scientific
observation. Strong evidence can show that a chosen model is wrong without
authorizing an agent to change a reserved commitment. Professional judgment
interprets applicability and acts within constraints; it is not a source of
evidence ranked last, below every published document.

Current instructions and assignments identify where decisions belong. Roles
help organize contributions, but their names or numerical types do not create
professional authority.

---

## 6.7 Quality Control and Assurance

### 6.7.1 Architectural Controls

A proposed control should identify the failure it addresses, the evidence it
produces and its cost. Schema validation can reject malformed inputs, path
containment can refuse an escaping write, and a numerical oracle can detect a
particular class of calculation error. Each has a bounded claim.

A candidate arrangement of controls needs to be evaluated in actual practice.
Adequate support for professional reliance concerns the work, examination and
engagement it enables. Architectural coherence supplies a rationale to
examine, not a finding that obligations have been discharged.

Current assurance selects checks according to consequence, detectability,
overlap and cost. Reuse applicable evidence and repeat a check when a relevant
change or unresolved concern warrants it. A requirement to demonstrate a
specific property still applies even when the general process becomes lighter.

### 6.7.2 Instruction Governance as Release Engineering

Instruction changes can alter behaviour and deserve to be versioned and
reviewable. The depth of examination depends on the affected behaviour. A
permission change warrants different scrutiny from a clarified entry point.

Instructions must also agree with their enforcement. Removing a read-only
sentence while a resolver still discards authorized write targets does not
change the effective policy. Conversely, broader tool availability must not
silently become broader authorization. The relevant consumer and enforcement
path belong in the same change.

### 6.7.3 The Deterministic and Probabilistic Boundary

Use reliable tools for operations they perform well: resolving identities,
comparing revisions, applying a structured operation or evaluating a defined
formula. Agents can then investigate, interpret, propose and coordinate
around those results.

Deterministic does not mean correct. A repeatable calculation can use a
wrong formula, precision rule, unit conversion or design basis. The strength
of its evidence depends on validated behaviour and applicability. Agents may
also make useful observations about a deterministic tool's failure.

The division of labour is open to revision. A reusable tool is worthwhile
where it improves reliability or effort enough to justify building and
maintaining it. That an algorithmic solution is possible does not require a
new tool for every one-off action.

### 6.7.4 Technology Provider Due Diligence

The provider and model affect the system's behaviour. Useful evaluation asks
whether the available capability, failure modes and execution conditions fit
the work, including privacy, permission and recovery needs. Supplier claims
and general benchmarks cannot settle those questions for a particular
application.

As models improve, a control added for an earlier limitation can become
unnecessary overhead. Reassess the control against observed behaviour and
remaining risk. Stronger output does not by itself transfer accountable
judgment or remove the need to inspect results that matter.

### 6.7.5 Evidence and Auditability

A usable evidence arrangement makes relevant inputs, results, changes and
acts retrievable by an appropriate reader, and it states what was captured
and what was not. Source history, product logs and existing review records
may be sufficient; routine copies of the same information can obscure
inspection rather than improve it.

Three questions guide assessment: can a reviewer identify what supports the
claim, can a participant recover the state needed to continue, and can an
appropriate reader reconstruct an act that matters? Answering them requires
evidence from actual use, and an exhaustive-looking register is not a
substitute for it.

---

## 6.8 The Human-AI Contract

The contract here is the framework's allocation of responsibility, not a new
grant of product permissions or a claim that every instruction is
mechanically enforceable.

### 6.8.1 Human Responsibilities

The person establishes or accepts the work's purpose, material commitments,
limits and reliance conditions. They provide or arrange the competence needed
for decisions that matter, determine reserved risk acceptance and perform any
required professional act. They can authorize
agents to continue ordinary work without repeated approval.

Agent 0 supports continuity with that person but does not replace their
judgment. Meaningful engagement includes framing and revising the work, not
merely approving an output prepared elsewhere.

### 6.8.2 AI Agent Permitted Actions

Within the actual assignment and host permissions, agents can investigate,
extract, infer, plan, evaluate, criticize, propose, implement, check, repair and
integrate. They can select ordinary implementation details and apply decisions
already authorized. These activities may involve substantial initiative.

Agents can make operational selections within their assignment and adopted
policy. Their capability supports extensive initiative, but authority for
reserved commitments and accountable professional reliance remains with the
person.

### 6.8.3 AI Agent Prohibitions

The framework prohibits agents from inventing a human act of acceptance,
claiming professional authority they do not possess, concealing a material
conflict, presenting fabricated evidence as observation or exceeding the
assignment and host permissions.

Enforcement must be described accurately. A host can refuse an out-of-scope
operation; an instruction requests behaviour; review can detect some
violations. None alone guarantees all the others. The prohibition and the
mechanism that attempts to enforce it are separate claims.

---

## 6.9 Limitations of the Regulatory Mapping

### 6.9.1 The Mapping Is an Interpretation, Not a Regulatory Ruling

The mapping is an argument by the author using the cited historical sources.
It has not been established here as endorsed by APEGA or accepted by a court,
tribunal or professional reviewer. Its architectural examples are candidates
for support, not certificates of compliance.

### 6.9.2 Jurisdiction Specificity

The sources concern Alberta engineering practice. Similar practical questions
may arise elsewhere, but their legal meaning and required conduct cannot be
transferred merely by replacing the regulator's name. This chapter
establishes no claim of compliance across jurisdictions.

### 6.9.3 The "Relying on the Work of Others" and "Using a Tool" Distinction

Both classifications deserve consideration. The proposed “others” argument
does not follow necessarily from the text's emphasis on professional conduct.
Nor does a more demanding internal practice policy prove compliance with a
different legal interpretation. The support that discoverable evidence and
controlled operations offer can remain useful while that classification is
unresolved.

<a id="694-the-architecture-is-necessary-but-not-sufficient"></a>
### 6.9.4 The Architecture Is One Candidate, Not a Necessary or Sufficient Condition

The thesis has not shown that Chirality is required for competent practice.
Other arrangements can preserve evidence and responsibility. Nor has it shown
that installing Chirality is sufficient: inadequate examination, wrong
assumptions, misunderstood tools and mechanical approval can still occur.

The appropriate test is how an actual arrangement performs, including its
failures and the attention, delay and complexity it imposes.

### 6.9.5 Evolving Regulatory Context

The section references and interpretive mapping retain their 2026-07-02
source basis. This revision has not rechecked whether they are current. A current
professional application requires a separate examination of the applicable
sources and practice requirements. Repository development experience can
inform that examination but cannot determine its legal outcome.

---

## 6.10 Summary

The professional-practice analysis offers concrete questions for designing
agent-assisted work: what was directed, what supports the result, what was
examined, which limits remain and who stands behind reliance.

Chirality proposes ways to make those questions answerable. Continuing
ownership, discoverable current artifacts, useful checks and attributable acts
can support practice without a fixed hierarchy or a routine chain of records.
Their effectiveness remains an empirical question. Instructions, content
hashes and passed tests each establish only bounded facts.

The enduring commitment is to distinguish extensive agent reckoning from the
person's situated judgment throughout the work. Greater capability can change
which supervision and verification arrangements are appropriate without
itself transferring that accountable engagement. The revised mapping
preserves this commitment while withdrawing the claim that one architecture
guarantees, or is necessary for, professional compliance.
