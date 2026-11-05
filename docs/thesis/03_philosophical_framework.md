# Chapter 3 — Philosophical Framework

---

## 3.1 Introduction

Ontology, epistemology, praxeology and axiology are related questions, not a
sequence of mandatory forms. Ontology asks what exists and how it is
represented. Bunge and Wand and Weber provide a source for assessing
representations in information systems [CITE:Bunge_ontology]
[CITE:Wand_Weber_ontology]. Epistemology concerns knowledge and its grounds;
provenance models provide one operational vocabulary [CITE:W3C_PROV2013].
Praxeology concerns action and practical reasoning, for which systems
engineering offers methods [CITE:INCOSE2023]. Axiology concerns values,
purposes and consequences, including professional obligations
[CITE:APEGA_RWO2021].

**Normative commitments** state values or obligations. **Design hypotheses**
propose ways of serving them. **Empirical findings** report what examination
establishes. A coherent design still needs evidence of its performance.

---

<a id="32-the-four-pillars"></a>

## 3.2 The Four Perspectives

### 3.2.1 Ontology — What Exists in the System

The ontological commitment is to preserve distinctions that matter to the work.
A requirement, an assumption, a physical model, a proposed operation, a result
and an acceptance are different things. Confusing them can authorize an action
that nobody intended or make a result appear better supported than it is.

Three levels must remain distinct:

| Level | Example | What examination must establish |
|---|---|---|
| Work or domain entity | A support, an intended deliverable, a required input | What it is, how it relates to the purpose, and which constraints apply |
| Representation | A model object, ScopeOfWork, dependency declaration or graph view | What it denotes, what it omits, and whether it remains faithful |
| Implementation convenience | A lock, cache, index or temporary file | What operation it supports and whether its failure affects the work |

Domain representations should express the work faithfully [CITE:Bunge_ontology]
[CITE:Wand_Weber_ontology]. Locks and caches serve implementation needs, but
their presence does not give them authority over domain meaning.

The filesystem is a shared working medium, not the ontology itself. In current
repository practice, a deliverable folder brings together commitments, design
and declared needs, and tools derive relationships from those sources. The
folder can misrepresent the work, and the graph can omit a dependency. A query
must report its basis and unresolved inputs rather than treat successful
parsing as proof of suitability. Product engines may own domain state under
their applicable contracts, so not every authoritative fact is a Markdown file.

The tree answers what belongs within a larger piece of work, and the dependency
graph answers what one contribution needs from another. A network can expose
other relevant connections, such as a common source or decision. These are
views of the work and need not be separately authored stores. It is through
attention that participants relate these views to the work. A missing edge
cannot establish independence: shared writes, resources and interfaces may
still connect apparently separate tasks.

Telling descriptive records from constitutive ones also requires care. A stress
result describes a state of affairs and can be wrong. An approval record may be
part of an institutional act if the applicable process gives it that role. Its
formal presence alone does not establish that the actor had authority,
adequately examined the subject or engaged with its consequences. A recorded
decision and a well-founded decision remain different claims.

### 3.2.2 Epistemology — What Can Be Known, and How

Fluent output does not certify itself. A numerical value and a plausible
citation can look credible and still be unsupported. Retrieval and other
techniques can improve grounding, but the presence of a source does not
establish that it supports every inference made from it [CITE:Ji2023].

The framework therefore asks that material grounds and their limits be open to
inspection. A source can support a definition without supporting a numerical
formula extracted from it. A test can establish specified behaviour without
establishing fitness for every use. Agreement among agents can show consistency
with a shared premise while leaving that premise unexamined.

#### The Ontology of the Epistemology

The framework uses six concepts to expose these distinctions. They are tools
for inquiry, not an exhaustive state space of knowledge.

