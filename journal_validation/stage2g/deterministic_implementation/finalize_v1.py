"""Generate final feasibility report and integrity/preservation manifests."""
import sys
sys.dont_write_bytecode=True
from common_v1 import *
def main():
 s=load(OUT/'summary.json');comparison=rows(OUT/'three_path_comparison.csv');outcomes=rows(OUT/'outcome_validation.csv')
 instruments=rows(OUT/'instrument_validation.csv');bench=rows(OUT/'runtime_benchmarks.csv');plans=rows(OUT/'runtime_projections.csv')
 verification=load(OUT/'independent_verification.json');calibration=rows(OUT/'calibration_validation.csv')
 assert s['passed']==24 and s['unresolved']==0 and verification['passed']==24
 assert all(r['status']=='PASS' for r in calibration)
 env=load(OUT/'environment.json');env.update({'longdouble_significand_bits':np.finfo(np.longdouble).nmant+1,'longdouble_bytes':np.dtype(np.longdouble).itemsize})
 dump(OUT/'environment.json',env)
 numerics=[load(OUT/id/'outcome_numerics.json') for id in cases()]
 ic=[load(OUT/id/f'instrument_{j}_certificate.json') for id in cases() for j in (1,2)]
 native_ic=[load(OLD/id/'C'/f'instrument_{j}_certificate.json') for id in cases() for j in (1,2)]
 def maximum(key):return max(float(r[key]) for r in numerics)
 case_lines=[]
 for r in comparison:
  dec=lambda x:'accept' if str(x).upper()=='TRUE' else 'reject'
  case_lines.append(f"| {r['id']} | {float(r['historical_W']):.6f} / {dec(r['historical_accepted'])} | {float(r['Policy_C_W']):.6f} / {dec(r['Policy_C_accepted'])} | {float(r['proposed_W']):.6f} / {dec(r['proposed_accepted'])} | [{float(r['W_lower']):.12f}, {float(r['W_upper']):.12f}] |")
 case_table='\n'.join(case_lines)
 projection_table='\n'.join(f"| {r['scenario']} | {int(r['candidate_evaluations']):,} | {float(r['serial_hours_proxy']):.2f} | {float(r['ideal_5_worker_hours_proxy']):.2f} | {float(r['serial_hours_if_independent_audit_every_candidate']):.2f} | {float(r['retained_candidate_storage_GiB_proxy']):.1f} |" for r in plans)
 input_manifest={}
 def add(p,category):
  input_manifest[p.relative_to(ROOT).as_posix()]={'sha256':sha(p),'bytes':p.stat().st_size,'category':category}
 for id in cases():
  for p in (E/id).iterdir():
   if p.is_file():add(p,'original observations, candidate, penalties, RNG and historical comparison inputs')
  for name in ['exact_optimum.json','accuracy.json']:add(G/'results'/id/name,'exact outcome reference and historical objective accuracy')
  for p in (OLD/id/'C').iterdir():
   if p.is_file():add(p,'Policy C density, adaptive, projection and inference references')
 add(E/'cutoff.bin','unchanged cutoff bytes');add(E/'complete_24_problem_table.csv','complete fixed panel and candidate parameters')
 add(ROOT/'thesis_extension/config/extension_config.R','existing planning configuration, not authorization to execute')
 # Shared exact utilities are inputs to the versioned implementation.
 for p in [ROOT/'journal_validation/stage2f/analyze.py',ROOT/'journal_validation/stage2f/verify.py',
  ROOT/'journal_validation/stage2c/certification/exact_bounds.py',G/'full_path_validation/audit.py',
  G/'full_path_validation/common.py',G/'full_path_validation/verify_certificates.py',
  ROOT/'journal_validation/stage2b/diagnostics.R',ROOT/'thesis_extension/environment/check_author_environment.R']:
  add(p,'read-only numerical or environment utilities')
 dump(HERE/'INPUT_SHA256_MANIFEST.json',input_manifest)
 payload=s['mean_retained_candidate_payload_bytes']/1024**2
 report=f'''# Stage 2G-D — Deterministic high-accuracy implementation feasibility

2 November 2026, Asia/Tashkent. Version **2G-D.1**. Branch
`{env['branch']}`, starting HEAD `{env['HEAD']}`.

## Executive conclusion

**CONDITIONAL for Stage 2H overall. The numerical core is promising and
practical for a limited n=1000 pilot, but the full planned design is not yet
costed or validated at n=500 / other quantiles.** Stop after this feasibility
report; no Stage 2H or Monte Carlo was started.

All **24/24** fixed-panel candidates pass the new pipeline and the independent
audit, with **0 unresolved cases**. All **24,000 residual ranks agree with
Policy C**, and all **24 rejection decisions agree**. All **48** new final
instrument optima are certified unique for exactly the original final penalty
inputs. Maximum W change from native Policy C is
**{s['max_abs_W_change_from_C']:.6g}**, with no cutoff crossing. Historical A
differs in **{s['historical_decision_disagreements']}/24** decisions, retained
explicitly rather than suppressed.

The measured cost is **{s['mean_point_pipeline_seconds']:.3f} s/candidate** for
point computation and **{s['mean_qualified_pipeline_proxy_seconds']:.3f} s/candidate**
when the new certificates and inference qualification are included. A separate
independent audit costs another **{s['independent_audit_mean_seconds']:.3f} s/candidate**.
Raw prototype artifacts average **{payload:.2f} MiB/candidate**. Solver success
alone therefore understates both computational and storage cost substantially.

## 1. Numerical policy selected and pathway changes

Select **B-v1: exact-certified outcome ranks, preserved native adaptive
calibration, and deterministic high-accuracy final fixed-penalty solves**.
The precise contract is `IMPLEMENTATION_CONTRACT_v1.md`; settings are frozen
in `CONFIG_v1.json`, without decision- or coverage-driven tuning.

| Path | Outcome / signs | Instrument calibration and final solve |
|---|---|---|
| A: historical | Archived approximate outcome and historical residual evaluation | Archived historical native adaptive path |
| Policy C reference | Exact certified optimum and <=0 ranks | Original native adaptive path and its finite final fit |
| Proposed B-v1 | Independently assembled HiGHS-IPM LP, new exact basis certificate, exact <=0 ranks | Replay original adaptive path; preserve last-used penalties; replace only final fixed-objective numerical solve |
| Modified calibration C | Not implemented | Would feed refined fits into recalibration, potentially changing penalties; not equivalent to B without new evidence |

The new LP uses split positive/negative coefficients and residuals, rather
than the older free-coefficient/epigraph dual-simplex formulation. It uses
recorded deterministic solver settings, single-thread operation and repeats
each solve. Its proposed support/tied rows undergo exact rational checks.
The saved Stage 2G optimum is consulted only after reconstruction to compare
results, never to supply the basis or rank vector.

Instrument optimization uses zero initialization, ascending-column cyclic
coordinate descent (absolute KKT target 1e-10, at most 10,000 sweeps) and
direct active-set polish. Its proposed active set is then verified rationally.
A fresh inverse-Gram witness is built and checked exactly. The numerical
optimizer is not replaced by the archived exact reference coefficients.

`np.longdouble` has **{env['longdouble_significand_bits']} significand bits** and
{env['longdouble_bytes']} bytes on this Windows build: it gives no extra
precision over binary64. High accuracy here comes from convergence, polish
and exact verification, not an assumed extended-precision accumulator.

## 2. Mathematical equivalence: established scope

The original objective is preserved:
`sum rho_tau(y*-X beta) + sum lambda_j |beta_j|/2`, with the original positive
intercept penalty, saved numerical lambda and literal binary64 tau. Each
accepted outcome certificate proves exact primal feasibility, dual feasibility,
KKT, primal=dual and uniqueness for these input bytes.

The density remains `dnorm(e, mean(e), var(e))`, using sample variance as the
normal scale. Residuals are rounded once from the exact rational optimum;
authoritative ranks are carried separately. The transformed regression retains
an ordinary unpenalized intercept, followed by the original unweighted
`psi=Z-[1,X]gamma`. No weighted-intercept substitution, ridge, corrected
density formula or changed penalty is introduced.

The original R adaptive calibration was rerun online for all 24 cases.
**All density, native calibration-fit and final penalty bytes match Policy C**.
Original post-outcome-penalty RNG states are restored and unchanged. No new
random draws or pivotal-penalty simulation occur. Captured calibration traces,
last-used lambda and subsequently reported next lambda are stored separately.

For each exported centered design and last-used lambda, the new solver targets
the same mathematical problem:
`F(b)=||yc-Xc b||^2 + sum lambda_used,j |b_j|`.
All 48 exact reference optima reconstructed from the new solver agree exactly
with Policy C's fixed-objective reference optima. This establishes mathematical
equivalence of these final objectives and their penalty inputs, while the
returned approximate coefficients improve substantially.

Equivalence is **not** claimed to a recalibrated high-accuracy adaptive
trajectory, an adaptive fixed point, or bitwise historical A output. Refined
fits are never fed back into penalty calibration. Historical A and exact
outcome inference differ because approximate outcome ranks can differ.

The GMM moments are unchanged: `s=tau-r`, `z_i=psi_i*s_i`, `g=sum z_i`,
`S=sum z_i z_i'`, `W=g' solve(S,g)`. S is unnormalized. The unchanged cutoff
bytes display as **5.99146454710798**. Numerical equivalence and reproducibility
do not establish identification, regularity, asymptotic validity or coverage.

## 3. Outcome optimization, accuracy and ambiguity

| Check | Fixed-panel result |
|---|---:|
| Independent LP solves / repeated solutions | 24 pass; all repeats bitwise identical |
| Exact primal / dual / KKT / zero-gap optimum certificates | 24 pass |
| Exact uniqueness proofs | 24 pass |
| Exact ties | {sum(int(r['ties']) for r in outcomes)} |
| Certified rank disagreements with Policy C | 0 / 24,000 |
| Raw floating LP rank disagreements | {s['raw_LP_sign_disagreements']} / 24,000 |
| Maximum LP true objective gap above certified optimum | {s['max_LP_true_gap']:.6g} |
| Maximum raw LP fitted-value error | {s['max_LP_fitted_error']:.6g} |
| Maximum raw LP coefficient error | {maximum('LP_coefficient_max_error'):.6g} |
| Maximum split-LP equality violation | {maximum('primal_equality_max'):.6g} |
| Maximum numerical dual box violation | {maximum('dual_score_box_violation'):.6g} |
| Maximum numerical dual penalty violation | {maximum('dual_penalty_violation'):.6g} |
| Maximum split-LP stationarity residual | {maximum('split_KKT_stationarity_max'):.6g} |
| Maximum split-LP complementarity residual | {maximum('split_KKT_complementarity_max'):.6g} |

Numerical LP residuals are diagnostics; exact certification supplies the
authoritative feasible zero-gap optimum. High LP accuracy alone does not
resolve rank ambiguity: the {s['raw_LP_sign_disagreements']} raw disagreements
persist even with fitted-value errors below {s['max_LP_fitted_error']:.3g}.
Every authoritative rank is computed from exact residuals, with exact zero
assigned rank one under the unchanged <=0 convention.

The 1e-7 basis proposal threshold does not define a residual tie. A proposed
square basis must pass exact equations, all residual signs, dual box and
penalty feasibility, zero gap and strict-margin uniqueness. If it fails,
return OUTCOME_UNRESOLVED; non-square/degenerate/nonunique/unproved cases are
not resolved by a larger tie tolerance or arbitrary optimal-face selection.
No such failure occurred on this panel. New-sample degeneracy/failure rates
remain unmeasured. Dimension-generic numerical cores support future n=500,
but the saved validation adapter is deliberately restricted to these 24 n=1000
problems.

## 4. Instrument, score and decision validation

| Check | Result |
|---|---:|
| Independent new instrument solves / bitwise repeats | 48 / 48 |
| Exact KKT, primal=dual, positive Gram / uniqueness | 48 / 48 |
| Maximum returned fixed-objective true gap | {max(c['returned_true_gap']['float'] for c in ic):.6g} |
| Native Policy C maximum true gap, same 48 objectives | {max(c['native_true_gap']['float'] for c in native_ic):.6g} |
| Maximum returned coefficient discrepancy from exact optimum | {max(c['coefficient_max_error'] for c in ic):.6g} |
| Maximum numerical instrument KKT residual | {max(float(r['KKT_max']) for r in instruments):.6g} |
| Maximum instrument coefficient change from native C | {max(float(r['instrument_coefficient_max_change_from_C']) for r in comparison):.6g} |
| Maximum residualized-instrument change from C | {max(float(r['psi_max_change_from_C']) for r in comparison):.6g} |
| Maximum observation-score change from C | {max(float(r['observation_score_max_change_from_C']) for r in comparison):.6g} |
| Scalar rank-score changes from C | 0 |
| Maximum score-matrix condition number | {max(float(r['S_condition']) for r in comparison):.6g} |
| Maximum W versus exact exported-score reconstruction error | {max(float(r['W_exact_reconstruction_error']) for r in comparison):.6g} |
| Maximum W change from C | {s['max_abs_W_change_from_C']:.6g} |
| Maximum certified fixed-objective W interval width | {s['max_W_interval_width']:.6g} |
| Cutoff-separated W bounds / positive interval determinants | 24 / 24 |
| Policy C decision disagreements | 0 / 24 |
| Final numerical failures / unresolved cases | 0 / 24 |

For each new final solve, its exact returned objective gap and a certified
Gram eigenvalue lower bound enclose the coefficient error. Rational intervals
map the two objective regions through centering, psi, score sums and every
entry of S. Explicit verified intercept/psi arithmetic envelopes include the
returned floating quantities. The determinant is positive throughout these
fixed-objective regions, and every W interval excludes the cutoff.

These bounds certify B-v1's final fixed-objective qualification. They are not
the historical end-to-end adaptive-branch certificates attempted in Stage
2G-C. Exhaustive propagation through those historical branches is not used
as a gate here. Replay and independent trace evidence support the specified
finite calibration procedure; its mathematical accuracy is not silently
reinterpreted as an exact adaptive fixed point.

The independent verifier calls no optimizer or active-set reconstruction. It
uses direct rational residuals, a separate fraction-elimination determinant,
KKT gradients, primal/dual values, fresh Gram witnesses, exact psi arithmetic,
score moments and a separately assembled interval calculation. All **24**
primary paths and **48** instrument objectives pass; elapsed audit time is
**{verification['seconds']:.2f} seconds**. This is numerical/arithmetic
verification, not a claim of statistical validity or external human review.

## 5. All 24 candidate decisions

“Accept” means failure to reject at the original cutoff. Intervals below are
B-v1 fixed-final-objective bounds with exact outcome ranks and declared psi
arithmetic envelopes. Full machine precision, coefficient/score differences,
raw LP diagnostics, signs and certificates are retained in CSV/JSON/binaries.

| Candidate | Historical A W / decision | Policy C W / decision | Proposed B-v1 W / decision | Proposed conditional W bounds |
|---|---:|---:|---:|---:|
{case_table}

`results/three_path_comparison.csv` retains outcome, density, instrument,
scalar-score and observation-score comparisons against both historical A and
Policy C. No disagreement, numerical failure or unresolved case is excluded
to obtain favorable decisions. The same exact-rank policy is used throughout;
coverage closer to 95% is never a tuning target.

## 6. Benchmarks and Monte Carlo feasibility

All timings are observed on the original saved **n=1000, p=100, tau=.90**
panel: 24 candidates on eight archived datasets, not 24 independent
replications. No new Monte Carlo replications were run. Both LP and new instrument
solves were repeated bitwise. Production-like component sums exclude those
deliberate repeats, trace-capture replay and the separate independent audit.
The qualified proxy includes measured exact outcome / instrument certificates,
W qualification and residual inference/validation overhead; it is not a
timed new-sample Monte Carlo runner.

| Component | Mean seconds per candidate |
|---|---:|
| Point pipeline: LP + native density/calibration + refined instrument solves | {s['mean_point_pipeline_seconds']:.3f} |
| Qualified pipeline including exact certificates / inference overhead | {s['mean_qualified_pipeline_proxy_seconds']:.3f} |
| Qualified pipeline panel 95th-percentile runtime | {s['p95_qualified_pipeline_proxy_seconds']:.3f} |
| Additional independent direct-rational audit | {s['independent_audit_mean_seconds']:.3f} |
| Qualified pipeline plus independent audit on every candidate | {s['mean_qualified_pipeline_proxy_seconds']+s['independent_audit_mean_seconds']:.3f} |

The existing `thesis_extension/config/extension_config.R` specifies 500
replications, five tau values, four kappa values, 41 candidate points, sample
sizes 500/1000 and five workers. The following are arithmetic projections for
the **DML candidate component only**, not an approved Stage 2H design or an
observed full simulation. Other estimators and all unmeasured costs are extra.

| Planning scenario | Candidates | Qualified serial hours | Ideal five-worker hours | Serial hours with independent audit on every candidate | Current payload storage GiB |
|---|---:|---:|---:|---:|---:|
{projection_table}

Five-worker projections assume ideal scaling, which was not benchmarked.
The mean panel runtime is not a worst-case bound. Penalty simulation, data
generation, new-DGP effects, other quantiles, all other estimators, scheduler
overhead and new-sample degeneracy are not measured. All original outcome
penalties were saved inputs; their future simulation cost cannot be inferred
from the LP benchmark. Exact-certification feasibility is assessed using
observed certificate costs, not inferred from solver success alone.

**n=1000:** limited-pilot core computation is practical on these saved
problems. Large production is materially more expensive once certificates,
audits and storage are retained; the whole repository design requires an
explicit budget and retention strategy.

**n=500 with 100 controls:** no member of the required 24-problem panel has
n=500. No rows were truncated and no new candidate/dataset was constructed.
There is therefore **no direct n=500 benchmark or validation claim**. The
two-sample-size projection assigns n=500 the measured n=1000 cost solely as
a planning proxy, not a proved upper bound. Smaller n alone does not prove
LP basis or degeneracy behavior. A bounded authorized pilot must measure
these cases and failure rates before a broad n=500 production claim.

The retained prototype averages **{payload:.2f} MiB/candidate**; extrapolation
is about {float(plans[-1]['retained_candidate_storage_GiB_proxy'])/1024:.2f} TiB
for the two-size DML component before shared metadata and backups. This
prototype deliberately duplicates inputs to preserve evidence. A production
store should deduplicate immutable observations and record reproducible
bases/traces/certificates with unresolved statuses preserved. This task does
not change retention policy or discard evidence.

## 7. Remaining issues, numerical decision policy and Stage 2H

No ambiguous residual sign or fixed-panel decision remains in this version.
The remaining feasibility conditions are specific:

1. Validate the dimension-generic numerical cores and R adapter at n=500 and
   the other intended tau settings in a bounded, separately authorized pilot;
   record degeneracy, unresolved cases and actual full pipeline cost.
2. Budget per-candidate exact certificates, independent audit frequency,
   pivotal-penalty generation, parallel scaling and evidence storage. Do not
   use the 0.58-second point solver timing as the certified simulation cost.
3. Keep B-v1's historical calibration / final fixed-objective distinction
   explicit. Feeding refined fits back into calibration requires a new
   version and evidence for changed penalty inputs; it is not this policy.
4. Keep any bounded-treatment DGP and its identification/regularity review
   separate from this numerical feasibility result.

Recommended decision policy: use exact-certified outcome ranks and qualified
B-v1 final fits. Emit OUTCOME_UNRESOLVED, INSTRUMENT_UNRESOLVED or
INFERENCE_UNRESOLVED on failed certificates/decision qualification, retain
all cases in denominators, and never apply an arbitrary residual tie tolerance
or interpret a failure as acceptance. No exhaustive certification of every
historical adaptive branch is required before a bounded pilot.

**Recommendation: CONDITIONAL for Stage 2H overall.** The n=1000 saved-panel
numerical evidence supports a limited pilot of this separately versioned
implementation; it does not establish readiness of the entire two-size,
multi-quantile production design or validate asymptotic inference. The next
step should be the bounded feasibility/assumption review above, not renewed
indefinite interval propagation of the historical algorithm. Stage 2H is not
started by this task.

## Reproducibility, development errors and preservation

Environment: Python 3.11.9, NumPy {env['numpy']}, SciPy {env['scipy']}, bundled
HiGHS {env['HiGHS']}, frozen R 3.4.3 / hdm 0.2.0, single-thread settings and
recorded original RNG streams. Build details and complete numerical options
are saved. Bitwise reproducibility is demonstrated in this environment;
cross-platform bitwise identity is not asserted.

Two development errors were caught and corrected: an R matrix-versus-vector
attribute comparison and a shadowed dimension in an intermediate row-norm
bound. The independent verifier rejected the latter; all affected instrument
and inference certificates were regenerated and the final full audit passed.
Superseded failure logs/records are retained under explicit development names.
`EXECUTION_NOTES.json` and `results/processes.json` distinguish those attempts
from final statuses. No failed certificate is treated as a successful case.

SciPy's warning that serial/seed options are forwarded to HiGHS verbatim is
recorded per candidate. The R startup locale warning is preserved; direct
successful R return codes and unchanged native result bytes are checked.
These warnings are not suppressed or counted as statistical failures.

All writes are confined to this directory. Input hashes cover original
observations/candidates, penalties and RNG records, reference certificates,
calibration inputs/traces, instrument coefficients, scores and inference
artifacts. The local manifest covers the new versioned code, copied LP inputs,
configurations, results and certificates. Preservation snapshots exclude
only this directory and Git metadata; final comparisons must show no changes
outside scope. No historical estimator, prior validation, manuscript or saved
Monte Carlo output was modified. No new dataset, Monte Carlo, Stage 2H,
commit, push or merge was performed. Work stops after reporting.
'''
 (HERE/'DETERMINISTIC_IMPLEMENTATION_REPORT.md').write_text(report,encoding='utf-8')
 before=load(OUT/'protected_before.json');after=snapshot();dump(OUT/'protected_after.json',after)
 preservation={'checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
  'missing':sorted(set(before)-set(after)),'added_outside_scope':sorted(set(after)-set(before))}
 dump(OUT/'preservation.json',preservation)
 assert not any(preservation[k] for k in ['changed','missing','added_outside_scope'])
 manifest={p.relative_to(HERE).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in HERE.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json'}
 dump(HERE/'SHA256_MANIFEST.json',manifest)
 print('FINALIZED: 24 passed; preservation PASS;',len(manifest),'artifacts;',len(input_manifest),'input hashes',flush=True)
if __name__=='__main__':main()
