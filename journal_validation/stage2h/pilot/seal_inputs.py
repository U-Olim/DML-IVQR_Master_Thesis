"""Seal the independently replayed v2 inputs before any candidate execution."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import csv,json,hashlib
P=Path(__file__).resolve().parent;run=Path((P/'LATEST_RUN.txt').read_text().strip())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
rr=list(csv.DictReader((run/'input_validation.csv').open()));bb=list(csv.DictReader((run/'binary_input_validation.csv').open()))
assert len(rr)==720 and all(all(v=='PASS' for k,v in r.items() if k!='pair_id') for r in rr)
assert len(bb)==1440 and all(r['status']=='PASS' for r in bb)
assert not any((run/'results/pilot').iterdir()),'Seal must precede any fitting'
with (run/'INPUT_LOCK.json').open('x',encoding='utf-8') as f:json.dump({str(p.relative_to(run)):sha(p) for p in (run/'inputs').rglob('*') if p.is_file()},f,indent=2)
with (run/'PREFIT_FINAL_SOURCE_LOCK.json').open('x',encoding='utf-8') as f:json.dump({p.name:sha(p) for p in P.iterdir() if p.is_file() and p.suffix in ['.py','.R','.txt','.md','.json']},f,indent=2)
print('Sealed 720 independently replayed pairs and 1440 independently checked binary inputs',flush=True)
