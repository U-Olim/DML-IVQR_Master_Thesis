"""Presentation-only appendix tables from final records and analytical formulas."""
from pathlib import Path
from statistics import NormalDist
import csv, hashlib, itertools, json, math

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'thesis_extension/reporting/output'
TABLES = ROOT / 'thesis/tables'
inputs = {}
for name in ('thesis_extension/config/extension_config.R',
             'thesis_extension/src/dgp_kappa.R',
             'thesis_extension/diagnostics/coverage_audit/coverage_audit_functions.R',
             'thesis_extension/diagnostics/grid_sensitivity/grid_sensitivity_config.R',
             'thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_config.txt'):
    inputs[name] = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
def read(path):
    path = ROOT / path
    inputs[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
    with path.open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))
def key(r):
    return int(r['n']), float(r['tau']), float(r['kappa']), r['estimator']
def close(a, b):
    assert math.isclose(float(a), float(b), abs_tol=1e-12), (a, b)
est = ('Oracle-GMM', 'Full-GMM', 'DML-IVQR-BC')
expected = set(itertools.product((500,1000),(.1,.25,.5,.75,.9),(1,.5,.25,.1),est))
audit = {key(r):r for r in read('thesis_extension/diagnostics/coverage_audit/output/coverage_audit_all_cells.csv')}
raw = {}
for n in (500,1000):
    for r in read(f'thesis_extension/final/output/n{n}/results.csv'):
        raw.setdefault(key(r), []).append(r)
assert set(raw) == set(audit) == expected
z = NormalDist().inv_cdf(.975)  # documented two-sided 95% Wilson, no continuity correction
critical = -2*math.log(.05)
cells = []
for k in sorted(expected):
    g, a = raw[k], audit[k]
    assert len(g)==500 and {int(r['replication']) for r in g}==set(range(1,501))
    assert all(math.isfinite(float(r['W_true'])) and r['coverage_failed']=='FALSE' for r in g)
    assert all((float(r['W_true'])<=critical)==(r['covered']=='TRUE') for r in g)
    successes = sum(float(r['W_true'])<=critical for r in g)
    n = len(g); p = successes/n; den = 1+z*z/n
    center = (p+z*z/(2*n))/den
    half = z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    lo, hi = max(0,center-half), min(1,center+half)
    close(p,a['empirical_coverage']);close(lo,a['coverage_mc95_lower']);close(hi,a['coverage_mc95_upper'])
    assert int(a['R_available'])==int(a['total_rows'])==n
    assert int(a['number_missing'])==int(a['number_non_finite'])==0
    assert (lo<=.95<=hi)==(a['nominal_0p95_inside_mc_interval']=='TRUE')
    cells.append(dict(zip(('n','tau','kappa','estimator'),k),accepted=successes,R=n,
                      coverage=p,lower=lo,upper=hi,missing_nonfinite=0))
summary=[]
for e in est:
    for n in (500,1000):
        g=[r for r in cells if r['estimator']==e and r['n']==n]
        assert len(g)==20
        summary.append(dict(estimator=e.replace('-BC',''),n=n,cells=20,
                            min_coverage=min(r['coverage'] for r in g),max_coverage=max(r['coverage'] for r in g),
                            below=sum(r['upper']<.95 for r in g),above=sum(r['lower']>.95 for r in g),missing_nonfinite=0))