| Concept | Meaning | Limit |
|---|---|---|
| Claim | An assertion about a subject | A clear assertion may still be false |
| Warrant | Relevant grounds: a source, observation, calculation, test or argument | Confidence and fluency alone do not establish adequacy |
| Status | A scoped classification useful to examination | A label is not its supporting evidence |
| Gap | Missing information or grounds whose consequence matters | Recording a gap does not resolve it |
| Conflict | Incompatible claims requiring examination of sources, scope or meaning | Some conflicts can be resolved by inquiry; others require a choice |
| Ruling | A decision by the relevant authority | Authority can settle a choice, not manufacture factual support |

FACT, ASSUMPTION, PROPOSAL and TBD are useful conventions where a consumer needs
them. They must not imply that a cited statement is universally true or that
an adopted assumption has become an observation. Nor does every routine
implementation proposal require a new owner decision. Such a proposal's authority
depends on the assignment, commitments and reserved choices.

Provenance, explicit uncertainty, conflict surfacing and examination can make
unsupported claims easier to find. A source-field validator detects a missing
field, but assessing whether the source is faithful, relevant and sufficient
requires inquiry. An instruction against invention expresses a norm, and the
behaviour it produces needs examination. The representations serving these
purposes stay open to revision, and
[Appendix E](appendix_e_development_history.md) records their development.

#### Grounds, Examination and Reliance

Three relationships support the inquiry:

| Question | Relevant relation |
|---|---|
| What supports this claim? | Claim to evidence, with scope and limits |
| What examination has occurred? | A subject and revision to a review method, examiner and findings |
| What reliance has been accepted? | An accountable person to identified content, purpose and conditions |

These relationships can change independently. A claim can acquire contrary
evidence after review. A technically supported result may have no accepted use.
A person can accept reliance under stated uncertainty while that uncertainty
remains unresolved. Authentication changes normative standing but adds no
experimental observation.

Review is inquiry into whether something is adequate for a purpose. A content
hash can identify what was examined or accepted where that binding is required.
Assessing what an examination means, how good it is and whether it is
sufficient requires its grounds and findings. The person's committed engagement
remains distinct from the review record.

### 3.2.3 Praxeology — How Work Is Done

The praxeological question is how intention becomes a usable result through
investigation, production, examination, repair and integration. Responsibility
must persist across these activities, but it need not be divided among agents
at every boundary.

The current roles describe contributions. Agent 0 holds purpose and continuity
with the owner. HELPS_HUMANS contributes design. WORKING_ITEMS owns
implementation work and integration. TASK executes a bounded assignment and
does not delegate. Except for Agent 0's continuing responsibilities, the work
determines which roles are useful. One session may carry the work without
delegation.

Responsibility, staffing and permissions are different. A role identifies a
contribution; an assignment identifies the present objective and limits; a host
supplies actual tools and enforces some permissions. The role name alone cannot
grant tools or impose a universal read-only rule. Written boundaries and
mechanical containment must be described according to what they actually enforce.

One coordinator owns a shared result. Independent work need not wait behind an
unresolved branch, but shared writes, interfaces, resource limits and review
capacity can still justify sequencing. The graph identifies declared
relationships; participants must examine whether apparent independence is real.

Owners stay with the work through ordinary repairs. A finding changes the
relevant action, not necessarily the staffing. Existing evidence remains useful
unless a change, contradiction or uncovered concern invalidates it. An uncertain
outcome requires inspection before an action is repeated. A separate approval
is needed only where authority or an applicable condition requires it.

This practice preserves explicit holds and owner-reserved commitments. It
removes the inference that accountable work must have a gate at every phase or
a separate record at every handoff. The method must support progress,
correction and recovery within authority, with costs proportionate to the work.

### 3.2.4 Axiology — What the System Values

Professional responsibility and public welfare remain central commitments. Agent
capability does not authorize an agent to certify, seal or issue professional
work for reliance. Applicable professional obligations remain with the person
who undertakes them.

The axiology also includes useful attention, maintainability, user agency and
timely delivery. These are not costs that sit outside accountability. A
register can bury a decision that matters. A repeated approval can train a
person to respond mechanically. Unnecessary checking can crowd out examination
of an uncertainty that matters more. Removing such a control can improve both
throughput and responsible engagement.

