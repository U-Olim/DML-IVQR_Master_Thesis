"""Frozen two-worker Stage 2H pilot; all writes confined to this directory."""
import os,sys
sys.dont_write_bytecode=True
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
import json,hashlib,subprocess,shutil,datetime,time,csv,ctypes,struct,threading
from concurrent.futures import ThreadPoolExecutor
P=Path(__file__).resolve().parent;ROOT=P.parents[2];H=P.parent/'readiness'
R='C:/Program Files/R/R-3.4.3/bin/x64/Rscript.exe'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def dump(p,x):p.write_text(json.dumps(x,indent=2,allow_nan=False),encoding='utf-8')
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def table(p,rr):
 with p.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(dict.fromkeys(k for r in rr for k in r)));w.writeheader();w.writerows(rr)
def mem():
 b=ctypes.create_string_buffer(64);struct.pack_into('I',b,0,64)
 if not ctypes.windll.kernel32.GlobalMemoryStatusEx(b):raise OSError('memory status unavailable')
 return struct.unpack_from('Q',b,16)[0]
def snapshot():
 result={}
 for base,dirs,files in os.walk(ROOT):
  base=Path(base);dirs[:]=[s for s in dirs if base/s!=P and not(base==ROOT and s=='.git')]
  for name in files:
   f=base/name;result[f.relative_to(ROOT).as_posix()]=sha(f)
 return result
def manifest(run):return {str(f.relative_to(ROOT)).replace('\\','/'):sha(f) for base in [P,H,ROOT/'journal_validation/stage2g/deterministic_implementation',ROOT/'thesis_extension/src',ROOT/'thesis_extension/environment'] for f in base.iterdir() if f.is_file() and not f.name.startswith('.')}
def command(cmd,log):
 with log.open('x',encoding='utf-8') as f:subprocess.run(cmd,cwd=ROOT,env=os.environ.copy(),stdout=f,stderr=subprocess.STDOUT,check=True)
