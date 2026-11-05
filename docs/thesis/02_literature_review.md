# Chapter 2 — Literature Review

---

## 2.0 Introduction

This chapter reviews five bodies of work relevant to agent-assisted professional practice: agent architectures, model reliability, formal methods and safety engineering, professional regulation, and epistemic frameworks. It asks what these sources contribute to the design of work in which agents can produce substantial results while people remain answerable for reliance.

The review is selective, not an exhaustive survey or a claim to priority. It
uses its stated set of sources, including selected 2026 sources, to examine
architectural hypotheses that are open to revision. Research papers, engineering
reports, professional guidance and philosophical arguments serve different
purposes: a benchmark result supports a claim within its evaluated conditions,
an implementation report supplies experience and a design hypothesis, and a
professional standard specifies obligations within its scope. None alone
validates Chirality as a complete system.

This chapter keeps three kinds of claim separate throughout:

- **Normative commitments:** what the work chooses to preserve, including human answerability and access to relevant grounds for reliance.
- **Design hypotheses:** arrangements expected to support those commitments, such as bounded permissions, discoverable source artifacts or independent examination.
- **Observations:** what use, testing and repository evidence establish about a particular arrangement.

Ontology, epistemology, praxeology and axiology supply questions about
distinctions, grounds, action and values, and these questions correct one
another. The literature informs possible responses, but it does not determine a
unique staffing chart, sequence of gates or file format.
[Appendix E](appendix_e_development_history.md) preserves the particular arrangements
explored during development.

## 2.1 AI Agent Architectures and Multi-Agent Systems

Agent research supplies methods for reasoning, planning, tool use and
coordination, and these capabilities can extend reckoning considerably.
Following the philosophical account developed in Chapter 3, *judgment* has the
more specific sense of situated, committed, world-involving thought that takes
responsibility for its objects. That human engagement shapes purpose, inquiry
and reliance throughout the work. It is not confined to a final approval, and
greater computational capability does not itself transfer it to a model.

### 2.1.1 Foundation Agent Patterns

Three sources together help explain how models became participants in extended
activities rather than generators of isolated answers. Wei et al.'s
chain-of-thought work demonstrated the value of intermediate reasoning examples
on selected reasoning tasks [1]. Yao et al.'s ReAct combined reasoning with
interaction through external tools [2]. Schick et al.'s Toolformer examined
learned API use [3].

The practical lesson for Chirality is to connect assessment and action to
inspectable inputs and outcomes. A model can select a tool, interpret its
response and revise its plan, and a deterministic tool can implement a
calculation or a validated application operation. But these contributions do not
make every generated explanation faithful, and a tool's successful execution
does not prove that it was the right operation for the work.

So permissions and side effects remain separate design concerns, and they must
be implemented where operations execute. No particular prompting pattern
establishes a security boundary, and Chirality does not assume access to a
model's private reasoning as an evidentiary requirement.

### 2.1.2 Multi-Agent Frameworks

AutoGen studies composition through conversations among agents and human proxies
[4]. MetaGPT applies software-engineering roles and standard procedures to
collaborative production [5]. LangGraph provides a stateful, graph-based
foundation for agent workflows [6]. Wang et al. offer a taxonomy of agent
modules and applications [7]. These works show several ways to arrange
contributions, and their different aims should not be treated as evidence that
they lack all forms of governance.

For Chirality, a useful distinction is between a responsibility and how it is
allocated. Purpose, design, production, integration and independent review can
be distinguished without assigning a separate agent to each. A single agent may
do much of the work. Multiple agents can contribute where their work can
usefully proceed in parallel. Where independent scrutiny is required, it needs a
distinct perspective on the result rather than an additional layer above every
action.

A reusable framework also does not determine whether a particular deployment has
appropriate permission controls, evidence access or human decisions, because
those properties depend on its configuration, application and use. So comparison
concerns observable arrangements and outcomes, not a blanket contrast between
others' capability and Chirality's governability.

### 2.1.3 Generative Agent Societies

Park et al.'s generative-agent experiment combined stored observations, retrieval, reflection and planning in a simulated social environment [8]. It demonstrated temporally extended and socially coordinated behaviour under the study's conditions. It did not establish professional reliability or prescribe a record policy for engineering work.

The relevant question is how an agent recovers useful context. Current artifacts,
selective tool queries, conversation and existing change history support continuity;
a replaceable recovery note is justified when those are insufficient. The literature
motivates retrieval and continuity. The representation must help a participant
understand and continue the work, with its synchronization and attention costs
included in the assessment.

### 2.1.4 Principle-Based Alignment

Constitutional AI uses stated principles in model critique and training [9]. It is relevant because it treats normative guidance as something that can shape behaviour, while leaving open the question of how a deployment checks particular actions.

Chirality's instructions likewise express commitments and methods. They should
not be described as hard constraints merely because they use mandatory language:
an instruction can be misunderstood or ignored. A host permission, validated
operation or operating-system boundary can, if correctly implemented, refuse a
specific action. Review can identify errors within the evidence it
examines. These mechanisms have different assurance properties, which must be
stated individually.

### 2.1.5 Hierarchical Agent Architectures

Delegation hierarchies are one response to complex work. The Self-Organized
Agents framework explores a mother–child arrangement for code generation [21].
Research on faulty contributors compares resilience under different coordination
arrangements [10]. Shavit et al. discuss practices for governing agentic
systems, including oversight and reversibility [11]. These sources support
considering structure, but they do not establish that any single hierarchy is
universally superior.

A later preprint by Kim et al., revised in April 2026, compared 260
configurations across six benchmarks. Benefits varied with task structure, model
capability and coordination overhead; performance on some sequential tasks
deteriorated under multi-agent arrangements [CITE:Kim2026Scaling]. This is
bounded experimental evidence, not a result about all professional work, but it
supports making delegation depend on the work and examining the cost of
coordination.

In Chirality, Agent 0 names responsibility for purpose and continuity with the owner. Other roles describe contributions available when needed. The chosen bounded TASK role does not delegate. That is an explicit framework choice, not a deduction from agent capability or a claim that every host has the same delegation limits.

### 2.1.6 Design Question: Capability, Authority and the Cost of Coordination

