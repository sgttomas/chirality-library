# TOOLMAKER Requirement Brief — OpenPipeStress headless CLI entrypoint  (PROPOSAL)

> Emitted by DOMAIN_ENGINE; **not** implemented here. This is a **piping-side** (tier-2) deliverable — the owner routes it; tier-0 does not implement it or write into the piping subtree. Gates L2 (validated-kernel runs).

```markdown
TOOLMAKER_REQUIREMENT:
  RequestedBy: DOMAIN_ENGINE
  ToolCandidate: openpipestress_headless_cli
  Purpose: A thin CLI entrypoint wrapping the existing lib-only headless runner
           (projects/chirality-piping/core/runner/headless/src/lib.rs:655), so a
           validated-kernel run can be invoked read-only (JSON-in / JSON-out) without the GUI.
  Inputs:
    - model/state reference (per project_persistence / model_state schemas)
    - run settings; solver identity
  Outputs:
    - an analysis_run record per schemas/analysis_run.schema.json (read-only; no model mutation)
    - the engine professional_boundary notice on the result
  WhyToolNotAgent: deterministic solver invocation; no inference. The kernel already exists; only the entrypoint is missing.
  WriteScope: engine-owned run-record store only (domain-controlled write); never agent-direct.
  FailureBehavior: fail-fast; surface RULE_INPUTS_INCOMPLETE / completeness findings rather than inventing inputs.
  Constraint: DEC-042 prep-sanctioned (harness-independent, no network, no apply). Owner-routed to the piping loop.
```