below=sum(r['below'] for r in summary);above=sum(r['above'] for r in summary)
assert below+above==54, (below,above)
def write_csv(name, rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
write_csv('appendix_coverage_audit_cells.csv',cells)
write_csv('appendix_coverage_audit_summary.csv',summary)
lines=[r'\begin{table}[!ht]',r'\caption{Direct-at-truth coverage audit.}',r'\label{tab:coverage-audit-summary}',
       r'\centering',r'\begin{tabular}{lrrrrrrr}',r'\toprule',
       r'Estimator & $n$ & Cells & \shortstack{Coverage\\min.} & \shortstack{Coverage\\max.} & \shortstack{Upper\\$<0.95$} & \shortstack{Lower\\$>0.95$} & \shortstack{Missing/\\nonfinite} \\',r'\midrule']
for r in summary:
    lines.append(f"{r['estimator']} & {r['n']} & 20 & {r['min_coverage']:.3f} & {r['max_coverage']:.3f} & {r['below']} & {r['above']} & 0 "+r'\\')
lines += [r'\bottomrule',r'\end{tabular}',r'\begin{tablenotes}',
 r'Each row covers 20 quantile--$\kappa$ cells, with 500 direct-at-truth evaluations per cell. Coverage is reported as a proportion. The upper/lower columns count cells whose unrounded Wilson upper endpoint is below 0.95 or lower endpoint is above 0.95. Intervals use integer acceptance counts, the verified denominator, and the two-sided 95\% Wilson formula without continuity correction. They are pointwise Monte Carlo intervals, not simultaneous or multiple-testing-adjusted intervals; exclusion counts are descriptive audit summaries. Missing/nonfinite counts concern direct-at-truth $W$ evaluations (missing values are counted once).',
 r'\end{tablenotes}',r'\end{table}']
(TABLES/'appendix_coverage_audit_summary.tex').write_text('\n'.join(lines)+'\n')
illustration=[dict(kappa=k,coefficient=math.sqrt(2*(1-k*k)),signal_variance=2*k*k,
                   noise_variance=2*(1-k*k),total_variance=3.) for k in (1,.5,.25,.1)]
for r in illustration: close(r['signal_variance']+r['noise_variance']+1,3)
write_csv('appendix_kappa_illustration.csv',illustration)
lines=[r'\begin{table}[!tb]',r'\caption{Variance allocation in the $\kappa$-extension.}',r'\label{tab:kappa-illustration}',
 r'\centering',r'\begin{tabular}{rrrrr}',r'\toprule',
 r'$\kappa$ & \shortstack{Coefficient\\$\sqrt{2(1-\kappa^2)}$} & \shortstack{Signal variance\\$2\kappa^2$} & \shortstack{Noise variance\\$2(1-\kappa^2)$} & \shortstack{Total index\\variance} \\',r'\midrule']
for r in illustration:
    lines.append(f"{r['kappa']:.2f} & {r['coefficient']:.4f} & {r['signal_variance']:.4f} & {r['noise_variance']:.4f} & 3.0000 "+r'\\')
lines += [r'\bottomrule',r'\end{tabular}',r'\begin{tablenotes}',r'Values are calculated directly from the construction, not simulated. The disturbance $\epsilon_i$ contributes the remaining variance of one in every row.',r'\end{tablenotes}',r'\end{table}']
(TABLES/'appendix_kappa_illustration.tex').write_text('\n'.join(lines)+'\n')
# Check the original domain-table numbers without rewriting them.
domain=read('thesis_extension/diagnostics/grid_sensitivity/output/stage2/stage2_summary.csv')
assert len(domain)==135 and all(int(r['n'])==1000 and int(r['total_replications'])==100 for r in domain)
failed=[r for r in domain if int(r['failed_profiles'])]
assert {(key(r),r['range'],int(r['successful_profiles']),int(r['failed_profiles'])) for r in failed}=={
    ((1000,.9,.1,'DML-IVQR-BC'),d,99,1) for d in ('A_1_-3_5','A_2_-5_7')}
assert {float(r['kappa']) for r in domain}=={1,.25,.1}
lookup={(key(r),r['range']):r for r in domain}
for line in (TABLES/'appendix_grid_key.tex').read_text().splitlines():
    if not line.startswith('1000 &'):continue
    a=[x.strip() for x in line.removesuffix(r'\\').split('&')]
    k=(int(a[0]),float(a[1]),float(a[2]),a[3]+('-BC' if a[3]=='DML-IVQR' else ''))
    for j,dom in enumerate(('A_0_-1_3','A_1_-3_5','A_2_-5_7')):
        r=lookup[k,dom]
        assert abs(float(a[4+j])-float(r['median_grid_accepted_set_measure']))<=.000500001
        assert abs(float(a[7+j])-float(r['mean_grid_accepted_set_measure']))<=.000500001
truths=[1+NormalDist().inv_cdf(t) for t in (.1,.25,.5,.75,.9)]
distance=min(min(t+1,3-t) for t in truths)
assert distance>0
report=dict(cells=120,evaluations=sum(r['R'] for r in cells),below=below,above=above,excluded=below+above,
            missing_nonfinite=0,minimum_truth_boundary_distance=distance,diagnostic_replications=100,
            domain_table_values_unchanged=True,domain_cells_with_one_failed_profile=2,input_sha256=inputs)
(OUT/'appendix_tables_validation.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='input_sha256'},indent=2))
