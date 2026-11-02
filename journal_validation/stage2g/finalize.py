"""Final integrity recheck and self-excluding source/result SHA256 manifest."""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from validate import snapshot,sha,dump

def main():
 out=HERE/'results';before=json.loads((out/'protected_before.json').read_text());after=snapshot()
 preservation={'checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],'missing':sorted(before.keys()-after.keys()),'added':sorted(after.keys()-before.keys())}
 assert not any(preservation[k] for k in ['changed','missing','added']),preservation
 dump(out/'final_preservation.json',preservation)
 dump(HERE/'SHA256_MANIFEST.json',{p.relative_to(HERE).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(HERE.rglob('*')) if p.is_file() and p!=HERE/'SHA256_MANIFEST.json'})
 print(json.dumps(preservation))
if __name__=='__main__':main()
