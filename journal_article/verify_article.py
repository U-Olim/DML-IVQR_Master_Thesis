"""Read-only scientific/editorial checks; writes only journal_article/qa/validation.json."""
from pathlib import Path
import csv, hashlib, json, re, collections

here=Path(__file__).resolve().parent
root=here.parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return p.read_text(encoding='utf-8-sig')
def rows(p):
    return [line.strip() for line in read(p).splitlines()
            if '&' in line and line.strip().endswith('\\\\')
            and re.match(r'^(?:\d|\\SetCell|&)',line.strip())]
def cited(s):
    return {k.strip() for m in re.finditer(r'\\(?:textcite|parencite|cite)(?:\[[^\]]*\])*\{([^}]+)\}',s)
            for k in m[1].split(',')}
report={}
before=json.loads(read(here/'qa/original_files_sha256.json'))
changed=[p for p,h in before.items() if not (root/p).exists() or sha(root/p)!=h]
report['protected_files']={'checked':len(before),'changed_or_missing':changed}
report['bibliography_identical']=sha(here/'references.bib')==sha(root/'thesis/references.bib')
report['table_rows']={p.relative_to(here).as_posix():{'rows':len(rows(p)),
    'identical_to_original':rows(p)==rows(root/'thesis'/p.relative_to(here))}
    for p in (here/'tables').rglob('*.tex')}
report['figure_hashes']={p.relative_to(here).as_posix():sha(p)==sha(
    root/'thesis'/p.relative_to(here).parent/(p.stem+'_thesis.png' if p.name.startswith(('accepted_measure_n','rmse_n')) else p.name))
    for p in (here/'figures').rglob('*') if p.is_file()}
new='\n'.join(read(p) for p in here.rglob('*.tex'))
old='\n'.join(read(p) for p in (root/'thesis').rglob('*.tex'))
report['citations']={'original':len(cited(old)),'article':len(cited(new)),
    'removed_keys':sorted(cited(old)-cited(new))}
refs=set(re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',new))
labels=set(re.findall(r'\\label\{([^}]+)\}',new))|set(re.findall(r'label\s*=\s*\{([^}]+)\}',new))
report['undefined_source_references']=sorted(refs-labels)
report['thesis_self_references']=re.findall(r'\b(?:this|our|the present|master[’\x27]s|the)\s+thesis\b|\bchapter\b',new,re.I)
report['whitespace_word_counts_including_TeX']={
    'original_main_sections':sum(len(read(p).split()) for p in (root/'thesis/sections').glob('*.tex')),
    'article_main_sections':sum(len(read(p).split()) for p in (here/'sections').glob('*.tex'))}
# Recheck the archived validation manifests against their actual computational inputs.
manifest_inputs={}
for name in ['thesis_extension/reporting/output/appendix_tables_validation.json',
             'thesis/figures/generated/selected_figures_validation.json']:
    for p,h in json.loads(read(root/name))['input_sha256'].items():
        p=p.replace('\\','/')
        manifest_inputs[p]=sha(root/p)==h
report['archived_input_hashes']=manifest_inputs
def csvrows(name):
    with (root/'thesis_extension/reporting/output'/name).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))
point=csvrows('table_point_performance_full.csv')
groups=collections.defaultdict(list)
for row in point: groups[(row['n'],row['tau'],row['estimator'])].append(row)
report['point_accuracy_recheck']={
    metric+'_strictly_increasing_sequences':sum(
        all(float(a[metric])<float(b[metric]) for a,b in zip(seq,seq[1:]))
        for vals in groups.values() for seq in [sorted(vals,key=lambda x:-float(x['kappa']))])
    for metric in ['MAE','RMSE']}
cov=csvrows('table_coverage_full.csv')
report['coverage_recheck']={'cells':len(cov),
    'below':sum(float(x['coverage_mc95_upper'])<.95 for x in cov),
    'above':sum(float(x['coverage_mc95_lower'])>.95 for x in cov)}
report['pass']=(not changed and report['bibliography_identical']
    and all(x['identical_to_original'] for x in report['table_rows'].values())
    and all(report['figure_hashes'].values()) and all(manifest_inputs.values())
    and not report['citations']['removed_keys'] and not report['undefined_source_references']
    and not report['thesis_self_references'])
(here/'qa/validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ['table_rows','figure_hashes','archived_input_hashes']},indent=2))
if not report['pass']: raise SystemExit(1)
