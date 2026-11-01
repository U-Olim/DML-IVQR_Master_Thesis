"""Finalize immutable evidence manifests after scientific report preparation."""
import hashlib
import json
import platform
import sys
from pathlib import Path

import numpy
import scipy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def main():
    out = Path(sys.argv[1]).resolve()
    assert HERE in out.parents
    assert (HERE / 'STAGE2C_REPORT.md').is_file()
    preservation = json.loads((out / 'preservation.json').read_text())
    complete = preservation['run_status'] == 'COMPLETE'
    assert not any(preservation[k] for k in ('changed', 'missing', 'added_outside_stage2c'))
    (out / 'python_environment.json').write_text(json.dumps({
        'python': sys.version, 'executable': sys.executable, 'platform': platform.platform(),
        'numpy': numpy.__version__, 'scipy': scipy.__version__}, indent=2))
    checks = [json.loads(p.read_text()) for p in sorted(out.glob('pilot_*/verification.json'))]
    validation = [json.loads(p.read_text()) for p in sorted(out.glob('validation_*/verification.json'))]
    assert len(validation) == 2
    if complete:
        assert len(checks) == 40
    else:
        assert (out / 'FAILURE.txt').is_file()
    assert all(c['status'] == 'PASS' for c in checks + validation)
    computed = len(list(out.glob('pilot_*/computation_complete.txt')))
    summary = {'status': 'PASS' if complete else 'STOPPED_VALIDATION_FAILURE',
               'planned_replications': 40, 'fully_validated_replications': len(checks),
               'computed_replications': computed, 'validation_replications_excluded': 2,
               'computed_pilot_arms': computed*5, 'computed_outcome_fits': computed*4,
               'known_benchmarks': computed, 'critical_validation_failures': 0 if complete else 1,
               'protected_files_unchanged': preservation['files_checked'],
               'max_independent_W_difference': max(a['W_difference'] for c in checks for a in c['arms'].values()),
               'max_KKT_stationarity_over_n': max(a.get('kkt_stationarity_over_n', 0) for c in checks for a in c['arms'].values()),
               'max_P00_ordinary_fitted_difference': max(c['p00_ordinary_fitted_max_difference'] for c in checks)}
    (out / 'output_verification.json').write_text(json.dumps(summary, indent=2))
    source_files = sorted(p for p in HERE.iterdir() if p.is_file())
    source_hashes = {p.name: sha(p) for p in source_files}
    (out / 'source_sha256.json').write_text(json.dumps(source_hashes, indent=2))
    files = sorted(p for p in out.rglob('*') if p.is_file() and p.name != 'artifact_manifest.json')
    manifest = {p.relative_to(out).as_posix(): {'sha256': sha(p), 'bytes': p.stat().st_size} for p in files}
    (out / 'artifact_manifest.json').write_text(json.dumps(manifest, indent=2))
    for name, record in manifest.items():
        assert sha(out / name) == record['sha256'], name
    print(json.dumps(dict(summary, verified_artifacts=len(manifest)), indent=2))


if __name__ == '__main__':
    main()
