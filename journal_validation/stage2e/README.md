# Stage 2E - fixed independent primal-solver comparison

Exactly eight saved Stage 2C datasets and three candidate offsets (-.5,0,.5),
24 paired problems. No new datasets, replacements, profiles, 500-replication
study, Stage 2C continuation, manuscript edits, commit or push.

## Fixed design and source

`config.json` gives the complete fixed design. Targeted pilot_003/pilot_014;
index-selected pilot_001/002/004/005/006/007. All n=1000,p=100,tau=.90,kappa=1.
True alpha is computed with the historical R qnorm. Input RDS datasets,
truth P11 coefficients, numeric penalties and full RNG states are mandatory.
Missing inputs stop execution; none is regenerated or replaced.

Truth historical outcome fits are reused, not re-estimated. Their penalty
vectors are independently replayed from saved states as an input check.
False candidates use original pivotal generation with CMRG/Inversion master
seed 2026102905, streams 1-16 in dataset order, minus then plus. The original
historical rq(method='lasso') fits those 16 false-candidate outcomes once.
Both solvers receive the SAME exported numeric lambda, observations and
candidate-adjusted response. Independent fitting makes no penalty draws.

## Independent primal LP

SciPy linprog(method='highs-ds') explicitly solves the requested primal with
unrestricted beta, nonnegative r_plus/r_minus/t, equalities
X beta+r_plus-r_minus=y-alpha*D, and beta-t<=0/-beta-t<=0. Objective is
.9 sum(r_plus)+.1 sum(r_minus)+lambda't/2, including intercept penalty.
All LP inputs/results and algorithm settings are retained. This uses no
rqfnb algorithm. Existing Python/NumPy/SciPy are used without installation.

Exact primal objectives and feasible dual bounds treat saved binary64 inputs
as exact rationals and tau as 9/10, consistently with Stage 2C-V/P/S. A dual
vector obtained from the independent LP is made exactly feasible by rational
box/penalty scaling. Both fixed outcome vectors are evaluated against the
same dual lower bound. Auxiliary LP residual/absolute-value variables are
canonically reconstructed for feasibility; neither beta vector is altered.
Nonzero gaps do not prove exact optimality or uniqueness. A separate audit
checks feasibility, objectives, complementarity and inference arithmetic.

## Layers and randomization

Layer A freezes the historical density and psi and changes only outcome beta.
Layer B recomputes original dnorm(e,mean(e),var(e)) and the original transformed
hdm rlasso projection for each outcome beta. Outcome lambda is identical;
adaptive instrument penalties may change downstream of changed transformed
data. Their actual last-used vectors and replay checks are saved using the
existing private tracing helper. No instrument RNG draws are permitted;
full states before/after are checked. These numerical penalty differences are
downstream effects, not an independently varied tuning setting.

Both layers retain e<=0, uncentered second moment and original chi-square cutoff.
All outcome coefficients remain jointly fitted; no new tie-breaking is applied.

## Certification and interpretation fixed before results

Use the unchanged Stage 2C-S eta=max(original certified G/B) as the common
relative observed-accuracy envelope, with B=n*max(IQR(y*),unscaled MAD(y*),1)
for EACH candidate-adjusted response. Both solver objective-error upper bounds
must be within eta*B to use A/B rather than C. Eta is read and frozen before
this experiment, never fitted to W/coverage or expanded to include a case.
This is a comparison envelope, not a proof of universal scientific accuracy.

A: both adequately certified within that envelope, both layers agree in decisions.
B: both qualify and at least one layer differs in decision.
C: insufficient certificate or at least one bound exceeds the frozen envelope.
Keep every C/failure row and its raw statistics. Numerical active-set rank is
a nonuniqueness diagnostic, not proof of one or multiple exact optima.

## Run and preserve

From repository root on journal-validation:

```powershell
python -B journal_validation/stage2e/run_stage2e.py
# RUN is the unique output/paired_UTCSTAMP directory printed above:
python -B journal_validation/stage2e/verify.py RUN
python -B journal_validation/stage2e/binary_tau.py RUN
python -B journal_validation/stage2e/residual_review.py RUN
python -B journal_validation/stage2e/finalize.py RUN
```

The historical R 3.4.3 executable/library must already exist. Source wrappers
and historical helper definitions are read-only; environment guard is sourced
with write_outputs=FALSE. All new files are inside stage2e. Every file outside
stage2e except Git metadata is protected by pre/post SHA-256 snapshots.
Prior Stage 2C artifacts are verified before fitting. Unique output directories
cannot be reused. Save raw outputs separately: output/ is ignored by Git.

Stop after exactly 24 paired problems and the report. No retry or sample
replacement is authorized merely because a case is inconclusive.
