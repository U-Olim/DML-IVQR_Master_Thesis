from common_h0 import *
import subprocess,shutil,platform
from concurrent.futures import ThreadPoolExecutor
from win_memory import Monitor
def command(cmd,log):
 with log.open('w',encoding='utf-8') as f:
  p=subprocess.run(cmd,cwd=ROOT,env=os.environ.copy(),stdout=f,stderr=subprocess.STDOUT)
 if p.returncode:raise RuntimeError(str(cmd)+' failed; see '+str(log))
def main():
 assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()=='journal-validation'
 OUT.mkdir(exist_ok=True);INPUT.mkdir(exist_ok=True)
 if not (OUT/'protected_before.json').exists():dump(OUT/'protected_before.json',snapshot())
 # Freeze diagnostic design BEFORE any new fit. One truth candidate per cell.
 design=[{'id':f'n{n}_t{int(t*100):02d}_k{int(k*100):03d}','n':n,'tau':t,'kappa':k,'candidate':'truth','diagnostic_index':1}
  for n in (500,1000) for t in (.1,.5,.9) for k in (1.,.1)]
 table(HERE/'DESIGN.csv',design)
 dump(HERE/'DESIGN_LOCK.json',{'master_seed':2026110201,'primitive_samples':2,'diagnostic_cells':12,'candidates_per_cell':1,
  'pairing':'same original primitives across tau/kappa within n; separate n streams; separate tau penalty substreams shared across kappa',
  'DGP':'unchanged make_kappa_dataset, p100 s7 rho.3','statistical_Monte_Carlo':False,'bounded_DGP_implemented':False,
  'candidate':'original alpha_true(tau); no alternative candidates or replacements',
  'frozen_v1_config_sha256':sha(V1/'CONFIG_v1.json')})
 for d in design:dump(INPUT/d['id']/'metadata.json',d)
 shutil.copyfile(ROOT/'journal_validation/stage2e/output/paired_20261029T093009Z/cutoff.bin',INPUT/'cutoff.bin')
 source=load(V1/'SHA256_MANIFEST.json')
 for name,r in source.items():assert sha(V1/name)==r['sha256'],name
 dump(OUT/'source_integrity.json',{'version1_manifest_files_verified':len(source),'config_sha256':sha(V1/'CONFIG_v1.json')})
 modes=sys.argv[1:] or ['prepare','sequential','repeat','parallel']
 phases=load(OUT/'phases.json') if (OUT/'phases.json').exists() else []
 for mode in modes:
  mon=Monitor().start();start=time.perf_counter()
  if mode=='prepare':command([r'C:/Program Files/R/R-3.4.3/bin/x64/Rscript.exe','--vanilla',str(HERE/'prepare_original.R')],OUT/'prepare.log')
  else:
   (OUT/mode).mkdir(exist_ok=True)
   def one(d):
    command([sys.executable,'-B',str(HERE/'candidate_h0.py'),d['id'],mode],OUT/mode/(d['id']+'.log'))
   with ThreadPoolExecutor(max_workers=2 if mode=='parallel' else 1) as pool:list(pool.map(one,design))
  elapsed=time.perf_counter()-start;measurement=mon.finish()
  phases.append({'mode':mode,'workers':2 if mode=='parallel' else 1,'wall_seconds':elapsed,'memory':measurement})
  dump(OUT/'phases.json',phases);print(mode,'finished',elapsed,flush=True)
if __name__=='__main__':main()