A control is justified when what it contributes to understanding, reliability
or appropriate authority is worth its attention, delay and complexity. That is
not permission to disregard a required condition, but a basis for choosing and
revising the mechanisms that meet the condition. A silent numerical error calls
for a different examination than a reversible wording change does.

Axiological inquiry distinguishes applicable obligations and constraints,
uncertain premises, negotiable preferences and the costs of control. An
obligation must be identified in its actual scope; a preference for faster work
cannot simply outweigh it. An uncertain load assumption concerns the grounds of
an evaluation, rather than a value to trade away. Preferences among viable
alternatives can concern maintainability, access, cost or user agency. Checks
and approvals themselves consume time, attention and implementation effort, and
those costs belong in the assessment of how a condition is met.

These considerations need no universal scalar value function or mandated
sequence. They can conflict, and their interpretation can change through use.
Agents can expose consequences and compare practical alternatives. The person
judges which purposes, constraints and tradeoffs they can stand behind, including
when the question or available alternatives need revision.

Values can be expressed in requirements, defaults, interfaces and prohibitions.
Those expressions can guide action without becoming the person's commitment.
The framework cannot mechanize the person's answerability by encoding a value
function, but it can make tradeoffs visible, preserve their consequences and
help the person respond to them.

---

## 3.3 The Fractal Property

The *fractal property* names the way the four questions recur at different
scales. A numerical result, a deliverable, an application and the framework itself
can each be examined for their entities, grounds, course of action and values.
The term describes this recurrence rather than a mathematical fractal.

A ScopeOfWork or Design document can answer several of these questions, while
tools derive other useful views. The choice of representation follows the
consumer's need. [Appendix E](appendix_e_development_history.md) records the
particular document arrangements explored in developing this approach.

| Scale | Example of a useful distinction |
|---|---|
| Numerical result | A passing example does not establish accuracy outside its tested range |
| Deliverable | Implementation completion does not establish owner acceptance |
| Application | An available operation does not establish authority to apply it |
| Framework | A coherent mechanism does not establish that its benefit exceeds its cost |

Repeating the questions can expose a neglected relationship, but repeating the
forms without that purpose can create administrative work. Recurrence is a
design resource, not proof of completeness or a requirement for four documents.

---

## 3.4 Mutually Corrective Perspectives

Epistemology receives particular emphasis because plausible agent output can
hide weak grounds, but adequacy still depends on all four perspectives.
Evidence matters in relation to an intended use, and distinctions matter
through what they enable people to understand and do.

The four perspectives constrain one another:

- Purpose and consequences determine which uncertainty is worth investigating.
- Ontological distinctions identify the subject of a claim or operation.
- Evidence can expose a flawed distinction, assumption or intended use.
- Practice determines whether inquiry, correction and acceptance can affect the
  actual result.
- Experience of control costs can require a different method of examination.

Epistemology receives particular emphasis in this study, while adequacy depends
on all four perspectives.

Warrant that can be inspected is valuable because of what people need to do and
stand behind. It must be connected to a subject and a workable course of
action. No single perspective establishes suitability for professional practice.

Productivity and accountable reliance can support each other. Redundant records
can impede both, and useful checks can improve both. The design question is
which arrangement makes useful work possible with adequate evidence and
appropriate authority, not how much administrative structure shows concern for
accountability.

---

<a id="35-the-pillars-as-the-ontology-of-professional-accountability"></a>

## 3.5 The Perspectives as the Ontology of Professional Accountability

The four perspectives offer a compact evaluative framework. They are not an
exhaustive ontology of everything a professional can perceive or a proof that
every accountable system must adopt Chirality's vocabulary.

| Question | A failure it can expose |
|---|---|
| What kind of thing is this? | Treating a proposed model change as an applied result |
| What supports the claim? | Relying on a passing check beyond the claim it tested |
| How does this become usable work? | Leaving completed contributions without integration |
| What matters and to whom? | Improving a local metric while reducing user control or safety |

