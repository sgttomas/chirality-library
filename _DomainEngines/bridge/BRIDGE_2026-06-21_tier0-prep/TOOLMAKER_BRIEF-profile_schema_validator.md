# TOOLMAKER Requirement Brief — DomainEngineProfile schema validator  (PROPOSAL)

> Emitted by DOMAIN_ENGINE; **not** implemented here. The owner chooses the owning workflow (TOOLMAKER). Gates the `VALIDATED` ProfileStatus transition (D-T0-06).

```markdown
TOOLMAKER_REQUIREMENT:
  RequestedBy: DOMAIN_ENGINE
  ToolCandidate: validate_domain_engine_profile
  Purpose: Deterministically validate a DomainEngineProfile YAML against the generic
           contract schema (required fields, enum membership, 4-class path taxonomy,
           deterministic_tools shape, ProfileStatus 7-token enum, professional_boundary
           structured object). LLM-independent; pass/fail with reasons.
  Inputs:
    - profile path (e.g. _DomainEngines/profiles/<id>.yaml)
    - the generic contract schema (the merged canonical DomainEngineProfile shape; see CONTRACT_DIRECTION + FM-01/FM-04)
  Outputs:
    - exit 0 (VALID) / non-zero (INVALID) with per-field findings
    - a machine-readable report the DOMAIN_ENGINE captures as a project file
  WhyToolNotAgent: schema/enum/required-field validation is deterministic and checkable; no inference.
  WriteScope: a declared report path under _DomainEngines/ (no profile mutation)
  FailureBehavior: fail-fast with exit code + per-field stderr; never auto-fix; never mark ADOPTED.
  Note: this validator is what lets ProfileStatus move DRAFT -> VALIDATED. Until it exists,
        no profile may be claimed VALIDATED (D-T0-06).
```
