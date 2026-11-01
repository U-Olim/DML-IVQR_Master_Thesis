# Stage 2C-S - Numerical stability of rank scores and inference

29 October 2026, Asia/Tashkent. Branch: `journal-validation`.
Run: `saved_stability_20261029T084737Z/`.

## 1. Executive conclusion

**Recommendation C: Stage 2C should remain stopped because numerical inference
is insufficiently reliable under the tested certified accuracy envelope.**

All 92 original fitted-arm baselines were reconstructed successfully. A
common, response-scaled objective-error envelope was frozen from the prior
exact certificates BEFORE examining perturbed inference. Among 736 fixed
saved coefficient perturbations, **278** independently satisfy that envelope.
Across these alternatives and their original coefficient vectors:

- **18 arms:** observed opposite rejection decisions between certified
  near-optimal coefficient vectors.
- **74 arms:** unchanged decisions under the tested certified alternatives.
- **0 arms:** numerically indeterminate or not assessable under the stated
  finite-set classification.

There are **21 qualifying alternatives** that change the original decision,
including six intercept perturbations of only about **9.095e-13**. This is
not merely a question of rounding W close to its cutoff: one original W of
14.4361 becomes 4.9589 under a certified alternative.

The alternatives are NOT new fitted estimates or exact optimizers. Their
primal objectives and exactly feasible dual lower bounds rigorously bound
suboptimality under a common empirical solver-accuracy envelope. The result
demonstrates sensitivity of the preserved implementation, not the population
frequency of numerical error or the invalidity of every original decision.

No original file, fit, data sample, gate, proxy, projection, cutoff, indicator
rule, manuscript, commit or push was changed. No replication 22-40 ran.

## 2. Protocol, scope and preservation

`PROTOCOL.md` was written before inference comparisons. The protocol, Python
generator and R helper were hashed before execution and remained unchanged.
The 92 fitted arms comprise 23 saved datasets (two preflight and pilot 1-21)
times P11/P01/P10/P00. The 23 KNOWN anchors are not fitted arms and are not
counted as additional replications.

The existing Stage 2C-P manifest (409 artifacts) and original Stage 2C manifest
(393 artifacts) were verified. Pre/post SHA-256 snapshots protect **7,077
files** outside stability, excluding Git metadata: zero changed, missing or
added outside the authorized directory. Historical reports, certificates,
arrays, Stage 2A/2B and the original stopped-run scientific summaries remain
intact. Working branch was confirmed as journal-validation.

## 3. Baseline reconstruction: all gates passed

The R helper uses historical R 3.4.3 and saved RDS objects only. It does not
source estimator functions, load a quantile-regression solver, fit a model,
or generate random numbers. It recomputes

    y*=Y-(1+qnorm(.90))*D,
    e=y*-[1,X]b,
    s=.90-1{e<=0},
    g=sum_i psi_i*s_i,
    S=sum_i psi_i*psi_i'*s_i^2,
    W=g'*solve(S)*g.

S here is the UNNORMALIZED sum. The same W results from the corresponding
consistent n-normalized formulation. The frozen P11 density and original
instrument residuals are read unchanged from the saved records. Both f and
psi are retained in the new run; no density or projection is recomputed.

Across all 92 baselines:

| Check | Maximum discrepancy |
|---|---:|
| Recomputed versus saved R residual | 0 |
| Rank-indicator disagreement | 0 |
| Normalized score moment | 9.3675e-17 |
| Normalized second moment | 8.3267e-17 |
| W | 6.3949e-14 |
| Acceptance/rejection | 0 differing decisions |

All baseline checks completed before the probe phase began. Every score uses
the unchanged <=0 rule. The critical value is the original R binary64
`qchisq(.95,2)`, displayed as **5.99146454710798**. Acceptance remains W<=cutoff.

All 828 original/probe W evaluations were additionally verified by exact
rational calculation for their stored binary64 scores and instruments. A
separate direct Fraction implementation checked g, all three S entries, W
and its exact side of the stored cutoff. Thus observed decision differences
are not artifacts of rounding the final quadratic form.

These exact calculations condition on the historical R-computed ranks. They
do not assert that rounding-sensitive residual signs equal an exact-real
optimizer's unique score or certify every alternative floating execution path.

## 4. Near-zero residual and matrix diagnostics

All saved residual arrays have **zero exactly zero entries**. They nevertheless
contain many extremely small nonzero residuals. The table gives minimum--maximum
counts across 23 datasets for each arm:

| Arm | <=1e-12 | <=1e-10 | <=1e-8 | <=1e-7 | <=1e-6 |
|---|---:|---:|---:|---:|---:|
| P11 | 0-26 | 2-37 | 23-37 | 23-37 | 23-37 |
| P01 | 0-4 | 0-8 | 5-8 | 8-8 | 8-8 |
| P10 | 0-51 | 4-99 | 92-100 | 98-100 | 100-100 |
| P00 | 0-70 | 6-101 | 94-101 | 100-101 | 100-101 |

