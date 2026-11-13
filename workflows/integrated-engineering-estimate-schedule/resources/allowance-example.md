---
name: allowance-appraisal-example
description: Synthetic contribution reconciliation and analytic uncertainty checks for a small engineering drawing set.
metadata:
  kind: example
  surface: reference
---
# Synthetic allowance appraisal

This invented example illustrates [allowance appraisal](allowance-appraisal.md).
All quantities, hours, distributions and probabilities are teaching judgments,
not observed productivity, recommended norms or calibrated project data. It
shows what a comparison would retain; it is not evidence of an actual independent
estimating exercise or a completed simulation.

## Align the work, then reconcile contributions

The hypothetical brief covers ten comparable drawings, suitable preliminary
inputs, initial native production, author verification and independent checking,
one ordinary integration return on all ten drawings and a lighter closure return
on five. An affected drawing in each return is a separate touch. Two issue
manifests and final packaging are included. Supplier internal design, a new
design basis and additional formal issues are excluded. Roles describe work;
required independent checking remains separate from authorship.

Suppose a unit construction returns 134 h and an independently elicited phase
appraisal returns 164 h on that brief. Preserve both inputs. Compare their actual
work and role allowances before choosing a result. In this example, the unit
construction omitted 1 Designer h per initial drawing for own verification and
initial comment closure, 4 Lead h for set-level technical decisions, and two
manifests of 1 Lead + 1 Document Controller h each. Those distinct contributions
add 18 h; Engineer correction time was already included and is not added again.

The selected construction is therefore 152 h, rather than the 149 h midpoint.
Here `E`, `D`, `C`, `L` and `DC` mean Engineer, Designer, independent Checker,
Lead and Document Controller. Entries are person-hours per stated unit; blank
roles contribute zero for this example only.

| Component | Quantity and unit | E | D | C | L | DC | Total h |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Set preparation | 1 set | 6 | — | — | 4 | — | 10 |
| Initial drawing, including own verification and initial comment closure | 10 drawings | 3 | 5 | 1 | — | — | 90 |
| First ordinary integration | 10 affected-drawing touches | 1 | 1 | 0.5 | 0.5 | — | 30 |
| Lighter ordinary closure | 5 affected-drawing touches | 0.5 | 1 | 0.5 | — | — | 10 |
| Set-level technical decisions | 1 set | — | — | — | 4 | — | 4 |
| Final file packaging | 1 set | — | — | — | — | 4 | 4 |
| Discipline manifest | 2 issues | — | — | — | 1 | 1 | 4 |

The added Lead decisions do not buy a second independent check; discipline
manifest work does not buy a project-wide transmittal. The selected role totals
and residual comparison are:

| Role | Original unit h | Selected unit h | Independent phase appraisal h | Phase appraisal minus selected h |
| --- | ---: | ---: | ---: | ---: |
| E | 48.5 | 48.5 | 50 | 1.5 |
| D | 55 | 65 | 70 | 5 |
| C | 17.5 | 17.5 | 18 | 0.5 |
| L | 9 | 15 | 18 | 3 |
| DC | 4 | 6 | 8 | 2 |
| Total | 134 | 152 | 164 | 12 |

The phase view also makes the remaining difference visible:

| Work phase | Original independent appraisal h | Projection of selected unit build h |
| --- | ---: | ---: |
| Preparation | 12 | 10 |
| Initial production and examination | 96 | 90 |
| Ordinary returns | 42 | 40 |
| Set-level decisions | 4 | 4 |
| Packaging and manifests | 10 | 8 |
| Total | 164 | 152 |

The projection simply groups the selected components. It is not an independent
estimate. The residual 12 h expresses different judgments about preparation,
initial work, ordinary returns and packaging. Retain the 164 h alternative with
those reasons if the current evidence cannot settle them. A subsequent claim
for another sketch/review cycle would need its distinct work and role allocation
before selection; do not silently add it to the ordinary boundary or hide it in
a larger spread. The phase and role tables are marginal summaries: their totals
agree, but by themselves they do not establish a phase-by-role allocation.

## Give the reference an explicit probability meaning

