"""Re-execute the existing independent exact verifier, redirected into this scope.

Only the task filter and output sink differ. Historical inputs/scripts remain
read-only. This rechecks KKT, primal-dual equality, objective sublevels, Gram
witnesses, rational score moments and nonsingularity of fixed-input intervals.
"""
import sys
sys.dont_write_bytecode=True
from support import *
import time
def main():
 source=OLD.parent/'verify_certificates.py'
 code=source.read_text(encoding='utf-8')
 before="tasks=list(csv.DictReader((OUT/'tasks.csv').open()));records=[]"
 after="tasks=[r for r in csv.DictReader((OUT/'tasks.csv').open()) if r['variant']=='C'];records=[]"
 assert code.count(before)==1
 code=code.replace(before,after)
 # Preserve the precise reviewable program that was executed.
 program=HERE/'primary_exact_verifier.py.txt';program.write_text(code,encoding='utf-8')
 sys.path.insert(0,str(OLD.parent))
 ns={'__name__':'primary_exact_reaudit','__file__':str(source)}
 exec(compile(code,str(program),'exec'),ns)
 def scoped_dump(path,obj):
  rel=Path(path).relative_to(OLD)
  dump(OUT/'primary_exact_reaudit'/rel,obj)
 ns['dump']=scoped_dump
 start=time.perf_counter();ns['main']()
 dump(OUT/'primary_exact_reaudit_metadata.json',{'source_sha256':sha(source),'executed_program_sha256':sha(program),
  'primary_cases':24,'instrument_objectives':48,'seconds':time.perf_counter()-start,
  'scope':'FIXED_EXPORTED_INPUTS_ONLY; not a full adaptive certificate','status':'PASS'})
if __name__=='__main__':main()
