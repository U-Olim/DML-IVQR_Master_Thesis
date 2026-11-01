# Stage 2C-P: protocol frozen before systematic reassessment

Scope: saved two preflight datasets and pilot 1-21 only. Four fitted arms
(P11/P01/P10/P00) give 92 fits; KNOWN is not a fitted arm and its 23 diagnostic
anchors are not optimized or counted as fits. No new data, fit, continuation,
historical edits, commits or pushes. All new files stay in this directory.

## Exact problem and certificates

Treat the saved full-precision binary64 design, candidate-adjusted response,
coefficients and penalties as exact rationals, with tau=9/10. Let r=y-Xb.
P(b)=sum rho_tau(r)+sum lambda_j*abs(b_j)/2. The dual maximizes y'v over
tau-1<=v_i<=tau and |X_j'v|<=lambda_j/2; zero penalties require equalities.
Use saved coefficients as the only primal candidate. LPs for dual witnesses
do not fit or update outcome coefficients. Correct unpenalized equalities by
exact rational linear algebra, then shrink the witness toward zero as needed
to enforce every remaining box/penalty inequality exactly. A rational
certificate must verify all constraints, objective values and complementarity.
P(b)-D(v) is then an upper bound on suboptimality, not a lower bound on error.
Floating gaps with approximate dual feasibility are diagnostics only.

Normalize objective gaps by n and by B=n*max(IQR(y),median(abs(y-median(y))),1).
B describes response units and is not an acceptance tolerance. Report original
objective discrepancies, column RMS scales, singular-value conditioning,
coefficient/residual scales, original KKT classifications and solver settings.
No prescribed tolerance for coefficient/prediction/score accuracy is available.
Historical rq eps=1e-6 is not assumed to imply a universal KKT or gap bound.

## Classification rule (fixed before running)

- Numerically acceptable under the new protocol: exact zero primal-dual gap;
  or a rigorous bound meets an independently specified application accuracy
  budget with a justified transfer to the required fitted-value/score accuracy.
- Numerically unacceptable: proven primal infeasibility/inconsistent required
  inputs, or a certified lower bound on suboptimality/application error violates
  such an independently specified budget. A merely large upper bound cannot
  establish unacceptability.
- Indeterminate: meaningful certified finite objective-error upper bound is
  available, but nonzero and insufficient to establish required application
  accuracy because no such budget/transfer theorem has been specified.
- Insufficient evidence: inputs or useful independently verifiable certificate
  are unavailable (a trivial zero dual alone is not informative).

There is deliberately no new universal numerical threshold. Nonzero tiny
gaps do not automatically justify predictions or discontinuous indicator scores.
No rule uses W, rejection/acceptance or empirical coverage. Original gate
results are immutable provenance, separate from these classifications.

## Stability probes (not refits or optimization)

Evaluate fixed intercept perturbations +/-2**(-40,-30,-20,-10) of each saved
coefficient vector. Evaluate their exact objectives against the same feasible
dual lower bound and exact rank-sign changes. Report fitted-value shifts and
saved-versus-exact residual sign differences. These are deterministic saved-data
probes, not estimates or replacements for any arm. They can demonstrate local
score sensitivity; failure to find a large prediction difference is not a
uniform uniqueness/conditioning result. Compare saved ordinary-QR/P00 fitted
value evidence separately. No classification is tuned to a probe's outcome.

## Verification and preservation

The certificate generator and independent integer audit must agree on exact
box feasibility, zero-penalty equations, penalty inequalities, primal/dual
objectives, nonnegative gap and complementarity. Verify existing Stage 2C-V
manifests/P10 dual certificate without modifying them. Preserve all failure
attempts and partial evidence. SHA-256 snapshots protect everything outside
validation_protocol except Git metadata. Document source hashes before
execution and final artifacts after reporting. Do not implement continuation.
