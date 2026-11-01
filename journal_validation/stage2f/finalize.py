"""Scientific report, summary tables and final integrity; no fitting."""
from pathlib import Path
from fractions import Fraction as F
import json,sys
from analyze import HERE,SOURCE,dump,sha,snapshot,read,table


def main():
 run=Path(sys.argv[1]).resolve();assert HERE in run.parents
 assert json.loads((run/'run_status.json').read_text())['status']=='COMPLETE'
 initial=json.loads((run/'initial_state.json').read_text())
 assert sha(HERE/'analyze.py')==initial['source_hashes_before_analysis']['analyze.py']
 audit=json.loads((run/'independent_validation.json').read_text());assert audit['status']=='PASS'
 near=json.loads((run/'independent_near_optimal_validation.json').read_text());assert near['status']=='PASS'
 cases=json.loads((run/'case_summaries.json').read_text());assert len(cases)==2
 summary=[]
 for case in cases:
  id=case['id'];folder=run/id;c=json.loads((folder/'exact_decimal_optimum.json').read_text())
  errors=json.loads((folder/'exact_errors_of_saved_solutions.json').read_text());inference=json.loads((folder/'inference.json').read_text())
  beta0=float(F(int(c['beta_numerators'][0]),int(c['beta_denominator'])))
  summary.append({'id':id,'mechanism':'B primary; C additionally demonstrated; A excluded for certified problem',
   'exact_optimum_unique':c['unique_beta_and_fitted_values'],'exact_primal_equals_dual':c['primal']['float'],
   'exact_intercept':beta0,'intercept_range_width':0,'all_fitted_value_range_widths':0,
   'active_coefficient_count':len(c['active_coefficients_zero_based']),
   'exact_zero_residual_count':len(c['tied_observations_one_based']),
   'historical_actual_suboptimality':errors['historical']['decimal']['exact_suboptimality']['outward_upper'],
   'independent_actual_suboptimality':errors['independent']['decimal']['exact_suboptimality']['outward_upper'],
   'historical_W':inference['historical']['W']['float'],
   'independent_frozen_W':inference['independent_layer_A']['W']['float'],
   'independent_complete_W':inference['independent_complete_path']['W']['float'],
   'exact_outcome_score_at_saved_historical_psi_W':inference['exact_optimum_score_fixed_historical_psi']['W']['float'],
   'changed_observations_one_based':';'.join(map(str,case['changed_observations_one_based'])),
   'all_changed_rows_are_exact_optimum_ties':case['all_changed_observations_exact_optimum_ties'],
   'minimum_tied_dual_box_margin':c['minimum_tied_dual_box_margin']['float'],
   'minimum_inactive_penalty_margin':c['minimum_inactive_penalty_margin']['float']})
 table(run/'case_summary_table.csv',summary)
 before=json.loads((run/'protected_before.json').read_text());after=snapshot()
 preservation={'files_checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
  'missing':sorted(before.keys()-after.keys()),'added_outside_stage2f':sorted(after.keys()-before.keys())}
 assert not any(preservation[k] for k in ['changed','missing','added_outside_stage2f'])
 dump(run/'final_preservation.json',preservation)
 report=REPORT.replace('@@RUN@@',run.name).replace('@@COUNT@@',str(len(before)))
 target=HERE/'STAGE2F_REPORT.md'
 if target.exists():assert target.read_text(encoding='utf-8')==report,'Refuse to overwrite a different report'
 else:target.write_text(report,encoding='utf-8')
 dump(run/'technical_attempts.json',{'initial_attempt':'output/exact_face_20261029T102522Z',
  'initial_issue':'New-source support verification assertion used != rather than ==; corrected after direct equality checks.',
  'second_issue':'Independent-audit JSON conversion of NumPy integer; converted to Python int; mathematical checks had passed.',
  'no_input_tolerance_or_historical_code_changed':True,'completed_attempt':run.name})
 dump(run/'review_commands.json',{'commands':[
  ['python','-B','journal_validation/stage2f/analyze.py'],
  ['python','-B','journal_validation/stage2f/verify.py',str(run)],
  ['python','-B','journal_validation/stage2f/near_optimal.py',str(run)],
  ['python','-B','journal_validation/stage2f/verify_near_optimal.py',str(run)],
  ['python','-B','journal_validation/stage2f/representation_split.py',str(run)],
  ['python','-B','journal_validation/stage2f/finalize.py',str(run)]],
  'note':'Only exact reconstruction, witness verification and saved-coefficient representation diagnostics; no new data or candidate problem.'})
 dump(run/'source_sha256.json',{p.name:sha(p) for p in sorted(HERE.iterdir()) if p.is_file()})
 final={'status':'COMPLETE','problems':2,'exact_optimum_certificates_verified':audit['exact_optimum_certificates'],
  'unique_optimum_proofs':audit['unique_optimum_proofs'],'arbitrarily_near_optimal_frozen_decision_noninvariance_proofs':near['general_noninvariance_proofs'],
  'classification':'Both cases B primary (unique exact optimum); C residual arithmetic/representation effects coexist.',
  'regularity_controlled_DGP_simulation_decision':'Do not start yet: define and validate numerical score evaluation policy first.',
  'no_new_candidate_problems':True,'no_Monte_Carlo':True,'no_Stage2C_continuation':True,'preservation':preservation}
 dump(run/'final_status.json',final)
 files=sorted(p for p in run.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json')
 manifest={p.relative_to(run).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in files}
 dump(run/'SHA256_MANIFEST.json',manifest)
 for name,r in manifest.items():assert sha(run/name)==r['sha256']
 print(json.dumps(dict(final,verified_artifacts=len(manifest)),indent=2))


REPORT='''# Stage 2F - Optimal-face analysis of two DML-IVQR disagreements

29 October 2026 (Asia/Tashkent). Branch journal-validation.
Commit: d48972324e4c23e416a157958fcc4a0b26fa9b8a.
Completed analysis: `output/@@RUN@@/`.

## Executive conclusion

**Both saved optimization problems have a UNIQUE exact optimum.** Independent
exact primal-dual certificates prove optimality and strict dual margins plus
nonsingular active systems prove uniqueness of coefficients and fitted values.
The proof holds for both rational tau=9/10 and the literal software binary64 tau.

For both disagreements, the primary classification is **B: a unique exact
optimum exists, but numerically near-optimal solutions produce different rank
indicators**. Mechanism **C** (floating residual arithmetic/representation) is
also directly demonstrated. Mechanism A, multiple exact optimal coefficient
solutions, is excluded for these precise saved-input problems. Mechanism D
is no longer needed for their optimum-uniqueness question.

Every differing historical/independent rank occurs at an observation whose
residual is EXACTLY ZERO at the unique optimum: 19 changed signs among 29
exact ties in pilot_002 minus, and 14 among 33 in pilot_006 truth.

A stronger local result is proved: under frozen historical instruments,
opposite decisions are possible for mathematically near-optimal coefficient
vectors within EVERY positive objective-error budget, however small. Thus
tightening an objective-gap tolerance alone cannot guarantee score/decision
stability. This is not a claim about the frequency of floating solver errors,
nor a theorem about every complete downstream candidate path.

**Decision: do not begin the regularity-controlled DGP simulation yet.** Define
and validate the numerical score-evaluation policy first. No new policy,
estimator, data, candidate problem, Monte Carlo or continuation was implemented.

## 1. Preserved scope and exact problem

Only Stage 2E `pilot_002_minus` (alpha0-.5) and `pilot_006_truth` (alpha0) are
analyzed. Both use n=1000,p=100,tau=.90,kappa=1 and the original P11 penalties
on intercept and all slopes. Responses, designs, candidate values, lambda,
both coefficient vectors, R residuals and both downstream branches are copied
from the saved Stage 2E records. No outcome solver or numerical LP optimizer
was rerun. Exact linear algebra reconstructs certificates on the proposed
basis of these SAME two problems.

The Stage 2E manifest (859 artifacts) was checked. Its 21 A / 2 B / 1 C
classifications are preserved. The inconclusive pilot_007 minus is not analyzed
or reinterpreted here. Source/hash checks confirm original coefficients and
response/penalty inputs to the two solvers are the same exported arrays used
by the independently audited Stage 2E primal LP. Candidate values are retained
from the original R calculation; no normal quantile is substituted.

The exact objective is

    Q(beta)=sum rho_tau(y-alpha*D-Xt beta)+sum lambda_j |beta_j|/2,

with Xt=[1,X], beta unrestricted. The dual is maximize y*'v subject to
tau-1<=v_i<=tau and |Xt_j'v|<=lambda_j/2. All lambda_j are positive, including
the intercept. Stored binary64 X, y*, lambda and saved coefficients are treated
as exact rational inputs. Separate certificates cover tau=9/10 and literal
binary64 tau; they have the SAME unique beta, although objective values depend
slightly on tau. No intended-objective or quantile-rounding ambiguity remains.

## 2. Exact optimum, certified errors and optimal-face ranges

The independent LP fit proposed a numerical active coefficient set and
near-zero residual rows using a 1e-7 DIAGNOSTIC band. This band was not used
as a rank/tie definition. Exact reconstruction then verifies the support and
zero residual rows WITHOUT tolerance.

| Quantity (tau=9/10 display) | pilot_002 minus | pilot_006 truth |
|---|---:|---:|
| Historical primal | 662.0670813176204 | 637.5173423715748 |
| Independent primal | 662.0670813174701 | 637.5173423666050 |
| Exact optimum = exact dual | 662.0670813174700 | 637.5173423666047 |
| Historical TRUE suboptimality | 1.5042861671e-10 | 4.9702372659e-9 |
| Independent TRUE suboptimality | 1.2311385492e-13 | 3.4126401859e-13 |
| Exact-optimum active coefficients | 29 | 33 |
| Exact zero residuals | 29 | 33 |
| Exact-optimum intercept | .9087272196635814 | .8715634718853877 |
| Active-basis condition (floating diagnostic) | 294.5374 | 153.8785 |

The exact optimum value enclosure has ZERO width: Q*=D* is recorded as a
rational, not merely as these rounded decimals. Historical and independent
errors are now exact differences from Q*, not just previous feasible-dual
upper bounds. All four original primal feasibility/objective evaluations are
checked; unrestricted beta admits canonical nonnegative residual/absolute-value
variables. No coefficient vector is altered to make its certificate pass.

The historical-versus-independent maximum coefficient differences are about
4.64824e-10 and 6.91783e-9; maximum fitted-value differences are about
3.77758e-10 and 4.87738e-9. Independent coefficients are much closer in objective
value, but this does not imply a corresponding monotone improvement in W.

Historical coefficient errors relative to the exact optimum have maxima
4.64728e-10 / 6.91781e-9; independent maxima are 9.57707e-14 / 7.27109e-14.
Historical maximum fitted errors from the exact optimum are
3.77702e-10 / 4.87752e-9; independent maxima are 7.44473e-14 / 1.76465e-13.

The optimal-face intercept range is a singleton at the value above. EVERY
coefficient and EVERY one of the 1,000 fitted values also has a singleton
range, width exactly zero. `optimal_face_ranges.csv` displays all fitted
values; the certificates retain their exact common-denominator representations.
No numerical min/max face search is needed once uniqueness has been proved.

## 3. Uniqueness proof and degeneracy

Let S be active coefficients and T exact-zero residual rows. The square
Xt[T,S] matrices have dimensions 29x29 and 33x33 and exact nonzero determinants.
Exact integer elimination reconstructs beta_S satisfying y*_T=Xt[T,S]beta_S,
with beta outside S zero. A dual vector sets nonzero-residual observations to
their required endpoints and solves the active coefficient gradient equations.

Both primal and dual are exactly feasible and Q=D. The independent verifier
uses separate Fraction arithmetic and rational Gaussian determinant evaluation.
It verifies all box/penalty constraints, support, exact zero set and zero gap.

The decisive strict margins are:

| Margin | pilot_002 minus | pilot_006 truth |
|---|---:|---:|
| Minimum distance of v_T from box endpoints | .0249303482 | .0283199411 |
| Minimum inactive coefficient penalty slack | .1702019317 | .0626513892 |

For ANY optimizer, zero complementarity with this exact dual forces all
residuals in T to zero (v_T strictly interior), and all inactive beta to zero
(their dual penalty inequalities strictly slack). Nonsingular Xt[T,S] then
forces beta_S to the reconstructed value. This proves global coefficient
uniqueness for the exact saved-input optimization problem, not merely local
uniqueness in a numerical neighborhood.

The dual scores are likewise fixed on nonzero residuals and determined on T
by the nonsingular active equations. Auxiliary LP zeros/bounds can permit
basis degeneracy or redundant active constraints without implying multiple
optimal points. We do not use the number of simplex bases as a uniqueness test.

No materially different residual sign vector is possible among EXACT
minimizers: there is only one coefficient/fitted-value vector, and <=0
unambiguously includes its exact zero residuals. Near-optimal points are a
different set and must not be called exact minimizers.

## 4. Residual signs responsible for the two discrepancies

All changed ranks belong to the certified exact-zero residual set.
Observation identifiers are one-based, in original dataset order:

- pilot_002 minus: **87, 97, 183, 296, 314, 338, 393, 412, 540, 577, 584,
  596, 655, 880, 920, 925, 927, 934, 957**.
- pilot_006 truth: **101, 149, 181, 327, 371, 567, 588, 595, 597, 630, 743,
  869, 935, 963**.

Neither historical nor independent floating solution has to place these
mathematically tied observations at literal floating zero. Tiny signed errors
on either side change the raw indicator. At a mathematical zero, the check-loss
optimizing subgradient is interval-valued; it is NOT interchangeable with the
specified raw indicator score, which equals tau-1 at e=0. No subgradient was
substituted into the scientific score in this analysis.

## 5. Score and second-moment decomposition: frozen layer

Using historical psi_H in both branches, with g=sum psi*s and unnormalized
S=sum psi*psi'*s^2:

| Case / branch | g1 | g2 | S11 | S12 | S22 | W | W-cutoff |
|---|---:|---:|---:|---:|---:|---:|---:|
| pilot_002 H | 15.93441 | 35.66744 | 216.59027 | 4.19087 | 242.20184 | 6.3361024310 | +.3446378839 |
| pilot_002 I, frozen | 1.81196 | 26.36698 | 245.40412 | -1.01460 | 231.56040 | 3.0174556529 | -2.9740088942 |
| pilot_006 H | -21.26046 | -28.55945 | 197.30274 | 23.93273 | 213.84109 | 5.4908735661 | -.5005909810 |
| pilot_006 I, frozen | -22.74834 | -29.46546 | 197.08458 | 21.72692 | 215.15385 | 6.0413873521 | +.0499228050 |

The cutoff remains the exact stored historical binary64 value displayed as
5.99146454710798. All W calculations and cutoff-side decisions were verified
with exact rational arithmetic conditional on stored psi and score values.

Individual additive contributions are

    delta g_i = psi_H,i*(s_I,i-s_H,i),
    delta S_i = psi_H,i*psi_H,i'*(s_I,i^2-s_H,i^2).

At tau=.90, squared scores switch between .01 and .81. The 19 changed rows
sum to delta g=(-14.1224493,-9.3004611), delta S11/S12/S22=
(28.8138443,-5.2054664,-10.6414344). The 14 changed rows sum to
(-1.4878878,-.9060130) and (-.2181604,-2.2058102,1.3127579).
Every row's contributions and residuals/psi/ranks are saved in
`observation_decomposition.csv` and `changed_observations.csv`. The sums were
independently checked EXACTLY. W is nonlinear in g and S, so these are not
misrepresented as additive observation-level contributions to W itself.

## 6. Complete-path layer and exact-optimum diagnostics

The original Stage 2E complete paths are preserved and independently checked:

| Case | H complete W | I complete W | Decision |
|---|---:|---:|---|
| pilot_002 minus | 6.3361024310 | 3.0174556528 | Reject -> accept |
| pilot_006 truth | 5.4908735661 | 6.0413873527 | Accept -> reject |

The complete-path difference is decomposed into the frozen sign effect plus
the projection term (psi_I-psi_H)*s_I for g and
(psi_I psi_I'-psi_H psi_H')*s_I^2 for S. Additional projection changes in
delta g are about (-1.68e-10,-5.28e-10) and (8.83e-10,-2.46e-9);
second-moment projection changes are also around 1e-9. Exact decompositions
confirm the dominant effect is the changed rank pattern, not changed instruments.
No downstream component is refitted in Stage 2F; these are the saved original
complete candidate paths under unchanged conventions.

For the unique mathematical outcome optimum, all its exact ties satisfy <=0.
Evaluating THAT score with historical fixed psi gives W=5.1744454935 and
2.8064740967 (both accept). Using the saved independent psi gives nearly
identical values 5.1744454935 and 2.8064740974. These are clearly labeled
conditional fixed-psi diagnostics, NOT a newly recomputed native complete
path at beta*. No exact-optimum full-path inference value is claimed.

## 7. Exact versus near-optimal sets: uniform-in-accuracy result

The unique exact optimal face has one coefficient/rank vector. For specified
fixed psi and exact residual evaluation, inference over that face is therefore
invariant by proof, not by a finite search. This does not imply numerical
inference is stable over NEAR-optimal coefficient vectors.

For each historical and independent rank pattern, its non-tied observations
have the same signs as the exact optimum. Nonsingular Xt[T,S] allows a
direction d, supported on S, satisfying Xt[T,S]d_S=-z, where z_i is +1 or -1
according to the desired tied-residual sign. Then beta*+h*d has residual h*z
on T. For sufficiently small positive h, all non-tied residual signs and
active coefficient signs remain fixed.

The certificates give an exact positive h0 guaranteeing these sign conditions
and an objective Lipschitz bound

    L=sum_i |Xt_i d| + sum_j lambda_j |d_j|/2.

For EVERY epsilon>0, choose 0<h<=min(h0,epsilon/(2L)). The vector is strictly
nonoptimal by uniqueness, has 0<Q-Q*<=epsilon/2, and exactly reproduces the
chosen historical or independent rank pattern. Those patterns give opposite
frozen-psi decisions. Thus **frozen inference is noninvariant over every
positive near-optimal objective neighborhood** for both cases.

Four exact rational witness vectors demonstrate epsilon=1e-20; their actual
positive objective errors are approximately 8.11e-24, 3.74e-23, 2.38e-23 and
2.20e-23. Independent checks verify all 1,000 signs, primal objectives, direction
constraints and W values. This is a mathematical certificate, not a random
perturbation or an assumed near-optimality label.

These extremely small rational directions are not claimed to be distinguishable
as separate binary64 solver outputs. The general proof concerns objective-only
control and frozen historical psi. It does NOT prove a native adaptive
projection-path limit for every epsilon. Native-path noninvariance under the
previous fixed accuracy envelope remains established by the two saved Stage 2E
solutions, not by extrapolating this frozen-layer theorem.

## 8. Floating residual evaluation: mechanism C in addition to B

For the SAME stored independent coefficient vector, exact input algebra and
the original R residual evaluation differ on two signs in pilot_002 minus
and four in pilot_006 truth. Historical coefficient vectors have no such
same-vector discrepancies in these two cases. Replacing only residual algebra
with exact evaluation does not remove the original cross-solver discrepancy:
Stage 2E's diagnostic frozen W comparisons are 6.33610 versus 2.84866 and
5.49087 versus 6.65866, still on opposite sides.

A separate representation experiment evaluates the unique rational beta*,
its nearest binary64 coefficient vector under exact algebra, and that same
binary64 vector under original R matrix arithmetic. No optimization or new
solution-selection rule is used:

| Representation, fixed historical psi | pilot_002 W | pilot_006 W |
|---|---:|---:|
| Rational beta*, exact residuals | 5.17445 | 2.80647 |
| Rounded beta*, exact residual algebra | 3.16299 | 13.57863 |
| Same rounded beta*, original R residuals | 4.26077 | 7.03782 |

Coefficient rounding alone changes 29 and 33 ranks relative to the mathematical
optimum. For the same rounded coefficients, residual arithmetic changes 21
and 16 signs. Combined representation differences are eight and 17; R produces
seven and nine literal zero residuals, compared with 29 and 33 mathematical
zeros. These counts are not added as though disjoint effects.

This separates approximation of a unique coefficient vector from arithmetic
evaluation of an unchanged finite vector. Both contribute to the practical
problem. None of the diagnostic scores replaces historical results, and no
new near-zero threshold changes the original <=0 convention.

## 9. Mechanism classification and numerical policy

| Case | A: multiple exact optima | B: unique optimum / near-optimal rank differences | C: residual arithmetic | D: insufficient evidence |
|---|---|---|---|---|
| pilot_002 minus | Excluded by exact uniqueness proof | Established; primary mechanism | Demonstrated; additional effect | Not needed for certified questions |
| pilot_006 truth | Excluded by exact uniqueness proof | Established; primary mechanism | Demonstrated; additional effect | Not needed for certified questions |

Deterministic LP tie-breaking is NOT the missing remedy for these two exact
problems: there is only one beta*. Merely lowering solver tolerances is also
not a sufficient rank-accuracy criterion, as the uniform-in-epsilon proof shows.

A scientifically justified candidate policy is: preserve the original
objective and <=0 mathematical score; obtain certified primal/dual solutions;
certify residual signs, including exact zero where a valid optimal basis
proves it; explicitly flag unresolved cases. Fix arithmetic, data ordering,
penalty streams and software environment. Do not round all small residuals
to zero using an outcome-selected threshold, and do not substitute dual
subgradients for the scientific indicator without a separate methodological
definition and theory review.

For other problems with actual multiple optima, a predeclared lexicographic
or optimal-face secondary criterion could define a deterministic selection.
That would be a substantive selection convention. Adding an epsilon ridge
to the primary loss is not the same objective and must not be hidden as
tie-breaking. No such rule is implemented here.

Even faithful certified evaluation of the original mathematical <=0 rule is
a NEW COMPUTATIONAL VERSION relative to the archived floating executable.
Changing the score/tie functional would be a new estimator definition. Either
requires versioning and newly produced simulation evidence before claims
about that version can use revised numerical results. Do not choose the rule
because one version happens to have better coverage.

## 10. Publication and historical Monte Carlo implications

The disagreements are attributable to near-optimal approximations around a
unique optimum, with additional floating residual-evaluation effects, not
multiple exact minimizers in these cases. This is stronger and more specific
than Stage 2E's unresolved uniqueness assessment.

The original simulations may still be reported honestly as outputs of the
preserved implementation. Their numerical values are not overwritten or
declared fraudulent/incorrect records. They cannot automatically be presented
as solver-invariant properties of a mathematically specified P11 procedure.
This two-case selected analysis estimates no population instability frequency
and does not quantify how many archived 500-replication results would change.

The journal paper should disclose the two selected cases, identical objectives
and penalties, exact uniqueness/error certificates, near-zero-rank mechanism,
both evaluation layers, and limits of generalization. Distinguish numerical
reproducibility from numerical stability and inferential validity. A different
LP algorithm alone is not established as a calibration repair.

A reviewed numerical score-evaluation policy is essential before further
simulations intended to represent reliable mathematical inference. Continuing
only a study of the legacy executable would require an explicitly narrower
scientific claim. No existing article text was changed in this task.

## 11. Decision before the regularity-controlled DGP

**NO: do not start a regularity-controlled DGP Monte Carlo experiment yet.**
Bounding treatment away from zero addresses population density regularity;
it does not remove in-sample quantile-regression residual ties or this numerical
discontinuity. Changing the DGP first would conflate the population and
computational issues.

Minimum additional work: review and freeze a versioned residual-sign/solution
evaluation policy grounded in the estimator's mathematical definition, then
validate it prospectively on the existing fixed Stage 2E panel, retaining
all legacy results and unresolved cases. This need not be a 500-replication
rerun. The policy must not be tuned to favorable inference. Once that
computational definition is settled, complete the bounded-DGP analytical
assumption checks before authorizing new simulation evidence.

No new selection policy, additional candidate, new sample, resumed Stage 2C,
manuscript edit, commit or push occurred here. Stage 2F ends for review.

## Reproducibility, integrity and technical provenance

All new material is under Stage 2F. Pre/post and final SHA-256 checks protect
**@@COUNT@@ existing files** outside this directory, excluding Git metadata:
zero changed, missing or added outside scope. Original Stage 2E outcomes and
its C case remain intact. The completed reconstruction generator is unchanged
since its run began. Exact arrays, matrices, basis determinants, strict margins,
primal/dual values and witness vectors are retained for independent checking.

An initial attempt `output/exact_face_20261029T102522Z` is preserved. A new-source
support assertion accidentally tested inequality rather than equality; direct
equation/support checks identified that coding error and the assertion was
corrected. No data, basis rule, tolerance or historical fit changed. The new
unique directory contains the completed result. An audit JSON NumPy-integer
serialization issue was separately corrected; mathematical checks had already
passed, and existing R representation diagnostics were retained rather than
rerun. These are implementation/reporting issues, not scientific exclusions.

Scripts: `analyze.py`, `verify.py`, `representation.R`, `near_optimal.py`,
`verify_near_optimal.py`, `representation_split.py`, `finalize.py`; instructions
are in `README.md`. Under the completed run:

- `case_summary_table.csv`, `case_summaries.json`.
- Per case `saved_inputs.npz`, exact decimal/binary optimum certificates,
  exact errors of saved solutions, and singleton optimal-face ranges.
- Full observation/sign/score decompositions and changed-observation tables.
- Exact inference records and independently verified decomposition identities.
- Four exact near-optimal rational witnesses and the uniform direction proof.
- Rounded-representation diagnostic arrays, R logs and separated error counts.
- `independent_validation.json`, `independent_near_optimal_validation.json`.
- Initial state/source hashes, input integrity check, preservation snapshots,
  final preservation, technical provenance, source/output manifests and status.

Raw output is ignored by Git and must be preserved separately when sharing.
'''


if __name__=='__main__':main()