These are descriptive potential-vulnerability counts for the stated absolute
residual bands, not proofs of sign error and not replacement tie definitions.
Per-arm minimum/median residual margins, complete residual arrays and observed
union counts of signs that change within the qualifying set are retained.

Original score-matrix condition estimates range from **1.0359 to 2.2514**.
All evaluated matrices were invertible; exact determinant positivity was
checked. No matrix singularity is needed to explain the observed sensitivity.

Original W proximity, across 92 arms:

| Descriptive absolute distance from cutoff | Count |
|---|---:|
| <=1e-6 | 0 |
| <=.01 | 0 |
| <=.1 | 1 |
| <=.5 | 6 |
| <=1 | 14 |

The nearest original value is pilot_020 P01, W=6.0291159245, distance .0376514.
The full continuous signed margins are saved. These bands did not select
probes, change indicators, or determine the objective budget.

## 5. Saved perturbation: rank changes versus inference changes

The Stage 2C-P example is validation_001 P00 with intercept lowered by 2**-40.
Reconstruction in historical R gives:

| Quantity | Result |
|---|---:|
| Fitted-value RMS change | 9.094947017729282e-13 |
| Rank indicators changed | 44/1000 |
| Mean rank-score change | +.044 |
| Score-sum change | (-16.05199,-1.66859) |
| Unnormalized S11/S12/S22 changes | (94.98710,.16178,40.46982) |
| Original W | 1.2074604363 |
| Alternative W | .4185676943 |
| Original / alternative decision | Accept / accept |
| Certified objective-error upper bound | 3.4864288614396824e-11 |

Thus 44 changed signs alone did not change THIS decision. The opposite
intercept shift changes 24 signs and gives W=.8609805021, also acceptance.
This distinction is retained rather than treating every sign change as an
inferential failure.

The fixed perturbation is not called an exact solution. Its certification
comes separately from exact primal evaluation and a verified feasible dual;
its small size alone is not an optimization certificate.

## 6. Common certified near-optimal envelope

For each original arm j, take Stage 2C-P's exact G_j=P_j-D_j and stored
response-scale constant

    B_j=n*max(IQR(y*), median(abs(y*-median(y*))),1).

Before any inference comparisons, freeze the common dimensionless envelope

    eta=max_j G_j/B_j = approximately 5.6290557342834175e-12.

Each B_j is treated as its exact stored binary64 scale constant; eta and
every product eta*B_j are represented by exact rationals. An alternative
qualifies only if its independently verified P_j(b_alt)-D_j<=eta*B_j.
Allowed absolute gaps range from about **2.77505e-8 to 3.12346e-8**.

This is independently tied to the certified numerical accuracy already
demonstrated across ALL 92 saved fits. It has no arbitrary multiplier and
does not use W, coverage, acceptance or a chosen favorable case. Every
original vector qualifies. It is a justified comparison envelope for the
observed solver accuracy, NOT proof of an adequate future scientific tolerance.
Other scientifically motivated budgets could define different tested sets;
no universal optimization-accuracy criterion is claimed.

Only the previously fixed +/-2**(-40,-30,-20,-10) intercept probes are used.
They are deterministic candidates, not refits. For every candidate, the
actual R binary64 coefficient shift was checked against the coefficient
used in its exact objective certificate; all slopes match the original.

The independent audit rechecked all 92 exact dual witnesses and all 736 exact
probe objectives. For each alternative the new run retains exact primal P,
the relevant dual-feasible lower bound D, G, qualification flag, original
certificate hash, coefficient/residual arrays and inference quantities.
The certified problems interpret tau as exact 9/10 and stored full-precision
X/y*/b/lambda as exact inputs, as in Stage 2C-P. Inference retains the historical
floating score convention; the two arithmetic scopes are explicitly separate.

**278 alternatives qualify:** 183 of the signed 2**-40 probes and 95 of the
signed 2**-30 probes. None of the larger two steps qualifies. All 736 probes
remain reported; nonqualifying probes are not used to claim certified
near-optimal decision instability. No stochastic perturbation or random
search was performed.

## 7. Score, W and acceptance stability

For fixed psi, a sign crossing changes its contribution to g by +/-psi_i
and to S by +/-.8*psi_i*psi_i' at tau=.90, because squared scores change
between .01 and .81. Tiny coefficient changes near residual kinks can therefore
move both numerator and studentization materially, even with well-conditioned S.

Among qualifying candidates, 21 probes change their original decision:
14 rejection-to-acceptance and seven acceptance-to-rejection. Six are
2**-40 steps and 15 are 2**-30 steps. These counts are sensitivity diagnostics,
not independent simulation replications or a coverage improvement estimate.

Examples, with both original and alternative inside the same frozen envelope:

| Dataset / arm | Intercept step | Original W | Alternative W | Alternative certified gap upper | Decision |
|---|---:|---:|---:|---:|---|
| pilot_002 P00 | -2**-40 | 4.86454 | 8.48136 | 3.12116e-11 | Accept -> reject |
| pilot_003 P10 | +2**-40 | 9.00223 | 5.94065 | 8.18441e-11 | Reject -> accept |
| pilot_005 P01 | -2**-40 | 6.49365 | 5.46110 | 1.42030e-11 | Reject -> accept |
| pilot_012 P01 | -2**-40 | 5.87520 | 6.73910 | 2.87196e-11 | Accept -> reject |
| pilot_003 P11 | +2**-30 | 14.43610 | 4.95892 | 1.76926e-8 | Reject -> accept |

