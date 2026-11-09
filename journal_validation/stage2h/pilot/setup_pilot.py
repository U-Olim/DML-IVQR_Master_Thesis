"""Create mechanical H0 adapters without editing historical source."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
H=P.parent/'readiness'
def save(name,s): (P/name).write_text(s,encoding='utf-8')
common=(H/'common_h0.py').read_text()
common=common.replace("HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];OUT=HERE/'results';INPUT=HERE/'inputs'", "HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];RUN=Path(os.environ['STAGE2H_RUN']);OUT=RUN/'results';INPUT=RUN/'inputs'")
save('common_h0.py',common)
save('win_memory.py',(H/'win_memory.py').read_text())
candidate=(H/'candidate_h0.py').read_text()
candidate=candidate.replace("result['error']=repr(exc)","result['failure_component']=('OUTCOME_UNRESOLVED' if not (f/'outcome_certificate.json').exists() else 'INSTRUMENT_UNRESOLVED' if not (f/'instrument_2_certificate.json').exists() else 'INFERENCE_UNRESOLVED'); result['error']=repr(exc)")
candidate=candidate.replace("finally:\n  result['total_candidate_seconds']", "finally:\n  if result['status']!='PASS':\n   t=time.perf_counter()\n   try: independent=audit(id,mode)\n   except Exception as exc: independent={'status':'UNRESOLVED','error':repr(exc),'scope':'independent audit of retained attempted certificates; missing artifacts explicit'}\n   dump(f/'independent_verification.json',independent);result['independent_audit_seconds']=time.perf_counter()-t\n  result['total_candidate_seconds']")
save('candidate_h0.py',candidate)
cal=(H/'calibrate_original.R').read_text().replace("file.path('journal_validation/stage2h/readiness/inputs',id,'task.rds')","file.path(Sys.getenv('STAGE2H_RUN'),'inputs',id,'task.rds')")
save('calibrate_original.R',cal)
save('independent_auditor_source.py.txt',(H/'independent_auditor_source.py.txt').read_text())
names=['common_h0.py','candidate_h0.py','calibrate_original.R','win_memory.py','independent_auditor_source.py.txt']
save('ADAPTER_CHANGES.json',json.dumps({'base':'Stage 2H-0 audited dimension adapter','changes':['Input/output roots point to immutable pilot run via STAGE2H_RUN','Explicit component status and independent audit attempts for failed candidates','No numerical objectives, tolerances, calibration or certificate arithmetic changed'], 'sources':{n:{'historical_sha256':hashlib.sha256((H/n).read_bytes()).hexdigest(),'pilot_sha256':hashlib.sha256((P/n).read_bytes()).hexdigest()} for n in names}},indent=2))