The literature makes three separations useful: what an agent can do, what an
assignment authorizes, and what a host permits. Role names can express
responsibility without granting or denying tool access by themselves. Work can
continue through ordinary repairs while decisions about commitments, acceptance
and release remain reserved.

Recent engineering guidance also treats scaffolding as open to revision.
OpenAI's September 2026 guidance recommends revisiting accumulated prompts and
skills, loading material selectively and avoiding unnecessary testing
instructions [CITE:OpenAI2026Prompts]. Anthropic's April 2026 account describes
harness assumptions becoming obsolete as model behaviour changes, and it
separates replaceable implementations from more durable interfaces
[CITE:Anthropic2026Managed]. These are supplier reports and recommendations, not
controlled evidence of Chirality's productivity, but they provide relevant
hypotheses to examine against Chirality's own history.

The resulting research question is not whether more or less orchestration is
always better, but which responsibilities, permissions and feedback arrangements
enable useful work under the conditions at hand, and whether their benefits
justify the attention, latency and integration costs they impose.

---

### References — Section 2.1

[1] J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. H. Chi, Q. V. Le, and D. Zhou, "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 35, New Orleans, LA, USA, 2022. [Online]. Available: https://arxiv.org/abs/2201.11903

[2] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao, "ReAct: Synergizing Reasoning and Acting in Language Models," in *Proc. 11th Int. Conf. Learning Representations (ICLR)*, Kigali, Rwanda, 2023. [Online]. Available: https://arxiv.org/abs/2210.03629

[3] T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, L. Zettlemoyer, N. Cancedda, and T. Scialom, "Toolformer: Language Models Can Teach Themselves to Use Tools," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 36, New Orleans, LA, USA, 2023. [Online]. Available: https://arxiv.org/abs/2302.04761

[4] Q. Wu, G. Bansal, J. Zhang, Y. Wu, B. Li, E. Zhu, L. Jiang, X. Zhang, S. Zhang, J. Liu, A. H. Awadallah, R. W. White, D. Burger, and C. Wang, "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation," in *Proc. First Conf. on Language Modeling (COLM 2024)*, 2024. [Online]. Available: https://arxiv.org/abs/2308.08155

[5] S. Hong, M. Zhuge, J. Chen, X. Zheng, Y. Cheng, C. Zhang, J. Wang, Z. Wang, S. K. S. Yau, Z. Lin, L. Zhou, C. Ran, L. Xiao, C. Wu, and J. Schmidhuber, "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework," in *Proc. 12th Int. Conf. Learning Representations (ICLR)*, Vienna, Austria, 2024. [Online]. Available: https://arxiv.org/abs/2308.00352

[6] LangChain Inc., "LangGraph: Build Resilient Language Agents as Graphs," open-source software library, 2024. [Online]. Available: https://github.com/langchain-ai/langgraph

[7] L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen, J. Tang, X. Chen, Y. Lin, W. X. Zhao, Z. Wei, and J.-R. Wen, "A Survey on Large Language Model based Autonomous Agents," *Frontiers of Computer Science*, vol. 18, no. 6, 2024. doi: 10.1007/s11704-024-40231-1. [Online]. Available: https://arxiv.org/abs/2308.11432

[8] J. S. Park, J. C. O'Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein, "Generative Agents: Interactive Simulacra of Human Behavior," in *Proc. 36th ACM Symp. User Interface Software and Technology (UIST)*, San Francisco, CA, USA, 2023, pp. 1–22. doi: 10.1145/3586183.3606763

[9] Y. Bai, S. Jones, K. Ndousse, A. Askell, A. Chen, N. DasSarma, D. Drain, S. Fort, D. Ganguli, T. Henighan, et al., "Constitutional AI: Harmlessness from AI Feedback," *arXiv preprint arXiv:2212.08073*, 2022. [Online]. Available: https://arxiv.org/abs/2212.08073

[10] J. Huang, J. Zhou, T. Jin, X. Zhou, Z. Chen, W. Wang, Y. Yuan, M. R. Lyu, and M. Sap, "On the Resilience of LLM-Based Multi-Agent Collaboration with Faulty Agents," *arXiv preprint arXiv:2408.00989*, 2024. [Online]. Available: https://arxiv.org/abs/2408.00989

[11] Y. Shavit, S. Agarwal, et al., "Practices for Governing Agentic AI Systems," OpenAI Technical Report, Dec. 2023. [Online]. Available: https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf

[21] Y. Ishibashi and Y. Nishimura, "Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization," *arXiv preprint arXiv:2404.02183*, 2024. [Online]. Available: https://arxiv.org/abs/2404.02183

---

## 2.2 LLM Reliability, Hallucination, and Trustworthiness

Reliability research concerns the relationship between generated material,
evidence and the world. It cautions against treating fluency as a warrant, but
it does not imply that all agent contributions require identical verification or
an attached metadata record for every sentence.

### 2.2.1 Hallucination: Definition and Taxonomy

Ji et al. review hallucination across natural-language generation tasks and distinguish source-contradicting from source-extrinsic content [12]. Huang et al. examine factuality and faithfulness in large language models [13]. Maynez et al.'s summarisation study shows that surface-similarity metrics can fail to track faithfulness to the input [14].

These distinctions matter in professional work. A statement can accurately
repeat a source whose assumptions do not fit the current case, and an inference
can be useful without appearing verbatim in a source. Conversely, a plausible
statement can be unsupported or contradicted. Evaluation must identify which
relationship is being claimed and examine the relevant evidence.

So Chirality keeps observation, inference, proposal and unresolved matter
distinct. It does not prohibit novel hypotheses or design, but it requires that
invention not be presented as an observed fact, established requirement or
accepted decision. The evidence needed, and how uncertainty is expressed, depend
on the claim and its intended use.

### 2.2.2 Factuality Evaluation

FActScore breaks generated text into atomic factual claims and evaluates whether
an external knowledge source supports them [15]. Its value is that it examines
text claim by claim, because a long answer can contain both supported and
unsupported material. Its reported results concern the evaluated
biography-generation tasks and models, not all model outputs.

A similar examination can be useful for claims that matter in an engineering
document, but it does not follow that all work must be transformed into an
atomic-claim database. Selection of claims, adequacy of sources, retrieval
failures and the meaning of support remain substantive problems. A citation
field can make a ground retrievable, but only examination can establish whether
that ground supports the claim in context.

