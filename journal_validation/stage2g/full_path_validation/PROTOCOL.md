# Fixed complete-path protocol

Only the existing 24 problems. All new files stay under full_path_validation.
The Stage 2G source and certificates are protected inputs. Priority cases run
first in the original Stage 2G order. No new sample or outcome fit is generated.

Primary C path: evaluate y*-X beta in exact rational arithmetic at the
certified optimum; export each residual rounded once to nearest binary64.
Carry exact <=0 ranks separately. Do not form residuals from rounded beta.
Use historical R 3.4.3, hdm 0.2.0, dnorm(e,mean(e),var(e)), the original
matrix/formula path and ordinary transformed intercept, post=FALSE. Export
the actual last-used slope penalties separately from the reported next-step
penalties. Start every path from its recorded post-outcome-penalty RNG state;
verify the downstream state remains unchanged. Repeat native fits from the
same state and compare outputs bitwise. No seed or penalty tuning.

Near-optimal assessment: the 12 previously identified cases, each saved
minimum/maximum rank pattern, at predeclared objective budgets 1e-8 and 1e-20.
Construct rational coefficient directions via the nonsingular tied/active
basis. Restrict steps to preserve other signs and guarantee the check-loss
Lipschitz objective bound. Independently verify actual gaps and all ranks.
Round exact residuals once for the density proxy; retain rational ranks.
These are mathematical near-optimal vectors, not claims of representability
of all coefficient perturbations in binary64. Recompute every downstream
path, even when rounded density weights coincide. Finite comparisons do not
establish global full-path stability or a full-path uniform-in-epsilon theorem.

Validation: independent high-precision Decimal mean/variance/normal-density
evaluation, direct verification of residualized instruments, exact rational
score moments and W on exported psi, inverse residual and condition numbers,
and analysis of the final fixed-penalty quadratic lasso objective. Native
adaptive penalty traces and stopping behavior are preserved. A fixed final
penalty objective certificate does not certify an ideal adaptive fixed point.

Screening tolerances fixed before results: density relative error <=1e-12;
psi reevaluation <=1e-12 times (1+max abs psi); W reconstruction relative
error <=1e-10. These are numerical cross-check thresholds, not exact interval
certificates. Exact feasibility/optimality checks use no numerical tolerance.
Native repeatability must be bitwise. Failures and ambiguities remain in all
tables. Readiness depends on actual downstream evidence and explicit scope,
not closeness to nominal coverage. Cutoff is the archived chi-square binary64.
