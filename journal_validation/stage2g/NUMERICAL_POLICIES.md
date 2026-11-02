# Stage 2G policy specification

Fixed before the saved-panel results are inspected. All observations, candidate
values and positive numeric penalty vectors are from the 24 Stage 2E problems.
The primary arithmetic target is the literal software binary64 tau interpreted
as a rational, not an independently rounded decimal target.

Let x_i include the intercept, y_i*=y_i-aD_i, and

    Q(b)=sum_i rho_tau(y_i*-x_i'b)+sum_j lambda_j |b_j|/2,
    rho_tau(u)=u(tau-1{u<0}).

The dual maximizes y*'v subject to tau-1 <= v_i <= tau and
|X'v|_j <= lambda_j/2. Intercept penalization is retained.
For a selected b, e_i=y_i*-x_i'b, r_i=1{e_i<=0}, s_i=tau-r_i,
z_i=psi_i s_i, g=sum z_i, S=sum z_i z_i', W=g'S^{-1}g.
Reject precisely when W exceeds the archived binary64 chi-square cutoff.
Singular S is a numerical/inferential failure, never automatic acceptance.
S here is the unnormalized second-moment sum, not the sample average.

An exact optimizer, a near-optimal vector, floating fitted values, residual
ranks, and W are distinct objects. Strict convexity is not assumed. For a
certified unique optimum, strict complementary margins and a nonsingular
tied-row/active-column system identify b exactly. Uniqueness does not make
the discontinuous indicator continuous at its zero residuals.

| Policy | Operational definition | Certification and limitation |
|---|---|---|
| A | Archived solver, settings, R residuals, <=0 ranks, saved historical psi | Reproducible legacy baseline; no sign guarantee from objective accuracy |
| B | Saved independent HiGHS solution to identical objective; retain its archived R ranks and both saved psi paths | Exact primal/dual error bounds; better objective accuracy does not certify optimum ranks |
| C | Independent numerical solution proposes support/ties; reconstruct rational primal/dual witnesses; certify strict margins, nonsingularity and unique optimum; evaluate rational residual signs with <=0 | Exact signs and exact W conditional on declared saved psi; unresolved certification is explicitly a failure/ambiguity, never a tolerance-based sign |
| D | At certified optimum use 1{e<0}, assigning exact ties to rank zero | Separately named finite-sample statistic; differs from <=0 at every exact tie; not a replacement for A or C |

B plus certified exact reconstruction is C, not a claim that nearest-double
coefficients preserve signs. No residual tolerance is adopted. The 1e-7 band
in the reused reconstruction code ONLY proposes a basis; every subsequent
equality, inequality and tie is checked exactly. Failure is retained without
relaxation, new solver selection or case exclusion.

For C, saved historical psi is the primary controlled comparison. Saved
independent psi is an additional conditional comparison. Neither is a newly
recomputed complete C path. Exact arithmetic in W uses the binary64 score
values produced by .9-r, and saved binary64 psi interpreted as rationals.
Thus it certifies arithmetic conditional on these inputs, not the unknown
real-arithmetic solution of the instrument regressions.

## Sign and decision certificates

At the singleton exact optimizer all 1000 signs can be certified, including
zero. At a positive objective-error budget, tied residuals are locally
ambiguous: the invertible tied/active basis maps any prescribed tied residual
direction to a coefficient direction. Taking a sufficiently small positive
step preserves all nonzero residual signs and stays in the budget by the
finite Lipschitz bound for Q. Every binary tie pattern is therefore locally
realizable in these certified square-basis cases. Untied signs are locally
stable; this is not a global certification over an entire positive sublevel.

Coordinate search over tie patterns is deterministic and diagnostic. A pair
of opposite exact W decisions proves noninvariance for every positive budget
under fixed psi. Failure to find such a pair proves nothing globally. Search
extrema are attained values, NOT enclosing bounds on W. Trivial global
conditional bounds are 0 <= W <= n whenever S is positive definite: W is
the squared length of the projection of the all-ones vector onto the column
space of the observation-score matrix. These bounds cannot certify the
present rejection cutoff. No exhaustive 2^m search is claimed.

Validated intervals can certify a residual sign only when the interval
excludes zero; intervals containing zero cannot distinguish a tie from an
unresolved small residual. A feasible primal and dual give an objective
sublevel containing the optimum, but not individual sign certainty.
Constrained LP minimization/maximization of each fitted value over that
sublevel could certify signs when its extrema exclude zero. Exact LP and
strict complementarity are more decisive here because they identify exact
ties and the singleton optimum. Degenerate/nonunique bases need a distinct
optimal-face analysis and an explicitly justified selection rule; this
implementation does not invent one.

## Proposed future contract (conditional recommendation)

Use C as a versioned certified-sign procedure, with B as a basis proposal and
A retained as an audit baseline. Record exact input hashes, candidate, penalty
RNG states, solver status, feasible primal/dual witnesses, support, ties,
uniqueness, sign certificates, g, S, W, cutoff and failures for EACH candidate.
Never replace unresolved cases with acceptance or delete them from coverage
denominators. Return an unresolved status and report its count separately.
Freeze a downstream density/projection arithmetic contract and validate it
before claiming this is a complete simulation-ready estimator. A changed
finite-sample tie score or optimal-face selection requires its own version.
No coverage criterion enters policy selection.
