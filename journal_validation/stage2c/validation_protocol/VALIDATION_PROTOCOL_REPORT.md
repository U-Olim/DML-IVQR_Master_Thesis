# Stage 2C-P - Numerical validation protocol and consistent reassessment

29 October 2026 (Asia/Tashkent). Branch: `journal-validation`.
Saved-input reassessment: `reassessment_20261029T083111Z/`.

## Executive conclusion

**Recommendation B: further numerical validation is required before continuation.**

All **92 saved fitted arms** now have useful, exactly feasible dual certificates,
independently checked objective-error upper bounds, complementarity diagnostics,
and scale information. The certified upper bounds on unscaled objective
suboptimality range from **1.0106613570362076e-11 to 2.7750496737268564e-8**.
No materially inaccurate optimization has been demonstrated.

These strong objective certificates do not establish the accuracy of the
discontinuous rank-indicator statistic. An explicit saved-data probe changes
44 residual signs with an intercept shift of only 9.094947017729282e-13,
while remaining within a certified 3.4864288614396824e-11 of the optimum.
This prevents treating a small objective gap alone as sufficient numerical
validation for the scientific score comparison.

Under the deliberately conservative protocol frozen BEFORE reassessment,
all 92 arms are **Indeterminate for application-level numerical acceptability**.
Their objective-error certificates themselves are not indeterminate: all 92
passed independent exact arithmetic verification. No universal new tolerance
or score-accuracy budget was invented to force an acceptance decision.

The historical classifications remain permanently **91 certified passes and
one certified failure**, pilot_021 P10. Its historical failure was not relabeled.
Its new objective-error upper bound remains 1.1776241822846186e-8.

No samples, outcome refits, pilot continuation, manuscript edits, commits or
pushes occurred. Only new validation_protocol files were created.

## 1. Scope, preservation and prereassessment protocol

The current branch was confirmed as journal-validation and the known working
tree contained the pre-existing untracked Stage 2C directory. Before numerical
reassessment, `PROTOCOL.md` documented the objectives, certificate construction,
classification rule and fixed stability probes. Its SHA-256 and the generator's
source hash were recorded in `initial_state.json`. Finalization verifies both
files remain unchanged since execution began. Postprocessing/audit scripts and
the report were subsequently added without changing that rule or generator.

The user request's phrase 'five fitted arms from replication 21' includes
KNOWN, which has no outcome optimization. There are four fitted arms per
dataset: P11, P01, P10, P00. Two preflight datasets and 21 pilot datasets give
**23 x 4 = 92 fits**, plus 23 separate non-fitted KNOWN diagnostic anchors.

The Stage 2C-V manifest was independently checked against all 1,679 listed
artifacts before reconstruction. Historical Stage 2C, Stage 2C-V, Stage 2A/2B,
manuscript and all other repository files outside validation_protocol were
protected by pre/post SHA-256 snapshots: **6,658 files, zero changed, zero
missing, zero additions outside scope**. The original failed run and its
20-replication scientific summaries remain unchanged.

## 2. Exact primal and dual derivation

Let X include its constant column and y*=Y-alpha0 D, with the same saved true
candidate alpha0=1+qnorm(.90). The full-precision response is read from the
Stage 2C-V export of the original R candidate adjustment, not reconstructed
using a different candidate or an unrelated response vector.

