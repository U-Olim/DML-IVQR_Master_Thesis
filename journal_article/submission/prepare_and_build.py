"""Build documents and copy frozen evidence only; never run research or install packages."""
from pathlib import Path
import csv, io, json, os, re, shutil, subprocess, sys, time, zipfile

ARTICLE = Path(__file__).resolve().parents[1]
REPO = ARTICLE.parent
ROOT = Path(__file__).resolve().parent
WORK, QA = ROOT / 'work', ROOT / 'qa'
INSTALL = Path(os.environ['LOCALAPPDATA']) / 'Programs/MiKTeX'
RUNTIME = ARTICLE / 'qa/batch4/runtime'
for folder in [WORK, QA, ROOT / 'named', ROOT / 'review']:
    folder.mkdir(parents=True, exist_ok=True)

relative = ['main.tex', 'preamble.tex', 'references.bib']
for directory in ['sections', 'supplementary', 'tables', 'figures']:
    relative.extend(p.relative_to(ARTICLE).as_posix() for p in sorted((ARTICLE / directory).rglob('*'))
                    if p.is_file() and p.suffix.lower() in ['.tex', '.bib', '.png', '.pdf', '.jpg', '.jpeg'])
for variant in ['named', 'review']:
    for rel in relative:
        target = WORK / (variant + '_source') / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ARTICLE / rel, target)

paths = sorted({value for rel in relative if rel.endswith('.tex')
                for value in re.findall(r'\\path\{([^}]+)\}', (ARTICLE / rel).read_text(encoding='utf-8'))
                if not re.fullmatch('[0-9a-f]{40}', value)})
ids = {value: 'R%03d' % (i + 1) for i, value in enumerate(paths)}
selected = {
    'thesis_extension/final/output/n500/summary.csv': 'Full performance and grid summaries, n=500',
    'thesis_extension/final/output/n500/power_summary.csv': 'False-candidate rejection summaries, n=500',
    'thesis_extension/final/output/n1000/summary.csv': 'Full performance and grid summaries, n=1000',
    'thesis_extension/final/output/n1000/power_summary.csv': 'False-candidate rejection summaries, n=1000',
    'thesis_extension/reporting/output/table_cr_informativeness_full.csv': 'Grid informativeness, all main design cells',
    'thesis_extension/reporting/output/table_grid_domain_diagnostic.csv': 'Domain-expansion summaries',
    'thesis_extension/calibration/instrument_strength_100rep/kappa_strength_summary.csv': 'Instrument-relevance calibration summaries'
}
assert set(selected) <= set(ids)
review = WORK / 'review_source'
main = (review / 'main.tex').read_text(encoding='utf-8')
a, b = main.index('% Confirmed author order,'), main.index('\\date{}')
main = main[:a] + '% Review copy: no identities or affiliation/contact block.\n\\author{}\n' + main[b:]
main = re.sub(r'pdfauthor=\{[^}]*\}', 'pdfauthor={}', main)
(review / 'main.tex').write_text(main, encoding='utf-8', newline='\n')

