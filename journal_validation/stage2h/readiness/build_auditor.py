"""Dimension adapter for the unchanged v1 independent rational verifier."""
from common_h0 import *
def main():
 source=V1/'verify_v1.py';code=source.read_text(encoding='utf-8')
 for name in ['verify_outcome(id)','verify_instruments(id,X)']:
  target='def '+name+':\n';assert code.count(target)==1
  code=code.replace(target,target+" n=int(load(E/id/'metadata.json')['n'])\n")
 code=code.replace('(1000,','(n,')
 before="assert np.array_equal(read(f/(prefix+'last_penalty.bin')),read(OLD/id/'C'/(prefix+'last_penalty.bin')))"
 after="assert sha(f/(prefix+'last_penalty.bin'))==load(f/'calibration_hashes.json')[prefix+'last_penalty.bin']"
 assert code.count(before)==1;code=code.replace(before,after)
 (HERE/'independent_auditor_source.py.txt').write_text(code,encoding='utf-8')
 dump(HERE/'AUDITOR_ADAPTATION.json',{'source':str(source.relative_to(ROOT)),'source_sha256':sha(source),
  'adapted_sha256':sha(HERE/'independent_auditor_source.py.txt'),
  'changes':['Read n from each fixed diagnostic metadata; replace n=1000 reshape dimensions',
    'Replace old-panel penalty comparison with checksum locked immediately after native calibration',
    'Set input/output roots at execution; do not call old main'],
  'unchanged':'direct rational KKT, uniqueness, Gram witness, psi rounding, determinant and W interval verification'})
if __name__=='__main__':main()