Consider an agent that proposes a support change in SWBPIPE. The physical
model, proposal, applied operation, analysis result and acceptance must remain
distinct. The result depends on identified inputs, methods and assumptions. The
operation needs an actual route through validation and application, including
refusing stale inputs and recovering where that is supported. The person
retains applicable engineering and reliance decisions. These questions guide
the design without selecting a unique API, file format or process topology.

Systems engineering supplies methods that can serve those questions
[CITE:INCOSE2023]. Their selection is a design hypothesis to examine in use.
A failed recovery can reveal that the outcome model was incomplete. A new risk
can require a different test. A more capable agent can make an old supervision
step unnecessary. These revisions can improve coherence because the framework
is mutually corrective, rather than a one-way derivation from philosophy to code.

---

## 3.6 The Chirality of Knowledge

The project's name points to a philosophical commitment: externalizable
information and accountable knowing are not identical. Within this account,
that distinction is the permanent accountability gap. Its permanence is a
feature of the position being argued, not an empirical finding proved by the
software cases.
The metaphor is deliberately limited. It does not supply a geometry of
knowledge, divide knowledge into a fixed number of parts, or make every duality
in the architecture chiral.

### 3.6.1 Information and the Knower

Information can be recorded, transmitted, copied, cited, compared, and
organized, but knowledge is a situated achievement of a knower. Without a
knower, information is not known as knowledge. The thesis does not impose the
usual factive condition that only true belief can count as knowledge: a person
may know wrongly, incompletely, or provisionally and later revise what they
know. Professional evidence and review matter partly because knowing can be
mistaken.

This position separates two questions that are easily confused:

1. **What does a person know from the information?** This is situated in the
   knower and may differ with context, purpose, experience, and time.
2. **What reliance has an accountable actor accepted?** This is recorded by a
   scoped act bound to identified content.

Evidence and review may discipline what a person knows. Authentication answers
the second question by providing evidence of the actor's attributable
acceptance of reliance; it neither creates knowledge nor establishes reality as
it ultimately is.

### 3.6.2 The Accountability Gap and Operational `Gap`

The **accountability gap**, understood here as a philosophical distinction, is
the non-identity between information and accountable knowing. No artifact,
provenance chain, semantic model, or
approval record is identical with a person's knowing. More information may
change what a person knows, but it does not remove the need for a knower or
make the resulting knowing universal.

The operational primitive `Gap` has a narrower meaning. It records that a
warrant has not been found for a claim. An operational `Gap` can be remedied:
a source may be located or a claim revised. A ruling may authorize action
under uncertainty without supplying the missing warrant. The accountability
gap is not missing evidence and cannot be closed by another citation. Keeping
the terms separate distinguishes the philosophical account from a remediable
workflow condition. The observed usefulness of this distinction does not prove
a metaphysical conclusion about every possible knower or future machine.

### 3.6.3 Configurational Multiplicity

Identical information may occasion different knowledge in different
knowers, or in one knower under different contexts, purposes, or times. This
thesis calls that openness **configurational multiplicity**. The phrase does
not claim that every interpretation is equally good or that evidence is
irrelevant. It says that information does not fully determine the situated
knowing it may occasion.

Chirality's schemas, Knowledge Types, semantic lenses, and knowledge graphs
are therefore scaffolding rather than complete classifications. They make
important questions and relationships inspectable, support comparison, and
focus professional review. They do not define a closed state space containing
everything any knower can perceive in the information. A semantic model can
organize a work product for a stated purpose, but it does not dictate the
limits of knowledge.

Authentication stabilizes one accountable relationship within this
multiplicity. An identifiable actor binds acceptance to identified content or
SHA, scope, and purpose, and that act gives the information accountable-reliance
status within the stated relationship. Another knower may know something
different from the same information, and the authenticating actor may later
revise their own knowing through a new attributable act.

