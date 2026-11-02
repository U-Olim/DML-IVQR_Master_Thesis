# Policy C complete-path specification, version 2G-F

Status: implemented and numerically validated on the fixed 24-problem panel.
Strict full-path certification remains conditional as described below. This
specification does not authorize a new simulation or change the DGP.

## Inputs and outcome solution

For EACH candidate use the original observation ordering, candidate-adjusted
response bytes, positive outcome penalties (including the intercept), tau
bytes and complete recorded penalty RNG state. Certify the same outcome
objective sum rho_tau(y*-X beta)+sum lambda_j|beta_j|/2. The exact arithmetic
target is the exported binary64 problem, with literal binary64 tau.

An independent outcome solver may propose an active basis. Exact rational
primal/dual feasibility, zero gap and uniqueness must pass before using its
ranks. Nonunique, degenerate, failed or unavailable certificates return
OUTCOME_UNRESOLVED. Do not add a ridge, change penalties, relax a residual
tolerance, silently choose an optimal-face point or substitute a legacy fit.

Compute e=y*-X beta in rational arithmetic. Save r_i=1{e_i<=0}; exact zero is
rank one. Round each exact residual ONCE to binary64 for the density proxy.
Do not calculate these residuals by subtracting fitted values from rounded
coefficients. Export rounded beta for diagnostics only. Exact ranks remain
the authority even if residual export underflows on a future sample.

## Historical downstream convention

Use R 3.4.3 and hdm 0.2.0 from the frozen library. Evaluate

    f = dnorm(e_binary64, mean(e_binary64), var(e_binary64))

where var is the sample variance and is passed as the NORMAL SCALE. This
unusual convention is historical and is deliberately preserved. Check finite
strictly positive f. Use sqrt(diag(f)) %*% X and sqrt(diag(f)) %*% Z_j in the
historical formula rlasso(yw ~ Xw, post=FALSE). Retain the ordinary unpenalized
intercept in transformed space, NOT a weighted intercept. Recover instruments
by psi_j = Z_j-[1,X] gamma_j, exactly as in the historical procedure.

Restore the recorded post-outcome-penalty state before each candidate and each
paired variant. The present heteroscedastic, X-independent penalty rule uses
no new random draws; verify that the state is unchanged. Record all adaptive
penalty vectors, coefficients, inner/outer iteration counts and options.
The last penalty actually supplied to LassoShooting.fit defines its final
quadratic objective. fit$lambda is the NEXT update and must not be used to
certify the preceding fit. Retain c=.5, gamma=.1/log(n), historical shooting
optTol=1e-5, zeroThreshold=1e-6 and the original outer control values.

## Score and numerical validation

s=tau-r; z_i=psi_i s_i; g=sum z_i; S=sum z_i z_i'; W=g'S^{-1}g.
Use the archived cutoff bytes (5.99146454710798 in displayed decimal).
Never reinterpret an unresolved inverse or certificate as acceptance.

Validate density independently at high precision; verify transformed arrays,
centering, initial OLS, signed-correlation selection, adaptive loading updates,
RNG matching, psi, score moments and W. Save exact rational W on the exported
binary64 psi and score values, plus the actual R W and inversion residual.
Reproducibility requires fixed package versions, ordering and arithmetic.

Certify each final centered lasso

    F_j(b)=||yc_j-Xc b||^2+sum_k lambda_used,jk |b_k|.

Use an exact active-set solution only as an audit reference; do not replace
the native coefficients or rerun the adaptive procedure with refined fits.
Verify KKT inequalities and primal=dual, and certify positive-definite Gram
matrix via an exact check of an approximate inverse. Preserve native outputs.
Use the true native objective gap and certified Gram bound to enclose the
two native-objective sublevels. Map these coefficient regions through the
historical psi formula and bound W with rational interval arithmetic.
Record ACCEPT_CERTIFIED, REJECT_CERTIFIED or DOWNSTREAM_UNRESOLVED with the
explicit qualifier FIXED_DENSITY_AND_FINAL_PENALTIES.

## Certification boundary and readiness

The implemented certificates cover the exported density weights, centered
designs, means and last-used penalties as fixed inputs. Independent 80-digit
density checks and independent adaptive-trace reconstruction validate the
numerical implementation, but are not an interval propagation proof through
the adaptive algorithm. They do not prove that all admissible changes in
density arithmetic or intermediate shooting error yield the same penalty
trajectory and final decision. The estimator is a finite historical adaptive
algorithm; an exact adaptive fixed point is neither computed nor assumed.

Strict readiness decision: B — Conditional. Minimum remaining numerical work:
outward bounds for density/centering from the certified residuals, and a local
propagation check through initialization, penalty updates and stopping
branches. It must either certify those branches and their resulting penalty
regions, or enclose all branches consistent with the bounds. Propagate that
uncertainty to W rather than freezing the final penalties. Use these same 24
problems; no additional data or Monte Carlo is needed for that validation.
No numerical failure or decision reversal was observed in the completed
checks; this remaining condition concerns the scope of the proof.

## Future Stage 2H integration, after the condition is met

Freeze this as a separately versioned computational implementation. Keep the
bounded-treatment DGP change in a separate version and retain its analytical
regularity/identification checks. Predeclare streams, candidate grids, outcome
and density arms, and how unresolved cases enter reporting denominators.
Store certificates and status per candidate, not only per simulated sample.
Do not select policies, tolerances or DGP parameters by nominal coverage.
No legacy result or manuscript is to be overwritten by the new version.