availability = r'''\section*{Data and code availability}
This study uses simulated data and archived computational outputs. A local optional evidence bundle, \texttt{frozen\_summaries\_review.zip}, contains seven existing compact CSV summaries and a record inventory. These files have been copied without numerical changes; they support inspection without re-estimation. Their inclusion in this local package is not verification of reviewer access through the journal. Anonymous access to the full external archive and remaining provenance records has not been arranged or verified.

Appendix~\ref{app:evidence-map} retains the claim-to-evidence map with neutral record identifiers. The bundle inventory distinguishes included summaries from records that are not attached. The full original path/revision mapping is retained in the named package. The historical freeze checkout remains unresolved; its identifying token is withheld in this review copy, not replaced by a verified release claim. A checked evidence checkpoint does not identify the current manuscript revision.

Historical rerunning requires the recorded R~3.4.3 environment and pinned dependencies. Their presence in the original archive does not establish portability or exact replay. Main-run worker-specific penalty states are not recoverable from the parent seed alone. Large grid-diagnostic profiles/primitives and Stage 2H pilot raw outputs and their seal are local, Git-ignored artifacts, not promised public or attached data. No public deposit of those artifacts or portable historical runtime is established. Historical estimator results have not been replaced by later certified solutions.
'''
(review / 'sections/data_availability.tex').write_text(availability, encoding='utf-8', newline='\n')
p = review / 'supplementary/D_implementation.tex'
s = p.read_text(encoding='utf-8')
s = s.replace(s.splitlines()[5], 'The full archive location, revision identifiers and original paths are withheld in this review copy to limit direct identification. Neutral record identifiers below preserve the evidence associations; the full mapping is retained with the named package. Only the compact CSV summaries identified in the optional bundle inventory are attached locally. Full external anonymous access is not arranged or verified, and the historical freeze checkout remains unresolved. These access limits do not imply bit-for-bit regeneration from a seed on arbitrary systems.', 1)
p.write_text(s, encoding='utf-8', newline='\n')
p = review / 'supplementary/D_evidence_map.tex'
s = p.read_text(encoding='utf-8')
s = s.replace(s.splitlines()[2], 'Repository locations and revision identifiers are withheld in this review copy. Neutral record identifiers below correspond to the retained named evidence map; the optional CSV bundle inventory states which records are included and which are not attached. Full external anonymous access remains unresolved. Keys E1--E6 retain their original claim/evidence associations; no comparison count or statistic is recomputed.')
p.write_text(s, encoding='utf-8', newline='\n')
for rel in relative:
    if rel.endswith('.tex'):
        p = review / rel
        original = p.read_text(encoding='utf-8')
        s = re.sub(r'\\path\{([^}]+)\}', lambda m: r'\texttt{' + ids[m.group(1)] + '}'
                   if m.group(1) in ids else r'\texttt{revision identifier withheld}', original)
        if s != original:
            p.write_text(s, encoding='utf-8', newline='\n')

for rel in relative:
    if rel.startswith(('figures/', 'tables/')) or rel == 'references.bib' or re.match(r'sections/0[1-6]_', rel):
        assert (review / rel).read_bytes() == (WORK / 'named_source' / rel).read_bytes(), rel
abstract = lambda s: s.split('\\begin{abstract}\n', 1)[1].split('\n\\end{abstract}', 1)[0]
assert abstract((review / 'main.tex').read_text()) == abstract((WORK / 'named_source/main.tex').read_text())

inventory, private_map = [], []
for original, record_id in ids.items():
    attached = original in selected
    entry = {'record_id': record_id, 'description': selected.get(original, 'Original evidence/source/provenance locator; not included in this CSV bundle'),
             'attachment': ('data/' + record_id + '.csv') if attached else '',
             'status': 'Included unchanged CSV' if attached else 'Not included in this CSV bundle; document dependencies may be in the source archive; external record access unresolved'}
    inventory.append(entry)
    private_map.append(dict(entry, original_path=original))
with (ROOT / 'named/provenance_mapping.csv').open('w', encoding='utf-8', newline='') as h:
    writer = csv.DictWriter(h, fieldnames=list(private_map[0])); writer.writeheader(); writer.writerows(private_map)
