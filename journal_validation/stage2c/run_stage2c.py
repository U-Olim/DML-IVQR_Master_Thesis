"""Preservation-first sequential gated pilot; no canonical writes or Git mutations."""
import csv
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from verify_one import verify

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RSCRIPT = Path(r'C:\Program Files\R\R-3.4.3\bin\x64\Rscript.exe')


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def snapshot():
    result = {}
    for directory, subdirs, files in os.walk(ROOT):
        base = Path(directory)
        subdirs[:] = [d for d in subdirs if base / d != HERE and not (base == ROOT and d == '.git')]
        for name in files:
            p = base / name
            result[p.relative_to(ROOT).as_posix()] = sha(p)
    return result


def main():
    cfg = json.loads((HERE / 'config.json').read_text())
    branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=ROOT, text=True).strip()
    assert branch == 'journal-validation', branch
    status = subprocess.check_output(['git', 'status', '--porcelain=v1', '--untracked-files=all'], cwd=ROOT, text=True)
    assert all(line[3:].startswith('journal_validation/stage2c/') for line in status.splitlines()), status
    backup = json.loads(Path(cfg['backup_manifest']).read_text())
    assert backup['verification'] == 'PASS'
    assert sha(Path(cfg['backup_archive'])) == backup['sha256']
    for name, digest in backup['files'].items():
        assert sha(ROOT / name) == digest, 'Backup/source mismatch: ' + name
    for stage in ('stage2a', 'stage2b'):
        p = ROOT / 'journal_validation' / stage / 'output/controlled_20261022_01/output_verification.json'
        assert json.loads(p.read_text())['status'] == 'PASS'
    out = HERE / 'output' / cfg['run_id']
    out.mkdir(parents=True, exist_ok=False)
    (out / 'config.json').write_text(json.dumps(cfg, indent=2))
    (out / 'initial_git_status.txt').write_text(status)
    (out / 'git_head.txt').write_text(subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True))
    (out / 'backup_verified.json').write_text(json.dumps({k: backup[k] for k in ('archive', 'sha256', 'verification')}, indent=2))
    print('Backup verified. Hashing protected files.', flush=True)
    before = snapshot()
    (out / 'protected_before.json').write_text(json.dumps(before, indent=2))
    commands = []
    run_status = 'FAILED'
    try:
        old_hashes = set()
        for st, filename, col in [('stage2a', 'pilot_pairs.csv', 'data_sha256'), ('stage2b', 'all_evaluations.csv', 'data_hash')]:
            with (ROOT / 'journal_validation' / st / 'output/controlled_20261022_01' / filename).open() as f:
                old_hashes.update(r[col] for r in csv.DictReader(f))
        pilot_hashes = set()
        for phase, count in [('validation', cfg['validation_replications']), ('pilot', cfg['replications'])]:
            for idx in range(1, count + 1):
                argv = [str(RSCRIPT), '--vanilla', str(HERE / 'run_one.R'), str(out), phase, str(idx)]
                entry = {'argv': argv, 'cwd': str(ROOT), 'started_utc': datetime.now(timezone.utc).isoformat()}
                print('RUN', phase, idx, flush=True)
                with (out / f'{phase}_{idx:03d}.log').open('w', encoding='utf-8') as log:
                    process = subprocess.run(argv, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
                entry.update(exit_status=process.returncode, finished_utc=datetime.now(timezone.utc).isoformat())
                commands.append(entry)
                (out / 'commands.json').write_text(json.dumps(commands, indent=2))
                assert process.returncode == 0, f'{phase} {idx} computation failed; inspect saved log'
                folder = out / f'{phase}_{idx:03d}'
                evidence = verify(folder)
                (folder / 'verification.json').write_text(json.dumps(evidence, indent=2))
                with (folder / 'evaluations.csv').open() as f:
                    data_hash = next(csv.DictReader(f))['data_hash']
                assert data_hash not in old_hashes and data_hash not in pilot_hashes, 'Data reuse'
                pilot_hashes.add(data_hash)
                print('PASS', phase, idx, 'KKT/frozen components/independent W/canonical replay', flush=True)
            if phase == 'validation':
                (out / 'VALIDATION_PASS.txt').write_text('Two separate preflight samples passed all gates. Pilot authorized by prespecified request.\n')
        run_status = 'COMPLETE'
        (out / 'RUN_COMPLETE.txt').write_text('Exactly 40 fresh pilot datasets completed; two separate validation datasets excluded.\n')
    except Exception as exc:
        (out / 'FAILURE.txt').write_text(repr(exc))
        raise
    finally:
        after = snapshot()
        (out / 'protected_after.json').write_text(json.dumps(after, indent=2))
        record = {'run_status': run_status, 'files_checked': len(before),
                  'changed': [p for p in before if p in after and before[p] != after[p]],
                  'missing': sorted(before.keys() - after.keys()),
                  'added_outside_stage2c': sorted(after.keys() - before.keys())}
        (out / 'preservation.json').write_text(json.dumps(record, indent=2))
        assert not any(record[k] for k in ('changed', 'missing', 'added_outside_stage2c')), record
        print('PRESERVATION', json.dumps(record), flush=True)


if __name__ == '__main__':
    main()