### 2.2.3 Alignment and Mitigation Approaches

Ouyang et al.'s instruction-following work illustrates how human demonstrations and preferences can improve model behaviour [16]. Retrieval-augmented generation connects generation to external material [17]. Constitutional AI introduces principle-guided critique during training [9]. These approaches address different parts of the reliability problem and can be combined with application-level validation and review.

It is misleading to set model improvement against governance, as though one
reduces errors and the other necessarily detects all remaining errors. Better
models can improve the assessment of evidence, and better access to information
can prevent errors before generation. Independent examination can still share a
mistaken premise. A source can be stale or inapplicable even when retrieval and
citation work correctly.

Roles and workflows can support examination suited to the consequences at stake.
For a change to a solver, an independent numerical oracle may supply more useful
evidence than a second agent reading the same explanation. For an ambiguous
commitment, dialogue with the owner may be necessary. Whatever method is
selected needs grounds appropriate to the actual claim and possible failure.

### 2.2.4 Confidence Calibration

Guo et al. show that, in the neural networks they evaluated, predictive
confidence can differ from observed accuracy [18]. This motivates care when
interpreting confidence, though probability calibration in their setting is not
the same as a language model's verbal confidence.

Labels such as observation, inference or assumption describe a relationship to
evidence; they are not calibrated probabilities of correctness. A directly
quoted value can be wrong in its source; a carefully supported inference can be
reliable. The framework should show material uncertainty and the grounds for
assessment without turning a derivation label into a certificate of truth.

### 2.2.5 Trustworthiness Frameworks

NIST's AI Risk Management Framework supplies a vocabulary for reliability,
safety, transparency, accountability and other concerns, organised around
Govern, Map, Measure and Manage [19]. It is a resource for asking whether a
deployment's risks are understood and addressed. A local implementation can
support some of those concerns without being an implementation or certification
of the whole framework.

The EU AI Act is included as a historical regulatory source relevant to
transparency and human oversight [20]. Its duties depend on applicability,
system category, actor and implementation dates. This chapter does not classify
Chirality or claim compliance. An architecture's evidence access and permission
controls may be relevant to an assessment, but their existence does not
establish the legal result.

Trustworthiness also includes the conditions under which people can use the
controls effectively. Excessive reports and routine approval demands can obscure
the few matters that need attention. Their cost belongs in the evaluation,
alongside the failures they are intended to detect.

### 2.2.6 Design Question: Useful Evidence at the Point of Reliance

The reviewed methods support improving models, grounding particular claims,
checking behaviour and examining outcomes, but they leave a practical question
for each piece of work: what evidence must be available for the intended use,
and how can a person or another contributor inspect it without reconstructing
the whole project?

The current design hypothesis is that relevant source artifacts, conditions,
calculation or test results and meaningful uncertainty should be discoverable
together. Existing artifacts and change history can supply this information.
Additional records are justified when a consumer, acceptance requirement or
recovery need requires them.

This approach does not make every error detectable; it aims to make the grounds
and limits of claims that matter easier to examine. Whether it is adequate must
be evaluated through the failures found and missed under it, recovery and the
cost it imposes on actual work.

---

### References — Section 2.2

[12] Z. Ji, N. Lee, R. Frieske, T. Yu, D. Su, Y. Xu, E. Ishii, Y. J. Bang, A. Madotto, and P. Fung, "Survey of Hallucination in Natural Language Generation," *ACM Computing Surveys*, vol. 55, no. 12, article no. 248, Mar. 2023. doi: 10.1145/3571730

[13] L. Huang, W. Yu, W. Ma, W. Zhong, Z. Feng, H. Wang, Q. Chen, W. Peng, X. Feng, B. Qin, and T. Liu, "A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions," *ACM Transactions on Information Systems*, vol. 43, no. 2, pp. 1–55, 2025. doi: 10.1145/3703155. [Online]. Available: https://arxiv.org/abs/2311.05232

[14] J. Maynez, S. Narayan, B. Bohnet, and R. McDonald, "On Faithfulness and Factuality in Abstractive Summarization," in *Proc. 58th Annual Meeting of the Association for Computational Linguistics (ACL)*, Online, 2020, pp. 1906–1919. doi: 10.18653/v1/2020.acl-main.173

[15] S. Min, K. Krishna, X. Lyu, M. Lewis, W.-T. Yih, P. W. Koh, M. Iyyer, L. Zettlemoyer, and H. Hajishirzi, "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation," in *Proc. 2023 Conf. Empirical Methods in Natural Language Processing (EMNLP)*, Singapore, 2023, pp. 12076–12100. [Online]. Available: https://arxiv.org/abs/2305.14251

[16] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton, F. Kelton, L. Miller, M. Simens, A. Askell, P. Welinder, P. Christiano, J. Leike, and R. Lowe, "Training Language Models to Follow Instructions with Human Feedback," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 35, New Orleans, LA, USA, 2022. [Online]. Available: https://arxiv.org/abs/2203.02155

[17] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W.-T. Yih, T. Rocktäschel, S. Riedel, and D. Kiela, "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 33, Virtual, 2020, pp. 9459–9474. [Online]. Available: https://arxiv.org/abs/2005.11401

[18] C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger, "On Calibration of Modern Neural Networks," in *Proc. 34th Int. Conf. Machine Learning (ICML)*, Sydney, Australia, 2017, pp. 1321–1330. [Online]. Available: https://proceedings.mlr.press/v70/guo17a.html

[19] National Institute of Standards and Technology (NIST), "Artificial Intelligence Risk Management Framework (AI RMF 1.0)," NIST AI 100-1, Gaithersburg, MD, USA, Jan. 2023. doi: 10.6028/NIST.AI.100-1. [Online]. Available: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf

[20] European Parliament and the Council of the European Union, "Regulation (EU) 2024/1689 of the European Parliament and of the Council laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)," *Official Journal of the European Union*, L Series, 2024. [Online]. Available: https://eur-lex.europa.eu/

