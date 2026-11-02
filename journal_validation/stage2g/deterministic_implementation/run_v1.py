import os,sys
sys.dont_write_bytecode=True
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from common_v1 import *
import subprocess,platform,scipy
from scipy.optimize._highspy import _core
def main():
 OUT.mkdir(exist_ok=True)
 baseline=OUT/'protected_before.json'
 if not baseline.exists():dump(baseline,snapshot())
 manifests=[]
 for directory in [G/'full_path_validation',G/'end_to_end_certification']:
  mf=load(directory/'SHA256_MANIFEST.json')
  for name,r in mf.items():assert sha(directory/name)==r['sha256'],(directory,name)
  manifests.append({'directory':str(directory.relative_to(ROOT)),'files':len(mf)})
 dump(OUT/'source_integrity.json',manifests)
 dump(OUT/'environment.json',{'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,
  'longdouble_significand_bits':np.finfo(np.longdouble).nmant+1,'longdouble_bytes':np.dtype(np.longdouble).itemsize,
  'HiGHS':'.'.join(str(getattr(_core,'HIGHS_VERSION_'+v)) for v in ['MAJOR','MINOR','PATCH']),
  'platform':platform.platform(),'threads':{k:os.environ[k] for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']},
  'branch':subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip(),
  'HEAD':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
  'numpy_configuration':str(np.show_config(mode='dicts'))})
 steps=sys.argv[1:] or ['outcome','calibration','instrument','verify','compare']
 processes=load(OUT/'processes.json') if (OUT/'processes.json').exists() else []
 for step in steps:
  command=([r'C:/Program Files/R/R-3.4.3/bin/x64/Rscript.exe','--vanilla',str(HERE/'calibration_v1.R')] if step=='calibration'
   else [sys.executable,'-B',str(HERE/({'outcome':'outcome_v1.py','instrument':'instrument_v1.py','verify':'verify_v1.py','compare':'compare_v1.py'}[step]))])
  start=time.perf_counter()
  with (OUT/(step+'.log')).open('w',encoding='utf-8') as log:
   result=subprocess.run(command,cwd=ROOT,env=os.environ.copy(),stdout=log,stderr=subprocess.STDOUT)
  processes.append({'step':step,'returncode':result.returncode,'seconds':time.perf_counter()-start});dump(OUT/'processes.json',processes)
  print(step,result.returncode,flush=True)
  if result.returncode:raise RuntimeError('Stage failed; see '+step+'.log')
if __name__=='__main__':main()