For this illustration only, the three per-drawing/touch component role vectors
are conditional medians with lognormal uncertainty of log spread `s = 0.20`.
The fixed set and issue components remain deterministic, totaling 22 h. The
152 h reference is thus `22 + 130` at the stated quantities and conditional
component medians. It is neither the mean nor an asserted aggregate P50.

Use independent standard-normal latent factors `Z0`, `Zinitial`, `Zreturns`.
The initial component uses `Z = sqrt(0.4) Z0 + sqrt(0.6) Zinitial`; both ordinary
returns share `Z = sqrt(0.4) Z0 + sqrt(0.6) Zreturns`. Each multiplier `exp(0.20 Z)`
is drawn once per component group and reused for every role and every unit in
that group. Both marginal log variances are `0.20²`. The shared structure models
uncertainty in common unit allowances, not independent drawing-to-drawing
scatter. The two return multipliers are identical; the initial/return log
correlation is 0.4, which is not a claim of calibrated correlation in hours.
Changing dependence with these marginals fixed affects aggregate tails, not
the ordinary mean at fixed quantities.

The fixed-quantity analytic mean is:

`22 + 130 exp(0.20²/2) = 154.6262 h`.

Now introduce a separate quantity hypothesis: `Q = 8, 10, 14` with probabilities
`0.25, 0.50, 0.25`. These are alternatives about the amount of comparable
engineering content, not merely its pagination. They are independent of the
unit multipliers. First-return touches equal `Q`; closure touches equal
`ceil(Q/2)`. All three counts are coherent in each draw. `E[Q] = 10.5` and
`E[ceil(Q/2)] = 5.25` for this particular discrete set. Fixed set/issue work
remains 22 h. Enumeration gives:

`22 + (9 × 10.5 + 3 × 10.5 + 2 × 5.25) exp(0.20²/2) = 161.2575 h`.

Do not substitute `ceil(E[Q]/2)`, which is 6 and gives a different answer.
Odd-count alternatives would also need explicit enumeration. A positive
quantity–unit-effort dependence would require a joint expectation instead of
the independent product used here.

## Reappraise the additional response

After ordinary closure but before final issue, suppose one limited same-scope
interface change is processed with probability 0.25, otherwise none. Its affected
extent is two or four drawings with equal probability, independent of the
quantity and ordinary effort draws. Cap the extent at `Q`; here the cap never
binds because the smallest population is eight. Several comments consolidated
into that response count as one processed change.

The incremental response is 2 E + 2 D + 1 C h per affected drawing, plus 2 L h
per occurrence. These fixed response judgments buy renewed interpretation,
native edits and independent checks after ordinary closure. Existing final
packaging still suffices. They exclude a new formal issue and redevelopment.
The ordinary-closure allowance is 2 h per touch; the additional response is
5 h per affected drawing plus fixed Lead work. The difference needs appraisal
against renewed work, not acceptance merely because it is larger. Reappraise
this response if ordinary closure or its timing changes.

`E[additional h] = 0.25 × (3 × 5 + 2) = 4.25 h`.

The conditional mean including that mechanism is `165.5075 h`. Its proximity
to the independent 164 h appraisal is accidental: one is an expectation with
quantity uncertainty and additional work; the other appraises the reference
ordinary work. It does not validate either construction.

## Check and use the result

A checker can independently recompute the component/role sums and the 18 h
adjustment bridge, enumerate quantities, and recover the three analytic means.
Setting variability to zero, `Q = 10`, closure touches to five and event count
to zero must reconstruct exactly 152 h. A simulation would separately test its
means against 154.6262, 161.2575 and 165.5075 h under the corresponding settings,
with justified sampling error, and conserve each draw's role/component hours.
No task/project percentile has been calculated here.

Useful unweighted sensitivities include reduced ordinary first-return extent,
a different spread at fixed medians, and a coupled high-quantity/high-effort
case. They answer parameter questions; increasing sample count answers a
numerical-precision question. If later scheduling is requested, pass each
compatible draw's role demand through finite resources and actual handoffs.
Neither 152 h nor 165.5075 h alone determines a finish date.

If suitable preliminary input fails to arrive, the condition underlying these
allowances no longer holds. Keep the checked reference recoverable, isolate
that affected case, and appraise the changed production/review work before
retuning hours or interpreting old percentiles. This walkthrough establishes
arithmetic and intended meaning only; a real use still needs its own source,
work and parameter appraisal.