[9] Y. Bai, S. Jones, K. Ndousse, A. Askell, A. Chen, N. DasSarma, D. Drain, S. Fort, D. Ganguli, T. Henighan, et al., "Constitutional AI: Harmlessness from AI Feedback," *arXiv preprint arXiv:2212.08073*, 2022. [Online]. Available: https://arxiv.org/abs/2212.08073

---

## 2.3 Formal Methods and Safety-Critical Systems Engineering

Formal methods and safety engineering provide resources for specifying
behaviour, identifying hazards and examining containment. Using them requires a
defined model and assumptions. Neither a familiar notation nor a strong
instruction gives an agent system the assurance of a verified safety-critical
implementation.

### 2.3.1 Safety Engineering Foundations: System-Theoretic Accident Models

Leveson's STAMP and STPA treat safety as a system-level control problem, including interactions that cannot be understood from component reliability alone [1]. This perspective is useful when an agent, tool, interface and person can each perform their local task while their combined activity produces an unsafe result.

For Chirality, this perspective motivates asking which actions, omissions,
timing errors or misunderstandings could produce harm. The answer can inform a
refusal condition, review, interface design or operating limit. Naming
constraints does not demonstrate that STPA has been performed or that the
resulting system is safe.

### 2.3.2 Avionics Software Assurance: DO-178C

DO-178C provides a software-assurance framework for airborne systems [2]. It is
relevant here for its disciplined connection between requirements,
implementation and verification evidence, with assurance related to how
significant a failure would be.

For Chirality, this tradition motivates identifying required product behaviour
and the evidence needed to examine it. Current commitments and checks appropriate
to a change serve those questions. This is neither a DO-178C process nor an
equivalent assurance argument; that claim would require its own applicable basis.

Software levels and agent roles are also different kinds of classification.
Assigning Agent 0, manager or TASK responsibility does not establish a safety
level or determine which writes a contributor is permitted to make.

### 2.3.3 Functional Safety: IEC 61508 and Safety Integrity Levels

IEC 61508 is a reference for the treatment of functional safety and systematic software failures [3]. It supports attention to consequence, specification, verification and the limitations of claims based on component performance. The thesis borrows those questions without claiming conformity to the standard.

Instructions, prompts, runtime checks and human examination should not
automatically be counted as independent protection layers, because they may
share sources, assumptions and failure modes. If a design relies on independent
protection, it needs an argument for the relevant independence and evidence that
the mechanism works within the claimed scope. Repeating the same rule at several
levels supplies no such argument by itself.

### 2.3.4 Partitioning and Fault Containment: Rushby on Avionics Architectures

Rushby's work examines the requirements, mechanisms and assurance of partitioning in integrated avionics [4]. It gives a useful distinction between a component's behaviour and a boundary that contains the effects of its failure.

Applied cautiously to agents, this directs attention to the host, filesystem
permissions, process isolation and validated application operations. A prompt
telling an agent to stay within a write scope is guidance; it is not equivalent
to spatial partitioning. An enforced boundary can refuse an out-of-scope action
only to the extent that the boundary itself is correctly implemented and the
relevant paths pass through it.

So the current Chirality distinction is responsibility through roles,
authorization through the assignment, and executable limits through the host and
tools. A read-only assignment remains read-only; a role concerned with
continuity can write when authorized. Those arrangements need boundary tests
rather than assertions that an agent cannot escape through reasoning.

### 2.3.5 Formal Verification in Safety-Critical Domains

Hoare logic relates program actions to preconditions and postconditions [5]. Model checking explores a specified transition system against properties [6]. The NASA Formal Methods proceedings contain applications and developments in such techniques [7]. TLA+ provides a language and method for specifying concurrent systems [8]. These approaches are relevant to application state transitions, permission handling, persistence and recovery.

Their scope is not restricted to deterministic algorithms: formal models can
represent nondeterministic choices, and probabilistic verification is possible
under suitable assumptions. The difficulty for an open-ended agent is obtaining
a tractable model that captures the property of interest and its environment. A
natural-language lifecycle diagram is not a formal verification result.
Likewise, model checking a bounded tool protocol does not verify all the
semantic consequences of how an agent uses it.

Smith's *The Limits of Correctness* distinguishes the relationship established
between program and specification from the specification's relationship to the
world [25]. MacKenzie's history of mechanised proof examines the human practices
through which proof and assurance gain authority [26]. These sources set
important limits on the thesis's own claims. A verified operation can still
implement an inadequate model; a person must consider whether its assumptions
fit the work.

### 2.3.6 Formal Methods and AI Safety

Hou et al. argue for combining language models with formal methods rather than expecting either to provide sufficient assurance alone [9]. The cited review of safety-critical machine learning examines verification methods and their scope [10]. Xu et al.'s governance-first proposal represents another attempt to make constraints explicit in agent engineering [11]. These are different approaches to a shared problem, not evidence that no prior approach exists.

The useful application is local and stated precisely: a schema can reject
malformed input; an operation can enforce a precondition; a permission check can
reject an unauthorized target; a recovery protocol can prevent a demonstrated
duplicate action. Whether those mechanisms combine into a sufficient argument
for the actual work remains to be established.

### 2.3.7 Design Question: What Is Enforced, and What Remains to Be Judged?

For each claimed control, Chirality must distinguish four things:

1. The commitment or property being sought.
2. The instruction, tool, host boundary or human act intended to support it.
3. The evidence that the mechanism works under stated conditions.
4. The assumptions and failures outside that evidence.

This is a bounded use of the verification tradition. It does not claim to govern
arbitrary model behaviour through invariants written in prose, or to make
professional responsibility a property of software. It also permits a control to
be replaced when another arrangement serves its purpose more effectively.

## 2.4 Professional Engineering Regulation and AI

This section preserves the regulatory setting that motivated the research. It is
a selective interpretation of the cited editions and dated guidance, not a
current compliance checklist, legal opinion or certification of Chirality.
Provincial regulation, national professional positions, international standards
and government policy have different force and scope, so they must not be
combined into a universal rule of liability or authentication.

### 2.4.1 APEGA: The Primary Regulatory Context

The Alberta setting makes APEGA's practice standards relevant to the study. *Relying on the Work of Others and Outsourcing* and *Authenticating Professional Work Products* informed the questions about evidence, supervision and responsibility [12][13]. Applying either standard to a particular product or use requires its actual terms and the circumstances, not a correspondence table alone.

