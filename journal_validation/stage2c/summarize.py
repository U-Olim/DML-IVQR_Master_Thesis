"""Deterministic summaries of completed saved fits; no model estimation."""
import csv
import itertools
import json
import math
import statistics as stats
import sys
from pathlib import Path


def read(p):
    with p.open(newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def write(p, rows):
    with p.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def mcse(values):
    return stats.stdev(values) / math.sqrt(len(values))


def wilson(k, n):
    z = 1.959963984540054
    p = k / n
    den = 1 + z*z/n
    center = (p + z*z/(2*n)) / den
    half = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den
    return center-half, center+half


def main():
    out = Path(sys.argv[1])
    complete = (out / 'RUN_COMPLETE.txt').is_file()
    computed_folders = sorted(out.glob('pilot_[0-9][0-9][0-9]'))
    folders = [p for p in computed_folders if (p / 'verification.json').is_file()]
    if complete:
        assert len(folders) == 40
    else:
        assert (out / 'FAILURE.txt').is_file(), 'Partial run must retain explicit failure'
    count = len(folders)
    # Retain EVERY computed arm, including the dataset that stopped validation.
    all_computed = []
    for folder in computed_folders:
        if (folder / 'evaluations.csv').is_file():
            all_computed.extend(dict(r, validation_status='PASS' if folder in folders else 'FAILED_GATE')
                                for r in read(folder / 'evaluations.csv'))
    write(out / 'all_computed_evaluations.csv', all_computed)
    (out / 'summary_scope.json').write_text(json.dumps({
        'run_complete': complete, 'planned_replications': 40,
        'computed_replications': len(computed_folders), 'fully_validated_replications': count,
        'summary_replications': count,
        'interpretation': 'Preserved partial prefix only; outcome-dependent stopping prevents fixed-40 pilot conclusions.' if not complete else 'Complete fixed pilot',
        'failed_gate_folders': [p.name for p in computed_folders if p not in folders]}, indent=2))
    rows = []
    supports = []
    validation = []
    checks = []
    for folder in folders:
        r = read(folder / 'evaluations.csv')
        assert len(r) == 5 and len({x['arm'] for x in r}) == 5
        assert json.loads((folder / 'verification.json').read_text())['status'] == 'PASS'
        rows.extend(r)
        validation.append(dict(replication=folder.name, **read(folder / 'r_validation.csv')[0]))
        for arm, c in json.loads((folder / 'verification.json').read_text())['arms'].items():
            checks.append(dict(replication=folder.name, arm=arm, **c))
        coefficients = read(folder / 'coefficients.csv')
        for arm in ['P11', 'P01', 'P10', 'P00', 'KNOWN']:
            selected = [int(x['coordinate']) for x in coefficients
                        if x['arm'] == arm and x['selected'] == 'TRUE' and int(x['coordinate']) > 0]
            supports.append({'replication': int(folder.name[-3:]), 'arm': arm,
                             'selected_count': len(selected), 'selected_coordinates': ';'.join(map(str, selected))})
    write(out / 'all_evaluations.csv', rows)
    write(out / 'selected_supports.csv', supports)
    write(out / 'canonical_and_qr_checks.csv', validation)
    # KNOWN has no KKT columns; keep rectangular independent-check CSV.
    keys = list(dict.fromkeys(k for r in checks for k in r))
    write(out / 'independent_checks.csv', [{k: r.get(k, '') for k in keys} for r in checks])
    arms = ['P11', 'P01', 'P10', 'P00', 'KNOWN']
    groups = {a: sorted([r for r in rows if r['arm'] == a], key=lambda r: int(r['replication'])) for a in arms}
    metrics = ['mean_rank_score', 'W', 'intercept_error', 'slope_l2_error', 'coefficient_l2_error',
               'prediction_RMS', 'selected_slopes', 'rank_disagreements', 'raw_Z1', 'raw_Z2',
               'score_sum_1', 'score_sum_2', 'second_moment_11', 'second_moment_12', 'second_moment_22']
    def values(arm, metric):
        return [float(r[metric]) for r in groups[arm]]
    acceptance = {a: [float(r['accepted'] == 'TRUE') for r in groups[a]] for a in arms}
    summaries = []
    for arm in arms:
        g = groups[arm]
        k = int(sum(acceptance[arm])); lo, hi = wilson(k, count)
        s = {'arm': arm, 'replications': count, 'acceptances': k, 'rejections': count-k,
             'acceptance': k/count, 'acceptance_MCSE': math.sqrt(k/count*(1-k/count)/count),
             'Wilson95_lower': lo, 'Wilson95_upper': hi, 'failures': sum(r['failed'] == 'TRUE' for r in g)}
        for metric in metrics:
            v = values(arm, metric)
            s['mean_' + metric] = stats.mean(v)
            s[metric + '_MCSE'] = mcse(v)
        summaries.append(s)
    write(out / 'variant_summary.csv', summaries)
    paired = []
    paired_raw = []
    comparisons = [('P01', 'P11'), ('P10', 'P11'), ('P00', 'P11'),
                   ('P00', 'P10'), ('P00', 'P01'), ('P01', 'P10')]
    comparisons += [('KNOWN', a) for a in arms[:-1]]
    for alternative, baseline in comparisons:
        for metric in metrics + ['acceptance']:
            u = acceptance[alternative] if metric == 'acceptance' else values(alternative, metric)
            v = acceptance[baseline] if metric == 'acceptance' else values(baseline, metric)
            d = [x-y for x, y in zip(u, v)]
            paired.append({'comparison': alternative + '-' + baseline, 'metric': metric,
                           'pairs': count, 'mean_difference': stats.mean(d), 'MCSE': mcse(d),
                           'gains': d.count(1) if metric == 'acceptance' else '',
                           'losses': d.count(-1) if metric == 'acceptance' else ''})
            paired_raw.extend({'comparison': alternative + '-' + baseline, 'metric': metric,
                               'replication': i+1, 'difference': x} for i, x in enumerate(d))
    for metric in metrics + ['acceptance']:
        v = acceptance if metric == 'acceptance' else {a: values(a, metric) for a in arms}
        d = [v['P11'][i]-v['P10'][i]-v['P01'][i]+v['P00'][i] for i in range(count)]
        paired.append({'comparison': 'interaction_P11-P10-P01+P00', 'metric': metric,
                       'pairs': count, 'mean_difference': stats.mean(d), 'MCSE': mcse(d), 'gains': '', 'losses': ''})
        paired_raw.extend({'comparison': 'interaction_P11-P10-P01+P00', 'metric': metric,
                           'replication': i+1, 'difference': x} for i, x in enumerate(d))
    write(out / 'paired_summary.csv', paired)
    write(out / 'paired_differences.csv', paired_raw)
    frequency = []
    for arm in arms:
        sets = [set(map(int, r['selected_coordinates'].split(';'))) if r['selected_coordinates'] else set()
                for r in supports if r['arm'] == arm]
        for j in range(1, 101):
            frequency.append({'arm': arm, 'coordinate': j, 'true_nonzero': j <= 7,
                              'selected_count': sum(j in s for s in sets), 'replications': count})
    write(out / 'selection_frequency.csv', frequency)
    print('VARIANTS')
    for r in summaries:
        print(r['arm'], 'W', r['mean_W'], 'acceptance', r['acceptances'],
              'score', r['mean_mean_rank_score'], 'intercept error', r['mean_intercept_error'],
              'slope L2', r['mean_slope_l2_error'], 'prediction RMS', r['mean_prediction_RMS'],
              'support', r['mean_selected_slopes'], 'rank disagreements', r['mean_rank_disagreements'])
    print('PAIRED MAIN QUANTITIES')
    for r in paired:
        if r['metric'] in ['mean_rank_score', 'W', 'acceptance']:
            print(r)
    print('NUMERICAL GATES', 'canonical max', max(float(r['canonical_W_difference']) for r in validation),
          'P00 fitted max', max(float(r['p00_ordinary_fitted_max_difference']) for r in validation),
          'KKT max', max(float(r.get('kkt_stationarity_over_n', 0)) for r in checks))


if __name__ == '__main__':
    main()
