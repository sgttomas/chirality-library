# Course 08: Planning and Managing Project Execution

[Series](../index.html) · [Northbank case](../case-study.html) · [Glossary](../glossary.html) · [References](../references.html)

## Purpose and preparation

A plan connects the intended result to work, people, resources, and decisions, and it becomes useful when the team can act on it.

This course teaches you how to keep that connection as conditions change, in a team where people work with AI agents. Use the project basis from Course 07, and apply the reasoning and communication methods from Courses 05 and 06.

Read Northbank Packets A, B, and C, and keep each record's revision and status visible. All prices and durations are teaching inputs.

### How this course is built

The series index explains [how the series is built](../index.html#how-the-series-is-built). In short, the classical method of execution control remains sound, and you need it, because much of a physical project still runs at the speed of suppliers, fabrication, and site work. But the classical method assumes that producing work costs people's time, and that the person producing the work is also paying attention to it. Agents separate production from accountable attention for much of a project's information work.

As in the beam analogy, the ratio that matters here is the time production takes compared with the time examination and decision take. When production takes most of the time, the classical method's single estimate is adequate. When agents shrink production, examination and decision can become the terms that control the plan.

Lessons 1 to 5 each follow four steps: the classical method, what it assumes, what changes with agents, and the extended method with its tradeoffs. Lesson 6 treats the arrangement of people and agents as a system to engineer.

### The teaching arrangement

Use the case's [arrangement for working with agents](../case-study.html#working-with-agents-in-the-case): the agents hold no appointment under A01, and every Northbank record stays as written. You will work with real agents in the practice and the assessed assignment.

### Outcomes

After this course, you can:

- Define readiness conditions for an activity.
- Build a schedule from dependencies and available resources, and identify the time that production, examination, decisions, and external processes each take.
- Distinguish a budget, estimate, commitment, actual expenditure, and forecast.
- Connect procurement and contracts to the technical basis.
- Assess change and report progress with its consequences.
- Design how people and agents divide the work, and defend the tradeoffs.
- Direct, examine, and accept agent contributions, and show which judgments are your own.

## Lesson 1: Plan from conditions for work

### The classical method

An activity needs more than a date: it needs usable inputs, competent people, access, resources, and authority. These conditions determine readiness.

For example, equipment installation needs delivered equipment and ready site works. An equipment order needs a reviewed technical package and expenditure authorization; a supplier's requested date does not establish either condition.

Define the output before you estimate the activity. State the required input and its condition, name the owner who supplies it, and name the person who checks its suitability.

Use a small dependency table:

| Activity | Required condition | Supplier | Readiness evidence |
| --- | --- | --- | --- |
| Release equipment order | Reviewed package and expenditure authorization | Engineering and authorized expenditure approver | Identified decisions for the purchase package |
| Install equipment | Delivered equipment and ready site works | Supplier and site team | Delivery check and site readiness confirmation |
| Commission installation | Completed installation and prerequisite checks | Installation and assurance teams | Records for the identified configuration |

The table records needed relationships, but it does not assert that Northbank has satisfied them.

Some activities can proceed while others wait. The team can prepare a review plan while equipment selection remains open, but it cannot complete selection-dependent checks without the selection data.

Avoid making every open question a project-wide stop. Find the work that depends on the question, and continue the work that has sufficient inputs and authority.

Build the schedule in this order:

1. Identify the required outputs.
2. Identify each activity's prerequisites.
3. Estimate each activity's duration.
4. Assign available resources.
5. Calculate the earliest supported sequence.
6. Compare the result with the target.

A dependency calculation can expose impossible dates, but it cannot establish that the durations are reliable. State their basis and uncertainty.

### What it assumes

The 'What it assumes' passages in this course describe working arrangements for comparison. They are not universal facts about human practice; examine whether they hold in the task at hand.

The classical method estimates a duration from the effort of the people who will do the work, and it treats the duration as one number. That works when most of an activity's time goes into producing its output, and the people producing it check it as they go.

### What changes with agents

Readiness conditions do not change. An agent cannot supply an expenditure authorization, a checked electrical survey, or operations' confirmation of the changeover function. A supplier's delivery time and the time needed to install a pump do not change either.

What changes is the inside of an information activity, such as a technical review, an impact assessment, or a purchase package. Its duration has four parts, and agents affect them differently:

| Part of the duration | What happens in it | Effect of agents |
| --- | --- | --- |
| Production | Drafting, calculating, comparing, searching | Can shrink sharply, often from days to hours |
| Examination | A competent person checks the output for its intended use | Does not shrink by itself, and grows with the amount produced |
| Decision | The person with authority decides | Does not shrink; depends on that person's availability and evidence |
| External | Suppliers, fabrication, delivery, site access, physical tests | Unchanged |

In a human team, production often took most of the time, so one number described the activity well enough. With agents, the other three parts can take most of the time, and people's availability and the physical world set them. Whether they do on a given activity is a question for evidence.

### The extended method

Build the schedule in the same order, but estimate each information activity by its four parts. When you claim that agents shorten an activity, show which part they shorten and what evidence supports the shorter time.

In Northbank, C03's release at the end of Week 6 depends on a corrected purchase package. Agents might shorten the drafting of the project's technical review of B01. But they cannot supply the electrical engineer's determinations that A04 leaves open, the operating conditions that A02 requires the project to establish, or the expenditure authorization. The records do not show how much of the time before release is production, so agent use alone does not support an earlier release date.

Cheap production also tempts a team to start every activity at once. An activity started before its inputs are ready still creates rework. Agents can produce rework quickly, but each round of it still needs a person to examine it.

## Lesson 2: Connect the schedule to people and resources

### The classical method

Two activities can have independent inputs and still compete for one person, so a calendar that assigns both at the same time may be impossible.

Consider a clearly invented teaching example, separate from Northbank. Two four-hour reviews need the same reviewer during one four-hour shift. Their inputs are ready, but their resource plan still needs another shift or another competent reviewer.

Check resource demand at the level that supports decisions. Include review, coordination, repair, travel, site access, and required operating support: these activities use capacity even when they produce few documents.

Estimate remaining work with the people who will do it. Ask what conditions the duration assumes, and identify access windows, interruptions, and decisions that can extend it.

Adding people can increase output when work has suitable boundaries, but it can also increase coordination and review demand. Assess the limiting activity before you change staffing.

A critical path is a sequence that controls the calculated finish under stated assumptions. The controlling sequence can change after a delay or resource adjustment, so recalculate it when the relevant basis changes.

An earlier start is useful only when the activity can produce a usable result. Work started too early can create rework or unsafe exposure. If partial inputs permit partial progress, define an authorized, bounded activity.

Keep the baseline schedule as the comparison reference and maintain a current forecast beside it. Record changed assumptions and decisions. A revised forecast reports the present outlook; it does not silently change the approved target.

### What it assumes

The classical method treats people's working time as the limiting resource. Adding a person adds production capacity and some attention together, and it also adds coordination: newcomers need context, and every additional person adds communication paths.

### What changes with agents

Agent production capacity is elastic: you can add agents in minutes. But every agent assignment adds work for the people who brief it, examine its output, and combine that output with the rest.

Return to the invented review example. Suppose agents prepare ten review packages in an hour, and each still needs four hours of a competent reviewer's examination. The agents have removed production as the constraint, and the reviewer's shift is now the constraint.

When work arrives for examination faster than people can examine it, unexamined work accumulates. That accumulation is not progress. Each item in it may contain an error, and the error spreads into dependent work as soon as someone relies on it. This course calls the accumulated, unexamined work **verification debt**.

An agent may or may not retain project history between assignments. Retained history can carry superseded premises, so establish the current basis either way. A brief that omits C03's statement that each forecast item includes actual expenditure invites the double count in Lesson 3.

### The extended method

Plan examination capacity as you would plan any constrained resource. For each information activity, name the person who examines it, estimate the examination time, and check when that person is available. Then size the agent assignments to what the examiner can check: a bounded output with stated inputs, limits, and checks.

Find the critical path through examination and decisions as well as through physical work. Agents make recalculation cheap, so you can recalculate whenever the basis changes. Report a change to the controlling sequence when it affects a decision; frequent recalculation does not require frequent reports.

Agents also make it cheap to prepare several options at once, such as an alternative supplier slot, a bounded overlap, and the impact assessment that A05 requests. A team can therefore keep options open longer than it could afford before. But each option still needs examination before anyone relies on it, and long-lead commitments, such as an equipment order, still fall due on the classical schedule.

Each arrangement gains something and costs something:

| Choice | Gain | Cost |
| --- | --- | --- |
| More agents working in parallel | Faster production and more options | A longer examination queue and more integration work |
| Larger agent assignments | Fewer briefs and less context lost between assignments | Harder examination; errors hide in volume |
| Smaller agent assignments | Easier examination | More briefs, more integration, and context lost at each boundary |
| Several options prepared at once | Decisions can wait for better information | Each option uses examination and decision time |

Choose the arrangement that shortens the route to an examined, usable result, not the one that produces the most output.

## Lesson 3: Maintain a credible cost account

### The classical method

A budget is an authorized amount for a defined scope. An estimate assesses expected cost. A commitment records an obligation, such as an order. Actual expenditure records incurred cost. A forecast assesses the expected final outcome.

These amounts answer different questions. Spending below the budget does not show that enough money remains to finish; a forecast must include the work still required.

Use a consistent cost structure. State the date, currency, scope, price basis, and treatment of taxes or escalation when relevant. Match the cost structure to the team's accounting arrangements.

A simple forecast can use:

> Expected final cost = recorded actual expenditure + estimated remaining cost.

This equation requires amounts that do not overlap: a forecast item that already includes actual expenditure must not receive the actual expenditure again.

Treat commitments with the same care. An unpaid order can form part of remaining cost, but adding the entire order to a forecast that already includes it counts the order twice.

Contingency is an identified allowance for uncertainty under the project's rules, not permission to expand scope. Explain whether a forecast includes the allowance and how approved use affects its balance.

Report a forecast excess promptly, and identify its scope and evidence. Present options with their technical, delivery, and commercial effects, and get the decision from the person with the required authority.

Do not repair a cost forecast by removing necessary checks or hiding unfinished work. A reduced scope needs an authorized decision and an assessment of its consequences.

### What it assumes

The classical method estimates engineering and coordination cost from people's hours. It also assumes that calculating takes effort, so arithmetic is a common source of error that careful people catch.

### What changes with agents

The definitions do not change. A budget remains an authorization, and a forecast remains an assessment that authorizes nothing. This part of the classical method carries over unchanged.

Three things do change:

1. **The cost structure.** Agent use has its own cost, such as subscription or usage charges. That cost varies with use and can grow quickly when many agents run in parallel. Record it as the team's accounting arrangements require.
2. **The cost that agents do not reduce.** The examination and decision hours of competent people remain. A forecast that lowers an engineering cost because agents draft the documents must still include examination, repair, and integration.
3. **The kind of error that remains.** Agents make arithmetic cheap. With a calculation tool, an agent's sums are usually right, so more of the remaining errors are errors of basis: which amounts belong in the sum. An agent will add actual expenditure to C03's inclusive total as readily as a careless colleague would, and it will present the result with the same confidence as a correct one. Still check the sum.

Forecasts also become cheap to regenerate, so a team can produce a new one every day. Issue a new forecast when its basis changes, because each forecast uses the attention of the people who must read and act on it.

### The extended method

Give the agent the cost basis in its brief: for Northbank, that C03's items include their recorded actual expenditure and that C03 excludes the 22 litres per second proposal. Then examine the basis of the returned forecast, not only its sum.

Whatever agent use the team adopts, C03 remains the current forecast. Do not reduce it in expectation of savings from agent use; a lower forecast needs evidence for each amount it changes.

## Lesson 4: Connect purchasing, risk, and change

### The classical method

Procurement turns an authorized need into a commercial transaction. The purchase package must identify the required configuration, technical conditions, submission requirements, delivery terms, and examination arrangements.

Keep technical review separate from expenditure approval; procurement must know both dispositions before release. A price quotation or delivery promise cannot approve a technical substitution.

Contracts allocate duties and commercial consequences, so read the actual contract before you assert rights, penalties, warranties, or notice obligations. Northbank supplies no contract terms that establish such rights.

Coordinate the supplier's information dates with engineering's point of need: a vendor drawing received after foundation construction may create avoidable rework. Include review and repair time in the procurement sequence.

A risk concerns uncertainty and its possible effects, while an issue is a present condition that requires attention. Northbank's voltage discrepancy is a present issue; an uncertain future delivery slot presents a different problem.

For each material risk or issue, state the objective it affects, its evidence, owner and response, and the point at which it will be reconsidered. Use estimates with their basis, and do not invent precise probabilities to fill a form.

Assess a proposed change across the whole project:

1. Identify the departure from the approved basis.
2. Explain the reason for the departure.
3. Assess technical and operating effects.
4. Assess cost, schedule, resources, and contractual effects.
5. Identify the required decisions.
6. Propagate the actual disposition to affected work.

A proposal remains a proposal until it receives its authorized decision. A correction within existing scope can still change cost and schedule, so it needs the appropriate spending and commitment decisions.

### What it assumes

The classical method assumes that assessing a change is expensive, so teams collect changes and assess them in batches. It also assumes that carrying a decision through the documents takes days, and that delay gives people time to notice an error. Suppliers prepare their submissions at the same human pace.

### What changes with agents

**Change assessment becomes fast.** Agents can draft the structure of the A05 impact assessment, its comparisons, and its cost and schedule parts within hours. The hydraulic part cannot be completed until the project establishes the operating conditions that A02 requires, and B02 records that the hydraulic basis is incomplete. A team can therefore prepare an assessment when a change is raised, instead of batching changes to save drafting effort. The specialists' examination and the sponsor's decision remain the slow steps, and they may still be best taken together at the decision-maker's rhythm.

**Propagation becomes fast in both directions.** An agent can carry an approved disposition into every affected document quickly, and it can carry a proposal into them just as fast. A05 Rev 0 is a proposal. An agent given A05 without its status may design for 22 litres per second, and no delay remains in which someone might notice. So configuration control must govern what agents read: give each agent the identified basis, with revisions and status, and check which basis its output used.

**Suppliers may use agents too.** B01 copied its 480 V value from A03. A supplier's agents can make the same kind of copying error faster, in a submission that looks more complete. A complete-looking submission is still not a reviewed one. Agents can help the team reply within B01's two working days with the deficiencies it found. That reply cannot be an approval: B01 is not accepted, and the electrical engineer's determinations that A04 leaves open still take the time that competent examination takes.

**Agent work brings its own risks.** An agent's error can look the same as correct work. Several agents that share one model or one brief can make the same error. Context can be lost between a brief and a return. Treat these as ordinary risks and issues: state the objective each affects, its evidence, owner, response, and reconsideration point.

### The extended method

Use the same six steps. Agents can speed the drafting in Steps 3 and 4 and the mechanical work of Step 6. They do not speed the examination of Steps 3 and 4, and they do not make the decisions in Step 5.

Before any agent propagates a disposition, confirm that the disposition exists and identify its scope. After propagation, check the affected outputs against the disposition. Sending the instruction does not show that each output adopted it.

## Lesson 5: Measure progress by usable results

### The classical method

Document counts are useful for some workload questions, but they provide weak evidence about technical readiness: ten completed drawings may still contain one unresolved interface that prevents construction.

Report completed outputs with their examination and remaining conditions. Distinguish production complete, review complete, accepted, and available for dependent use, and use the project's actual status definitions.

A weekly account should help someone decide or act. Include the results achieved, unresolved conditions, forecast changes, decisions needed, and the next ready work. Identify the basis date.

Compare the present forecast with both the baseline and the previous forecast, and explain meaningful departures. Avoid repeating an unchanged issue without a response or a route to a decision.

When the target is threatened, present credible options. Assess expedited delivery, resequencing, overlap, additional resources, or scope change where relevant. Each option needs supported prerequisites and consequences.

Overlap can reduce time when activities have suitable boundaries, but it can also expose people or invalidate tests. Define those boundaries before you count a schedule saving.

### What it assumes

The classical method treats production as weak but real evidence of progress, because a finished drawing took someone's effort and some of their attention.

### What changes with agents

Production no longer shows that anyone spent effort or attention on the work, so a count of produced documents stops being weak evidence and starts to mislead. Agents can produce ten draft documents in an afternoon. Of the statuses above, those that still report progress are review complete without open findings, accepted, and available for dependent use.

Agents also make continuous reporting easy, and each report uses its reader's attention. Report at the rhythm of the decisions the report serves.

Adding agent capacity is a new option when the target is threatened. It helps only where production limits the finish. In Northbank, C03's finish is three weeks later than the target because release moves from the end of Week 4 to the end of Week 6 and delivery takes five weeks instead of four. Agents cannot shorten the delivery. They could shorten the release only if producing documents limits the corrected purchase package, and the records do not show that.

### The extended method

Report the gap between produced and examined work: what is waiting for examination, for how long, and which dependent work it holds up. A growing gap is verification debt, and it belongs in the account with the decisions needed to reduce it.

Before you propose more agent capacity, identify what limits the finish. If examination, a decision, or an external process limits it, more agents lengthen the queue without moving the finish.

## Lesson 6: Engineer the arrangement that does the work

In a human team, much of the team's working arrangement comes with the people. Hiring sets its size, and each person brings a sense of when to stop and ask. With agents, the arrangement is a design that you choose. Agents do not reliably recognize the limits of their competence or their authority, so the arrangement must make those limits explicit.

Design the arrangement as a project engineer designs any system: from its required function, its interfaces, and its failure modes.

**Allocate each function by its consequence.** Agents can produce, compare, and check against stated criteria. Deterministic tools can perform fixed calculations and comparisons. People examine work for reliance, decide, accept, and deal with the sponsor, operations, suppliers, and authorities. Where an error would be serious and hard to detect, arrange stronger examination.

**Design the two interfaces.** The brief tells an agent the purpose, the identified basis with revisions and status, the output wanted, its limits, the checks to perform, and the conditions that require a person's decision. The return reports the output, the scope completed, the checks performed, the limits, and any open choices. It distinguishes what the agent prepared from what it actually changed. [Course 06](06-working-relationships.html#lesson-5-support-reliable-contributions) treats the brief and the return as communication.

**Provide independence where it matters.** An agent that checks another agent's work, using the same model and the same brief, may share its errors. Their agreement shows consistency, not correctness. Where the consequence warrants it, change the basis of the check, the way the check is prepared, or the examiner. Where the work will be relied on, the examiner is a competent person.

**Size the arrangement to examination capacity.** Lesson 2 showed that production beyond examination capacity becomes verification debt.

**Design against the known failure modes:**

- A confident error that looks like correct work.
- A proposal treated as approved basis.
- A superseded revision used as current.
- Context lost between the brief and the return.
- Unexamined work accumulating behind a busy examiner.
- Agreement between agents mistaken for independent review.
- Records produced because they are cheap, not because anyone needs them.

A useful aim for the arrangement is warranted confidence per unit of the accountable person's attention. It is a design aim, not a measurement. Confidence without adequate grounds does not satisfy it, and saving attention by hiding uncertainty defeats it.

This lesson also supports a broader argument. Part of the classical discipline exists to manage the cost of coordinating people's labour on information work: estimating it from production hours, batching changes to save drafting effort, and measuring progress by documents produced. Where agents do the production, these practices lose much of their reason, so do not carry them over by habit. Some keep part of their reason in a new form. Batching decisions can still save the sponsor's and specialists' attention, and site crews still need their workload levelled.

The practices that manage authority, evidence, acceptance, and the physical world keep their reasons, and agents make them more important, because work can now reach the point where someone relies on it without anyone having attended to it while it was produced.

This is an argument from how the costs have changed, not a measured result. Agent capability and cost vary with the task and the system, so test the premise against your own work.

### Worked arrangement: one contribution with delegated help

This teaching arrangement changes no Northbank record or result. The project manager asks a coordinating agent to prepare the cost-and-sequence comparison from C01 and C03, through examination and ordinary repairs. The manager identifies the current basis, the required explanations, and decisions reserved by A01. No delegation is required if one agent can carry the contribution effectively.

Suppose the chosen system permits bounded delegation. The coordinating agent assigns the cost comparison and schedule calculation separately, giving both the same identified records and their conditions. It receives the returns, checks their common basis, resolves inconsistencies and prepares one integrated comparison. It carries that contribution through repairs instead of sending every intermediate question to the manager.

Both helpers could omit the same qualification in C03. Their agreement would then repeat a shared mistake. The manager examines the inclusive cost basis, the delivery count, the retained assumptions and the actual combined output. Any required independent reviewer prepares from the source and criteria, rather than merely accepting the coordinator's summary. Delegation supplies production capacity; it does not itself supply independent assurance.

The examination record names the production direction, which agent wrote the consequential briefs, which returns were used, and what the manager actually examined. Links to recoverable briefs and returns can suffice. There is no requirement to copy every child message. If a return is unavailable, report the resulting evidence limit instead of attributing a check that nobody observed.

Compare this arrangement with one agent doing the same work. Explain when delegation would preserve useful continuity and when its preparation, coordination or review cost would outweigh the benefit. Neither arrangement changes the keyed cost or schedule answers.

## Worked Northbank example

The project definition supplies the scope and conditions for planning, and the new forecast shows how cost and timing can change while the approved commitments remain in force.

The project manager receives C03 Rev 0, whose forecast covers the existing 18 litres per second scope. A05 Rev 0 is still a proposal for 22 litres per second.

C03 assumes order release at the end of Week 6, and five delivery weeks place delivery at the end of Week 11. Installation takes Weeks 12 and 13, commissioning takes Week 14, and handover takes Week 15.

The resulting finish is the end of Week 15, three weeks beyond A02's end-of-Week-12 target. This calculation assumes ready site works and no overlap.

The forecast total is:

> 80,000 + 55,000 + 30,000 + 45,000 + 23,000 + 12,000 + 20,000 = 265,000.

The authorized budget is 240,000, and the forecast exceeds it by 25,000, or approximately 10.4 percent. C03 already includes actual expenditure in each item.

This is a forecast, not an approval to spend 265,000, and it gives no conclusion about pump suitability. B01's submission and A02's unresolved operating conditions still need technical resolution.

### The same work with agents

The project manager briefs an agent to compare C03 with C01 and to calculate the forecast finish. The brief identifies both records with their revisions and status, states that each C03 item includes its recorded actual expenditure, states that C03 excludes A05, and asks the agent to show each step.

The agent returns the comparison and the sequence. The manager does not accept them because they look right. The manager checks that the agent counted delivery from the end of Week 6, kept contingency at 20,000, added no actual expenditure, and left A05 out. The arithmetic is the same as in the classical account; agents change who performs it and what the manager must check.

The team divides the examination by A01's responsibilities:

| Contribution | Produced by | Examined by | The examination checks |
| --- | --- | --- | --- |
| C03 and C01 cost comparison | Agent | Project manager | Inclusive basis, no duplicated amounts, contingency treatment |
| Forecast delivery sequence | Agent | Project manager | Release date, delivery duration, no-overlap and site-readiness assumptions |
| Draft technical review of B01 | Agent | Project engineer, with the electrical and mechanical engineers | Voltage, missing pump curve and configuration, the limits that A04 states |
| Sponsor briefing | Project manager, with agent drafting | Project manager, and a reviewer where the project requires independent review | Each claim's support, the exclusions, and the decisions requested |

A useful manager's account states:

> The current 18 litres per second scope forecasts 265,000 and handover at the end of Week 15. These estimates retain C03's assumptions. Technical release remains dependent on the reviewed purchase package. The 22 litres per second proposal is excluded. The sponsor must decide any change to budget or target. The team uses agents to prepare comparisons and drafts, and this forecast claims no cost or schedule saving from that use.

The team can investigate alternatives before requesting a decision, and agents make it cheap to investigate several at once. But the team must not describe an unconfirmed saving as achieved progress.

## Transfer example: laboratory instrument replacement

A laboratory needs an installed, calibrated instrument. The order requires a selected instrument and an approved acquisition package, and installation needs delivered equipment, a suitable room, and utilities.

Calibration depends on installation, and staff training depends on the identified operating configuration. A shipment date alone cannot forecast usable service.

Use the same dependency and cost methods, and add the laboratory's actual accreditation, safety, and purchasing requirements. Establish those requirements from the sources that govern them.

Agents can draft the acquisition package and the calibration plan. The governing requirements, the laboratory's acceptance, the instrument's delivery, and the time calibration takes stay where they were.

## Practice

Use A01 Rev 0, A02 Rev 1, A05 Rev 0, B01 to B03 Rev 0, and C01 to C03. Do not use Packet D.

First calculate C03's sequence and cost totals yourself, without an agent. You then know what an agent's return should contain. Work with an agent for every output that follows.

Prepare four outputs:

1. Draw the baseline and corrected delivery sequences.
2. Compare each C03 cost item with C01.
3. Prepare a purchase-release readiness table.
4. Write a sponsor briefing of no more than 250 words.

Include the supported forecast, unresolved prerequisites, decision authority, and one option requiring investigation. State what evidence would make that option usable.

For each output, keep the brief you gave the agent and a short note of what you checked in its return, what you found, and what you changed.

Then complete three further exercises:

1. **Divide the durations.** For each activity before order release, identify its production, examination, decision, and external time. Mark where the records support your division and where they are silent.
2. **Examine an agent's return.** For a separate cost exercise, use invented actual expenditure of 90,000; the remaining-cost estimate is 175,000. An agent returns a forecast of 355,000, made by adding 90,000 to C03's 265,000 total. Explain the two calculation bases and the agent's error. Then write the sentence in the brief that would have guarded against it.
3. **Design an arrangement.** Design how the team would prepare the impact assessment that A05 requests: the agent assignments, who examines each, where independence is needed, and what reaches the sponsor. State two tradeoffs in your design.

## Knowledge check

1. What conditions distinguish a ready activity from a scheduled activity?
2. How can a resource conflict invalidate a dependency schedule?
3. Why does C03's forecast not change the authorized budget?
4. When would adding actual expenditure to a forecast duplicate cost?
5. What decisions and evidence does Northbank need before equipment order release?
6. What must the team establish before reporting a schedule saving from overlap?
7. Why does adding agents to an activity limited by examination increase unfinished work instead of shortening the activity?
8. Two agents that use the same model agree on a forecast. What does their agreement establish, and what does it not establish?
9. Name one classical practice from this course that loses most of its reason when agents do the production, and one that keeps its reason. Explain each from the cost it was answering.

## Assessed assignment

Prepare an execution control package for Northbank's existing scope, working with agents. Include the schedule, cost comparison, procurement conditions, response priorities, and sponsor decision request. Add a short account of how you arranged the agents' work and how you examined it, with the briefs you used.

Then defend the package to your instructor. Explain how you reached its main conclusions and what you checked, and reason through changed premises that your instructor poses, such as a different cost basis or delivery time. Your instructor rates the defense as the teaching guide describes; in text-only study it is rated on changed-premise reasoning with the medium recorded.

As the series index explains under [Work with agents](../index.html#work-with-agents), your instructor is in your sponsor's position: the package alone cannot show how much judgment went into it, so your briefs, examination record, and defense carry that evidence.

Use these seven observable criteria:

1. The schedule reproduces the stated durations, prerequisites, and no-overlap assumptions. Where it claims that agents shorten an activity, it identifies the part of the duration they shorten and the supporting evidence.
2. The cost account reconciles totals without duplicating actual expenditure or contingency.
3. Purchase readiness distinguishes technical suitability, expenditure authority, and supplier timing.
4. Proposed responses preserve the existing scope until the authorized decision changes it, and they claim no saving from agent use without supporting evidence.
5. The briefing identifies supported progress, forecast departures, uncertainty, and decision owners.
6. The account of the arrangement shows the design: who examines each agent contribution, what that examination must check, and where independence is needed and how it is provided. Your own examination record shows what you actually checked in each agent return, what it found, and what you changed.
7. In the defense, you explain the package's main conclusions and their grounds, show what your examination of the agents' work found, identify which judgments are your own, and reason correctly through the changed premises your instructor poses.

Before the defense, explain your package to a peer as practice, and repair defects found during that examination or the assessment. Retain the previous revision and the repair basis.

## Portfolio continuation and reading

Keep the package as Portfolio 08 and add it to your Course 07 project basis. Carry unresolved technical conditions into Course 09, and examination and handover prerequisites into Course 10.

Read management manual (Edition 9) chapter 3, §§4.3–4.5, §§5.2–5.3, chapter 6, §8.1 and §9.1 in [References](../references.html). They connect dependencies, ready work, examination, change propagation, completion, integration, and the whole cost of a result.

The optional APM readings give a wider account of project management, but the supplied case contains all inputs for this course's core exercises.