### 3.6.4 Philosophical Precedents and Limits

The framework draws on six philosophical precedents without claiming exact
correspondence or derivation.

**Niels Bohr's complementarity** [CITE:Bohr1958] provides a precedent for
resisting the demand that every adequate account collapse into one
description. The thesis borrows only that restraint and does not import a
physical theory into epistemology.

**Michael Polanyi's personal and tacit knowing** [CITE:Polanyi1958]
[CITE:Polanyi1966] and his later work with Harry Prosch [CITE:Polanyi1975]
support the priority of the knower, the personal contribution to knowing, and
the fiduciary character of professional commitment. Polanyi is a principal
resource for understanding why knowing cannot be exhausted by explicit
information. The framework does not claim to formalize Polanyi exactly.

**Brian Cantwell Smith's registration and answerability**
[CITE:Smith1996], together with his distinction between computational
reckoning and judgment [CITE:Smith2019], provides a principal resource for
the accountability gap. Registration is an achievement of a situated
subject, and judgment involves answerability not supplied by formal
calculation alone. The framework uses this distinction without treating
Smith's metaphysics as an architectural specification.

**Reckoning can be extensive.** In this framework, agents can investigate,
infer, compare, propose, assess, plan, check and act within granted authority.
Those activities can involve sophisticated reasoning and adaptation. Calling
them reckoning does not reduce them to trivial calculation or imply a need for
rigid procedures.

**Judgment is situated and committed.** It is the person's world-involving
engagement with what the work means, what matters and what they will stand
behind. It shapes purpose, framing, interpretation and action throughout the
work. Final acceptance is one expression of judgment; an approval record
neither exhausts it nor proves sufficient engagement.

**Responsibility is distinct from capability.** As professional responsibility
is currently allocated, accountable judgment and duty of care rest with the
person. Greater agent capability can change delegation, supervision and
verification without itself transferring that responsibility. This is not a
metaphysical proof of what every future machine could or could not become. It
also prescribes no read-only Agent 0, mandatory manager layer or repeated
approval of ordinary work.

For clarity, this thesis uses *assessment*, *evaluation*, *interpretation* and
*selection* for agent activities when *judgment* would confuse this distinction.
Ordinary operational uses of the word elsewhere do not confer professional
authority.

**Wilfrid Sellars' space of reasons** [CITE:Sellars1956] clarifies that
justification is not reducible to causal description. In Chirality this
supports the practical distinction between producing an output and giving
inspectable grounds for reliance. It does not place machines and humans in
mutually exclusive metaphysical realms.

**Robert Brandom's inferentialism** [CITE:Brandom1994] sheds light on the
normative statuses a person undertakes when they make and defend a claim. It
helps explain why attributed commitment matters, but the project's
operational `Claim`, `Warrant`, and `Ruling` primitives are governance
constructs rather than translations of Brandom's system.

**Nishida Kitaro's account of maintained tension**
[CITE:Nishida1945] provides a precedent for relations whose difference need
not be erased through synthesis. The framework takes from Nishida the
permission to leave a constitutive gap open, not a claim that his
contradictory self-identity and this accountability account share one
structure.

Polanyi and Smith carry the principal philosophical weight: Polanyi for the
knower's personal and fiduciary involvement, Smith for situated registration,
judgment, and answerability. The other precedents sharpen particular
features. None warrants a claim of geometric refinement or exact
correspondence.

### 3.6.5 What the Chirality Metaphor Contributes

The metaphor gives the project a compact name for an orientation that cannot
be delegated away: information may be externalized, while knowing and
accountable reliance remain situated in persons. The architecture can expose
the informational substrate and record an accountable relationship across the
gap, but it cannot replace the knower with the record.

