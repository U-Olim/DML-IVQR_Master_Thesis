"""No data generation: saved-input replay and certification diagnostics only."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
import sys
sys.dont_write_bytecode=True
from support import *
import subprocess,time
def main():
 OUT.mkdir(exist_ok=True)
 before=snapshot();dump(OUT/'protected_before.json',before)
 assert len(cases())==24 and len(set(cases()))==24
 # Validate every Stage 2G-F manifest entry, including all 72 input paths.
 parent=OLD.parent; manifest=load(parent/'SHA256_MANIFEST.json')
 for name,record in manifest.items():
  expected=record['sha256'] if isinstance(record,dict) else record
  assert sha(parent/name)==expected,(name,'input checksum mismatch')
 dump(OUT/'source_manifest_verification.json',{'status':'PASS','files':len(manifest),'primary_cases':24,'paths':72})
 commands=[['C:/Program Files/R/R-3.4.3/bin/x64/Rscript.exe','--vanilla',str(HERE/'native_replay.R')],
  [sys.executable,'-B',str(HERE/'density_bounds.py')],
  [sys.executable,'-B',str(HERE/'branch_bounds.py')],
  [sys.executable,'-B',str(HERE/'adaptive_analysis.py')],
  [sys.executable,'-B',str(HERE/'independent_verify.py')],
  [sys.executable,'-B',str(HERE/'reaudit_primary.py')]]
 processes=[]
 for command in commands:
  t=time.perf_counter(); name=Path(command[-1]).stem
  with (OUT/(name+'.log')).open('w',encoding='utf-8') as log:
   result=subprocess.run(command,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,env=os.environ.copy())
  processes.append({'script':name,'returncode':result.returncode,'seconds':time.perf_counter()-t})
  dump(OUT/'processes.json',processes);print(name,result.returncode,flush=True)
  if result.returncode:raise RuntimeError('Stopped: '+name+' failed; see log. No certification may be inferred.')
 after=snapshot();dump(OUT/'protected_after.json',after)
 preservation={'checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],
  'missing':sorted(set(before)-set(after)),'added_outside_scope':sorted(set(after)-set(before))}
 dump(OUT/'preservation.json',preservation)
 assert not any(preservation[k] for k in ['changed','missing','added_outside_scope'])
 print('PRESERVATION PASS',flush=True)
if __name__=='__main__':main()