APEGA's March 23, 2026 notice states that professionals using AI remain
responsible for their work and must have the competence to assess AI risks,
limitations and results. It treats the accuracy and appropriateness of AI
results as a due-diligence matter, and connects use in professional work
products to its authentication and validation standard [24]. This supports
designing for meaningful examination of results, but the notice does not
classify an AI agent as a licensed delegate or endorse a particular software
architecture.

Chirality reserves professional authentication for the appropriate person. The
software can distinguish a proposal from an applied operation or record an
attributable decision, but it cannot establish that the person's examination was
sufficient or make the content true by recording approval. Human judgment also
informs the problem, assumptions and consequences before authentication is
considered.

### 2.4.2 Engineers and Geoscientists British Columbia

The cited November 2024 EGBC advisory discusses AI use in professional practice,
including competence, automation bias, checking, supervision and review [14].
This study uses it to identify questions a useful system should help a
professional address.

A workflow may make relevant evidence available and prevent specified
unauthorized actions, but it cannot ensure meaningful supervision merely by
requiring an approval click. Whether an arrangement supports professional
practice depends on what the person can inspect and understand, and on how the
work is actually done.

### 2.4.3 Professional Engineers Ontario

The earlier review consulted PEO's practice-resource collection and its reference to the EGBC material [15]. That historical search is not a finding that no Ontario-specific guidance exists at the time of every later revision.

The methodological point is that applicability must be established in the jurisdiction and use at issue. A framework intended to transfer between applications should make the relevant requirements discoverable without presenting one province's interpretation as a universal technical contract.

### 2.4.4 Engineers Canada: National Framework

Engineers Canada's position on artificial intelligence, machine learning and
data science places these technologies within competent professional work in the
public interest [16]. National position statements contribute policy context,
while provincial and territorial regulation governs the details of professional
practice.

For the thesis, the relevant design concern is how a person can examine a result and the grounds on which it is used. This does not establish that every engineering application needs the same review workflow, records or authentication operation.

### 2.4.5 American Professional Engineering Positions

NSPE Position Statement 03-1774, revised February 2026, argues for professional standards in AI systems affecting public safety and addresses verification, transparency and accountability [17]. Its Board of Ethical Review supplies a separate case-based resource [23]. ASCE Policy Statement 573 addresses professional judgment and engineering responsibility in AI use [18].

These are professional positions and ethical resources, and their legal force is
not interchangeable with that of a state licensing board. They motivate
competent examination and attention to consequences, but they do not prove that
Chirality or any particular gate structure satisfies an applicable requirement.

### 2.4.6 International Frameworks

Engineers Australia's cited ethics guidance and the United Kingdom's February
2024 guidance to regulators provide broader context [19][20]. Their audiences
and purposes differ. This revision does not infer from earlier searches that
AI-specific guidance is still absent, and it does not treat a government's
advice to regulators as imposing the same duty on every practitioner.

The transfer question for Chirality is practical: can a new application identify its actual obligations, represent the relevant objects and provide suitable evidence and action boundaries? Transfer requires contextual interpretation, not a universal compliance template.

### 2.4.7 Academic Literature: Regulation and Accountability

The cited work on AI regulation and risk governance examines tensions among
innovation, institutional responsibilities and practical accountability
[21][22]. Such work helps explain why stating an obligation does not specify
every means of fulfilling it, but such work does not establish that there is a single
missing architectural solution.

So the thesis's own contribution must stay narrower: it proposes and examines
arrangements that may support accountable reliance. The assessment should
include whether the person can understand and intervene, which errors and
uncertainty are made visible, and the attention and delay that the controls
consume.

### 2.4.8 Design Question: Supporting Professional Obligations

The regulatory sources motivate competent use, examination appropriate to the
work, and human professional responsibility. Specific obligations still depend
on the source and the jurisdiction.

A design can support these concerns by preserving the identity of the work,
making relevant evidence available, distinguishing proposed from applied changes
and keeping reserved decisions attributable. A source link, permission check or
approval record contributes to that support, but none makes professional
compliance an architectural property that is satisfied automatically.

The research question is whether the arrangements make professional examination practicable and effective in use. Chapters 6 and 8 must distinguish a proposed mapping, an implemented control and observed practice rather than treat them as equivalent evidence.

---

### References — Sections 2.3 and 2.4

[1] N. G. Leveson, *Engineering a Safer World: Systems Thinking Applied to Safety*. Cambridge, MA: MIT Press, 2011. [Online]. Available: https://direct.mit.edu/books/oa-monograph/2908/Engineering-a-Safer-WorldSystems-Thinking-Applied. ISBN: 9780262533690.

[2] RTCA, Inc. / EUROCAE, *DO-178C: Software Considerations in Airborne Systems and Equipment Certification*. Washington, DC: RTCA, Inc., Dec. 2011. [Also published as EUROCAE ED-12C.]

[3] International Electrotechnical Commission, *IEC 61508: Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems*, Parts 1–7, 2nd ed. Geneva: IEC, 2010.

[4] J. Rushby, "Partitioning in Avionics Architectures: Requirements, Mechanisms, and Assurance," NASA Contractor Report CR-1999-209347, Computer Science Laboratory, SRI International, Menlo Park, CA, Jun. 1999. [Online]. Available: https://ntrs.nasa.gov/api/citations/19990052867/downloads/19990052867.pdf.

[5] C. A. R. Hoare, "An Axiomatic Basis for Computer Programming," *Communications of the ACM*, vol. 12, no. 10, pp. 576–580, Oct. 1969. DOI: 10.1145/363235.363259.

[6] E. M. Clarke, O. Grumberg, and D. Peled, *Model Checking*. Cambridge, MA: MIT Press, 1999. ISBN: 9780262032704.

[7] NASA Langley Research Center, "NASA Formal Methods Symposium (NFM) Proceedings Series," published annually since 2009 in Springer *Lecture Notes in Computer Science*. Most recent: NFM 2024 (16th), Moffett Field, CA, Jun. 2024. DOI: 10.1007/978-3-031-60698-4.

[8] L. Lamport, *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers*. Boston, MA: Addison-Wesley, 2002. [Online]. Available: https://lamport.azurewebsites.net/tla/book.html. ISBN: 9780321143068.