with zipfile.ZipFile(ROOT / 'review/frozen_summaries_review.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    temp = io.StringIO(newline='')
    writer = csv.DictWriter(temp, fieldnames=list(inventory[0])); writer.writeheader(); writer.writerows(inventory)
    z.writestr('record_inventory.csv', temp.getvalue())
    z.writestr('README.txt', 'Optional local review evidence bundle: seven archived compact CSV summaries, unchanged.\nRecord IDs match the review manuscript. Other records are not included in this CSV bundle; some document dependencies are in the separate source archive.\nJournal acceptance of ZIP uploads, reviewer visibility and full external anonymous access are unverified.\nNo simulations, estimation or statistical validation were performed to create this attachment.\n')
    for original in selected:
        z.write(REPO / original, 'data/' + ids[original] + '.csv')
with zipfile.ZipFile(ROOT / 'review/frozen_summaries_review.zip') as z:
    for original in selected:
        assert z.read('data/' + ids[original] + '.csv') == (REPO / original).read_bytes()
for variant in ['named', 'review']:
    with zipfile.ZipFile(ROOT / variant / ('source_' + variant + '.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for rel in relative:
            z.write(WORK / (variant + '_source') / rel, rel)
terms = ['umurzokov', 'kostaev', 'olimumurzokov022', 'umidjonkostaev2025', 'orcid.org/0009',
         '0009-0008-0090-7100', '0009-0000-0205-5142', 'Tashkent State University',
         'github.com/U-Olim', 'DML-IVQR_Master_Thesis', '15b8b4dc', 'ac9a9cca', '0f4188ca']
for rel in relative:
    if rel.endswith(('.tex', '.bib')):
        s = (review / rel).read_text(encoding='utf-8')
        assert not any(t.lower() in s.lower() for t in terms), rel

assert (RUNTIME / 'miktexstartup.ini').exists()
records = []
if '--review-only' in sys.argv and (QA / 'build_results.json').exists():
    records = [x for x in json.loads((QA / 'build_results.json').read_text()) if x['variant'] == 'named']
for variant in (['review'] if '--review-only' in sys.argv else ['named', 'review']):
    out = WORK / (variant + '_build'); out.mkdir(parents=True, exist_ok=True)
    source = WORK / (variant + '_source')
    env = os.environ.copy()
    env.update({'MIKTEX_USERCONFIG': str(RUNTIME / 'config'), 'MIKTEX_USERDATA': str(RUNTIME / 'data'),
                'MIKTEX_USERINSTALL': str(INSTALL), 'MIKTEX_USERSTARTUPFILE': str(RUNTIME / 'miktexstartup.ini'),
                'LANG': 'C', 'LC_ALL': 'C', 'PAR_GLOBAL_TEMP': str(RUNTIME),
                'TEXINPUTS': str(out) + ';' + str(source) + ';', 'BIBINPUTS': str(source) + ';'})
    for name in ['main.aux', 'main.bcf', 'main.bbl', 'main.out', 'main.run.xml']:
        target = out / name
        assert target.parent == out and out.is_relative_to(ROOT)
        if target.exists():
            target.unlink()
    latex = [str(INSTALL / 'miktex/bin/x64/pdflatex.exe'), '--disable-installer', '-no-shell-escape',
             '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory=' + str(out), 'main.tex']
    biber = [str(INSTALL / 'executables/windows-x64/biber/biber.exe'), '--input-directory', str(out), '--output-directory', str(out), 'main']
    for step, cmd in [('latex1', latex), ('biber', biber), ('latex2', latex), ('latex3', latex)]:
        print('Starting', variant, step, flush=True)
        start = time.monotonic()
        with (QA / (variant + '_' + step + '.txt')).open('w', encoding='utf-8') as log:
            process = subprocess.Popen(cmd, cwd=out, env=env, stdout=log, stderr=subprocess.STDOUT)
            try:
                code = process.wait(timeout=240)
            except subprocess.TimeoutExpired:
                process.kill(); code = 'TIMEOUT'
        records.append({'variant': variant, 'step': step, 'exit_code': code,
                        'seconds': round(time.monotonic() - start, 2), 'command': cmd})
        (QA / 'build_results.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
        print(variant, step, code, flush=True)
        if code != 0:
            raise SystemExit(1)
    shutil.copyfile(out / 'main.pdf', ROOT / variant / ('manuscript_' + variant + '.pdf'))
(ROOT / 'named/package_manifest.json').write_text(json.dumps({'records': private_map,
    'scientific_inputs_identical': True, 'source_files': relative,
    'reviewer_access': 'Local attachment assembled only; portal visibility and full external access unverified'}, indent=2), encoding='utf-8')
print('Both document builds completed; no submission or anonymous repository created.', flush=True)

# Optional separate full-table supplement: use existing entries, no numerical regeneration.
source = WORK / 'review_source'
out = WORK / 'tables_build'; out.mkdir(parents=True, exist_ok=True)
pre = (source / 'preamble.tex').read_text(encoding='utf-8')
pre = '\n'.join(line for line in pre.splitlines() if '{biblatex}' not in line and '\\addbibresource' not in line) + '\n'
(out / 'supplement_preamble.tex').write_text(pre, encoding='utf-8')
wrapper = r"""\input{supplement_preamble}
\hypersetup{pdftitle={Supplementary Tables: Full Frozen Results},pdfauthor={}}
\renewcommand{\thetable}{S.\arabic{table}}
\begin{document}
\section*{Supplementary Tables: Full Frozen Results}
These optional tables reproduce existing frozen presentation assets without new calculations. They retain all sample sizes, quantiles and relevance settings in those assets. Direct-at-truth acceptance, false-candidate rejection and finite-grid informativeness are distinct summaries. The historical Coverage label is not independently validated coverage of the stored finite-grid accepted set. Interpretation remains subject to the implementation and numerical limitations in the manuscript.
\input{tables/generated/appendix_point_performance}
\input{tables/generated/appendix_coverage}
\input{tables/generated/appendix_power}
\input{tables/generated/appendix_cr_informativeness}
\end{document}
"""
(out / 'supplementary_tables.tex').write_text(wrapper, encoding='utf-8')
env = os.environ.copy()
env.update({'MIKTEX_USERCONFIG': str(RUNTIME / 'config'), 'MIKTEX_USERDATA': str(RUNTIME / 'data'),
            'MIKTEX_USERINSTALL': str(INSTALL), 'MIKTEX_USERSTARTUPFILE': str(RUNTIME / 'miktexstartup.ini'),
            'TEXINPUTS': str(out) + ';' + str(source) + ';', 'LANG': 'C', 'LC_ALL': 'C'})
cmd = [str(INSTALL / 'miktex/bin/x64/pdflatex.exe'), '--disable-installer', '-no-shell-escape',
       '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', 'supplementary_tables.tex']
for step in ['tables_latex1', 'tables_latex2']:
    print('Starting', step, flush=True)
    start = time.monotonic()
    with (QA / (step + '.txt')).open('w', encoding='utf-8') as log:
        process = subprocess.Popen(cmd, cwd=out, env=env, stdout=log, stderr=subprocess.STDOUT)
        try:
            code = process.wait(timeout=240)
        except subprocess.TimeoutExpired:
            process.kill(); code = 'TIMEOUT'
    records.append({'variant': 'supplement', 'step': step, 'exit_code': code,
                    'seconds': round(time.monotonic() - start, 2), 'command': cmd})
    (QA / 'build_results.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
    print(step, code, flush=True)
    if code != 0:
        raise SystemExit(1)
shutil.copyfile(out / 'supplementary_tables.pdf', ROOT / 'review/supplementary_tables_review.pdf')
shutil.copyfile(out / 'supplementary_tables.pdf', ROOT / 'named/supplementary_tables.pdf')
for variant in ['named', 'review']:
    with zipfile.ZipFile(ROOT / variant / ('source_' + variant + '.zip'), 'a', zipfile.ZIP_DEFLATED) as z:
        for rel in ['supplementary_tables.tex', 'supplement_preamble.tex']:
            z.write(out / rel, rel)
print('Optional existing-table PDF completed; no portal requirement or reviewer access is asserted.', flush=True)
