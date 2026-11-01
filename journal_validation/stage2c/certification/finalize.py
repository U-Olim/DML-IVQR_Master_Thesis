"""Tables, checksums and final preservation for certification artifacts only."""
import csv
import json
import sys
from pathlib import Path
from collections import Counter

from certify import HERE,ROOT,dump,sha,snapshot


def table(path,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def main():
    run=Path(sys.argv[1]).resolve();assert HERE in run.parents
    assert json.loads((run/'run_status.json').read_text())['status']=='COMPLETE'
    audit=json.loads((run/'independent_rational_audit.json').read_text());assert audit['status']=='PASS'
    cases=json.loads((run/'all_case_summary.json').read_text());assert len(cases)==92
    rows=[]
    for r in cases:
        rows.append({'dataset':r['dataset'],'arm':r['arm'],'historical_record':r['historical_record'],
            'historical_recorded_kkt':r['historical_recorded_kkt'],
            'historical_csv_classification':r['historical_csv']['classification'],
            'historical_csv_lower':r['historical_csv']['lower'],'historical_csv_upper':r['historical_csv']['upper'],
            'full_precision_classification':r['full_precision']['classification'],
            'full_precision_lower':r['full_precision']['lower'],'full_precision_upper':r['full_precision']['upper'],
            'tie_classification_changes':r['tie_classification_changes']})
    table(run/'classification_summary.csv',rows)
    diagnostic=json.loads((run/'pilot_021/P10/historical_csv_lp/highs_diagnostics.json').read_text())
    raw=run/'full_precision/pilot_021'
    import numpy as np
    b=np.fromfile(raw/'P10_beta.bin',dtype='<f8');lam=np.fromfile(raw/'P10_penalty.bin',dtype='<f8')
    coords=[]
    for j in range(101):
        coords.append({'coordinate':j,'name':'intercept' if j==0 else 'X'+str(j),
            'coefficient':b[j],'penalty':lam[j],
            'group':'numerical_zero_penalized_intercept' if j==0 else 'active_zero_penalty_slope',
            'normalized_stationarity_float':diagnostic['normalized_stationarity_float'][j],
            'chosen_penalty_subgradient':diagnostic['clamped_penalty_subgradients'][j],
            'Xt_score_float':diagnostic['clamped_Xt_score'][j],
            'lower_bound_witness_q':diagnostic['certificate']['witness_q'][j],
            'exact_max_at_clamped_witness':j in diagnostic['certificate']['max_coordinates_zero_based']})
    table(run/'replication21_P10_coordinate_diagnostics.csv',coords)
    sensitivity=json.loads((run/'pilot_021/P10/tie_sensitivity.json').read_text())
    table(run/'tie_sensitivity_summary.csv',[{'tie_tolerance':r['tie_tolerance'],'tie_count':r['tie_count'],
        'diagnostic_only':True,'lower':r['lower'],'upper':r['upper'],'classification_of_alternative_LP':r['classification']} for r in sensitivity])
    before=json.loads((run/'protected_before.json').read_text());after=snapshot()
    preservation={'files_checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
        'missing':sorted(before.keys()-after.keys()),'added_outside_certification':sorted(after.keys()-before.keys())}
    assert not any(preservation[k] for k in ['changed','missing','added_outside_certification'])
    dump(run/'final_preservation.json',preservation)
    assert (HERE/'CERTIFICATION_REPORT.md').is_file()
    dump(run/'source_sha256.json',{p.name:sha(p) for p in sorted(HERE.iterdir()) if p.is_file()})
    count=Counter(r['historical_csv']['classification'] for r in cases)
    final={'status':'COMPLETE','decision':'B - Certified failure of original P10 gate',
        'cases':len(cases),'historical_LP_classifications':dict(count),
        'full_precision_LP_classifications':dict(Counter(r['full_precision']['classification'] for r in cases)),
        'independent_LP_problems_audited':audit['LP_problems'],'independent_LP_witnesses_audited':audit['LP_witnesses'],
        'QR_exact_dual_audit':audit['qr_certificate'], 'preservation':preservation,
        'no_outcome_fits':True,'no_Monte_Carlo':True,'no_pilot_continuation':True}
    dump(run/'final_status.json',final)
    files=sorted(p for p in run.rglob('*') if p.is_file() and p.name!='SHA256_MANIFEST.json')
    manifest={p.relative_to(run).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in files}
    dump(run/'SHA256_MANIFEST.json',manifest)
    for name,r in manifest.items():assert sha(run/name)==r['sha256']
    print(json.dumps(dict(final,verified_artifacts=len(manifest)),indent=2))


if __name__=='__main__':main()
