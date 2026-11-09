"""Versioned operational repair after host interruption; frozen estimators unchanged.

Never overwrite an existing candidate artifact. Three late completions retain
their original artifacts and receive explicit time-limit decision overrides.
Unfinished interrupted attempts remain under results/pilot and are independently
audited; resumed work uses results/resume_v2 with the SAME input IDs and streams.
"""
import os,sys
sys.dont_write_bytecode=True
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
from pathlib import Path
import json,csv,time,datetime,subprocess,threading
from concurrent.futures import ThreadPoolExecutor
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
run=Path((P/'LATEST_RUN.txt').read_text().strip());os.environ['STAGE2H_RUN']=str(run)
from common_h0 import dump,load,sha,table
from run_pilot import mem
from win_memory import Monitor
def main():
 design=list(csv.DictReader((run/'DESIGN.csv').open()))
 for name,h in load(run/'SOURCE_LOCK.json').items():assert sha(ROOT/name)==h,name
 for name,h in load(run/'INPUT_LOCK.json').items():assert sha(run/name)==h,name
 for name,h in load(run/'PREFIT_FINAL_SOURCE_LOCK.json').items():assert sha(P/name)==h,name
 events=[json.loads(s) for s in (run/'execution.jsonl').read_text().splitlines()]
 late={e['id']:{'status':'TIME_LIMIT_UNRESOLVED','attempted':True,'failure_component':'TIME_LIMIT_UNRESOLVED','error':'Host interruption: original process wait returned after 180-second wall deadline; numerical PASS does not qualify decision.','observed_external_elapsed_seconds':e['elapsed_seconds']} for e in events if e['elapsed_seconds']>180}
 if not (run/'status_overrides.json').exists():dump(run/'status_overrides.json',late)
 assert load(run/'status_overrides.json')==late
 interrupted=[]
 from candidate_h0 import audit
 (run/'interruption_audits').mkdir(exist_ok=True)
 for d in design:
  f=run/'results/pilot'/d['id']
  if (f.exists() or (run/'results/pilot'/(d['id']+'.log')).exists()) and not (f/'result.json').exists():
   interrupted.append(d['id']);dest=run/'interruption_audits'/(d['id']+'.json')
   if not dest.exists():
    t=time.monotonic()
    try:r=audit(d['id'],'pilot')
    except Exception as exc:r={'status':'INTERRUPTED_UNRESOLVED','error':repr(exc)}
    r['audit_seconds']=time.monotonic()-t;r['artifacts_preserved']=True;dump(dest,r)
 # Conservatively include preparation in the immutable 12-hour total envelope.
 deadline=run.stat().st_ctime+43200
 info={'version':'operational-v2','reason':'host interruption and stale monitoring host; original wait timeout excluded or failed to enforce elapsed interruption time','numerical_policy_changed':False,'late_completed_records':list(late),'interrupted_attempts_preserved':interrupted,'same_input_ids_and_streams':True,'total_deadline_utc':datetime.datetime.fromtimestamp(deadline,datetime.timezone.utc).isoformat(),'previous_session':'93047','original_events':len(events),'time_limit_rule':'180 seconds including all elapsed wall time; post-completion check as well as repeated waits','original_artifacts_immutable':True}
 if not (run/'INTERRUPTION_REPAIR_v2.json').exists():dump(run/'INTERRUPTION_REPAIR_v2.json',info)
 # New source files only; historical numerical source and previous locks unchanged.
 if not (run/'RESUME_SOURCE_LOCK.json').exists():dump(run/'RESUME_SOURCE_LOCK.json',{f.name:sha(f) for f in P.iterdir() if f.is_file() and f.suffix in ['.py','.R','.md','.txt','.json']})
 for name,h in load(run/'RESUME_SOURCE_LOCK.json').items():assert sha(P/name)==h,name
 output=run/'results/resume_v2';output.mkdir(exist_ok=True)
 lock=threading.Lock();stop=threading.Event();completed=[0];storage=[sum(f.stat().st_size for f in run.rglob('*') if f.is_file())]
 mon=Monitor().start();start=time.time()
 def one(d):
  id=d['id'];folder=output/id;result=folder/'result.json'
  if (run/'results/pilot'/id/'result.json').exists() or result.exists():return
  with lock:
   if time.time()>=deadline or storage[0]>=20*2**30 or mem()<2*2**30:stop.set()
   stopped=stop.is_set()
  if stopped:folder.mkdir(exist_ok=True);dump(result,dict(d,status='RESOURCE_NOT_EXECUTED',attempted=False));return
  log=output/(id+'.log');t=time.time();timed=False
  with log.open('x',encoding='utf-8') as f:
   child=subprocess.Popen([sys.executable,'-B',str(P/'candidate_h0.py'),id,'resume_v2'],cwd=ROOT,env=os.environ.copy(),stdout=f,stderr=subprocess.STDOUT)
   while child.poll() is None:
    remaining=180-(time.time()-t)
    if remaining<=0:
     timed=True;subprocess.run(['taskkill','/PID',str(child.pid),'/T','/F'],stdout=f,stderr=f);child.wait();break
    try:child.wait(timeout=min(1.,remaining))
    except subprocess.TimeoutExpired:pass
  elapsed=time.time()-t
  if elapsed>180:timed=True
  if timed:
   # Preserve any late numerical result; use an operational sidecar status.
   folder.mkdir(exist_ok=True);dump(folder/'operational_status.json',dict(d,status='TIME_LIMIT_UNRESOLVED',attempted=True,elapsed_seconds=elapsed))
   try:timeout_audit=audit(id,'resume_v2')
   except Exception as exc:timeout_audit={'status':'TIME_LIMIT_UNRESOLVED','error':repr(exc),'scope':'independent audit attempt on retained partial certificates after process deadline; does not salvage decision'}
   dump(folder/'timeout_audit.json',timeout_audit)
  if not result.exists():folder.mkdir(exist_ok=True);dump(result,dict(d,status='TIME_LIMIT_UNRESOLVED' if timed else 'PROCESS_UNRESOLVED',attempted=True,returncode=child.returncode))
  with lock:
   completed[0]+=1;storage[0]+=sum(f.stat().st_size for f in folder.rglob('*') if f.is_file())+log.stat().st_size
   e={'id':id,'status':'TIME_LIMIT_UNRESOLVED' if timed else load(result)['status'],'elapsed_seconds':elapsed,'resume_completed':completed[0],'retained_bytes':storage[0]}
   with (run/'resume_execution.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(e)+'\n')
   if completed[0]%12==0:print('resume',completed[0],e['status'],round(time.time()-start),flush=True)
 with ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(one,design))
 dump(run/'EXECUTION_RESUME_v2.json',{'elapsed_seconds':time.time()-start,'memory':mon.finish(),'resource_stop':stop.is_set(),'resumed_evaluations_completed':completed[0],'deadline_utc':info['total_deadline_utc'],'retained_bytes_estimate':storage[0]})
 print('RESUME FINISHED',completed[0],flush=True)
if __name__=='__main__':main()
