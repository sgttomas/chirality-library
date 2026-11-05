# Product boundaries

These existing product commitments remain applicable to their adopted consumers.
They do not reinstate development gates or record duties. Repository work follows
[AGENTS.md](../AGENTS.md); product acceptance remains with the owner.

Applicability follows the identified consumer and its adopted source basis.
Reading this catalog does not adopt every product contract, transfer Root's
repository authority, or amend an earlier adoption. The invariant tables retain
their original meanings and enforcement descriptions; those descriptions are
not evidence that a current host implements the mechanisms. Current behavior
and named-consumer compatibility require evidence for that implementation.

## Professional accountability

Professional accountability requires identifying what exists, what is warranted,
how the work was performed, and the values governing decisions. Agent output is
structured assistance, not professional approval. A licensed professional retains
scope, code/design-basis, hazard/risk, conflict-adjudication and issuance decisions.
No AI system may certify, approve, sign, seal or issue engineering work for reliance.
An engineer must be competent to verify the work and the tools they use.
Laws/regulations, applicable codes/standards and approved project specifications
precede analysis and professional judgment; agent output carries no independent
professional authority.

## Retained invariant identifiers

The following original definitions remain references for adopted product consumers.
They do not restore repository procedures superseded by AGENTS.md. In particular,
K-WRITE-1 describes the legacy product's declared write scope, not a requirement
for new development header records. K-PROV-1's legacy CSV fields are documented
in [Compatibility formats](COMPATIBILITY_FORMATS.md#legacy-dependency-csv).

| ID | Invariant | Enforcement |
|---|---|---|
| **K-AUTH-1** | Only **humans** author binding approval records. No agent may claim to certify, approve, sign, seal, or issue work for reliance. | Agent instruction constraints; human review |
| **K-AUTH-2** | Approvals bind to a **specific git SHA**. Content change after approval voids the approval. | Human review; future tooling (SHA comparison) |
| **K-CLAIM-1** | Claims, conclusions, and characterizations must not **overstate what the available warrant supports**. Statements of necessity, sufficiency, universality, completeness, exclusivity, or direct regulatory conclusiveness may be used only when the cited evidence supports that strength; otherwise they must be framed as interpretation, implementation-specific design, or proposal. | Agent instruction constraints; governance audits (AUDIT_GOVERNANCE); human review |
| **K-PROV-1** | Every non-trivial governed claim must cite evidence with a source path and best-effort section reference, or carry explicit `location TBD`. Dependency rows are a schema-specific instance of this rule and use **`EvidenceFile` + `SourceRef`** per `SPEC.md` §6.5. | Agent instruction constraints; TASK+dependency-extract row validation; governance audits; human review |
| **K-INVENT-1** | Unknown values become **`TBD`**, not guessed. Agents must not invent scope items, dependency targets, parameter values, or engineering content. | All agent instruction invariants; human review |
| **K-CONFLICT-1** | Conflicts between sources must be **surfaced, not silently resolved**. Agents expose disagreements with pointers to the conflicting sources. | Workflow-component standard R7; agent instruction invariants; human adjudication |
| **K-WRITE-1** | Every agent has an **explicit write scope** declared in its header block. No agent writes outside its declared zone. | Agent Type table (WRITE_SCOPE property); human review of diffs |

K-DEP-1 combines the acceptance principle with superseded DAG-currency and
register procedures. Its complete original definition remains in the
[archived CONTRACT](https://github.com/sgttomas/chirality/blob/archive/pre-docs-cleanup-1/docs/CONTRACT.md#14-dependencies).
Current dependency handling follows AGENTS.md and the deliverable CLI; ordinary
edge changes do not acquire a new acceptance gate from this historical reference.

## Domain integration

| ID | Invariant | Enforcement |
|---|---|---|
| **K-DOMAIN-1** | **Domain engines own authoritative domain truth.** Canonical model files, model states, analysis runs, comparisons, solver outputs, and handoff internals are owned by the domain engine. Chirality governs the work around it (profiles, manifests, proposals, review notes, gates); it is not the solver and is never the source of accepted engineering truth. | DOMAIN_ENGINE persona; profile `protected_write_paths`; human review |
| **K-DOMAIN-2** | **Protected domain paths are write-quarantined.** Agents must not directly write protected domain artifacts. Domain-controlled writes occur only through declared deterministic tools under the active profile. | DOMAIN_ENGINE; TASK ScopePath/AllowedWriteTargets; profile; human review |
| **K-DOMAIN-3** | **Domain operations require an OperationProposal record and explicit human acceptance.** A proposal is `proposal_only` until validated by a declared deterministic tool and accepted by a human; application occurs only through a domain-engine-controlled apply. | DOMAIN_ENGINE Gate 5; profile; K-AUTH-1/K-AUTH-2; human review |
| **K-DOMAIN-4** | **Domain-engine outputs must not be represented as professional approval.** A green validation/PASS is structural evidence only - never code-compliance, certification, sealing, authentication, or external-prover validation absent a cited human authoritative record. Validation-passed is necessary, not sufficient, for engineering correctness. | DOMAIN_ENGINE professional_boundary; K-CLAIM-1; K-AUTH-1; AUDIT_GOVERNANCE; human review |

*Note:* Per the D-GOV-01 ([archived decisions](https://github.com/sgttomas/chirality/tree/archive/pre-efficiency-cleanup-2026-10-09/docs/governance_harness/_DECISIONS)) scope note, ruled 2026-07-01, engine-owned domain stores are sanctioned authoritative domain truth under K-DOMAIN-1 and are exempt from the governance rebuildable-cache rule.

## Frozen Runtime reference

Runtime is retired and not verified. It is reproducible from
`archive/pre-docs-cleanup-1`, alongside frozen App v3. The contracts below
apply only if Runtime is explicitly reactivated; they do not describe App v4's
architecture or current development obligations. Its historical basis is in
[Runtime PRD](https://github.com/sgttomas/chirality/blob/archive/pre-frozen-products-2026-10-10/projects/chirality-runtime/docs/PRD.md) and
[PRD authority](https://github.com/sgttomas/chirality/blob/archive/pre-frozen-products-2026-10-10/projects/chirality-runtime/docs/PRD_AUTHORITY.md).

| ID | Invariant | Enforcement |
|---|---|---|
| **K-RUNTIME-1** | The Chirality App starts, owns, and stops one simplified Runtime service as a child process, and that service is the exclusive owner of the stock, version-pinned `codex app-server` child together with sessions, delegation, tools, turn locks, and interruption for that App instance. There is no per-user LaunchAgent and no exclusive per-user daemon. Credentials are custodied by Codex within Chirality's effective Codex home; the App never reads, copies, or relays credential material. Desktop, CLI, and project proxies MUST NOT construct a competing runtime (D-GOV-43 items 1, 6 and 7 as re-expressed by the A2 supplement). | Child-process ownership, relaunch, and quit tests; client conformance; packaged-process inspection |
| **K-CONTROL-1** | Runtime control uses authenticated, project-scoped HTTP/1.1 over one Unix-domain socket beneath the application user-data directory, with a `0700` parent directory and a `0600` socket, and per-launch client tokens private to the application. Stale-socket recovery verifies current-user ownership and absence of a live recorded process before removal. The accepted supervisor-socket design (R7-A through DEL-02-07) is retired with the daemon under D-GOV-43 item 7 as re-expressed by the A2 supplement. No second socket and no TCP control listener are permitted under any configuration. | Socket-mode, authorization, stale-owner, and listener tests |
| **K-PROJECT-1** | A tracked `chirality.project.json` contains stable identity and relative authority references only. Secrets, resolved machine paths, client tokens, and approval metadata remain user-data state. Authority-affecting manifest drift disables adapters until explicit re-registration. | Manifest schema/hash/containment tests; secret scan |
| **K-STORE-2** | Central runtime sessions remain JSON/JSONL and import legacy project-local sessions lazily and non-destructively. Runtime state never replaces checkout-contained governance truth. | Migration, replay, restart, and source-preservation tests |
| **K-ROLE-2** | Agent 0/1/2 names authority and responsibility, not a durable model assignment. Runtime session attribution identifies the actual adapter/provider/model and substitutions; this creates no repository run-record duty. | AgentRun/session attribution; governance scan |
| **K-EXPORT-1** | The public export may include generic runtime packages, CLI, contracts, and safe adapters. Credentials, machine state, and private project adapters are excluded. | Export allowlist/boundary checks |

Project writes retain [K-WRITE-2 path containment](COMPATIBILITY_FORMATS.md#paths-and-containment). The
Runtime service's socket, per-launch client tokens, logs, the App's thread
index, and Chirality's effective Codex home (including the shared Codex
sessions store and the Codex-custodied `auth.json`) may live beneath the
application user-data directory because they are explicitly non-authoritative
operational state; they do not grant an agent permission to write outside its
checkout scope.

## Optional Task Management product

These invariants do not require using Task Management or maintaining development registers.

| ID | Invariant | Enforcement |
|---|---|---|
| **K-TM-1** | Task Management owns per-loop Action Item registers and nothing else. Every other domain's state is displayed by citation and remains with its owner | Governance audit; future tooling (`taskmgmt validate`) |
| **K-TM-2** | Registers are git-tracked files inside the owning loop's coordination surface. Any service store or index is a rebuildable, gitignored projection per D-GOV-01, never cited as authority. No engine-store exemption | Governance audit; future tooling (`taskmgmt validate`); D-GOV-01 projection discipline |
| **K-TM-3** | Register writes are judgment acts of the owning loop. Rows carry no directives; no cross-loop register writes; reading a register creates no duty outside a loop's own adopted instruments; no agent appears as accountable (A) for any row (K-AUTH-1) | Human review (the owner triage session is the sole disposition authority); agent instructions |
| **K-TM-4** | Graceful absence, re-scoped `[FINDING F-20]`: no act **outside a loop's own adopted instruments** may require a Task Management read or write. A loop binds itself by its own revocable ruling; deleting the service and its projections blocks nothing anywhere; registers remain plain readable, writable files. Kill test at every release (PEC-K-01 / PEC-SVC-004 pattern) | Release kill test (PEC-K-01 / PEC-SVC-004 pattern); human review |
| **K-TM-5** | A register row, view, or scan output never constitutes approval, acceptance, scope, priority authority, or lifecycle effect. Closure evidence binds to bytes (`EvidenceSha`); a row whose evidence changed after closure is stale, not still-closed | Human review; future tooling (`EvidenceSha` byte comparison per K-AUTH-2) |
| **K-TM-6** | Closure-capable schema: every register schema version carries `Status` and `Disposition`; a register that cannot record its own closure is invalid | Future tooling (register schema validation); governance audit |

Row text is verbatim from the adopted Chirality Task Management PRD §10
(Revision 2, adopted by D-GOV-32; subject SHA-256
`97e2ae6525ecbfdc52ff22aee85e1182a751c1090c2aa2f52faaf9e080f35d18`). D-GOV-32
Effect 5 adopted K-TM-1..6 as product invariants and reserved their entry
into this catalog to a governed tranche; this subsection is that entry, and
the "candidate" label in the PRD's §10 heading ends here.

---
