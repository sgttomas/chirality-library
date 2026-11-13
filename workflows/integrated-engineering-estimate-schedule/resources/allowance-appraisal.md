---
name: allowance-appraisal
description: Appraise and reconcile engineering work allowances and their median, mean and uncertainty meanings before using them in a coupled model.
metadata:
  kind: instruction
  surface: reference
---
# Appraise work allowances

Use this resource when constructing or revising material effort allowances in
[the coupled estimating workflow](../WORKFLOW.md#3-develop-distinct-coupled-projections).
Its result is an inspectable selected work basis, reasons for changes and
remaining alternatives, with the numerical meanings needed by its consumers.
Keep these in the owning model inputs and review, not a parallel register.
An adequate existing appraisal can be reused. This is neither a separate work
definition method nor a requirement to simulate every estimate.

## Compare constructions through the work

Use two independently developed constructions where they illuminate consequential
uncertainty. For example, one estimator can build quantities and role-hours from
work units while another appraises the effort by phases and roles. Give both the
same scope, output population, input maturity, production/review practice,
ordinary return assumptions and exclusions. Develop their allowances before
showing either estimator the other's totals. Record inherited common norms or
assumptions: separate authors do not make a shared numerical basis independent.
Where independence is unavailable, describe the comparison as a cross-check.

Compare contributions, not just totals. Map the work behind each view to a common
basis: interpretation, native production, author verification, independent
checking, comment disposition, ordinary affected-unit revisions, coordination,
responsible technical decisions and issue packaging, as applicable. A phase name
can hold several of these; a work unit can span several phases. Distinguish
native production from receiving/incorporation work, recurring per-unit work
from fixed set/issue work, and technical approval from independent checking.
Do not add a role merely because it appears in a standard roster.

Trace the major differences to omissions, duplicated work, incompatible
populations or conditions, role boundaries, or different judgments about the
same contribution. An affected-unit return is not automatically a complete
redesign; author verification does not automatically replace independent
changed-content checking. Explain what is already included before adding an
allowance. Reconcile role totals as well as the whole total: similar totals can
hide materially different work or skill demand.

Select corrections on that basis, with the integration owner carrying their
reasons into the selected inputs. Show the bridge from each original estimate
to the selected construction and any unresolved difference. Keep a plausible
alternative when the available evidence cannot resolve a work-content or
parameter judgment. Do not average totals by default, add the second estimate
as contingency, or widen a distribution to conceal a scope disagreement.
Independent scrutiny can expose omissions and improve coherence; agreement
among agents is not empirical productivity calibration.

Preserve the independently elicited phase appraisal as its own original basis.
A phase view allocated from the selected unit build is a **projection of that
build** and should reconcile to it. It is not new independent corroboration,
nor does it turn accounting phases into schedule gates. If the comparison
reveals inadequate work definition, return the bounded gap to its owner through
[define-work](../../define-work/WORKFLOW.md); continue supported portions.

## State the median, mean and uncertainty contract

For each component or coherent group, make the following meanings recoverable
from the actual inputs. Prose and existing input fields can suffice; no new
schema is prescribed.

| Subject | What the model must distinguish |
| --- | --- |
| Quantity and unit | Physical count, affected-unit touch, modeled equivalent, issue or service period; reference value and quantity rule; included content/density, boundaries and source maturity. More pages with the same content need not mean more engineering. State whether quantities describe whole work or remaining work. |
| Role allowance | Person-hours per defined unit, included production and reviews, excluded/additional work and the conditions under which the allowance applies. Distinguish a conditional median, an arithmetic expectation and an unclassified point judgment. A provisional population and conditional unit medians produce a reference workplan, not automatically a task or project P50. |
| Distribution and parameters | Chosen family, anchoring convention, spreads/bounds/probabilities, units, evidence or elicitation basis, applicability and material omissions. Separate observations from analogs, expert judgments and placeholders. An earlier estimate or a desired total is not observed execution. Where evidence does not support probability claims, use explicit alternatives or ranges without assigning percentiles. |
| Dependence and sampling unit | Which uncertainty is common to a project, family, component, unit, role or event; what is drawn once and reused, what is independent, and how quantity depends on effort. A common uncertain class allowance is different from independent unit-to-unit scatter. Preserve joint quantities, feasible class mixes and role relationships. |
| Ordinary and additional work | Which initial corrections, normal returns, affected extents and issues the ordinary allowance already funds; which additional processed response is counted, when, and with what incremental roles. Distinguish uncertainty about the ordinary work from genuinely additional work. |
| Interpretation and use | Reference sum, analytic mean, sampled total, or quantile of a named variable and population; selected model version, conditional limits, sensitivity and numerical precision. Pricing and scheduling consumers need the compatible role detail, not just an unlabeled total. |

For a lognormal unit allowance with conditional median `m` and log standard
deviation `s`, `D = m exp(s Z)` for standard-normal `Z`, and
`E[D] = m exp(s²/2)`. If the stored value is instead the mean `d`, use
`D = d exp(s Z - s²/2)`. Do not uplift a stored mean again. A spread change at
fixed median changes the mean; a spread change at fixed mean changes the median.
State which is held fixed. Lognormal is an example, not a required family.

A shared multiplier may move all roles of a component together, preserving
its appraised role composition in each draw. If roles need different responses,
define their dependence explicitly rather than independently resampling rows by
accident. For independent standard-normal factors, weights whose squares sum
to one preserve unit log variance. If factors are correlated, include their
covariances. Distinguish a proposed common-factor structure from demonstrated
correlations; components in only one family cannot establish separate project
and family effects from that sample alone.

## Reappraise additional responses after ordinary revisions

Describe the physical response, not just a list of risk causes. Several comments
or causes can lead to one processed change; count its shared response once.
Separate occurrence count, affected extent (capped or otherwise constrained by
the modeled population), incremental role effort and any fixed response work.
Repeated changes to one unit need a stated treatment: distinct successive
responses may be real, while duplicate descriptions of one response are not.

When ordinary allowances change, reappraise the event response boundary, extent
and incremental effort before retaining the event model. For example, increased
ordinary review closure may already fund work previously assigned to a change
allowance. Conversely, a limited change after ordinary closure may need renewed
interpretation, native edits and independent checks. Identify whether existing
final packaging still suffices or an additional issue really occurs. New scope,
a new design basis and whole-output redevelopment need their own consequence
assessment; a bounded local-change mechanism does not cover them automatically.
An event expectation is capacity allowance, not an incident guaranteed in a draw.

## Check numerical meaning before interpreting samples

Use analytical means where available. Linearity gives `E[sum H] = sum E[H]`
without requiring independent components. Factoring `E[Q D]` into `E[Q] E[D]`
does require independence (or a justified zero covariance). Otherwise calculate
conditional expectations or the joint expectation. Enumerate discrete quantity
cases when rounding, capping or class mixes matter. For independent identically
distributed event responses, independent of the count, expected additional
hours are `E[N] E[response]`; dependent counts, extents and responses require
their conditional calculation.

Check a selected reference case with variability disabled at its reference
quantities and no additional events. This checks reconstruction of the workplan,
not an expected value. Separately check fixed-quantity ordinary means, uncertain
quantity means and additional-response means so errors cannot cancel in a total.
Reconcile component, role, phase and task allocations to each other wherever
those views exist, with shared production counted once. Test affected-unit
bounds and ordinary/additional overlap. Inspect saved inputs and outputs and
bind the checks to the version used. See the [synthetic example](allowance-example.md).

When simulation is justified, retain the distribution/dependence specification,
code/input identity, seed and sample count. Compare simulated means with the
analytic checks within justified Monte Carlo error; inspect convergence of the
reported quantiles separately. More draws reduce numerical sampling error.
They do not establish the chosen distributions, narrow uncertainty in their
parameters, or prove predictive coverage. Vary consequential parameters and
structural assumptions in distinct sensitivity cases; label unweighted cases
as such rather than presenting them as a probability interval.

A sum of component medians is generally not the median of their sum. Task or
project quantiles require compatible joint draws and the stated coverage;
summing task percentiles does not produce a project percentile. A modeled
percentile is conditional on scope, parameters and dependence, and says nothing
about omitted families or unknown external clocks. Estimation precision and
demonstrated predictive accuracy are different claims.

For completion-date uncertainty, propagate each compatible draw's role demand
through the technical handoffs, calendars and qualified finite-resource
allocation. Preserve shared causes across tasks, and reconcile allocated hours
to that draw's budget; mean effort scheduled once is not expected finish.
A representative draw is one coherent scenario selected by a stated rule.
A project percentile belongs to one named project metric across draws. A draw
near a finish percentile does not put all its costs, task hours and milestones
at that same percentile, nor does a componentwise percentile table describe one
jointly realizable scenario.

Return the selected allowance basis, contribution bridge, residual alternatives,
checks and material limits at the owning input/review home. If a source or
boundary changes, preserve the preceding checked basis, isolate the affected
candidate and repeat the affected appraisal/checks. Resume interrupted work
from those actual artifacts; a partial comparison has no completed reconciliation
claim. Method completion establishes an appraised planning basis, not empirical
validation, engineering readiness or owner acceptance.