[9] Z. Hou et al., "Position: Trustworthy AI Agents Require the Integration of Large Language Models and Formal Methods," in *Proc. 42nd Int. Conf. on Machine Learning (ICML 2025)*, Vancouver, Canada, Jul. 2025. [Online]. Available: https://zhehou.github.io/papers/Position-Trustworthy-AI-Agents-Require-the-Integration-of-Large-Language-Models-and-Formal-Methods.pdf.

[10] A. Newcomb and O. Ochoa, "Formal Methods for Safety-Critical Machine Learning: A Systematic Literature Review," *Frontiers in Artificial Intelligence*, vol. 9, article 1749956, 2026. DOI: 10.3389/frai.2026.1749956.

[11] Q. Xu, X. Wen, C. Xu, Z. Li, and J. Zhong, "From Craft to Constitution: A Governance-First Paradigm for Principled Agent Engineering," arXiv preprint arXiv:2510.13857, Oct. 2025. [Online]. Available: https://arxiv.org/abs/2510.13857.

[12] Association of Professional Engineers and Geoscientists of Alberta (APEGA), *Relying on the Work of Others and Outsourcing*, Practice Standard, v4.0. Edmonton, AB: APEGA, May 2021 (enforceable May 2022). [Online]. Available: https://www.apega.ca/docs/default-source/pdfs/standards-guidelines/relying-on-the-work-of-others-and-outsourcing.pdf.

[13] Association of Professional Engineers and Geoscientists of Alberta (APEGA), *Authenticating Professional Work Products*, Practice Standard, revised ed. Edmonton, AB: APEGA, Nov. 1, 2024. [Online]. Available: https://www.apega.ca/docs/default-source/pdfs/standards-guidelines/authenticating-professional-work-products.pdf.

[14] Engineers and Geoscientists British Columbia (EGBC), *Use of Artificial Intelligence (AI) in Professional Practice*, Practice Advisory. Burnaby, BC: EGBC, Nov. 22, 2024. [Online]. Available: https://tools.egbc.ca/registrants/practice-resources/guidelines-advisories/Document/01525AMWZDBFA4VTKQBRHJXVI6AR4UUFGV/Use%20of%20Artificial%20Intelligence%20in%20Professional%20Work.

[15] Professional Engineers Ontario (PEO), "Knowledge Centre — Practice Advice Resources and Guidelines," Toronto, ON: PEO, 2025. [Online]. Available: https://www.peo.on.ca/knowledge-centre/practice-advice-resources-and-guidelines/practice-guidelines. [Note: PEO references EGBC advisory; no Ontario-specific AI guideline issued as of Mar. 2026.]

[16] Engineers Canada, "Artificial Intelligence, Machine Learning, and Data Science," National Position Statement, Ottawa, ON: Engineers Canada, Mar. 2026. [Online]. Available: https://engineerscanada.ca/public-policy/national-position-statements

[17] National Society of Professional Engineers (NSPE), "Artificial Intelligence," Position Statement No. 03-1774, Alexandria, VA: NSPE, adopted Sep. 2023, latest revision Feb. 2026. [Online]. Available: https://www.nspe.org/nspe-advocacy/explore-issues/professional-policies-and-position-statements/artificial-intelligence.

[18] American Society of Civil Engineers (ASCE), "Policy Statement 573 — Artificial Intelligence and Engineering Responsibility," Reston, VA: ASCE, adopted Jul. 18, 2024. [Online]. Available: https://www.asce.org/advocacy/policy-statements/ps573---artificial-intelligence-and-engineering-responsibility.

[19] Engineers Australia, *Code of Ethics and Guidelines on Professional Conduct*. Canberra, ACT: Engineers Australia, 2022. [Online]. Available: https://www.engineersaustralia.org.au/about-us/professional-standards-framework. [Note: no normative AI practice standard as of Jul. 2026; see also Institution of Engineers Australia, "The impact of AI and generative technologies on the engineering profession," research report, Jan. 2025, ISBN 978-1-925627-92-3.]

[20] Department for Science, Innovation and Technology (UK), *Implementing the UK's AI Regulatory Principles: Initial Guidance for Regulators*, UK Government, London: DSIT, Feb. 2024. [Online]. Available: https://assets.publishing.service.gov.uk/media/65c0b6bd63a23d0013c821a0/implementing_the_uk_ai_regulatory_principles_guidance_for_regulators.pdf.

[21] G. Perboli, N. Simionato, and S. Pratali, "Navigating the AI Regulatory Landscape: Balancing Innovation, Ethics, and Global Governance," *Economic and Political Studies*, vol. 13, no. 4, pp. 367–397, 2025. DOI: 10.1080/20954816.2025.2569584.

[22] E. Hohma, A. Boch, R. Trauth, and C. Lütge, "Investigating Accountability for Artificial Intelligence Through Risk Governance: A Workshop-Based Exploratory Study," *Frontiers in Psychology*, vol. 14, article 1073686, 2023. DOI: 10.3389/fpsyg.2023.1073686. PMC9905430.

[23] National Society of Professional Engineers (NSPE), "Use of Artificial Intelligence in Engineering Practice," Board of Ethical Review Case, Alexandria, VA: NSPE, 2024. [Online]. Available: https://www.nspe.org/career-growth/ethics/board-ethical-review-cases/use-artificial-intelligence-engineering-practice.

[24] Association of Professional Engineers and Geoscientists of Alberta (APEGA), "Guidance for Registrants Regarding the Use of Artificial Intelligence Tools," Edmonton, AB: APEGA, first published Jul. 2025, updated Mar. 23, 2026. [Online]. Available: https://www.apega.ca/news/2026/03/23/guidance-for-registrants-regarding-the-use-of-artificial-intelligence-tools

[25] B. C. Smith, "The Limits of Correctness," *ACM SIGCAS Computers and Society*, vol. 14–15, no. 1–4, pp. 18–26, Jan. 1985. doi: 10.1145/379486.379512

[26] D. MacKenzie, *Mechanizing Proof: Computing, Risk, and Trust*. Cambridge, MA, USA: MIT Press, 2001. ISBN: 978-0-262-13393-7.

---

