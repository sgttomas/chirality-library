# Course 10: Assurance, Delivery, and Handover

[Series](../index.html) · [Northbank case](../case-study.html) · [Glossary](../glossary.html) · [References](../references.html)

## Purpose and preparation

Assurance provides justified confidence in an identified result. It connects the requirements, the configuration produced, the examinations, the evidence, and the proposed reliance.

Delivery provides the result to its recipient. Handover transfers continuing responsibilities with the information needed to carry them.

This course teaches you how to establish that confidence and carry out that transfer in a team where people work with AI agents. Complete Courses 01 to 09. Bring your project basis, execution package, and technical interface account. Read Northbank Packets A, B, and C.

### How this course is built

The series index explains [how the series is built](../index.html#how-the-series-is-built). In this course the shifted constraint is independence: in a human team an independent review needs a second competent person, so it is expensive and sampled and can bring separately prepared reasoning, though a different person alone does not establish independence, while an agent's review is cheap and repeatable but can share the producer's model, brief, or reference. Commissioning and physical tests still set the pace, and because agents can overstate what an observation supports and can assemble a complete-looking package quickly, the scope of evidence and the identity of the delivered configuration matter more; Lessons 1 to 5 follow the series' four steps, and Lesson 6 treats the design of the assurance arrangement.

### The teaching arrangement

Use the case's [arrangement for working with agents](../case-study.html#working-with-agents-in-the-case). The records do not say who drafted C04's cover sheet or how any record was produced, so this course labels any supposition that an agent prepared or examined a record as a teaching assumption.

### Outcomes

After this course, you can:

- Plan examination when defining the work.
- Select suitable checks, reviews, inspections, and tests.
- Limit conclusions to the evidence obtained.
- Establish commissioning and handover prerequisites.
- Transfer identified responsibilities and preserve unfinished obligations.
- Design where examination needs independence and how to obtain it, in proportion to consequence and detectability.
- Examine agent-prepared evidence accounts and handover packages for overstated scope and unidentified configuration.
- Direct, examine, and accept agent contributions, and show which judgments are your own.

## Lesson 1: Plan quality with the work

### The classical method

A final inspection cannot recover every opportunity lost during production: some features become hidden, and some decisions need review before ordering or construction. So plan their examination while the work is still accessible.

Start from each applicable requirement and identify its output, examination method, evidence, examiner, and decision. State the point when examination becomes necessary.

Use a coverage table:

| Requirement or needed condition | Identified result | Examination | Expected evidence |
| --- | --- | --- | --- |
| Required flow under established conditions | Selected and installed configuration | Competent technical assessment and defined performance examination | Conditions, measurements, configuration, and interpretation |
| Required changeover behavior | Equipment and controls together | Review and defined functional test | Starting state, event, response, and observed result |
| Operating readiness | Instructions and trained receiving team | Document examination and readiness demonstration | Applicable records and receiving decision |

This table proposes an examination route; it does not claim that Northbank has completed the route or approved the methods.

Set the level of independence according to the requirement and the consequences. A competent producer's check and an independent review answer related but different questions. Assign the reviewer a clear purpose and enough context.

Allow time for correction and re-examination. A plan that schedules review immediately before an irreversible action may leave no workable response to findings.

Agree the required records with the people who will use them. Retain enough evidence to understand and challenge the conclusion, but avoid collecting forms that nobody uses.

### What it assumes

The 'What it assumes' passages in this course describe working arrangements for comparison. They are not universal facts about human practice; examine whether they hold in the task at hand.

The classical method assumes that each examination is a person's work, so examinations cost time and the project chooses where to spend them. An independent review needs a second competent person, so the project reserves it for the most consequential claims and samples elsewhere. It also assumes that each record costs effort to produce, which by itself restrains the number of forms.

### What changes with agents

**Information checks become cheap and repeatable.** An agent can check a calculation, a drawing against the basis, or a coverage table against the requirements at every revision instead of at a sampled few. It can check the coverage table itself for requirements with no examination and examinations with no requirement.

**Cheap checks are not automatically independent.** A check by an agent that shares the producer's model, brief, or reference can share the producer's error. A01 says that a reviewer examines assigned work independently where the project requires it; an agent check does not satisfy that requirement merely because a different agent ran it. Lesson 6 treats this in full.

**Records become cheap, so forms multiply.** The effort that restrained unused records disappears. Each unused record still uses the attention of the person who must read past it.

**Some costs do not change.** A competent person's examination of work that will be relied on still takes that person's time. Physical inspections and tests still need access, equipment, and the installation itself. Agents can repair a document quickly after a finding, but re-examining the repair still needs the examiner, and repeating a physical test still needs the test.

### The extended method

Plan examination with the work, as before, and add two columns to the coverage table: who or what performs each examination, and what makes it independent where independence is needed.

| Requirement or needed condition | Examination | Performed by | Source of independence |
| --- | --- | --- | --- |
| Required flow under established conditions | Competent technical assessment and defined performance examination | Mechanical engineer, and the test team for the physical examination | The physical test observes the installation directly, though its conditions and expected behavior come from the basis; the assessment is prepared from the established operating cases |
| Required changeover behavior | Review and defined functional test | Controls and mechanical engineers, with operations | Required behavior defined with operations before the test is prepared |
| Operating readiness | Document examination and readiness demonstration | Operations lead, with agent checks of instruction applicability | The receiving team demonstrates its own readiness |

This table, like the classical one, is a teaching proposal, not a record of Northbank's arrangements.

Use agent checks freely where they answer the question and an error would show itself in time. Plan competent people's examination as a constrained resource, as Course 08 Lesson 2 taught, and allow time for re-examination and repeated physical tests after repair. Agree records with the people who will use them, and decline records that nobody needs, however cheap they are to produce.

## Lesson 2: Choose examinations for the claim

### The classical method

Verification examines conformity to specified requirements; validation examines fitness for intended use under the relevant conditions. The same test can contribute to both when its basis supports both questions.

A calculation checks predicted behavior under its model and inputs. A review examines reasoning, assumptions, coverage, and conclusions. An inspection examines observable features. A test exercises behavior under defined conditions.

Choose a method that can answer the actual question: reading a drawing cannot establish an installed dimension, and observing one operating condition cannot establish all operating cases.

Component checks matter, but connected behavior also needs examination: a standby pump, controller, and power system can each pass separate checks while their changeover interaction remains untested.

Define a test before you treat its result as a pass:

1. Identify the governing requirement.
2. Identify the configuration and starting state.
3. State the test conditions.
4. State the justified expected behavior.
5. Identify measurement and observation methods.
6. Define the decision and finding route.

A real test plan also needs the relevant safety, access, operational, and authorization arrangements. In this course you prepare examination plans; the course does not supply instructions to energize or operate equipment.

Protect the acceptance criteria during repair. If the result fails, investigate the cause. A defective test can require correction, but that correction needs a substantive basis and the proper authority.

Changing an expected value only to get a pass removes the meaning of the check.

### What it assumes

The classical method chooses methods partly by their cost. A calculation check or a review of reasoning takes a competent person hours, an inspection takes access, and a test takes equipment, time, and authorization. It also assumes that the people who define a test know which parts of the expected behavior are established and which are not.

### What changes with agents

**Check the actual cost and capability of each examination.** An agent can assist calculation checks and reviews of test definitions. In the supplied Northbank exercise it has records, not access to the installation or test equipment. It cannot obtain an installed dimension or exercise changeover merely by reasoning about those records. A system connected to instruments would need its own capability, authorization and evidence. Physical access, competent participation and test conditions still constrain assurance.

**An agent's review answers a narrower question than it may appear to.** An agent reviewing reasoning can establish that the reasoning is consistent with the inputs it was given. It cannot establish that those inputs describe the installation.

**Agents can fill an expected value that the basis leaves open.** Asked to draft a changeover test, an agent can write a complete-looking expected response. A02 requires the changeover function to be confirmed with operations, and A05's request for automatic changeover is a proposal that does not amend A02. So the justified expected behavior is not yet established, and any expected response the agent writes is invented.

**An agent directed to make a check pass can change the check.** An agent tasked with getting a failing check to pass may alter the expected value, the test conditions, or the scope, unless its brief forbids it. The classical rule against changing an expected value only to get a pass now needs to be written into the brief.

### The extended method

Assign each claim the method that can answer it. Use agents for calculation checks and reviews of reasoning, and repeat them whenever their inputs change. Plan physical inspections and tests for installed and behavioral claims, and schedule assurance around them.

Before an agent drafts a test definition, establish the required behavior it tests, or have the agent mark the expected behavior as unresolved. In every brief that touches a check, state: do not change expected values, conditions, or acceptance criteria; report a failure as a failure, with its observations. Any correction to a defective test still needs a substantive basis and the proper authority.

## Lesson 3: Preserve the scope of evidence

### The classical method

Evidence belongs to an identified result, conditions, method, and observation, so retain those relationships. An unqualified statement such as “tested successfully” leaves out too much to support reliance.

Keep observation separate from interpretation and decision. A witness can confirm that a measurement occurred, but whether the measurement is adequate for acceptance is still a further question.

Read evidence in both directions: for each obligation, find the relevant result and examination, and for each acceptance claim, find the actual evidence that supports it.

Record limits openly. An incomplete configuration list limits traceability, missing test conditions limit interpretation, and scenarios that were not performed leave their behavior unestablished.

A later observation does not prove that earlier design gaps were resolved, but it can establish observed behavior within its own scope. Resolve other gaps through evidence or a decision within the decision owner's authority. A disposition can limit reliance; it cannot establish unexamined behavior.

After a repair, assess the evidence it affects. A setting change can invalidate a functional test, but a corrected spelling in an unrelated instruction may leave that test valid. Re-examine according to the actual relationship.

Use a finding that supports action:

- Observation and source.
- Affected requirement or claim.
- Consequence for the proposed reliance.
- Responsible owner.
- Required closure evidence or authorized disposition.

Keep unresolved findings visible until the basis for closing them exists. A meeting record's “closed” label does not create missing evidence.

### What it assumes

The classical method assumes that writing an evidence account costs a person's effort, and that the person who writes it usually took part in the examination and knows its conditions. Overstatement comes from human pressures, such as schedule and optimism, and experienced reviewers know where to look for it. Reading evidence in both directions across a whole project is laborious, so it is often done only for the claims that matter most.

### What changes with agents

**Agents can overstate what an observation supports.** An agent writes a fluent summary at almost no cost, and a summary generalizes. "A flow of 18 litres per second during one normal transfer condition" can become "flow performance verified" or "the installation meets the flow requirement". C04's draft cover sheet shows the result: it says that the complete installation passed acceptance, while the report records one flow observation without the full hydraulic conditions and four scenarios not exercised. The records do not say who drafted that cover sheet. An agent summarizing C04 can make the same overstatement, faster and in more polished form, and an agent asked C05's question, whether the project can report handover as complete, may answer the question it was asked rather than the one the evidence allows.

**An agent summary may not carry the examiner's knowledge of the conditions.** The classical writer was often present at the test. An agent was not, so it knows only what the record states. Where C04 does not state the full hydraulic conditions, an agent can only report that they are missing, or it can fill them in.

**Reading in both directions becomes cheap.** An agent can trace every acceptance claim to the evidence that supports it, and every obligation to its examination, across the whole project. This can be one of the most useful contributions agents make to assurance. The trace is itself a claim to examine, because an agent can link a claim to evidence that concerns the same subject without supporting it.

**Agents can find the evidence a repair affects.** After a repair, an agent can list the tests and checks whose basis included the changed item. A person decides which of them must be repeated.

### The extended method

In every brief that asks for an evidence account, require each statement to carry its observation, configuration, conditions, method, and limits, and forbid unqualified words such as "passed", "verified", or "tested successfully" without them. Keep C04's original observation separately from any corrected conclusion.

Use agents to trace claims to evidence and obligations to examinations. Examine each link that supports a consequential claim: open the evidence and confirm that it supports the claim within its scope. Use the same finding format as before, whoever raises the finding. An agent can raise an observation; the responsible owner closes the finding on evidence or an authorized disposition.

## Lesson 4: Establish commissioning readiness

### The classical method

Commissioning establishes readiness and behavior under defined conditions before the relevant operating handover. Its scope depends on the installation and governing arrangements.

Define prerequisites for each commissioning activity. These can include complete installation, configuration records, prerequisite checks, approved procedures, suitable instruments, competent participants, and operating coordination.

Allocate boundaries where work continues nearby. Identify what is ready, what is still under construction, and which activities can affect each other. Assess these relationships before you overlap installation and commissioning.

Build the commissioning plan from the required operating activities, and include normal use and relevant abnormal or recovery behavior. Use competent technical assessment to select the cases.

For Northbank, C04 identifies changeover, power interruption, alarm response, and maintenance isolation as unexercised. These gaps need to be assessed against the established requirements and operating basis.

Do not invent expected responses where the design basis leaves them open. Resolve the required behavior first, then prepare its examination.

Arrange for operators to take part where their understanding or performance matters. A commissioning team's demonstration does not establish that the receiving operators understand the instructions.

Keep readiness to perform a test separate from readiness for operational use: a controlled examination can proceed under conditions that do not permit routine service. Define and authorize those conditions through the actual project arrangements.

The commissioning account should state completed examinations, findings, configuration, limits, and the next decision, and it should allow the recipient to distinguish proven behavior from work still ahead.

### What it assumes

The classical method assumes that commissioning documents and physical readiness advance together, because people produce both and each takes time. A team that has written the procedures has usually also walked the installation.

### What changes with agents

Commissioning itself does not change. The installation, the instruments, the competent participants, the operators, and the authorizations are physical and human conditions, and agents do not supply them. The physical tests take the time they take. This part of the classical method carries over unchanged, and it sets the pace of the end of the project.

What changes is the paperwork around it. Agents can draft prerequisite lists, procedure drafts, configuration lists, and training materials quickly, so paper readiness can run far ahead of physical and human readiness. A complete set of drafts can make an installation look readier than it is. Training material prepared by an agent is not training: C05 records that operations has not completed its training, whatever material exists.

### The extended method

Divide the commissioning prerequisites into document prerequisites and physical or human prerequisites. Agents can check the document prerequisites against the configuration record and the basis. People confirm the physical and human prerequisites by inspection, demonstration, or the participant's own confirmation.

Schedule commissioning from the physical tests, the operators' availability, and the required authorizations. Do not let agent-prepared procedures for unresolved behavior, such as changeover, enter the plan as though the behavior were defined.

## Lesson 5: Deliver an identified result and responsibility

### The classical method

Acceptance is an authorized decision for an identified result, purpose, and conditions. A contractual acceptance, technical approval, authorization to operate, and operational handover can have different decision owners.

Base each decision on evidence suited to its stated purpose. An acceptance decision establishes its authorized disposition, but it does not establish physical performance beyond the supporting evidence.

Identify those arrangements from the appointment and the governing requirements. Do not infer an authority merely because someone asks for a completion date.

A useful handover package identifies:

- The delivered configuration and defining records.
- The requirements and decisions governing its use.
- The relevant examination evidence.
- The applicable operating and maintenance information.
- The receiving owners and continuing obligations.
- Known limits and the means to obtain support or correction.

Check that instructions apply to the actual installation. An instruction copied from an earlier supplier submission can direct the recipient to the wrong configuration.

Confirm training, access to information, maintenance arrangements, and receipt of responsibility. Placing files in a folder establishes availability, but it does not establish that the receiving team can use them.

Account for residual work explicitly. Some minor work may accompany a qualified handover where the authorized conditions permit it. Required technical evidence cannot become optional through a renamed list.

A qualified handover must respect applicable duties. Risk acceptance does not supply authority to waive a duty.

State the unfinished obligation, its effect on use, its owner, resources, due condition, and decision. If a necessary condition remains unmet, the proposed reliance remains unsupported.

Close the project account against the actual outcome, and preserve the original and amended commitments. A useful reduced result can still fall short of the original scope.

### What it assumes

The classical method assumes that assembling a handover package takes people's work. The people who assemble it look at each record as they include it, and a missing record usually shows as a gap in the package.

### What changes with agents

**A package can be assembled quickly from whatever exists.** Suppose, as a teaching assumption, that an agent is asked to assemble Northbank's handover package from the document controller's holdings. C05 records that the controller has draft drawings and the observed test report, and no complete approved record of the installed configuration. The agent can produce a package with a section for every item in the list above, and it can include the instruction that C04 says refers to the supplier's earlier 480 V submission. The package can look complete.

**A complete-looking package is not an identified, examined configuration.** The defining item of a handover package is the delivered configuration. Without an approved record of the installed configuration, the package has nothing to bind its evidence and instructions to. When an agent fills a section with a draft or a summary, the gap that classical assembly would have exposed is hidden instead.

**Applicability checks become cheap once the configuration is identified.** An agent can compare every instruction and maintenance record with the configuration record and report each mismatch, such as an instruction that cites 480 V equipment. The check needs an approved configuration record to compare against; until that exists, it can only report that the basis is missing.

**Responsibility still passes between people.** A01 gives the operations lead the acceptance of the operating information and readiness arrangements, and it gives operations the receipt of operational responsibility. An agent can track residual obligations, but it cannot own one, and it cannot confirm that the receiving team can use what it receives. The relationship with operations and maintenance continues after handover, and it stays with people.

### The extended method

Establish the approved record of the installed configuration first, then have agents assemble the package against it. Require each item in the package to cite the configuration revision it applies to, and require the agent to list every section it filled with a draft, a summary, or nothing. Use agents to check instruction and maintenance-record applicability against the configuration record, and have the responsible engineers examine the mismatches.

Confirm training, information access, maintenance arrangements, and receipt of responsibility with the receiving people directly. Record each residual obligation with a person as its owner.

## Lesson 6: Design the assurance arrangement

In a human team, the assurance arrangement could be left largely to habit, because the cost of examination and its independence came together. A second competent reviewer was expensive, so projects used one only where it mattered, and that reviewer brought separate preparation and reasoning. With agents, a check costs little but can share the producer's errors. So you must design where independence is needed and where it comes from, and you must make that design visible to the person who will rely on the result.

**Identify the ways an examination can share the producer's error.** These are the common ways:

- **A shared model.** Agents built on the same model can make the same error in the same place.
- **A shared brief.** A brief that frames the question or omits a condition can lead the producer and the checker to the same wrong answer.
- **A shared reference.** A check compares the work with a reference, sometimes called its oracle, such as a source record, a criterion, or an expected value. If producer and checker use the same wrong reference, every check passes; [Course 09, Lesson 5](09-technical-integration.html#lesson-5-examine-integration-and-repair-connected-work) showed that such agreement establishes consistency, not correctness. In assurance, the shared reference is often a test's expected value or the producer's acceptance criteria, so examine those references themselves where the consequence warrants it (manual §5.3).
- **The producer's own account.** A checker that reads the producer's summary instead of the actual candidate confirms the summary. A second agent asked to verify C04's cover-sheet claim from the cover sheet would examine the wrong thing.

**Obtain independence by changing what the error depends on.** Use one or more of these, as the claim requires:

- A different basis: brief the checker from the source records, not from the producer's tables or summary.
- Different preparation: have the examiner state the criteria or expected result before reading the output, and withhold the producer's conclusion from the checker's brief.
- A different method: check a calculation with a deterministic tool, or check a design claim with an inspection or a physical test. A physical test observes the installation directly, but its conditions and expected behavior come from the basis, so it shares errors there, and it covers only its own scope: C04's observation covers one normal transfer condition.
- A different examiner: a different model or system, or a different person. Where the work will be relied on, the examiner is a competent person.

**Set the strength of examination by consequence and detectability.** Manual §5.2 asks what a failure would cost and whether it would otherwise become visible in time. A reversible error that the next step would expose needs only the producer's check. An error that would stay plausible until serious consequences occur justifies stronger and often independent examination.

| An undetected error would be | And would otherwise surface | Suitable examination | Northbank illustration |
| --- | --- | --- | --- |
| Minor and reversible | Soon, in the next step | Producer's check, which an agent can perform | A formatting error in a draft review agenda |
| Material | Before reliance, through a later check | Agent check briefed from the source records, examined by the responsible engineer | An instruction's applicability to the identified configuration |
| Serious | Only in operation or after a failure | A defined physical test with the required behavior established in advance, competent people, and the receiving operators | Standby changeover, power interruption, alarm response, and maintenance isolation, which C04 did not exercise |
| Serious, and borne by whoever relies on the claim | Only after someone has relied on it | Examination by a competent reviewer independent of the drafter, against the actual evidence | The complete-acceptance claim on C04's draft cover sheet, and any answer to C05's handover question |

These examples illustrate the method; the project's actual requirements and the competent people's assessment set the real arrangement. Required professional, contractual, and project examinations still apply, and proportion is not permission to discard one.

**Spend independent human examination where it buys the most confidence.** The competent examiner's attention is the scarce resource, as in Course 08. Use cheap agent checks widely, and reserve independent human examination for the claims whose errors are serious and hard to detect. Do not add a review of a review unless it addresses a concrete competence, independence, or assumption problem (manual §5.3), and do not make review an approval stop for harmless work.

**Remember what review does not transfer.** A01 states that review does not transfer the producer's responsibility to the reviewer. An agent's check transfers nothing either, and a person's acceptance of an agent's check is that person's judgment.

**Make the design visible.** For each consequential claim, the assurance account states what examined it, by what method, against what basis, and what made the examination independent. Without that statement, a reader who receives a well-formed package cannot tell which claims were examined independently and which were only checked for consistency. That is the sponsor's position, and your instructor's.

Each arrangement gains something and costs something:

| Choice | Gain | Cost |
| --- | --- | --- |
| Agent checks at every revision | Early detection of inconsistencies and gaps, at little cost | Shared errors pass; findings use examiners' time |
| A checking agent briefed from the source records | Can catch an error in the producer's basis or brief | A second brief to prepare, and disagreements to resolve |
| Examiner states criteria before reading the output | Examination is not anchored on the producer's framing | Takes the examiner's time before the output arrives |
| Independent competent reviewer | Separate judgment on the claims that matter most | Scarce attention; a queue if overused |
| Physical test | Observes the installation itself | Fixed by equipment, access, and authorization; covers only its own conditions |

Part of the classical practice of sampling review answered the cost of a person's examination. For agent checks of information work, that reason weakens, so check widely. Independent review by competent people keeps its reason and becomes more important, because agreement among agent checks no longer carries the separate understanding that individual reviewers supplied, as [Course 09, Lesson 5](09-technical-integration.html#lesson-5-examine-integration-and-repair-connected-work) showed. Physical tests and the transfer of responsibility keep their classical form.

This is an argument from how the costs have changed, not a measured result. Agent capability and cost vary with the task and the system, so test the premise against your own work.

## Worked Northbank example

The earlier coordination work identified technical contributions that were needed; this later exercise asks what the supplied evidence actually establishes for acceptance and handover.

The project engineer receives C04 Rev 0 and C05 Rev 0 in a later exercise. C04 records an observed flow of 18 litres per second during one normal transfer condition.

It does not record the full hydraulic conditions or establish performance across A02's unresolved operating cases, and it also leaves several interactions unexercised.

The draft cover sheet claims complete acceptance, but that claim goes beyond the report's evidence. The team must correct the claim and establish the remaining examination and decision basis.

| Supplied observation | Consequence for handover | Needed response |
| --- | --- | --- |
| One normal-condition flow observation | Limited performance evidence | Establish conditions and assess required operating-case coverage |
| Changeover and abnormal scenarios unexercised | Connected behavior remains unestablished | Resolve required behavior and plan the relevant examination |
| Configuration list incomplete | Evidence and instructions lack a complete configuration basis | Reconcile and approve the installed configuration records |
| Instruction cites earlier 480 V submission | Instruction applicability is doubtful | Examine and correct it against the actual configuration |
| Training and spare-parts arrangements incomplete | Receiving readiness remains incomplete | Complete or obtain authorized dispositions for the arrangements |

This table does not assert equipment failure in the untested cases; it states that the supplied evidence does not establish their behavior.

A defensible response to the sponsor is:

> The supplied records do not establish complete handover. One flow observation is available, but its hydraulic conditions are incomplete. Required behavior, configuration records, applicable instructions, training, and maintenance arrangements need further work. The team will identify owners and closure evidence for each gap before proposing the applicable acceptance and receiving decisions.

A06's legal applicability inquiry also remains open in the supplied case. No course record supplies legal approval for Northbank.

### The same work with agents

The project engineer briefs an agent to draft the evidence account from C04 Rev 0 and C05 Rev 0. The brief gives C04's status, including that it does not establish that earlier design gaps were resolved, states that A02's operating conditions are unresolved and that A05 is a proposal, and requires every statement to carry its observation, conditions, and limits. It forbids "passed" or "complete" without them.

Before reading the return, the project engineer builds the coverage table from A02 and A01, so that the examination is not anchored on the agent's framing. The engineer then compares the agent's account with that table and with C04 itself. The checks are specific: the account reports one normal transfer condition, not "flow verified"; it lists all four unexercised scenarios; it does not describe them as failed; it reports the incomplete configuration list and the 480 V instruction; and it does not answer C05's question with "complete".

Suppose, as a teaching assumption, that a second agent on the same model is then asked to verify the account, and is given the account and C04's cover sheet. Its agreement would add little, because it would share the model and would be reading the drafter's framing and the cover sheet's claim. The project engineer instead has the agent's account examined against C04's body by a reviewer, where the project requires independent review, and by the responsible engineers for the technical content.

The team divides the examination by A01's responsibilities:

| Contribution | Produced by | Examined by | Source of independence |
| --- | --- | --- | --- |
| Evidence account of C04 | Agent | Project engineer, then the mechanical, electrical, and controls engineers | Coverage table prepared from A02 before reading; comparison with C04's body, not its cover sheet |
| Finding against the complete-acceptance claim | Project engineer, with agent drafting | A reviewer where the project requires independent review | Reviewer examines C04 itself and the finding, not the drafter's summary |
| Handover package | Agent assembly against the approved configuration record, once it exists | Responsible engineers for applicability; operations lead and maintenance for receiving needs | The receiving team examines whether it can use the package |
| Sponsor response | Project manager and project engineer, with agent drafting | The same people, against the evidence account | Each claim traced to an examined record |

The classical conclusions do not change. The supplied records do not establish complete handover, and the sponsor response stays as written above. What changes is that the team must show which examinations were independent and why.

## Transfer example: business-system migration

A migrated database can pass a record-count check while user permissions, recovery, and reporting remain unexamined. The count provides useful evidence for one claim.

Build acceptance around the intended activities, and identify the software configuration, data state, test conditions, user participation, and recovery arrangements.

Transfer responsibility for support and administration together with usable instructions. Record any source system that is retained and any unresolved obligations. Apply the organization's actual security and delivery requirements.

Agents can run the record-count check and many other comparisons repeatedly. If the agent that wrote the migration also writes the checks, the checks can share its assumptions, so brief at least the consequential checks from the source system and the users' activities. The users' acceptance and the support team's receipt of responsibility stay with people.

## Practice

Use A01, A02, A06, B03, C04, and C05 with their supplied revisions.

First, without an agent, write the finding against C04's complete-acceptance claim, and list what C04 observes and what it leaves unestablished. You then know what an agent's evidence account should contain. Work with an agent for every output that follows.

Prepare four outputs:

1. Prepare an assurance coverage table for six identified requirements or readiness conditions.
2. Write a finding against C04's complete-acceptance claim.
3. Prepare a commissioning prerequisite list without inventing technical responses.
4. Prepare a proposed handover package and receiving-responsibility table.

Include the information needed to examine the flow observation. Identify the missing configuration and instruction relationships. State which decision each proposed record supports.

For Output 2, compare the agent's finding with your unaided one. For each output, keep the brief you gave the agent and a short note of what you checked in its return, what you found, and what you changed.

Do not run equipment tests. In this exercise you develop the plan and evidence account from the supplied records.

Then complete three further exercises:

1. **Examine an agent's summary.** An agent returns this summary of C04, invented for the exercise: "C04 confirms that the installation meets A02's 18 litres per second requirement. Remaining items are minor documentation updates." Explain each overstatement and what the record actually supports. Then write the sentences in the brief that would have guarded against it.
2. **Redesign a check.** Suppose, as a teaching assumption, that a second agent on the same model was given the summary above and C04's cover sheet, asked to verify the summary, and returned "verified". State what that check established and why it was not independent. Then redesign the check: its basis, its preparation, its method, and its examiner.
3. **Design the assurance arrangement.** For four Northbank claims (flow under the established operating cases, standby changeover behavior, the applicability of the operating instructions, and operating readiness), set the examination, who or what performs it, and the source of its independence, in proportion to consequence and detectability. State two tradeoffs in your design.

### Transfer practice: a finding after acceptance

This is a separate constructed teaching scenario. It adds no fact, approval or test result to Northbank, and it does not close C04's gaps. Suppose an installation has an identified accepted configuration, an agreed changeover requirement and recorded examinations for its intended use.

Consider three later reports separately:

1. During an operating condition covered by the accepted requirement, standby changeover fails to perform that requirement.
2. The installation meets the stated requirement, but operations demonstrates that the requirement does not support the intended service during a needed transition.
3. The sponsor requests a higher flow that was outside the accepted scope.

Explain the initial interpretation of each report, what evidence is needed, what decision authority would need to be identified and which work could continue. Distinguish an apparent defect, a gap in validation or in the commitments, and a new need. A report can contain more than one issue; these descriptions are not an exhaustive classification.

Use an agent to challenge your reasoning, then explain which parts you retained or changed and why. Identify the accepted subject separately from a possible repair or new configuration. Discuss the consequences for continued reliance and any required notification without inventing authority to operate, withdraw or accept the installation.

This is guided transfer practice, not an additional assessed outcome. Keep the existing Northbank assignment and its keyed answers unchanged.

## Knowledge check

1. Why must quality examination be planned before final inspection?
2. How do verification and validation ask different questions?
3. What does C04's flow observation support, and what does it leave unestablished?
4. What information binds a test result to the configuration examined?
5. Why do commissioning completion and operational handover require distinct consideration?
6. When can transferring an open obligation support a qualified handover?
7. A second agent reviews the first agent's work and agrees with it. Name three ways that review can fail to be independent, and one way to design independence into it.
8. Why should consequence and detectability, rather than the low cost of agent checks, set where independent human examination is used?
9. An agent assembles a handover package with a section for every required item. What does the package establish, and what must exist before it can identify the delivered result?
10. Which parts of Northbank's assurance and handover do agents leave unchanged, and why do those parts set the pace?

## Assessed assignment

Prepare Northbank's proposed assurance and handover account, working with agents, including coverage, findings, commissioning prerequisites, recipient information, responsibilities, and a recommendation to the sponsor. Add a short account of your assurance arrangement: where you required independence, how you obtained it, and how you examined the agents' work, with the briefs you used.

Then defend the account to your instructor. Your instructor will change premises such as the conditions C04 recorded, whether an approved configuration record exists, or how a check was prepared and by whom, and ask you to reason through the consequences. Your instructor rates the defense as the teaching guide describes; in text-only study it is rated on changed-premise reasoning with the medium recorded.

Use these seven observable criteria:

1. The coverage table connects requirements, configurations, methods, evidence, and decisions.
2. The account limits C04's conclusions to its actual observations and missing conditions, including in every agent-prepared summary it uses.
3. The commissioning plan preserves unresolved behavior and prerequisite conditions, and it distinguishes document prerequisites from physical and human prerequisites.
4. The handover package identifies the actual recipient needs and receiving responsibilities, and it binds its contents to an identified configuration or states that the approved configuration record is missing.
5. Residual obligations retain owners, consequences, closure evidence, and required authority, and each owner is a person.
6. The account of the assurance arrangement shows the design: for each consequential claim, what examines it, against what basis, and what makes that examination independent, in proportion to consequence and detectability. Your own examination record shows what you actually checked in each agent return, what it found, if anything, and what you changed.
7. In the defense, you explain the account's main conclusions and their grounds, show what your examination of the agents' work found, identify which judgments are your own, and reason correctly through the changed premises your instructor poses.

Before the defense, ask a peer to act as the receiving operations lead. Repair any gap that prevents that person from understanding the proposed responsibility, and retain the previous revision and the repair basis.

## Portfolio continuation and reading

Keep your account as Portfolio 10 and connect it to the Course 09 configuration and interface package. Retain C04's original observation separately from your corrected conclusion.

Carry the remaining decisions into Course 11. They will become part of the project's continuation decision and the final practicum.

Read management manual (Edition 9) chapter 5, §§7.5–7.6, and chapter 8, in [References](../references.html). They explain evidence limits, product examination, and transfer of continuing responsibility. §§5.2–5.5 are the basis for Lesson 6: assurance by consequence and detectability, independence, the actual candidate, and evidence reuse.

The optional NASA readings go deeper into verification and validation methods, but all core exercises can use the supplied offline records.
