from common import *

def main():
 assert json.loads((OUT/'independent_verification.json').read_text())['paths']==72
 assert json.loads((OUT/'adaptive_verification.json').read_text())['fits']==144
 assert json.loads((OUT/'verify_process.json').read_text())['returncode']==0
 assert (HERE/'FULL_PATH_REPORT.md').is_file()
 before=json.loads((OUT/'protected_before.json').read_text());after=snapshot()
 result={'files_checked':len(before),'changed':[p for p in before if p in after and before[p]!=after[p]],'missing':sorted(before.keys()-after.keys()),'added_outside_full_path_validation':sorted(after.keys()-before.keys())}
 dump(OUT/'protected_after.json',after);dump(OUT/'preservation.json',result)
 assert not any(result[k] for k in ['changed','missing','added_outside_full_path_validation']),result
 m=json.loads((G/'SHA256_MANIFEST.json').read_text())
 for name,r in m.items():assert sha(G/name)==r['sha256']
 dump(OUT/'stage2g_preservation.json',{'status':'PASS','listed_artifacts':len(m),'manifest_itself_sha256':sha(G/'SHA256_MANIFEST.json')})
 dump(HERE/'SHA256_MANIFEST.json',{p.relative_to(HERE).as_posix():{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(HERE.rglob('*')) if p.is_file() and p!=HERE/'SHA256_MANIFEST.json'})
 print(json.dumps(result),flush=True)
if __name__=='__main__':main()