Polanyi's account of tacit integration gives this limit a positive structure
[CITE:Polanyi1975]. In the from–to structure of knowing, a person attends
*from* subsidiary particulars *to* a focal whole, and particulars scrutinized
in themselves lose the joint meaning they subtend. The governed record is
designed to occupy the subsidiary position: the practitioner attends from
claims, grounds, models and their relationships to the engineering reality
that remains focal. On this reading, explicit representation can support
integrated understanding. A failure occurs when recording crowds out attention
to the work. This thesis names that failure mode directly (§6.9.4, §9.2.6).
Several disciplines serve the intended orientation: generated output must not
claim acceptance in its own voice (§6.8.3), and examination responds to the
consequences of an error and how detectable it is (§5.7). A record is useful
through what it lets participants examine and do, not merely because it exists.

This contribution is narrower than an architectural prescription. `Claim` and
`Warrant`, meaning and commitment, and the four accountability perspectives
remain important distinctions, but they are not independent chiral structures.
The primary chirality is only the accountability gap. The value of the metaphor
is explanatory economy, not formal precision.

### 3.6.6 Why the Gap Is Not a Synthesis Problem

The contrast with Hegelian synthesis is practical rather than a claim about
all dialectical philosophy. In professional AI governance, it would be a
mistake to treat better output as progressively eliminating the accountable
professional. Capability can reduce effort and error without changing who
holds which authority.

Chirality therefore optimizes for visibility and attributable reliance
across the gap, not for erasing it. This position does not deny that human and
machine activity can be deeply integrated; it denies only that integration,
accuracy, or fluency by itself transfers duty of care or makes authentication
automatic. The gap persists because information and accountable knowing are
not the same kind of status.

### 3.6.7 Engineering Regulation and Accountable Reliance

The APEGA practice standard *Relying on the Work of Others and Outsourcing*
[CITE:APEGA_RWO2021] is evidence for the practical importance of this
distinction, not proof of a metaphysical thesis. Its requirements for direct
supervision and control, thorough review, and authentication place obligations
on the professional who relies on work prepared by others. They do not make
the producer's capability a substitute for the professional's attributable
act.

Authentication, as used here, binds an accountable actor to identified
content, scope and purpose. It confers accountable-reliance status; it does
not turn information into knowledge, guarantee correctness or determine what
another knower must know. Evidence, examination and accountable commitment
remain distinct. Determining whether a particular process satisfies a
professional standard requires an assessment of the actual work and
applicable obligations.

Other frameworks address supporting parts of the architecture. Bunge and
Wand and Weber [CITE:Bunge_ontology] [CITE:Wand_Weber_ontology] inform the
ontological perspective; W3C PROV [CITE:W3C_PROV2013] supplies a provenance
vocabulary; Toulmin [CITE:Toulmin1958] is a precedent for the operational
distinction between claims and warrants; and the INCOSE handbook
[CITE:INCOSE2023] supplies the systems-engineering disciplines discussed in
Chapter 7. These relationships support the architecture without multiplying
the primary chirality.

---

### 3.6.8 Perspectives and Iterative Feedback

The [introduction](INTRODUCTION.md#one-undertaking-three-perspectives)
relates the normative, operative and evaluative emphases of this thesis.
Philosophically, that relationship keeps a commitment distinct from its
proposed means and from evidence of its adequacy. A finding about an
application can change what participants understand or value, as well as how
they act. The four questions make those revisions understandable while
preserving the person's answerability for the purpose and reliance at issue.

## 3.7 Summary

The four perspectives provide enduring, mutually corrective questions about work.
They direct attention to relevant distinctions, grounds, courses of action and
values. They do not uniquely derive a document kit, gate sequence, staffing
arrangement or runtime.

The distinction between reckoning and judgment preserves both sophisticated
agent capability and the person's situated commitment. Agents can carry
substantial authorized work. The person remains responsible for the
professional reliance they accept, and that engagement begins before the final
approval.

The primary chirality remains the non-identity between externalizable information
and accountable knowing. Evidence and records can support that relationship
without performing it. The recurring four questions apply to Chirality itself:
its mechanisms require examination for adequacy, cost and limits of transfer.
