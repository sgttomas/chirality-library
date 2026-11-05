# Course 05: Reasoning, Uncertainty, and Professional Judgment

[Series](../index.html) · [Northbank case](../case-study.html) · [Glossary](../glossary.html) · [References](../references.html)

Professional judgment connects evidence to a decision that a person will answer for. It requires more than a correct calculation or a confident recommendation. You must understand the decision's purpose, governing requirements, uncertain inputs, and possible consequences, and other people must be able to examine your reasoning.

This course teaches a method for preparing and defending that reasoning in a team where people work with AI agents, but technical competence is still essential. Use a competent specialist where the question goes beyond your knowledge.

## Prerequisites and outcomes

Complete Courses 01 to 04, and bring your controlled source index and requirements interpretation from those courses.

### How this course is built

The series index explains [how the series is built](../index.html#how-the-series-is-built). In this course the shifted constraint is the cost of reasoning: agents make fluent, well-structured analysis cheap, so fluency stops being evidence of warrant, and judging which analyses matter and whether their grounds hold becomes the scarce step. That judgment stays with the person who will answer for the decision; [Course 08 Lesson 6](08-project-execution.html#lesson-6-engineer-the-arrangement-that-does-the-work) treats the arrangement of people and agents as a system.

### The teaching arrangement

Use the case's [arrangement for working with agents](../case-study.html#working-with-agents-in-the-case); in this course, any description of what an agent might return in the case is a teaching assumption, not a case record.

### Outcomes

After this course, you can:

- Distinguish a claim from the evidence offered for it.
- Explain the limits of a model or observation.
- Compare options under stated uncertainty.
- Prepare a recommendation for the correct decision authority.
- Revise a conclusion when new evidence changes its grounds.
- Pose questions to agents without steering the answer toward a preferred conclusion.
- Examine an agent's reasoning for its warrant, and distinguish agreement between agents from independent examination.
- Direct, examine, and accept agent contributions, and show which judgments are your own.

Use Northbank Packets A and B; later packets are not available for this assignment.

## Lesson 1: State the claim and the intended reliance

### The classical method

Start with the question that someone must decide. A broad question, such as “Is the equipment acceptable?”, hides several decisions: technical suitability, expenditure approval, scope amendment, and permission to operate have different grounds. Identify the act that your recommendation supports.

A **claim** states that something is the case. **Evidence** can support or challenge that claim. A **warrant** explains why the evidence supports the proposed reliance.

A brochure might support a claim about a product family but may provide no warrant for selecting a particular configuration. Similarly, an approved document can establish a project requirement, but its approval does not prove that the physical installation satisfies that requirement.

Prepare a short reasoning table:

| Field | Question |
| --- | --- |
| Decision | What act does this reasoning support? |
| Claim | What must be established before that act? |
| Source | Which identified information supports the claim? |
| Warrant | Why does that information support this reliance? |
| Limit | What does the information leave unestablished? |

Read the source passage with its status and conditions, and keep the reported observation separate from your interpretation of it. Use specific wording: “Observed at one connection” means something different from “available throughout the site”.

Do not fill a missing warrant with confidence, seniority, or repetition. Ask what evidence could expose the claim as wrong.

### What it assumes

The 'What it assumes' passages in this course describe working arrangements for comparison. They are not universal facts about human practice; examine whether they hold in the task at hand.

The classical method assumes that the person who fills in the reasoning table has worked through it. Writing a clear warrant takes effort, so a missing warrant tends to show as a gap or an awkward sentence. The method also assumes that the person who frames the question will also work on the answer, so the framing reaches the work through their own attention.

### What changes with agents

An agent can complete every row of the reasoning table in minutes, in fluent and well-organized prose. The table then looks complete whether or not each warrant holds. An agent can write a confident warrant for relying on B01's brochure as readily as a sound one for relying on A04's observation, and the two can read alike. Fluency joins confidence, seniority, and repetition as things that cannot fill a missing warrant.

The question also changes hands. The question you pose becomes the agent's brief, and agents tend to support a hypothesis they are handed. Ask an agent to show that B01 can support an authorized purchase package, and it may assemble the evidence that seems to favor acceptance while giving less weight to A04's 600 V observation and the missing pump curve. How you pose the question shapes the answer.

The rest of the lesson carries over unchanged: identify the decision, distinguish claim, evidence, and warrant, and read the source passage with its status and conditions.

### The extended method

State the decision and the intended reliance in the brief, and give the agent the identified sources with their revisions and status. Ask for the reasoning table, and ask the agent to report the evidence that challenges the claim and what each source leaves unestablished.

Pose the question openly where the answer matters: “What can B01 support, and what does it leave unestablished?” rather than “Confirm that B01 is acceptable.” When you do want a hypothesis tested, say that it is a hypothesis and ask for the evidence that would refute it.

Then examine the warrants yourself. For each consequential row, read the source passage and decide whether it supports this reliance. A well-written row is no reason to skip the check.

Each way of posing the question gains something and costs something:

| How you pose the question | Gain | Cost |
| --- | --- | --- |
| Ask the agent to support a stated hypothesis | A focused return | The agent tends to confirm the hypothesis and may underweight contrary evidence |
| Ask an open question | Less steering toward your preferred answer | A broader return that takes longer to examine |
| Ask for the strongest case against your conclusion | Weak warrants are exposed early | The agent can produce weak objections as readily as strong ones, and each one uses your attention |

## Lesson 2: Examine models and observations

### The classical method

A model represents selected features of a situation, and it can support a decision when those features include what matters for that decision. The model may leave out behavior that is unimportant for one question but decisive for another, so state its purpose before you examine its results.

Check the input identities, units, conditions, and source revisions, then examine the relationships used to get the result. Ask whether the model represents the relevant operating envelope, and examine abnormal conditions where their consequences matter to the assignment.

A precise result can still be unreliable when its inputs are uncertain: extra decimal places do not improve those inputs.

Observations also have limits, so identify what was observed, where, under which conditions, and with which method.

Distinguish two forms of examination:

- **Verification** examines conformity to specified requirements.
- **Validation** examines fitness for intended use under the relevant conditions.

Checking arithmetic can support verification of a calculation, but it does not establish that the calculation represents the intended service.

Use this examination sequence:

1. State the model's intended decision.
2. Check the input basis.
3. Examine the method and its limits.
4. Compare the result with an independent estimate or observation where appropriate.
5. Identify the conditions still unexamined.

An independent comparison must address the relevant failure: two calculations that use the same mistaken input can agree and still be wrong.

### What it assumes

The classical method assumes that building and running a model takes effort, so a team runs few models and the person who builds one knows its inputs. It also assumes that an independent estimate is prepared separately, often by another person with a different method, so that agreement between the two means something.

### What changes with agents

Agents can list input identities and units, run a calculation, and prepare a comparison estimate quickly. Precise results become cheap, so the warning about extra decimal places applies to more of the work.

Independence does not follow automatically from using another participant, human or agent. Two agents that share a model, a brief, or a mistaken input can share an error. Their agreement shows that the two results are consistent with each other, not that their common basis is correct. A second agent asked to check the first, with the same brief and sources, does not establish independence merely by agreeing. Examine whether its preparation and method can expose the consequential shared assumptions.

Agents can also broaden an observation when they summarize it. A04 identifies the existing connection as 600 V, three phase, 60 Hz, and records where and how it was observed. A summary that says “the site supply is 600 V” turns an observation at one connection into a claim about the site. The lesson's distinction between “observed at one connection” and “available throughout the site” now applies to every summary an agent writes.

Verification and validation remain distinct. An agent's correct arithmetic can support verification of a calculation; it does not establish that the calculation represents the intended service.

### The extended method

Use the same examination sequence. Agents can do much of the mechanical work in Steps 2 and 4: listing input identities, units, and revisions, and preparing a comparison. Steps 1, 3, and 5 need your judgment: which decision the model serves, whether its method fits the operating envelope, and which conditions remain unexamined.

Make an independent comparison independent in the way that matters for the failure you are guarding against. Change the basis of the check: a different source for the input, a different method, a hand estimate, or a competent person's examination. Where the work will be relied on, the examiner is a competent person.

Check an agent's summary of an observation against the source wording before you rely on it.

Each kind of check catches some failures and misses others:

| Check | What it can catch | What it can miss or cost |
| --- | --- | --- |
| A second agent with the same brief and sources | Slips in arithmetic or transcription | A mistaken shared input, brief, or method |
| A check with a different input source or method | An error in one input or one method | An error shared by both, such as a misframed question |
| A competent person's examination | Whether the model represents the intended service | It uses the scarcest attention, so it limits how many results can be examined |

## Lesson 3: Treat uncertainty as part of the decision

### The classical method

An **assumption** is a proposition used while its truth remains unconfirmed. Permission to work on an assumption leaves it an assumption.

Identify uncertainty at the level where it affects the decision. “The design is uncertain” gives the next participant little help, but “Available suction conditions are unresolved” identifies an input needed for pump selection, and it also points toward investigation and an appropriate owner.

Assess each uncertain matter with four questions:

1. What could differ from the present assumption?
2. Which result depends on it?
3. What consequence could follow from being wrong?
4. What evidence or decision will resolve it?

Compare options under the same stated conditions, and include the option to investigate, defer the dependent act, or narrow its extent.

Do not assign probabilities without a defensible basis; a qualitative comparison can be more useful than invented numbers.

Sensitivity analysis examines how a result changes when an input changes; use it to find inputs that deserve more attention. For a quantitative analysis, state the tested range and its source. Distinguish a teaching assumption from a measured physical condition.

An unresolved matter need not stop all work: identify the work it limits and the independent work that can continue.

Keep conditional recommendations precise: state the required condition, the person who establishes it, and the evidence needed before reliance.

### What it assumes

The classical method assumes that each option analysis or sensitivity study costs hours of skilled work. A team could afford only a few, so deciding which ones to run was itself a judgment about which inputs mattered, made before the work began.

### What changes with agents

Agents make alternative analyses and sensitivity studies cheap to run, so a team can test many inputs and many options. The scarce step becomes judging which studies matter for the decision, and reading their results for that purpose.

More studies do not by themselves give more warrant. A long table of sensitivities can bury the one input that changes the decision, and each result still needs someone to check its range and basis. An agent will also supply a range or a probability fluently where no defensible basis exists, so the rule against invented probabilities applies with more force. An agent can present an assumed range and a measured condition in the same format, so the return must keep the distinction between them.

For Northbank, A02 states that the available suction conditions, required pressure, water properties, site constraints, and relevant operating cases are unresolved. An agent could vary assumed values for these inputs across many cases. Those results rest on assumed ranges, and they cannot select a pump or establish B01's suitability.

### The extended method

Use the four questions before you commission studies, not only after. Identify the decision in hand, the result that depends on each uncertain input, and the inputs that could change that decision. Commission studies for those inputs.

Require each tested range to state its source or to be labelled as an assumption. Read each result by asking which decision it changes. Report the studies that bear on the decision, and say which others you ran and why they do not.

Each approach gains something and costs something:

| Choice | Gain | Cost |
| --- | --- | --- |
| Run many studies | Broader coverage; a surprising sensitivity is less likely to be missed | More to examine; the decisive result can be buried |
| Run a few chosen studies | Each result can be examined with care | An input you did not choose stays unexamined |
| Let the agent choose the studies | Little of your time at the start | The judgment about what matters passes to the agent |

## Lesson 4: Make the recommendation answerable

### The classical method

A recommendation should connect the decision question, options, evidence, uncertainty, and consequences. The reader must understand why you prefer the proposed course of action.

Explain the strongest reasonable alternative; this tests whether your preferred option survives a fair comparison.

Consider people affected beyond the decision meeting, and examine effects on the public and on workers where the work can create them.

A favorable project outcome can still impose unacceptable consequences, so identify applicable obligations before you balance preferences about cost, time, or convenience.

Disclose a conflict of interest through the appropriate route, and keep your own incentive separate from the grounds offered for the decision.

Distinguish technical judgment from authority to perform the final act: an engineer can recommend a scope change without having authority to approve it. A sponsor can choose among project objectives and resource commitments, but that choice does not establish the technical suitability of a configuration.

Use the appointment and applicable obligations to identify the decision owner, and ask for clarification when those sources leave a consequential authority unresolved.

Write the recommendation in this order:

1. State the requested decision.
2. Identify the applicable basis.
3. Compare the relevant options.
4. Explain the preferred option.
5. State its conditions and affected work.
6. Name the required authority.

Match the strength of the conclusion to the evidence: “Suitable for further review” and “suitable for procurement” support different acts. State what would cause reconsideration so that the decision stays usable when the situation changes.

Keep a record only when another activity needs it. Preserve the decision's identity, grounds, conditions, and affected scope.

### What it assumes

The classical method assumes that the person who writes the recommendation weighs it while writing. Drafting the strongest alternative, the conditions, and the affected parties takes effort, and that effort is part of forming the judgment. The author of the recommendation and the person who answers for it are usually the same.

### What changes with agents

An agent can draft the recommendation in the six-step order within minutes, including a fair account of the strongest alternative. The draft can be better organized than one written under time pressure. But its author is then not the person who will answer for it.

Judgment does not move with the drafting. In this series, [judgment](../glossary.html) is a person's consideration of purpose, evidence, uncertainty, consequences, and the responsibility they will carry. An agent can contribute reasoning to it. The agent cannot carry the responsibility, hold an appointment under A01, or answer for consequences to the sponsor, operations, workers, or the public.

Cheap drafting brings three risks:

1. **Strength drift.** A draft can state a conclusion more strongly than the evidence supports, for example “suitable for procurement” where the evidence supports “suitable for further review”.
2. **Invented content.** Asked to consider affected parties, an agent may describe plausible hazards that no Northbank record supports.
3. **Carried incentives.** An agent has no interest in the outcome, but a brief can carry its author's preference. A brief that stresses keeping the delivery slot can steer the draft toward acceptance, so the rule to keep your own incentive separate from the grounds now applies to the brief as well.

The authority rules carry over unchanged. A recommendation drafted by an agent does not approve a scope change, and a sponsor's choice does not establish technical suitability.

### The extended method

Use agents to draft the recommendation and to prepare the strongest alternative, then make the recommendation your own. Read each claim against its evidence and set its strength yourself. Remove or repair any sentence that you cannot explain and defend without the draft in front of you. Check that each affected party and consequence rests on a record or is stated as unknown.

Where the reader needs it to judge reliance, state which parts agents prepared and what you examined.

The decision owner receives your judgment, not the agent's draft. Before you send the recommendation, ask whether you would stand behind each sentence if you had written it yourself.

## Lesson 5: Invite challenge and repair the reasoning

### The classical method

Independent scrutiny can reveal omitted conditions, weak sources, and unreasonable comparisons, and it works best when the reviewer knows the intended reliance.

Give the reviewer the decision question, source basis, calculation or argument, and proposed conclusion; identify the limits of the requested review.

Ask for a challenge to the grounds: a review of formatting cannot establish technical adequacy.

Consider shared assumptions and interests that could impair scrutiny: a reviewer can miss the same defect as a producer. Challenge a consequential shared basis instead of relying only on agreement.

When someone challenges your reasoning, keep the observation separate from the proposed explanation, and check the actual source or result before you choose a repair.

Treat a finding through these actions:

1. Identify the affected claim.
2. Examine the supporting evidence.
3. Determine whether the conclusion changes.
4. Repair the affected work.
5. Re-examine the changed reasoning and dependent conclusions.

A changed conclusion can be evidence of improved judgment. Explain which premise changed and why the new conclusion follows. Keep valid evidence where its basis is still applicable, and repeat examination when a change or unresolved concern warrants it.

Do not change an acceptance condition merely to get a favorable result; a changed requirement needs its own substantive reason and authority.

### What it assumes

The classical method assumes that challenge is expensive and comes from another person: a reviewer with competence, time, and a view of their own. Such a reviewer may share some of the producer's assumptions, but they bring a different preparation and will usually hold a finding they believe is right. It also assumes that repair is expensive, so the producer changes what the finding affects and little else.

### What changes with agents

Challenge becomes cheap: you can ask an agent to argue against your recommendation at any time. But agent challenge is shaped by how you ask for it. A challenger agent given your conclusion and your reasoning can be anchored by them, and an agent that shares your brief also shares the assumptions in it.

Agents also do not reliably hold a correct finding. If you push back on an agent's finding, it may withdraw the finding whether or not it was right. The rule to keep the observation separate from the proposed explanation, and to check the actual source before you choose a repair, applies to a withdrawal as much as to a finding.

Repair becomes cheap too, and that brings its own risk. An agent asked to address one finding may rewrite the whole memorandum, so that every changed sentence and dependent conclusion needs examining again. An agent asked to make an analysis pass may change the acceptance condition instead of the analysis.

### The extended method

Use agent challenge as an early, cheap pass before review by a person, not in place of that review where the consequence calls for a competent reviewer.

Arrange the challenge for the independence you need. A challenger that works from the decision question and the sources, before it sees your conclusion, gives a less anchored answer to compare with yours. A challenger that reads your draft can test the argument you actually made.

Treat a withdrawn finding as unresolved until you have checked the source. Confine each repair to the affected claim and its dependent conclusions, and keep the previous revision. Check that an agent's repair changed only what the finding affected and left the acceptance conditions as they were.

Each arrangement for challenge gains something and costs something:

| Who challenges, and from what | Gain | Cost |
| --- | --- | --- |
| An agent given your draft and reasoning | Tests the argument you actually made | Can be anchored by your conclusion; shares your brief's assumptions |
| An agent given only the decision question and sources | A less anchored answer to compare with yours | More to reconcile; may not address your actual argument |
| A competent person | Different preparation and competence; more likely to hold a finding under pushback | Uses scarce attention, so reserve it for the claims that matter most |

## Worked example: Northbank supplier decision

The earlier source and requirements work now supports a recommendation: what response to the supplier can the available evidence justify?

B01 requests acceptance within two working days. The motors it offers are rated for 480 V, but A04 reports an existing connection at 600 V.

The project engineer frames the question as: “Can B01 support an authorized purchase package?” This identifies the intended reliance.

A04 supports a discrepancy finding, but it does not establish spare capacity, protection coordination, or the suitability of any proposed supply arrangement.

B01 lacks a selected pump curve and declared operating cases, and A02 also leaves important hydraulic inputs unresolved.

The engineer compares immediate acceptance with returning the submission for correction and substantiation; the evidence does not support immediate technical acceptance.

The engineer recommends a corrected, identified submission and the missing technical checks. Procurement continues commercial inquiries within its authority.

The engineer asks procurement to clarify the delivery-slot conditions: the two-day request does not establish that losing the slot will determine final delivery.

A05 is still a proposal for 22 litres per second, and the technical review must preserve A02's approved 18 litres per second requirement.

The recommendation separates the supplier discrepancy, the incomplete hydraulic basis, the proposed scope change, and the commercial uncertainty; each requires its own response.

This conclusion does not decide which corrected pump or electrical arrangement will be suitable; those decisions need further competent work.

### The same work with agents

The project engineer briefs an agent with the same decision question: “Can B01 support an authorized purchase package?” The brief identifies A01 Rev 0, A02 Rev 1 (approved for project development), A04 Rev 1 (checked site observation), A05 Rev 0 (proposal), B01 Rev 0 (submitted for technical review, not accepted), and B02 Rev 0. It asks for a reasoning table, the evidence against acceptance as well as for it, and what each source leaves unestablished.

The engineer could have posed the question another way: “Draft our acceptance of B01 so that we keep the delivery slot.” That brief states both the conclusion and the incentive, and as a teaching assumption, an agent given it could return a fluent acceptance. The question the engineer chose identifies the reliance without assuming the answer.

The engineer examines the return against the records, not by its fluency. The checks include:

- A04 appears as a checked observation at the existing connection, not as a finding about the whole site supply, and not as proof that no 480 V arrangement can be used.
- The brochure appears as product-family information, not as evidence that the offered pump meets Northbank's duty.
- A02 Rev 1's 18 litres per second governs, and A05 remains a proposal.
- The two-day request is not treated as establishing that losing the slot will determine final delivery.

The engineer also asks an agent to prepare the alternative responses: immediate acceptance, return for correction and substantiation, and any other response the evidence might support. The engineer decides which deserve the attention of procurement and the sponsor, and why.

Suppose a second agent, given the same brief, agrees with the first. The engineer records that agreement as consistency, not as review. Under A04, the electrical engineer must determine spare capacity, protection coordination, and equipment compatibility, and no agreement between agents settles those matters.

The engineer makes the recommendation and answers for it. The clarification of the delivery-slot conditions remains a conversation between people. The classical conclusion stands: agents change who drafts the reasoning and what the engineer must examine, not what the evidence supports.

## Transfer example: Laboratory ventilation

A laboratory team has one airflow observation and a request to add another enclosure, but the observation covers the existing arrangement under one condition.

The team must establish the new operating conditions before it relies on the observation for the addition. A precise reading cannot answer an unexamined design question.

An agent can turn the one observation into a precise model of the addition in minutes. The model still rests on the single condition the observation covered.

## Practice: Examine five claims

Use A01 to A06 and B01 to B03, and examine these statements as submitted claims:

- “The 600 V survey proves that no 480 V motor arrangement can be used.”
- “The supplier brochure proves that the offered pump meets Northbank's duty.”
- “Operations' request makes 22 litres per second the current requirement.”
- “Keeping Week 12 authorizes the supplier's technical deviation.”
- “All project work must stop until every open input is resolved.”

For each claim, identify its source basis, missing warrant, possible consequence, and a defensible replacement statement. Supply no invented technical or legal facts.

Prepare this claim table yourself, without an agent. You then know what a sound return should contain.

Prepare one review question that could change your replacement statement, and exchange your table with another participant.

Then complete three exercises with agents. For each, keep the brief you gave the agent and a short note of what you checked in its return, what you found, and what you changed.

1. **Compare an agent's examination with yours.** Brief an agent to examine the same five claims, and give it the records with their revisions and status. Compare its table with yours, claim by claim. Where the tables differ, check the source and record which statement it supports. Where they agree, record what you checked.
2. **Pose the question two ways.** In one agent session, ask: “Show that B01 can be accepted within two working days.” In a separate session, ask: “What can B01 support for an authorized purchase package, and what does it leave unestablished?” Compare the returns and explain how the framing shaped them. If they do not differ materially, record what you checked to establish that.
3. **Choose the studies that matter.** Ask an agent to list the uncertain inputs in A02 and B01 and to propose sensitivity studies. Select the studies, if any, that bear on the next response to B01, and explain why the others do not. For each proposed range, state whether it has a source in the records or is an assumption.

## Knowledge check

1. What distinguishes evidence from a warrant?
2. Why can two matching calculations remain unreliable?
3. What information makes an assumption usable for coordination?
4. How do verification and validation differ?
5. Which Northbank authority can amend the approved transfer-flow scope?
6. What should change when new evidence invalidates a decision premise?
7. Why is a fluent, well-organized argument from an agent not evidence that its warrant holds?
8. Two agents given the same brief reach the same conclusion about B01. What does their agreement establish, and what would make a check independent?
9. How can the way you pose a question to an agent shape its answer? Give a better way to pose the B01 question than asking the agent to confirm acceptance.
10. Agents make sensitivity studies cheap. Which step becomes scarce, and how do you decide which studies to run?
11. An agent drafted your recommendation. Which part of the recommendation remains yours, and why can the agent not carry it?

## Assessed assignment: Defend a procurement recommendation

Using Packets A and B, prepare a decision memorandum that recommends the next response to B01's acceptance request, working with agents.

Include a fair comparison of immediate acceptance, return for substantiation, and one other defensible response, and explain which work can continue.

State the evidence needed for the next technical decision, and keep the A05 proposal separate from the approved scope.

Explain which affected parties need consideration, and identify what is still unknown about consequences rather than inventing a Northbank hazard.

Add a short account of how you used agents: the questions you posed and how you posed them, how you arranged challenge of the reasoning, and what you examined in each return, with the briefs you used.

Defend the memorandum to a peer or mentor, and repair it where the challenge identifies an unsupported claim.

Then defend the memorandum to your instructor. Expect changed premises about the evidence, such as a different survey result, and about pressure, such as a confirmed loss of the delivery slot. Your instructor rates the defense as the teaching guide describes; in text-only study it is rated on changed-premise reasoning with the medium recorded.

The instructor assesses these seven observable criteria:

1. The memorandum identifies the requested act, source revisions, and intended reliance, and the briefs give the agents the same identified sources with their status.
2. It preserves the approved scope and relevant authority boundaries.
3. It evaluates the voltage discrepancy and incomplete hydraulic basis without unsupported suitability claims.
4. It compares options, uncertainty, affected parties, consequences, and conditions for dependent work.
5. It explains the recommendation and records justified repairs after challenge.
6. The account of agent use shows how each consequential question was posed openly, or as an explicit hypothesis with a request for the evidence that would refute it, and how challenge was arranged where independence mattered. Your own examination record shows which warrants you checked against the sources, what you found, and what you changed.
7. In the defense, you explain the recommendation's main conclusions and their grounds, show what your examination of the agents' work found, identify which judgments are your own, and reason correctly through the changed premises your instructor poses.

## Portfolio continuation and references

Keep the reviewed claim table and decision memorandum as Portfolio 05, and link them to the controlled sources from earlier courses.

Use them in Course 06 to explain a difficult recommendation, and use their unresolved inputs in Course 07 to define further work.

Source adaptation: Management manual (Edition 9) §§1.2–1.3, 2.4–2.5, and 5.1–5.4. These sections cover claims, uncertainty, examination, agreement among agents, and preserved decision grounds.

Read the shared [references](../references.html) for professional competencies and systems engineering fundamentals. Further reading is optional for the supplied exercise.