## 2.5 Epistemic Frameworks and Knowledge Engineering

Provenance, representation and social epistemology help explain what a system can make inspectable and what remains beyond a record. The review treats them as resources for asking better questions about work, not as independent proofs of a universal set of agent invariants.

Naur's account of programming as theory building argues that code and
documentation do not exhaust the understanding held by a programme's
builders [13]. Collins distinguishes several forms of tacit knowledge, including
the collectively acquired understanding associated with participation in a
practice [14]. These accounts do not make documentation futile, but they limit
the claim that copying or completing the record reproduces the understanding
needed to continue the work.

Smith's reckoning/judgment distinction develops that limit in the thesis's
chosen vocabulary [CITE:Smith2019]. Reckoning can include sophisticated
interpretation, analysis, planning, evaluation and adaptive action. Judgment is
situated, committed engagement with the world and with what a person will stand
behind. It shapes the inquiry and the significance of its results throughout. A final
approval is one possible expression of that engagement, not its definition or an
adequate substitute for it.

### 2.5.1 Provenance Standards: W3C PROV

PROV-DM supplies a model for describing entities, activities, agents and derivations [1]. The PROV family includes representations and interchange mechanisms for such information [2]. These resources make it possible to ask where something came from and which activities contributed to it.

**Relation to Chirality.** A result that matters may need a retrievable source,
calculation basis or identified revision. Current source artifacts and their
existing change history can supply much of this. Historical `Dependencies.csv`
columns and mandatory provenance tables were implementation choices. The
presence of a few source fields did not establish formal equivalence with PROV
or prove that the recorded relationships were true. New provenance records are
useful where they answer an actual review, use or recovery need.

### 2.5.2 Database Provenance: Why, How, and Where

Buneman, Khanna and Tan distinguish why- and where-provenance in data processing [3]. Cheney, Chiticariu and Tan survey derivation, location and related forms of provenance [4]. Their formal accounts concern computations with defined semantics.

**Relation to Chirality.** These distinctions help separate a pointer to a
source from an explanation of how a conclusion follows. A quote does not
necessarily provide why-provenance in the formal database sense, and a human or
agent inference is not automatically a specified query. A useful record may need
both location and argument. Where a dependency condition has not been resolved,
a tool should report the uncertainty rather than invent a supporting path or
infer from presence alone that the condition is satisfied.

### 2.5.3 Knowledge Representation Foundations

Sowa connects logic, ontology, language and computational representation [5].
The selected representation makes some distinctions available to reasoning and
leaves others difficult or invisible. So formal consistency is not enough when
the representation misstates or leaves out a relevant domain distinction.

**Relation to Chirality.** Requirements, observations, assumptions, proposed
operations, results and acceptances are different objects or acts in the work.
Labels can help distinguish them, but a universal label taxonomy is not the only
method. A claim described as fact can still be wrong, and a model declared
schema-valid can still be inappropriate. Representation should help participants
find and examine those possibilities rather than encourage reliance on the label
itself.

### 2.5.4 Ontological Foundations: The Bunge–Wand–Weber Framework

Wand and Weber apply Bunge's ontology to information-system representation and decomposition [6][7]. Their work supports examining how a modelling grammar represents a domain and where its constructs introduce ambiguity or omit distinctions.

**Relation to Chirality.** The work must be distinguished from its
representations. A dependency is a need between contributions; a declared row
represents it. A deliverable is an intended work product; its folder is a
working home. A graph is a view of selected relationships, not proof that every
relevant dependency has been captured.

The old thesis's stronger claim that no construct may exist for system
convenience was unwarranted. Locks, caches and temporary files can be useful
implementation objects, but they need a clear purpose and must not quietly gain
domain authority. Likewise, a filesystem can be the authoritative location for
project declarations without being identical to the physical or organisational
state those declarations describe.

### 2.5.5 Social Epistemology: Goldman's Framework

Goldman examines the processes by which beliefs are formed and the social arrangements that can support or undermine epistemic performance [8][9]. This extends attention beyond an isolated assertion to testimony, disagreement, institutions and the quality of inquiry.

**Relation to Chirality.** A professional examines both a particular claim and
the processes that produced it. A contributor who raises a relevant disagreement
supplies information the work needs. Suppressing disagreement to produce a clean
result damages that examination.

This does not require a standing conflict register. A material conflict can be
exposed where it affects the work, investigated, and resolved within authority;
the current governing text and existing change record can preserve its
consequence. Nor does the framework adopt Goldman's factive account as its own
definition of knowing. The framework's account of a situated knower permits
mistake and revision, as Chapter 3 explains.

### 2.5.6 Epistemic Logic in Distributed Systems

Halpern and Moses analyse knowledge and common knowledge in distributed environments, with results that depend on assumptions about communication and time [10]. The work cautions against assuming that participants share information merely because a message was sent or a local state changed.

**Relation to Chirality.** Contributors can work from different revisions and receive different evidence. Making the observed basis explicit and querying current relationships can expose relevant divergence. A coordinator must examine how returns fit together. The theory does not imply that a particular Conflict Table is necessary, or that agreement establishes correctness. Several contributors can share the same mistaken premise.

### 2.5.7 Trust Conditions and Epistemic Governance

Jacovi et al. analyse trust in relation to specified contracts and distinguish trust from trustworthiness [11]. The practical implication is to identify what a user is relying on and the conditions under which that reliance would be appropriate. Natangelo's CUL/TCL preprint proposes an external arrangement for verification and claim status [12]. It is a related design proposal, not evidence of a settled consensus or a complete solution.

**Relation to Chirality.** A professional may need to inspect a source,
reproduce a calculation, understand a limitation or examine a refusal. Different
claims require different evidence. A format can expose a missing field and an
executable check can reject a defined violation, but neither can guarantee that
all suppressed conflicts have been detected or that all recorded sources support
their claims. Appropriate reliance requires attention to those limits.

### 2.5.8 Design Question: Inspectable Grounds Without Exhaustive Records

The reviewed work supports provenance, disciplined representation, attention to
social processes and explicit limits on what records carry, but it does not
establish that mandatory per-claim labels, append registers or a universal
record of every agent action are necessary.

