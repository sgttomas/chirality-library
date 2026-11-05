# D-T0-23 — Shared Runtime Domain Convergence

**Status:** RULED
**Date:** 2026-07-22
**Decision ID:** D-T0-23
**Companion rulings:** D-GOV-20, D-APP-73, D-PEC-56

## Owner direction

The owner explicitly instructed implementation of the complete Shared Runtime and Local-Agent Pilot plan on 2026-07-22. This record captures the tier-0 domain-engine consequence.

## Ruled convergence

1. App-dev and PEC register as distinct projects with one shared Chirality runtime daemon.
2. Runtime transport, sessions, credentials, engine execution, managed delegation, interruption, replay, and residency are shared infrastructure.
3. Project and domain authority do not converge. Each registered project retains its checkout-contained instructions, manifests, execution tree, approvals, tools, data boundaries, and acceptance rules.
4. PEC retains deterministic acts, RBAC, reporting, human-only acts, and project-specific tool semantics in a project adapter service.
5. PEC prospectively retires independent LLM, session, and delegation ownership. The temporary legacy agent endpoint may proxy to the shared daemon for one migration cycle, but no production dual execution loop is permitted.
6. Governed AgentRuns remain in each project execution tree and record parentage, sealed brief, role, actual engine/provider/model, residency epoch where applicable, permissions, evidence, and acceptance.
7. Project manifests contain stable references only. Resolved roots, client credentials, and approval metadata remain machine-local daemon registration state and never become project authority.

## Preserved PEC boundaries

D-T0-20/21 visibility and access bases remain in force. D-T0-22 remains historical but does not authorize ambient runtime authority in the shared daemon. PEC human-only acts, import acceptance/application, `force`, conversion dispositions, and production mutation remain unavailable to generic agents.

The pilot is scratch/demo-only. D-PEC-49 remains awaiting ruling. Production-data, production-mutation, and product-and-authority rebaseline decisions remain open and are not resolved here.

## Failure boundary

If the daemon, registration, authorization, or PEC adapter is unavailable or inconsistent, PEC agent execution fails closed. Deterministic human PEC operations remain under their existing app-owned contracts; no agent fallback starts the retired independent loop.