The largest absolute qualifying W change is approximately 9.85673
(pilot_014 P11). Such changes are far larger than the independently verified
quadratic-form arithmetic errors.

Arm-level finite-set classification:

| Arm | Stable under tested certified alternatives | Observed decision instability |
|---|---:|---:|
| P11 | 14 | 9 |
| P01 | 18 | 5 |
| P10 | 22 | 1 |
| P00 | 20 | 3 |
| Total | **74** | **18** |

Seventeen unstable arms are in the 21 pilot datasets and one is in the two
preflight datasets. All 18 unstable arms passed the historical KKT gate.
Conversely pilot_021 P10, the historical gate failure, is stable over its
tested qualifying alternatives, with W approximately .531325 throughout.
The historical gate failure is neither erased nor asserted to predict
inference instability.

Stable here means original plus at least one distinct qualifying candidate
were checked, all decisions agree, and cutoff-side arithmetic is resolved.
It is NOT a uniform assertion over all coefficient vectors satisfying the
objective envelope. The tested alternatives vary the intercept only; broader
near-optimal directions were not exhaustively optimized.

Every qualifying pair is retained in `qualified_pairwise_inference.csv`, not
only pairs against baseline. Full score vectors, g, S, W, conditions and paired
changes are available. Original saved scores/decisions are not overwritten.

## 8. Remaining limitations

- The accuracy envelope is based on finite saved-fit certificate upper bounds,
  which can be conservative. It is not a theoretically mandated error budget.
- Certified alternatives need not be exact minimizers or outputs returned by
  another solver. No repeated fitting demonstrated an optimizer selecting them.
- Exact inference arithmetic is conditional on the R-computed residual ranks.
  It does not remove the numerical discontinuity in constructing those ranks.
- Only a fixed one-coordinate probe family was tested. Non-detection is not
  global stability, and 18/92 is not an estimate from 92 independent samples.
- Two preflight datasets and the partial pilot are explicitly distinguished;
  this task does not complete or amend the historical Monte Carlo study.
- This investigation does not resolve density regularity, same-sample nuisance
  dependence or applicability of asymptotic chi-square inference.

## 9. Continuation recommendation

**C - Remain stopped.** Under a common envelope justified by the original
solver's certified accuracy, opposite decisions are demonstrable. Passing
the historical KKT gate or having a small primal-dual gap alone is insufficient
to authorize continuation of the intended scientific score comparison.

Before any continuation, review must specify the numerical target and supply
evidence that the chosen evaluation protocol controls the resulting score/W
error or explicitly reports its ambiguity. Necessary evidence includes:

1. A prospectively justified objective/prediction accuracy specification,
   independent of favorable W or coverage, with a defensible connection to
   rank-sign and decision stability.
2. Saved-fit verification showing stable inference or certified inference
   ranges under that specification, including treatment of all near-tie and
   unresolved cases. More accurate certificate/optimization investigation may
   be needed, but merely shrinking a budget until observed flips disappear
   would not justify it.
3. An explicit scientific decision on whether the target is the preserved
   executable's raw <=0 behavior or a different tie/subgradient convention.
   Any changed estimator must be versioned as a separate procedure; historical
   scores and gate records cannot be silently repaired.
4. A consistent all-arm policy and failure ledger before indices 22-40,
   preserving original streams, indices, datasets, arms and historical failure.

No continuation or estimator modification was implemented. No manuscript was
edited and no publication-calibration claim follows from these diagnostics.

## 10. Reproducibility and artifact index

Scripts and frozen instructions: `PROTOCOL.md`, `scores.R`, `analyze.py`,
`verify.py`, `finalize.py`, `README.md`.

Under the uniquely named run:

- `frozen_accuracy_budget.json`: exact eta and every arm's budget, frozen before
  baseline/probe inference.
- `baseline_R.csv`, `BASELINE_PASS.txt`, logs and session information.
- `near_zero_diagnostics.csv`, `baseline_cutoff_proximity.csv`.
- `all_probe_inference.csv`: all 736 probes, whether qualifying or not.
- `alternative_optimization_certificates.json`: exact alternative primal,
  dual lower bound and suboptimality bound.
- `arm_stability_classification.csv` and extended classification table.
- `observed_certified_decision_changes.csv`, `qualified_pairwise_inference.csv`.
- Per-arm baseline/alternative exact rational inference records and complete
  binary64 coefficients, residuals and score vectors; per-dataset frozen psi/f.
- `independent_validation.json`: 92 objectives, 736 alternatives and 828 exact
  W values independently checked, plus original artifact integrity.
- Initial source hashes, protected snapshots, final preservation, source hashes,
  artifact SHA-256 manifest and final status.

All raw output stays inside stability and is ignored by Git; preserve it
separately when archiving or sharing. Stage 2C-S stops here for review.