def main():
 mode=sys.argv[1]
 if mode=='init':
  assert subprocess.check_output(['git','branch','--show-current'],text=True,cwd=ROOT).strip()=='journal-validation'
  assert not subprocess.check_output(['git','status','--porcelain','--untracked-files=no'],text=True,cwd=ROOT).strip()
  for base in [H,ROOT/'journal_validation/stage2g/deterministic_implementation']:
   for name,r in load(base/'SHA256_MANIFEST.json').items():assert sha(base/name)==r['sha256'],str(base/name)
  backup=Path('C:/Users/User/DML-IVQR_validation_backups/stage2ab_before_stage2c_20261029T074433Z.zip')
  expected=load(backup.with_suffix('.sha256.json'))['sha256'];assert sha(backup)==expected
  disk=shutil.disk_usage(ROOT);available=mem();assert disk.free>22*2**30 and available>=2*2**30
  run=P/'runs'/('paired_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
  run.mkdir(parents=True);(run/'inputs').mkdir();(run/'results').mkdir();(run/'results'/'pilot').mkdir()
  os.environ['STAGE2H_RUN']=str(run)
  design=[]
  for n in [500,1000]:
   for r in range(1,21):
    for ti,t in enumerate([.1,.5,.9]):
     for ki,k in enumerate([1.,.1]):
      for ci,off in enumerate([-.5,0.,.5]):
       pair=f'n{n}_r{r:02d}_t{int(t*100):02d}_k{int(k*100):03d}_c{ci}'
       for arm in ['A','B']:design.append(dict(id=pair+'_'+arm,pair_id=pair,sample_id=f'n{n}_r{r:02d}',n=n,replication=r,tau=t,kappa=k,offset=off,arm=arm))
  table(run/'DESIGN.csv',design)
  for d in design:
   f=run/'inputs'/d['id'];f.mkdir();dump(f/'metadata.json',d)
  shutil.copyfile(H/'inputs/cutoff.bin',run/'inputs/cutoff.bin')
  dump(run/'CONFIG.json',{'seed':2026110281,'R':20,'p':100,'s':7,'rho':.3,'delta':.05,'workers':2,'threads':1,'candidate_wall_seconds':180,'max_elapsed_seconds':43200,'max_retained_bytes':20*2**30,'minimum_available_memory_bytes':2*2**30,'evaluations':1440,'pairs':720,'truth_evaluations':480,'streams':'40 successive nextRNGStream families, n then replication; primitive at family origin; 18 successive nextRNGSubStream penalty families ordered tau,kappa,candidate; A/B reuse same lambda','policy':'2G-D.1 via unchanged H0 arithmetic; no fallback or replacements'})
  dump(run/'PREFLIGHT.json',{'branch':'journal-validation','HEAD':subprocess.check_output(['git','rev-parse','HEAD'],text=True,cwd=ROOT).strip(),'disk_free_bytes':disk.free,'memory_available_bytes':available,'backup':str(backup),'backup_sha256':expected,'backup_scope':'historical Stage 2A/2B; not a complete current-repository backup','version_manifests':'PASS','initial_tracked_tree':'clean','commands':sys.argv,'python':sys.version})
  dump(run/'protected_before.json',snapshot())
  git={str(f.relative_to(ROOT)):sha(f) for f in (ROOT/'.git').rglob('*') if f.is_file()};dump(run/'git_before.json',git)
  dump(run/'SOURCE_LOCK.json',manifest(run))
  (P/'LATEST_RUN.txt').write_text(str(run),encoding='utf-8');print(run,flush=True);return
 run=Path(sys.argv[2] if len(sys.argv)>2 else (P/'LATEST_RUN.txt').read_text().strip());os.environ['STAGE2H_RUN']=str(run)
 for name,h in load(run/'SOURCE_LOCK.json').items():assert sha(ROOT/name)==h,name
 if mode in ['prepare','verify']:
  command([R,'--vanilla',str(P/('prepare_pilot.R' if mode=='prepare' else 'verify_inputs.R'))],run/(mode+'.log'))
  if mode=='verify':dump(run/'INPUT_LOCK.json',{str(f.relative_to(run)):sha(f) for f in (run/'inputs').rglob('*') if f.is_file()})
  return
 if mode=='execute':
  assert (run/'input_validation.csv').exists() and len(list(csv.DictReader((run/'input_validation.csv').open())))==720
  for name,h in load(run/'INPUT_LOCK.json').items():assert sha(run/name)==h,name
  from win_memory import Monitor
  mon=Monitor().start();start=time.monotonic();stop=threading.Event();lock=threading.Lock();completed=0
  design=list(csv.DictReader((run/'DESIGN.csv').open()));beforebytes=sum(f.stat().st_size for f in run.rglob('*') if f.is_file())
  storage=[beforebytes];events=[]
  def one(d):
   nonlocal completed
   id=d['id'];folder=run/'results/pilot'/id;result=folder/'result.json'
   if result.exists():return
   with lock:
    if time.monotonic()-start>=43200 or storage[0]>=20*2**30 or mem()<2*2**30:stop.set()
    stopped=stop.is_set()
   if stopped:
    folder.mkdir(exist_ok=True);dump(result,dict(d,status='RESOURCE_NOT_EXECUTED',attempted=False));return
   log=run/'results/pilot'/(id+'.log');t=time.monotonic()
   with log.open('x',encoding='utf-8') as f:
    p=subprocess.Popen([sys.executable,'-B',str(P/'candidate_h0.py'),id,'pilot'],cwd=ROOT,env=os.environ.copy(),stdout=f,stderr=subprocess.STDOUT)
    try:p.wait(timeout=180)
    except subprocess.TimeoutExpired:
     subprocess.run(['taskkill','/PID',str(p.pid),'/T','/F'],stdout=f,stderr=f);p.wait()
     folder.mkdir(exist_ok=True);dump(result,dict(d,status='TIME_LIMIT_UNRESOLVED',attempted=True,elapsed_seconds=time.monotonic()-t,independent_audit_status='interrupted or not reached; retained partial artifacts'))
   if not result.exists():folder.mkdir(exist_ok=True);dump(result,dict(d,status='PROCESS_UNRESOLVED',attempted=True,returncode=p.returncode))
   with lock:
    storage[0]+=sum(f.stat().st_size for f in folder.rglob('*') if f.is_file())+log.stat().st_size
    completed+=1;event={'id':id,'status':load(result)['status'],'elapsed_seconds':time.monotonic()-t,'completed':completed,'retained_bytes':storage[0]};events.append(event)
    with (run/'execution.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(event)+'\n')
    if completed%12==0:print(completed,'/ 1440',event['status'],'elapsed',round(time.monotonic()-start),flush=True)
  with ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(one,design))
  dump(run/'EXECUTION.json',{'elapsed_seconds':time.monotonic()-start,'memory':mon.finish(),'resource_stop':stop.is_set(),'events':len(events),'retained_bytes_estimate':storage[0]})
  return
 raise ValueError(mode)
if __name__=='__main__':main()
