# Prespecified Stage 2H paired diagnostic pilot — design only

Status: protocol, NOT an executed experiment. No bounded-DGP generator or
Monte Carlo driver is implemented by Stage 2H-0. This protocol must be frozen
with source/input hashes before any future pilot execution.

## Purpose and arms

Estimate finite-sample changes due solely to replacing original D=Phi(T) with
D_delta=.05+.90 Phi(T), retaining Y=1+D+X'b+uD with the arm-specific D.

- A: original DGP with deterministic numerical policy 2G-D.1.
- B: bounded-treatment DGP with the SAME policy 2G-D.1.

Use the same outcome objective, literal penalty rule/inputs within each pair,
exact <=0 rank convention, historical density proxy, adaptive calibration,
final fixed-objective solver and cutoff 5.99146454710798. The numerical code
and tolerances are common to both arms and frozen before execution. Historical
approximate estimation is not a third pilot arm and cannot be substituted for A.
Differences A/B therefore measure a DGP change under one numerical policy;
they do not confound bounded treatment with a numerical-policy improvement.

## Fixed design and streams

- n in {500,1000}; p=100; s=7; rho=.3; original primitive distributions.
- tau in {.10,.50,.90}; kappa in {1,.10}; delta=.05 in arm B only.
- R=20 independent primitive samples for EACH n (40 base samples total).
  Within a sample reuse primitives across tau/kappa, as well as between arms.
- Three prespecified candidates per profile: alpha_true(tau)+{-0.50,0,+0.50}.
  The truth is included exactly. No adaptive grid expansion or case replacement.
- Total: 12 design cells x 20 samples x 2 arms x 3 candidates = 1,440
  candidate evaluations; 480 evaluations are at truth. Each cell/arm has
  20 independent truth evaluations, not 240 or 480 independent replications.

This is a small truth-inclusion / off-truth rejection diagnostic, not a full
41-point confidence-set geometry study. Coverage means inclusion of the true
alpha by the inverted test: W(alpha_true)<=cutoff when numerically qualified.
The three-point pilot cannot support claims about continuous interval endpoints,
length, connectedness or global identification. A later broader grid would
need separate prespecification and budget.

Reserve seed 2026110281 for the future pilot; Stage 2H-0's seed 2026110201 and
all previous validation streams are excluded. Use recorded R 3.4.3
L'Ecuyer-CMRG/Inversion streams. Assign nonoverlapping stream families to n
and sample index; distinct substream families to primitive generation and each
(tau,kappa,candidate) penalty calculation. Store the full stream map and
before/after states. Assign streams by immutable IDs, never worker scheduling.

For a paired A/B candidate, use identical X and the SAME original 1,000-draw
pivotal penalty input stream, so the outcome lambda vector is byte-identical
between arms. Draw the primitive tuple (u,epsilon,x,z1,z2,v1,v2,w) once per
base sample, with original u-epsilon correlation and ordering. Construct T
once per kappa. All treatment/outcome changes in B are deterministic functions
of that tuple. Instrument calibration remains the original deterministic rule
conditional on each arm's residuals; its final penalties CAN differ between
arms because the DGP changes. Preserve those values, do not force them equal.

## Numerical qualification and failure policy

At every candidate require LP success; exact primal/dual/KKT/zero gap;
certified residual signs and the stated uniqueness proof; finite positive
historical density; native calibration records; final fixed-penalty KKT/
primal-dual/Gram checks; positive score determinant over certified final
regions; and a cutoff-separated W bound. Preserve native and exact reference
W and every status. Independently audit EVERY pilot candidate, including
attempted certificates, under the audited H0 dimension adapter.

Retain explicit OUTCOME_UNRESOLVED, INSTRUMENT_UNRESOLVED,
INFERENCE_UNRESOLVED, TIME_LIMIT_UNRESOLVED and resource/not-executed statuses.
No arbitrary residual-sign tolerance; no missing inverse means acceptance.
No new seed, favorable dataset, solver fallback, altered penalty, relaxed
tolerance, alternative tie convention or coverage-based tuning replaces a
failed candidate. A diagnosed implementation bug requires a versioned fix and
a reproducible rerun of the SAME frozen sample IDs, retaining failed attempts.

## Required outputs by n, tau, kappa and arm

1. Planned R, executed R, qualified truth decisions, accepted, rejected,
   unresolved and not-executed counts. Retain candidate-level denominator R.