Chirality's revised hypothesis is that participants can work more effectively
when current commitments, relevant grounds and unresolved conditions are
accessible in the artifacts they use. Tools can derive useful views from those
declarations. Further records need a concrete consumer or consequence.
Machine-generated execution history can remain valuable for diagnosis and
recovery, but that function differs from requiring agents to write repeated
summaries of the same work.

The four philosophical perspectives correct one another here. Ontology asks
whether the right distinctions are represented. Epistemology asks what supports
a claim and what remains uncertain. Praxeology asks whether participants can
act, integrate, repair and recover. Axiology asks whether the result and its
controls serve the values of the work at an acceptable cost. Experience can
require revising any of the answers.

This is a bounded contribution. Improving access to evidence may help expose
error, but it does not guarantee that error can be detected. A useful
representation may assist reckoning, but it does not carry the person's situated
judgment. These limits are part of the design account, not defects to hide with
additional metadata.

---

### References — Section 2.5

[1] L. Moreau and P. Missier, Eds., "PROV-DM: The PROV Data Model," W3C Recommendation, World Wide Web Consortium, 30 Apr. 2013. [Online]. Available: https://www.w3.org/TR/2013/REC-prov-dm-20130430/

[2] L. Moreau and P. Missier, Eds., "PROV-Overview: An Overview of the PROV Family of Documents," W3C Working Group Note, World Wide Web Consortium, 30 Apr. 2013. [Online]. Available: https://www.w3.org/TR/prov-overview/

[3] P. Buneman, S. Khanna, and W.-C. Tan, "Why and Where: A Characterization of Data Provenance," in *Proc. 8th Int. Conf. Database Theory (ICDT 2001)*, London, UK, Jan. 2001, pp. 316–330, Lecture Notes in Computer Science, vol. 1973. doi: 10.1007/3-540-44503-X_20

[4] J. Cheney, L. Chiticariu, and W.-C. Tan, "Provenance in Databases: Why, How, and Where," *Foundations and Trends in Databases*, vol. 1, no. 4, pp. 379–474, 2009. doi: 10.1561/1900000006

[5] J. F. Sowa, *Knowledge Representation: Logical, Philosophical, and Computational Foundations*. Pacific Grove, CA, USA: Brooks/Cole, 2000, ISBN: 0-534-94965-7.

[6] Y. Wand and R. Weber, "An Ontological Model of an Information System," *IEEE Trans. Softw. Eng.*, vol. 16, no. 11, pp. 1282–1292, Nov. 1990. doi: 10.1109/32.60316

[7] Y. Wand and R. Weber, "On the Deep Structure of Information Systems," *Inf. Syst. J.*, vol. 5, no. 3, pp. 203–223, 1995. doi: 10.1111/j.1365-2575.1995.tb00108.x

[8] A. I. Goldman, *Epistemology and Cognition*. Cambridge, MA, USA: Harvard University Press, 1986. ISBN: 978-0-674-25895-2.

[9] A. I. Goldman, *Knowledge in a Social World*. Oxford, UK: Clarendon Press, 1999. ISBN: 978-0-198-23777-8.

[10] J. Y. Halpern and Y. Moses, "Knowledge and Common Knowledge in a Distributed Environment," *J. ACM*, vol. 37, no. 3, pp. 549–587, Jul. 1990. doi: 10.1145/79147.79161

[11] A. Jacovi, A. Marasović, T. Miller, and Y. Goldberg, "Formalizing Trust in Artificial Intelligence: Prerequisites, Causes and Goals of Human Trust in AI," in *Proc. 2021 ACM Conf. Fairness, Accountability, and Transparency (FAccT '21)*, Virtual Event, Canada, Mar. 2021, pp. 624–635. doi: 10.1145/3442188.3445923

[12] S. Natangelo, "Externalising Epistemic Governance for Stateless Large Language Models: The CUL/TCL Architecture," Zenodo preprint, Dec. 16, 2025. doi: 10.5281/zenodo.17953956

[13] P. Naur, "Programming as Theory Building," *Microprocessing and Microprogramming*, vol. 15, no. 5, pp. 253–261, May 1985. doi: 10.1016/0165-6074(85)90032-8

[14] H. Collins, *Tacit and Explicit Knowledge*. Chicago, IL, USA: University of Chicago Press, 2010. ISBN: 978-0-226-11380-7.

---

## 2.6 Synthesis: A Bounded Contribution to Accountable Work

The five domains supply complementary questions and methods, but they do not
establish that Chirality is the first complete governance architecture, or that
one arrangement follows necessarily from the literature.

| Domain | Resource for the design | Question left to the undertaking |
|---|---|---|
| Agent architectures | Reasoning, tool use, delegation and coordination methods | Which arrangement enables useful work at acceptable cost? |
| Model reliability | Grounding, evaluation, calibration and behavioural checks | What supports this particular claim or result in context? |
| Formal methods and safety engineering | Specification, containment, hazard analysis and bounded verification | What is actually enforced, under which assumptions? |
| Professional regulation | Source-specific obligations and responsibility boundaries | What must the accountable person establish for this use? |
| Epistemic frameworks | Provenance, representation, social inquiry and limits of records | What can be made inspectable, and what still requires situated judgment? |

The enduring proposition is that purposeful agent-assisted work benefits from
understandable objects and relationships, inspectable grounds and limits,
practicable action and correction, and attributable consequential commitments. The
thesis chooses these as normative commitments. Discoverable current artifacts,
selectively loaded methods, coherent ownership, host-enforced permissions and
verification proportionate to consequence are design hypotheses for supporting
them.

The repository supplies substantial longitudinal case evidence of useful
production and preservation of meaning through redevelopment. Chapter 8 traces
that result from working predecessor behavior through successor definition and
deliverables to observed use of the rebuilt App, with functional extensions and
repairs. Human purpose, judgment and steering are foundational to the method
being examined. Comparative productivity, professional compliance and outcomes
in additional teams remain separate questions.
[Appendix E](appendix_e_development_history.md) preserves the history and
distinguishes observed results from broader causal comparisons.

So the following chapters examine how the philosophical account informs designs
that are open to revision, what the implementation enforces, what the case
history shows, and what remains to be established. The framework's own claims
are subject to the same discipline: commitments must be stated, hypotheses may
fail, and observations must not be promoted beyond their evidence.
