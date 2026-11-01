# Stage 2C-S: frozen saved-fit inference stability protocol

Before examining perturbed W or decisions, define a common relative objective
accuracy envelope from ALL 92 Stage 2C-P exact certificates. For arm j let
G_j=P_j-D_j be its certified objective-error upper bound and let B_j be the
existing response-scale reference n*max(IQR(y*),MAD_unscaled(y*),1).
Treat each stored B_j binary64 value as an exact scale constant. Freeze
eta=max_j G_j/B_j, using exact rational arithmetic. The study's common
criterion is P_j(b_alt)-D_j <= eta*B_j. No multiplier, coverage, W, rejection,
or selection of a favorable arm enters its definition.

This is an observed-solver-accuracy envelope derived from independently
verified objective errors, not a universally adequate scientific tolerance.
It includes every saved original fit. Exact feasible dual witnesses from
Stage 2C-P give the comparison's lower bounds; every qualifying alternative
has a rigorous suboptimality upper bound in its own dataset/arm objective.
The definition and eta must be recorded before any inference comparison.

## Baseline gate

Use historical R 3.4.3 arithmetic on original saved RDS objects, without
loading an outcome solver or generating data. Recompute candidate-adjusted
response, residuals, <=0 ranks, score sum, two-dimensional uncentered second
moment, W and original qchisq(.95,2) decision. All residuals/ranks must agree
exactly; moment/W discrepancies must be <=1e-9, with identical decisions.
Check all 92 baselines before any stability comparison. Failures stop the task.

## Fixed alternatives and scope

Study only the pre-existing Stage 2C-P fixed intercept perturbations
+/-2**(-40,-30,-20,-10), with all slopes and saved density/instrument
projection held fixed. No refit or data generation is permitted. Verify the
actual binary64 perturbed coefficient agrees with that used in its existing
exact objective certificate. Independently recheck those certificates and
original lower bounds before classifying an alternative as qualifying.
Score arbitrary probes separately from the subset certified within eta*B_j.
Do not label any probe an exact optimizer or independently estimated solution.

Evaluate inference with the original R residual computation and <=0 rule,
original frozen psi, uncentered second moment, critical value and acceptance
definition. Use exact rational score/instrument arithmetic additionally to
certify W and cutoff-side bounds for observed qualifying decision differences.
Never substitute optimizing dual subgradients into the scientific score.

## Classifications (tested set only)

- Observed decision instability between certified near-optimal alternatives:
  at least two qualifying vectors have rigorously resolved opposite decisions.
- Stable under the tested certified near-optimal alternatives: original plus
  at least one distinct qualifying alternative assessed, all their decisions
  agree, and none has an unresolved cutoff-side calculation.
- Numerically indeterminate: baseline passes but no distinct qualifying
  alternative is available or qualifying inference cannot be resolved.
- Not assessable: missing/corrupt inputs or failed baseline reconstruction.

Stability is NOT a uniform result over the entire near-optimal set. Probe
grid is fixed independently of outcomes; report every probe and failure.

## Descriptive diagnostics

Report exact zeros and |e| counts <=1e-12,1e-10,1e-8,1e-7,1e-6; residual
margins, condition estimates and signed W-cutoff distances. These bands never
change ranks/gates. Show proximity counts at fixed descriptive W distances
1e-6,.01,.1,.5,1, retaining exact continuous margins as primary evidence.

No historical file, statistic, configuration, validation classification or
summary may change. All new files live under stability. Preserve SHA-256
snapshots excluding only stability and Git metadata. No continuation,
manuscript edits, commits or pushes. Stop after the report.