2. Truth inclusion / coverage: accepted-qualified/R is the conservative
   lower bound; (accepted-qualified+unresolved)/R is the upper bound. Also
   report accepted-qualified/qualified as a labeled conditional diagnostic,
   not a replacement for unconditional reporting.
3. Truth rejection frequency: rejected-qualified/R and the corresponding
   upper bound adding unresolved. On fully qualified runs rejection is the
   complement of coverage. Report off-truth rejection separately at +/-0.50.
4. Mean W at truth, SD, median, quantiles and number of qualified W values.
   An unresolved/missing W is not imputed as zero. Qualified-only means are
   labeled as such, with unresolved counts and certification status.
5. Paired B-A truth coverage, rejection and W differences. Report complete
   paired counts and discordant decision counts. With unresolved indicators,
   aggregate the pairwise possible-difference interval [L_B-U_A,U_B-L_A]
   over ALL planned samples as an explicit missing-decision bound; do not
   silently discard incomplete pairs. Complete-pair summaries are additional.
6. Native density minima/maxima, score condition, objective/KKT error bounds,
   certificate widths and numerical failures by component.
7. Instrument diagnostics: sample Cov(D,Q_j), first-stage partial R^2 and
   conventional joint first-stage F controlling for [1,X], instrument
   residual variances, score covariance eigenvalues and analytical local
   profile-Jacobian magnitude. These are relevance diagnostics, not proof of
   a high-dimensional or weak-instrument theorem. Retain weak kappa=.10 even
   when results are unfavorable. No selection based on observed coverage.
8. Execution, certification and audit times, peak memory, storage, and all
   immutable input/code/config/stream hashes, including unresolved cases.

## Monte Carlo uncertainty and interpretation

Use per-cell exact binomial (Clopper-Pearson) 95% intervals for qualified
binary coverage/rejection when all R decisions are certified. With unresolved
decisions, give denominator-R missing-decision bounds and binomial intervals
for each extreme completion, clearly separating uncertainty sources. Report
the plug-in MCSE sqrt(p_hat(1-p_hat)/R); a zero plug-in MCSE is not certainty.
For zero discordances, report an exact binomial upper bound rather than
claiming paired policies are identical in the population.

For mean W and complete paired W differences report sample SD/sqrt(R_used),
with R_used and numerical selection stated. Paired indicator-difference MCSE
uses the sample variance of differences divided by the pair count. Report
exact discordance-based summaries as well; normal intervals at R=20 are
descriptive approximations. Do not pool dependent tau/kappa cells as if they
were new independent primitive samples. If intervals are presented across
many cells, label them pointwise, not simultaneous guarantees.

At nominal coverage .95, R=20 has ideal binomial MCSE about .0487. It is too
small to establish 95% coverage or an asymptotic approximation. The pilot
tests computational practicality and DGP sensitivity; neither apparent
nominal coverage nor better coverage in B proves asymptotic validity.

## Budget, guardrails and decision after the pilot

Use at most TWO simultaneous candidate workers, one numerical thread each,
matching the concurrency actually benchmarked by readiness. Preserve all
certificates and independent audit results. Budget estimates are generated
from the readiness measurements in `results/pilot_budget.csv`, including
original penalty calibration, both sample sizes and separate certificate/
audit times. Report raw measured budgets and a twofold planning allowance;
the allowance is not a mathematical runtime bound. Bounded-arm costs and
off-truth candidates remain unmeasured until the pilot.

Planning envelopes: 12 elapsed hours, 20 GiB retained outputs and at least
2 GiB available working memory for the limited two-worker pilot plus normal
host/OS requirements. Set an external per-candidate wall limit of 180 seconds;
do not change numerical tolerances when it is reached. A budget/resource
exhaustion stops further work and records all remaining planned IDs as not
executed/unresolved; it does not trigger new draws or conceal missing results.
If measured readiness plus its explicit allowance exceeds an envelope, revise
the proposal BEFORE any pilot execution, not midway based on decisions.

After the pilot, assess full numerical resolution rates, measured cost/storage,
paired DGP effects and instrument diagnostics. Any new numerical calibration
policy, grid, DGP parameter, replication count or production-scale run requires
a new frozen protocol. Statistical validity additionally needs the explicit
identification/high-dimensional assumption mapping in the mathematical
derivation; the pilot does not supply that proof.
