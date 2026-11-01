"""Fixed-study tables, scientific report and final integrity manifest; no fits."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,sys
from run_stage2e import HERE,ROOT,read,table,dump,sha,snapshot


def val(r):return F(int(r['numerator']),int(r['denominator']))


def main():
 out=Path(sys.argv[1]).resolve();assert HERE in out.parents
 initial=json.loads((out/'initial_state.json').read_text())
 for name in ['config.json','experiment.R','run_stage2e.py']:
  assert sha(HERE/name)==initial['source_hashes_before_execution'][name],name
 assert json.loads((out/'run_status.json').read_text())['status']=='COMPLETE'
 audit=json.loads((out/'independent_validation.json').read_text());assert audit['status']=='PASS'
 literal=json.loads((out/'binary_tau_verification.json').read_text());assert literal['status']=='PASS'
 rows=read(out/'paired_summary.csv');assert len(rows)==24
 numeric=json.loads((out/'numerical_statuses.json').read_text())
 paths={r['id']:r for r in read(out/'paired_paths_R.csv')}
 full=[];bounds=[]
 lines=['| Case | Offset | H W | LP A W | LP B W | Delta A | Delta B | Changed ranks | Max fitted difference | H gap upper | LP gap upper | Class |',
        '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|']
 for row in rows:
  folder=out/row['id'];h=json.loads((folder/'historical_objective_certificate.json').read_text());i=json.loads((folder/'independent_objective_certificate.json').read_text())
  H,I,D=val(h['primal_objective']),val(i['primal_objective']),val(h['dual_objective']);best=min(H,I)
  bounds.append({'id':row['id'],'historical_error_lower':str(max(F(0),H-best)),
   'historical_error_upper':str(H-D),'independent_error_lower':str(max(F(0),I-best)),'independent_error_upper':str(I-D)})
  n=next(x for x in numeric if x['id']==row['id']);path=paths[row['id']]
  data=dict(row,historical_primal=h['primal_objective']['float'],independent_primal=i['primal_objective']['float'],
   common_exact_dual_lower_bound=h['dual_objective']['float'],historical_error_lower=float(max(F(0),H-best)),
   historical_warning_count=int(row['warnings']),independent_solver_warning_count=len(n['warnings']),
   independent_path_warning_count=int(path['warnings']),LP_iterations=n['LP_iterations'],
   raw_LP_equality_violation=n['original_LP_equality_max_violation'],
   numerical_certificates_status='Exact feasible dual/primal bounds verified',
   literal_binary_tau_certification='PASS; envelope qualification unchanged')
  full.append(data)
  f=lambda name:float(row[name])
  lines.append(f"| {row['dataset']} | {float(row['offset']):+.1f} | {f('historical_W'):.6f} | {f('A_independent_W'):.6f} | {f('B_independent_W'):.6f} | {f('A_delta_W'):+.6f} | {f('B_delta_W'):+.6f} | {int(float(row['rank_changes']))} | {f('prediction_max'):.3e} | {f('historical_certified_gap'):.3e} | {f('independent_certified_gap'):.3e} | {row['classification']} |")
 table(out/'complete_24_problem_table.csv',full)
 dump(out/'suboptimality_intervals.json',bounds)
 paired_table='\n'.join(lines)+'\n'
 (out/'complete_24_problem_table.md').write_text(paired_table,encoding='utf-8')
 before=json.loads((out/'protected_before.json').read_text());after=snapshot()
 preservation={'files_checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
  'missing':sorted(before.keys()-after.keys()),'added_outside_stage2e':sorted(after.keys()-before.keys())}
 assert not any(preservation[k] for k in ['changed','missing','added_outside_stage2e'])
 dump(out/'final_preservation.json',preservation)
 report=REPORT.replace('@@TABLE@@',paired_table).replace('@@RUN@@',out.name).replace('@@COUNT@@',str(len(before)))
 destination=HERE/'STAGE2E_REPORT.md'
 if destination.exists():assert destination.read_text(encoding='utf-8')==report,'Refuse to overwrite a different report'
 else:destination.write_text(report,encoding='utf-8')
 dump(out/'review_commands.json',{'commands':[
  {'argv':['python','-B','journal_validation/stage2e/verify.py',str(out)],'exit_status':0},
  {'argv':['python','-B','journal_validation/stage2e/binary_tau.py',str(out)],'exit_status':0},
  {'argv':['python','-B','journal_validation/stage2e/residual_review.py',str(out)],'exit_status':0},
  {'argv':['python','-B','journal_validation/stage2e/finalize.py',str(out)],'purpose':'report/tables/manifests; no fitting'}]})
 dump(out/'source_sha256.json',{p.name:sha(p) for p in sorted(HERE.iterdir()) if p.is_file()})
 summary=json.loads((out/'summary.json').read_text())
 status={'status':'COMPLETE','paired_candidate_problems':24,'historical_truth_outcomes_reused':8,
  'historical_false_outcomes_fitted':16,'independent_outcomes_fitted':24,
  'classification_counts':summary['classification_counts'],'qualified_layer_A_decision_disagreements':2,
  'qualified_layer_B_decision_disagreements':2,'independent_exact_objective_certificates_verified':48,
  'literal_binary_tau_exact_certificates_verified':48,'independently_verified_W_values':72,
  'historical_config_and_fitting_generators_unchanged_since_start':True,
  'no_new_datasets':True,'no_Stage2C_continuation':True,'preservation':preservation}
 dump(out/'final_status.json',status)
 files=sorted(p for p in out.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json')
 manifest={p.relative_to(out).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in files}
 dump(out/'SHA256_MANIFEST.json',manifest)
 for name,r in manifest.items():assert sha(out/name)==r['sha256']
 print(json.dumps(dict(status,verified_artifacts=len(manifest)),indent=2))


REPORT='''# Stage 2E - Independent solver comparison for DML-IVQR

29 October 2026 (Asia/Tashkent). Branch `journal-validation`.
Base commit `d48972324e4c23e416a157958fcc4a0b26fa9b8a`.
Run: `output/@@RUN@@/`.

## 1. Executive conclusion

**Independently fitted solutions to the same P11 outcome objective produce
opposite DML-IVQR decisions in two of the 24 fixed candidate problems.**
Both disagreements occur in the frozen-component layer AND the complete
original candidate path. Both solution pairs satisfy the predeclared exact
objective-error qualification envelope. This realizes solver-dependent
inference sensitivity, rather than only sensitivity to arbitrary perturbations.

Final classification: **A=21, B=2, C=1**. All 24 pairs remain in the table.
There were zero outcome/LP/path failures and zero recorded estimator warnings.
The C case has exact numerical bounds, but its historical outcome solution
is certifiably outside the frozen comparison envelope; it is not discarded
or relabeled as adequately certified merely because its decisions agree.

No new Monte Carlo datasets were generated, no Stage 2C replication resumed,
and no manuscript, historical file, commit or push was changed. The study
stopped after its fixed 24 paired candidate problems.

## 2. Fixed design, solver and objective equivalence

Datasets: targeted pilot_003 and pilot_014; index-selected pilot_001, pilot_002,
pilot_004, pilot_005, pilot_006, pilot_007. All are original saved Stage 2C
samples at n=1000,p=100,tau=.90,kappa=1. Exact historical R candidate values
are alpha0 plus offsets -.5,0,.5, with alpha0=1+qnorm(.90), approximately
2.2815515655446. Candidate-adjusted responses are computed in historical R
and exported directly, not recomputed by a different normal-quantile library.

All required original data/fit/penalty/RNG artifacts existed. The original
Stage 2C manifest (393 artifacts) was checked before fitting. No substitutes
were generated. Eight truth-candidate historical coefficient vectors and
penalties were reused from saved P11 fits. Their penalty streams were replayed
as an exact input check and their downstream psi/W reproduced. The 16 false
candidate historical outcomes were fitted once using the original quantreg
5.34 rq(method='lasso'), R 3.4.3 and unchanged defaults.

False-candidate pivotal master seed: **2026102905**, L'Ecuyer-CMRG/Inversion.
Full streams 1-16 are assigned in configured dataset order, minus then plus.
Truth uses its original saved full state. Each problem generates/reuses ONE
numeric lambda vector, passed identically to both solvers. The independent
solver makes no penalty draws. Full states, before/after states, hashes and
numeric vectors are retained. Only penalty streams are generated; no data
samples are drawn.

The objective is exactly the requested structural formulation:

    sum rho_tau(y-alpha*D-[1,X]beta) + sum lambda_j*abs(beta_j)/2.

Intercept coefficient zero receives its original positive numeric penalty;
all 100 original slope penalties are retained. No new tie-breaking rule or
post-selection refit is introduced.

The independent solver is SciPy 1.17.1 `linprog(method='highs-ds')`, an explicit
primal LP with blocks beta (101 unrestricted), r_plus (1000 nonnegative),
r_minus (1000 nonnegative), t (101 nonnegative). It has 1000 response
equalities and 202 beta/t inequalities. Matrix dimensions are 1000x2202 and
202x2202. The requested LP formulation, coefficients, half-penalty factor,
intercept, bounds and every block were independently audited.

This algorithm is independent of the historical rqfnb interior-point solver.
LP primal/dual feasibility settings are 1e-10. They do not themselves certify
accuracy. The historical defaults, including rq.fit.lasso eps=1e-6 and
beta=.9995, were unchanged. No package was installed or substituted.

## 3. Numerical certification and fixed qualification

The explicit primal LP supplies a dual witness. Rational scaling toward zero
makes its score box and penalty inequalities exactly feasible. For either
fixed beta, canonical positive/negative residual parts and abs(beta) supply
an exactly feasible primal representation without modifying coefficients.
Independent exact evaluation gives P and D with

    max(0,P-P_other) <= P-P_optimum <= P-D.

Check-loss and L1 complementarity terms are separately nonnegative and sum
exactly to the gap. The independent audit verified all **48 objective/dual
certificates**, not merely solver statuses or printed objectives.

Primary certificate arithmetic uses tau=9/10 and exact rational interpretations
of the exported binary64 X, y*, lambda and beta, consistently with prior stages.
An additional audit independently certified all 48 solutions for the LITERAL
binary64 tau used in the software. Its exact score-box lower endpoint is
tau_binary-1, and its primal objective is evaluated at that same tau. Every
qualification is unchanged. Thus no objective-form or quantile-rounding
substitution explains the reported disagreements.

The frozen Stage 2C-S eta is retained, approximately 5.6290557342834175e-12.
For each candidate response, B=n*max(IQR(y*),unscaled MAD(y*),1). Both exact
gap upper bounds must satisfy G<=eta*B before a pair receives A or B. This is
an observed numerical-accuracy envelope, not a theorem of inferential validity.
No multiplier or threshold was changed after viewing W or coverage.

A: both qualify and both layer decisions agree. B: both qualify and either
layer decision differs. C: qualification/certification does not support an
adequately certified pair under this predeclared rule. C retains raw results
and all diagnostic evidence, rather than being a missing observation.

Across the 24 problems, historical objective-error upper bounds range from
4.64599e-11 to 4.48063e-8; independent-solver bounds range from 1.85402e-12
to 1.62743e-10. Raw independent LP equality residuals are at most 2.132e-13;
inequality and nonnegative-block violations are zero in recorded checks.
The independently evaluated objective and LP-reported objective differ by
at most about 1.365e-12 in floating display. Actual rational certificates,
not those small diagnostics, justify the error bounds.

Independent LP iterations range from 1604 to 1822. Full result objects and
warnings are saved. False-candidate historical fit objects retain their
convergence information. Original internal iteration counts for the eight
reused truth outcomes were not preserved by Stage 2C and are not invented.

## 4. Frozen-component findings (Layer A)

The original candidate's density weights and psi are held fixed; only the
outcome solution is changed. This isolates the outcome-solver implementation.
There are two adequately certified decision disagreements:

| Problem | Historical W | Independent W | Decision | Changed ranks | Max fitted difference |
|---|---:|---:|---|---:|---:|
| pilot_002, alpha0-.5 | 6.3361024310 | 3.0174556529 | Reject -> accept | 19 | 3.77758e-10 |
| pilot_006, alpha0 | 5.4908735661 | 6.0413873521 | Accept -> reject | 14 | 4.87738e-9 |

The cutoff remains the original R binary64 qchisq(.95,2), displayed as
5.99146454710798, with acceptance W<=cutoff. Neither rank indicators nor
critical values are adjusted to improve agreement or coverage.

For pilot_002 minus, historical/independent gap bounds are 1.78822e-10 and
2.85163e-11. For pilot_006 truth, they are 4.99824e-9 and 2.83398e-11. These
are well inside their approximately 2.979e-8 and 3.007e-8 frozen budgets.

For the first disagreement, delta score sum is approximately
(-14.12245,-9.30046); delta unnormalized S11/S12/S22 is
(28.81384,-5.20547,-10.64143). For the second, the corresponding changes
are (-1.48789,-.90601) and (-.21816,-2.20581,1.31276).

Targeted pilot_003 truth changes W from 14.43610 to 9.46101 but both reject;
pilot_014 truth changes 6.34334 to 9.59816 and both reject. The actual solver
experiment is not selected to reproduce the earlier perturbation's direction.
The two decision disagreements arise in index-selected additional cases.

## 5. Complete-path findings (Layer B)

Each outcome solution separately determines original dnorm(e,mean(e),var(e))
and the original sqrt-density-transformed hdm rlasso projections. The ordinary
transformed intercept, raw-scale residual convention, post=FALSE, default
adaptive instrument calibration, uncentered second moment and cutoff are
unchanged. No SD-proxy repair, projection correction or cross-fitting occurs.

The SAME two problems disagree in Layer B, with independent W=3.0174556528
and 6.0413873527 respectively. No additional decision disagreements appear.
The maximum difference between the independent Layer A and B W values is
about 9.56923e-6 (pilot_002 truth), with the same rejection conclusion.

Instrument fitting consumed no RNG in either branch. Independent path startup
states equal the historical post-penalty states; before/after states agree.
Actual last-used adaptive instrument penalty vectors were captured and their
original coefficient replay differences are zero in all 96 instrument checks.
Effective c=.5, gamma=.1/log(1000) and original calibration conventions match.

Numerical instrument penalties do change when residual-dependent transformed
data change: maximum coordinate difference is approximately 6.61428e-5. This
is an expected downstream effect, not a separately changed tuning rule. It
would be incorrect to claim the complete path freezes those numerical vectors.
Maximum density and psi differences are approximately 1.54194e-5 and
6.01036e-6. The source/library conventions are paired exactly; no unpaired
downstream randomness was detected. Layer A and B interpretations remain separate.

## 6. Complete 24-problem comparison

H=historical, LP A=frozen components, LP B=complete path. Gaps are certified
upper bounds; S elsewhere denotes the UNNORMALIZED score second-moment sum.
Offsets are relative to alpha0. The table is rounded for readability; complete
precision, decisions, warnings, failures, objectives and conditioning are in
`complete_24_problem_table.csv` and the exact JSON certificates.

@@TABLE@@

All rows have successful fit/path computations and zero recorded warnings.
The complete CSV gives separate historical/independent acceptance decisions
for both layers, coefficient/prediction differences and failure/status fields.

The C case, pilot_007 minus, has historical gap upper 4.48063e-8, compared
with frozen budget 2.95818e-8. More strongly, the independent feasible primal
proves historical objective suboptimality is at least 4.47758e-8. Thus the
historical vector is demonstrably outside this envelope; this is not simply
a loose or missing certificate. Both raw decisions reject (W 11.13496 versus
9.16911), but the case is NOT counted as an adequately certified agreement.
No new tolerance, retry, replacement or alternative solver was used to admit it.

## 7. Near-optimal solutions, residual arithmetic and nonuniqueness

Across all pairs, 9-23 original-versus-independent residual signs differ.
Maximum fitted-value differences range from 1.26406e-10 to 1.80448e-5; maximum
RMS difference is about 5.74177e-6. Numerical outcome-design condition estimates
range from 89.3964 to 97.6786. Score second-moment conditions range roughly
from 1.0353 to 1.6259 across branches; inversions succeeded. Matrix singularity
is not needed to explain the inference changes.

Both solutions have 25-39 residuals within 1e-7. In the two disagreeing cases,
historical residual magnitudes at changed ranks are at most approximately
1.1244e-10 and 5.6769e-10, while independent residual magnitudes there are at
most approximately 2.1316e-14 and 7.1055e-14. The disagreements concentrate
at numerical near-zero residuals, not substantive fitted-value differences.

The numerical active-constraint matrix (near-zero residual rows plus numerical
zero-coefficient restrictions) has rank 101 except historical pilot_002 truth,
which has rank 100 under the fixed diagnostic 1e-7 thresholds. That case also
has the largest fitted difference. These are near-degeneracy diagnostics, not
proofs of multiple EXACT optima. A nonzero certified gap and a floating active
set cannot distinguish uniquely between different approximations to one optimum,
multiple exact optima, or nearly nonunique solutions.

A separate saved-coefficient diagnostic recomputes residual signs with exact
input algebra, without changing beta or the primary R results. Historical
signs agree with exact algebra in all 24 cases; independent signs differ by
0-7 observations in 21 cases, reflecting their especially tiny vertex residuals.
Nevertheless the same TWO solver disagreements remain under that diagnostic:
pilot_002 minus compares exact-residual W 6.33610 versus 2.84866, and pilot_006
truth compares 5.49087 versus 6.65866. These diagnostic values never replace
the primary preserved-R values or alter classifications.

The evidence therefore distinguishes three facts: both solver coefficient
vectors solve the same objective accurately within quantified bounds in the
B cases; near-zero residual evaluation contributes additional sign sensitivity;
and exact-optimum uniqueness/solution-selection remains unresolved. No new
tie-breaking rule is introduced and no exact-optimality claim is made.

## 8. Implications for historical Monte Carlo results and limitations

The earlier arbitrary-probe concern is now supported by an independently
fitted primal LP comparison. Solver choice can change candidate-level inference
in BOTH complete and frozen paths. One change increases truth rejection;
the other increases acceptance of a false candidate. This is not a method
chosen for better coverage, and it cannot be interpreted as a uniform repair.

This narrow purposive study does NOT establish the frequency or direction of
changes in the archived 500-replication experiment. It contains only eight
saved datasets, one n/tau/kappa setting, three candidates, and correlated
candidate problems within datasets. It does not rerun profiles, compare grid
minimizers/RMSE or evaluate all archived power/coverage cells. Counts are not
population error-rate estimates, and no Monte Carlo significance claim is made.

The empirical accuracy envelope is transparent and frozen but is not a proof
of a universally adequate inferential tolerance. Exact gap certificates bound
objective error, not automatically rank-score error. Both decimal and literal
binary tau problems were certified, but neither establishes every internal
floating operation as exact. Complete-path instrument regressions retain the
historical solver; this experiment isolates a change of OUTCOME solver, not
an independent verification of every downstream optimization.

The original density-regularity problem, proxy definition, residualization,
same-sample fitting and asymptotic chi-square justification remain unresolved.
No manuscript or historical statistic has been changed by this experiment.

## 9. Next scientific task

Keep the large simulation and Stage 2C continuation stopped. The next focused
task should be **exact primal/dual basis and optimal-face analysis of the two
disagreeing problems, pilot_002 minus and pilot_006 truth**, to distinguish
solution nonuniqueness from approximation and residual-evaluation effects.
Use the same saved data/objectives/penalties and preserve both solver results.
Any proposed score/tie policy must be defined scientifically and versioned
separately, not selected because it gives favorable coverage.

Only after that review should numerical reliability criteria and any broader
archived-results sensitivity experiment be authorized. No 500-replication
rerun, new DGP, full profile or continuation was executed here.

## Preservation, commands and evidence index

Initial branch/commit/tree and source hashes are in `initial_state.json`.
The existing untracked Stage 2C work remains untouched. Pre/post and final
SHA-256 preservation cover **@@COUNT@@ files** outside Stage 2E, excluding Git
metadata: zero changed, missing or added outside scope. The config and two
fitting generators were unchanged after execution began. All new files are
under Stage 2E and output directories cannot be reused.

`commands.json` records the two R computation phases with exact arguments,
timestamps and statuses. `review_commands.json` records subsequent no-fit
audits/reporting. Historical data and RNG sources are retained unchanged;
each new historical_task.rds also retains its copied data, outcome lambda,
penalty states, projection coefficients and actual adaptive penalty traces.

- `README.md`, `config.json`, `experiment.R`, `run_stage2e.py`: design/execution.
- `verify_R.R`, `verify.py`: independent saved-trace, LP/objective and W audits.
- `binary_tau.py`: exact certification of the literal software quantile.
- `residual_review.py`: same-coefficient residual-arithmetic diagnostics only.
- `finalize.py`: tables/report/manifests; no fitting.
- `complete_24_problem_table.csv/.md`, `paired_summary.csv`, `paired_paths_R.csv`.
- `actual_instrument_penalties.csv`, `downstream_verification.csv`.
- Per-case LP inputs, full solver results, both coefficients/residuals,
  density/psi/score arrays, primal/dual/complementarity certificates and RDS fits.
- `independent_validation.json`: 48 objective certificates and 72 W evaluations.
- `binary_tau_verification.json`: 48 exact literal-tau certificates.
- `residual_arithmetic_diagnostics.csv`, `suboptimality_intervals.json`.
- Source/output SHA-256 manifests, preservation snapshots, environment and status.

Raw outputs are ignored by Git and require separate archival preservation.
Stage 2E ends here for scientific review.
'''


if __name__=='__main__':main()
