from pathlib import Path
import json, csv, hashlib, os
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OLD=HERE.parent/'full_path_validation/results'
OUT=HERE/'results'
E=ROOT/'journal_validation/stage2e/output/paired_20261029T093009Z'
def dump(p,x):
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(x,indent=2,allow_nan=False),encoding='utf-8')
def load(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def snapshot():
 d={}
 for base,dirs,files in os.walk(ROOT):
  base=Path(base);dirs[:]=[v for v in dirs if base/v!=HERE and not(base==ROOT and v=='.git')]
  for f in files:
   p=base/f;d[p.relative_to(ROOT).as_posix()]=sha(p)
 return d
def rows(p):
 with p.open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def table(p,r):
 with p.open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=list(r[0]));w.writeheader();w.writerows(r)
def read(p,shape=None):
 a=np.fromfile(p,dtype='<f8');return a.reshape(shape) if shape else a
def cases():return [r['id'] for r in rows(OLD/'tasks.csv') if r['variant']=='C']