For saved coefficient vector b and penalty vector lambda, the intended
historical objective is

    P(b) = sum_i rho_tau(y*_i-x_i'b) + (1/2) sum_j lambda_j |b_j|,

where tau=.90. The exact certificates interpret tau as rational 9/10 and all
stored binary64 X, y*, b and lambda as exact rational inputs. This specifies
the certified problem precisely; it does not claim the historical floating
solver performed exact real arithmetic. The same interpretation was used in
Stage 2C-V. Floating-versus-rational objective differences and recorded
objective agreement are separately quantified.

Using rho_tau(e)=max_{tau-1<=v<=tau} v*e and the conjugate of the weighted
absolute-value penalty gives the dual

    maximize D(v)=y*'v,
    subject to tau-1<=v_i<=tau,
               |X_j'v|<=lambda_j/2 for every j.

Zero penalties impose exact equalities X_j'v=0. Any b is primal-feasible;
objective evaluation must still use the correct response, penalties and scale.
For any EXACTLY dual-feasible v,

    0 <= P(b)-P* <= P(b)-D(v)=G.

The nonnegative gap decomposes exactly into

    sum_i [rho_tau(e_i)-v_i e_i]
    + sum_j [lambda_j |b_j|/2 - b_j X_j'v].

The first term is check-loss complementarity; the second is penalty
complementarity. A positive G is an error upper bound, not a positive lower
bound on suboptimality. A large upper bound alone cannot prove a fit bad.

Exact KKT requires BOTH dual feasibility and complementarity. At e_i=0,
v_i may range over [tau-1,tau]; at nonzero residuals it must equal the proper
endpoint. At b_j=0 the penalty derivative is interval-valued; at nonzero
b_j it has the corresponding sign. Zero-penalty slope gradients must vanish.

## 3. Certificate construction and independent verification

Saved outcome coefficients are never optimized or replaced. A numerical
dual LP supplies candidate dual coordinates only. For unpenalized coefficient
constraints, an appropriate dual-coordinate basis is selected and corrected
with exact integer Bareiss elimination and rational back substitution. The
resulting rational vector is scaled toward the feasible zero vector if needed
to enforce every remaining score-box and penalty inequality exactly. Scaling
preserves all exact zero-penalty equalities.

The four arms therefore require respectively:

| Arm | Exact unpenalized equations |
|---|---:|
| P11 | 0 |
| P01 | 1: intercept |
| P10 | 100: slopes |
| P00 | 101: intercept and slopes |

All box constraints and coefficient constraints were checked algebraically.
Primal residuals and objectives were recomputed with exact integers/rationals,
rather than trusting floating residual evaluation or LP success flags. Every
loss and penalty complementarity contribution was checked for nonnegativity.

`audit.py` is a separate no-solver implementation. It independently verified
all **92 dual certificates**, objectives and gap calculations and all **736
fixed probe objectives**. It also independently reverified the original
Stage 2C-V P10 exact dual witness. That witness gives primal
84.84584974882415, dual 84.8458497370479, and gap 1.1776241822846186e-8.

Numerical dual LPs use existing SciPy/HiGHS dual simplex with feasibility
settings 1e-10. Those settings locate witnesses; they are neither the new
acceptance criterion nor the basis of rigorous feasibility claims. The outcome
solver and its defaults are never invoked or changed. No packages were installed.

## 4. Scale-aware quantities and classification rule

Every arm reports unscaled P, D, G, G/n, and G/B, where

    B=n*max(IQR(y*), median(abs(y*-median(y*))), 1).

The unit floor is explicit and refers to this original response's units.
This reference is descriptive, not a universal error tolerance or a
unit-invariant theorem. Column RMS scales, outcome-design singular-value
conditioning, coefficient/residual magnitudes, exact-versus-saved residual
sign differences and floating stationarity diagnostics are also recorded.

The frozen classifications are:

- **Numerically acceptable under the new protocol:** exact zero certified gap,
  or rigorous numerical error bounds satisfy an independently specified
  application accuracy budget with a justified prediction/score transfer.
- **Numerically unacceptable:** proven input/primal inconsistency, or a
  certified lower bound violates such a justified error budget.
- **Indeterminate:** a useful finite objective-error upper bound is certified,
  but a nonzero gap and absent budget/transfer do not settle application accuracy.
- **Insufficient evidence:** needed inputs or useful independently verifiable
  certificates are unavailable.

No application budget or positive loss-growth condition was supplied or
established. Thus the protocol provides a transparent, quantitatively useful
reassessment but is not yet an operational automatic continuation gate.
It intentionally does not equate a threshold chosen from solver eps, favorable
coverage, or a small printed gap with scientific numerical acceptability.

Historical rq eps=1e-6 does not imply a universal absolute residual, prediction,
stationarity or objective-error bound. Likewise, the old fixed-tie 1e-7 gate
is not a theoretically necessary optimization accuracy.

## 5. Results for all 92 fitted arms

Ranges of certified upper bounds on unscaled objective suboptimality:

| Arm | Fits | Minimum gap upper bound | Maximum gap upper bound |
|---|---:|---:|---:|
| P11 | 23 | 1.0129370889374077e-11 | 2.338444445002788e-8 |
| P01 | 23 | 1.0106613570362076e-11 | 9.904258701568859e-9 |
| P10 | 23 | 1.915092883436412e-11 | 2.7750496737268564e-8 |
| P00 | 23 | 1.81095405883794e-11 | 1.5734739828486563e-8 |

The largest G/n is 2.7750496737268565e-11. Descriptive G/B ranges from
1.850493548171286e-15 to 5.6290557342834175e-12. The exact recomputed primal
and recorded original objective differ by at most approximately
6.821210263296962e-13 in floating display. These quantities support high
objective accuracy, without proving accuracy of every coefficient or score.

All exact dual feasibility checks passed. The outcome-design singular-value
condition estimate ranges from 89.3964 to 98.0649; these are floating design
diagnostics, not uniqueness or global loss-curvature certificates.

The new classifications are:

| New protocol classification | Count |
|---|---:|
| Numerically acceptable under the new protocol | 0 |
| Numerically unacceptable | 0 |
| Indeterminate | 92 |
| Insufficient evidence | 0 |

Indeterminate here refers to application-level accuracy, not absence or
uncertainty of the exact objective bounds. No fit is declared unacceptable
merely because its useful certificate has a positive gap.

Historical-versus-new comparison:

| Certified historical gate | New classification | Count |
|---|---|---:|
| Pass | Indeterminate | 91 |
| Failure | Indeterminate | 1 |

These are different assessments, not retrospective corrections of history.
Pilot 21 P10 remains the one certified historical failure. P11/P01/P00 at
replication 21 retain the provenance that the original dataset-level verification
was incomplete, alongside Stage 2C-V's later arm-level certified passes.

`arm_classification_table.csv` contains all 92 rows, including recorded
historical status, certified historical bounds, P, D, verified G, normalized
G, stationarity diagnostics, scale/conditioning information and new classification.
No fitted arm is silently dropped. The 23 KNOWN anchors are explicitly not
optimization tasks and are outside these counts.

## 6. Complementarity, fitted values and indicator stability

The numerical coefficient-stationarity diagnostic for the exactly feasible
dual vectors is at most approximately 3.27e-16 after division by n. This does
NOT imply full exact KKT at the saved coefficients: interior dual values at
nonzero near-tie residuals need not be exact loss subgradients there. The exact
nonzero complementarity gaps quantify that mismatch. It would be incorrect
to substitute these dual vectors into the historical scientific score or
declare the old fixed-sign LP repaired.

### Deterministic fixed probes

For every saved fit, predeclared intercept shifts +/-2**(-40,-30,-20,-10)
were evaluated without refitting. Exact objective gaps against the same
feasible dual and exact sign changes were independently audited. Neither W
nor candidate acceptance was used to choose a step, tolerance or classification.

For **validation_001 P00**, lowering the intercept by 2**-40 gives:

- Fitted-value RMS change: **9.094947017729282e-13**.
- Exact residual sign changes: **44/1000**.
- Mean rank-score change: **+.044** under the unchanged <=0 score convention.
- Certified objective suboptimality upper bound: **3.4864288614396824e-11**.

Raising the same intercept by that tiny amount changes 24 signs and gives a
3.900004615387009e-11 bound. These are evaluations of perturbed coefficients,
not fitted replacements and not new scientific replications.

Across all arms, 91 of the 184 signed 2**-40 probes change at least one sign;
the maximum is 44. All 184 signed 2**-30 probes change signs, up to 72.
This is a direct numerical counterexample to using tiny objective error or
tiny prediction perturbation alone to guarantee raw rank-score stability.

Exact re-evaluation of the original binary64 candidate coefficients also
changes one sign relative to the saved R-computed residuals in each of three
arms: pilot_007 P10, pilot_012 P11 and pilot_015 P10. The saved scientific
residuals and scores are NOT changed by this analysis.

### Previously saved ordinary-QR references

All 23 P00 fits were compared with the ordinary-QR coefficients already
stored in their original RDS records. Only those coefficients were exported;
no ordinary QR was rerun. Exact objectives and dual bounds were recomputed.

The largest maximum fitted-value difference is approximately 1.6758736051e-6
(pilot_011); maximum RMS difference across comparisons is approximately
5.0145657445e-7. Absolute objective differences are at most approximately
1.5734599078e-8. In validation_002, the two saved solutions differ on 67 exact
residual signs despite an objective difference of only about 7.2786e-11.

These comparisons show small fitted-value differences and substantial sign
sensitivity. They do not demonstrate large fitted-value differences among
near-optimal solutions, and they cannot rule such differences out globally.
The word 'material' requires an application budget that has not been defined.

Check loss is piecewise linear, not globally strongly convex. Full column
rank alone does not yield a quadratic objective-to-prediction bound or a
coefficient uniqueness certificate. At rank-score discontinuities, even such
a prediction bound would need residual-margin control to imply sign accuracy.
No universal conversion from the certified G values to primary-score error
has therefore been established.

## 7. Limits and publication interpretation

The certificates rigorously bound optimization error for the explicitly
defined saved-input problems. They do not bound nuisance-estimation error,
prove a correct conditional-density estimator, resolve the original DGP's
density regularity, validate chi-square inference, or establish coverage.

They also do not certify the historical solver's internal rounding path or
prove exact optimality. Normalized objective sizes are descriptive comparisons,
not universal acceptance thresholds. The local probes do not search every
near-optimal coefficient vector or prove global prediction stability.

The preserved executable's <=0 indicator rule and floating arithmetic define
the original reported statistic. A future protocol must decide whether its
target is that reproducible executable behavior or a numerically stable
approximation to a mathematical score. This is a scientific specification
decision, not a reason to rewrite previous results or silently substitute
dual subgradients for the saved indicators.

No evidence here requires blaming the historical outcome optimizer or changing
its solver. Conversely, objective accuracy alone cannot justify calling every
arm numerically acceptable for the intended score comparison.

## 8. Proposed non-destructive continuation plan (NOT IMPLEMENTED)

Continuation is technically reproducible but is not recommended automatically.
The remaining prerequisite is review of an application-level validation policy:
define the numerical estimand, an independently motivated accuracy budget,
and how near-tie signs, indeterminate cases and numerical failures will be
reported. The policy must be fixed without inspecting future W or acceptance.
If numerical acceptability is assessed only for the preserved executable,
state that scope explicitly rather than implying approximation to an exact
optimizer's unique indicator score.

After explicit review/authorization, a non-destructive continuation could:

1. Keep both original Stage 2C and Stage 2C-V immutable.
2. Save the amended validation policy and new output directory, with crosswalks
   to every existing dataset/arm. Apply it consistently to all 92 saved fits.
3. Include replication 21 only with its documented new-policy classification
   and its permanent historical P10 failure flag. No replacement or selective
   refitting/regeneration is permitted.
4. Generate only indices 22-40 from original pilot data seed 2026102901 and
   penalty seed 2026102902, advancing full CMRG streams by the original
   replication-index rule. Preserve n=1000, tau=.90, kappa=1, arms, penalties,
   frozen components, cutoff and all original sample identities.
5. Retain every failure/indeterminate arm and prespecify its treatment in the
   denominator. Do not silently discard observations or tune the policy to
   accept more tasks.
6. Produce separate original-protocol and amended-protocol numerical ledgers;
   preserve the existing 20-replication scientific summary as historical and
   label any later complete analysis separately.

No continuation runner was created and indices 22-40 were not executed.
Recommendation B reflects the unestablished score-accuracy specification,
not missing saved inputs or inability to obtain objective certificates.

## 9. Artifacts and reproducibility

- `PROTOCOL.md`: frozen mathematical criteria and classification rule.
- `reassess.py`: saved-input dual certificates and deterministic probes.
- `audit.py`: independent exact feasibility/objective/complementarity/probe audit.
- `export_references.R`, `reference_review.py`: saved ordinary-QR comparison only.
- `finalize.py`: arm tables, integrity manifests and final preservation.
- `README.md`: execution instructions.

Under the unique reassessment directory:

- `arm_classification_table.csv`, `historical_vs_new_classification.csv`.
- `arm_summary.json` and all per-arm exact certificate/solver/scale records.
- `independent_validation.json`: 92 certificates and 736 probes verified, plus
  independent recheck of Stage 2C-V's P10 witness.
- `stability_probe_table.csv`, per-arm exact probe records.
- `saved_reference_comparison.json/.csv`, saved reference binary exports/logs.
- `initial_state.json`: original source hashes, protocol hash and environment.
- `certification_manifest_check.json`: all Stage 2C-V artifacts verified.
- Protected-file snapshots, `preservation.json`, `final_preservation.json`.
- `source_sha256.json`, `SHA256_MANIFEST.json`, `final_status.json`.

The protocol and generator were not revised after examining reassessment
outcomes. Raw directories are ignored by Git and require separate archival
preservation. No historical file was edited. Stage 2C-P ends here for review.
