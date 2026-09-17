"""Validate final saved evaluations without running simulations.

Run before build_selected_figures.R. Fail rather than silently omit failures.
"""
from pathlib import Path
import csv
import hashlib
import itertools
import json
import math

ROOT = Path(__file__).resolve().parents[2]
FINAL = ROOT / 'thesis_extension/final/output'
OUT = ROOT / 'thesis/figures/generated'
CRITICAL = -2 * math.log(.05)  # chi-square(2), checked against R configuration
EST = ('Oracle-GMM', 'Full-GMM', 'DML-IVQR-BC')
CELLS = set(itertools.product((500, 1000), (.1, .25, .5, .75, .9), (1, .5, .25, .1), EST))
inputs = {}

def rows(path):
    inputs[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    with path.open(newline='', encoding='utf-8') as f:
        yield from csv.DictReader(f)

def key(r):
    return int(r['n']), float(r['tau']), float(r['kappa']), r['estimator']

def flag(s):
    assert s in ('TRUE', 'FALSE'), s
    return s == 'TRUE'

def close(a, b):
    assert math.isclose(float(a), float(b), abs_tol=1e-10, rel_tol=1e-10), (a, b)

raw, summary, power = {}, {}, {}
for n in (500, 1000):
    for r in rows(FINAL / f'n{n}/summary.csv'):
        assert key(r) not in summary
        summary[key(r)] = r
    for r in rows(FINAL / f'n{n}/results.csv'):
        k = key(r), int(r['replication'])
        assert k not in raw
        assert not any(flag(r[f]) for f in ('failed', 'profile_failed', 'coverage_failed'))
        assert math.isfinite(float(r['W_true']))
        assert flag(r['covered']) == (float(r['W_true']) <= CRITICAL)
        assert flag(r['rejected_true']) != flag(r['covered'])
        raw[k] = r
assert set(summary) == CELLS and len(raw) == 60000
checks = []
for k in sorted(CELLS):
    g = [raw[k, i] for i in range(1, 501)]
    s = summary[k]
    for f in ('total_replications', 'successful_profiles', 'successful_coverage_evaluations'):
        assert int(s[f]) == 500
    for f in ('numerical_failures', 'failed_profiles', 'failed_coverage_evaluations'):
        assert int(s[f]) == 0
    for field, rawfield in [('Coverage', 'covered'), ('Size', 'rejected_true'),
                           ('all_41_acceptance_rate', 'all_41_grid_points_accepted')]:
        close(s[field], sum(flag(r[rawfield]) for r in g) / 500)
    checks.append(dict(zip(('n', 'tau', 'kappa', 'estimator'), k),
                       R=500, coverage=float(s['Coverage']), size=float(s['Size']),
                       full_domain=float(s['all_41_acceptance_rate'])))

# Verify the full-domain event against every saved grid profile, not only flags.
profile_count = 0
seen = set()
for n in (500, 1000):
    for kr, group in itertools.groupby(rows(FINAL / f'n{n}/profiles.csv'),
                                       lambda r: (key(r), int(r['replication']))):
        assert kr not in seen
        seen.add(kr)
        g = sorted(group, key=lambda r: float(r['a']))
        assert len(g) == 41
        for i, r in enumerate(g):
            close(r['a'], -1 + .1 * i)
            assert math.isfinite(float(r['W']))
            assert flag(r['accepted']) == (float(r['W']) <= CRITICAL)
        assert all(flag(r['accepted']) for r in g) == flag(raw[kr]['all_41_grid_points_accepted'])
        profile_count += len(g)
assert seen == set(raw)

# Median power: saved Delta is candidate minus truth. Same cutoff and R at zero.
power_checks = []
for n in (500, 1000):
    for r in rows(FINAL / f'n{n}/power.csv'):
        if float(r['tau']) != .5:
            continue
        k = key(r) + (float(r['Delta']),)
        rid = int(r['replication'])
        assert not flag(r['power_evaluation_failed']) and math.isfinite(float(r['W_false']))
        close(r['a_false'], 1 + float(r['Delta']))
        assert flag(r['rejected_false']) == (float(r['W_false']) > CRITICAL)
        g = power.setdefault(k, {})
        assert rid not in g
        g[rid] = flag(r['rejected_false'])
    for s in rows(FINAL / f'n{n}/power_summary.csv'):
        if float(s['tau']) != .5:
            continue
        k = key(s) + (float(s['Delta']),)
        g = power[k]
        assert set(g) == set(range(1, 501))
        assert int(s['total_replications']) == int(s['successful_power_evaluations']) == 500
        assert int(s['failed_power_evaluations']) == 0
        close(s['power'], sum(g.values()) / 500)
        power_checks.append(dict(zip(('n', 'tau', 'kappa', 'estimator', 'delta'), k),
                                 R=500, rejection=float(s['power'])))
expected_power = {k + (d,) for k in CELLS if k[1] == .5 for d in (-1, -.5, -.25, .25, .5, 1)}
assert set(power) == expected_power and len(power_checks) == 144
for r in checks:
    if r['tau'] == .5:
        power_checks.append({k: r[k] for k in ('n', 'tau', 'kappa', 'estimator', 'R')} |
                            {'delta': 0, 'rejection': r['size']})
for name, values in [('selected_heatmap_values.csv', checks), ('selected_power_values.csv', power_checks)]:
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=values[0].keys())
        w.writeheader()
        w.writerows(values)
report = dict(nominal_coverage=.95, nominal_size=.05, critical_value=CRITICAL,
              replications_per_cell=500, heatmap_cells=120, power_points=168,
              profile_evaluations=profile_count, missing_or_failed=0,
              grid=dict(lower=-1, upper=3, points=41, step=.1), input_sha256=inputs)
(OUT / 'selected_figures_validation.json').write_text(json.dumps(report, indent=2))
print('Verified 120 heatmap cells, 168 median-power points, and 2,460,000 grid evaluations; no failures/missing values.')
