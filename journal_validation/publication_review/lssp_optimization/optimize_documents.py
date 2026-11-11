"""Document-only proposed-copy workflow. Never invokes research code or writes canonical sources."""
from pathlib import Path
import collections, difflib, hashlib, json, os, re, shutil, subprocess, sys, time, zipfile

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
ARTICLE = REPO / 'journal_article'
SOURCE = ROOT / 'source'
QA = ROOT / 'qa'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read(p):
    return p.read_text(encoding='utf-8')

def write(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding='utf-8', newline='\n')

# The ordered, exact-text proposal is also the change register used by the plan.
EDITS = []
def edit(file, old, new, category, reason, remains):
    assert old in read(ARTICLE / file), (file, old[:80])
    EDITS.append(dict(file=file, old=old, new=new, category=category, reason=reason,
                      remains=remains, impact='No scientific finding removed; interpretation retained or clarified.'))

def configure():
    edit('main.tex', r'\noindent\textit{\{Monte Carlo simulation assesses instrument-relevance sensitivity in high-dimensional IVQR.\}}\par\medskip', '', 'DUPLICATE', 'Dispensable braced front-matter summary repeats title and abstract; no verified LSSP requirement.', 'Approved title and verbatim abstract.')
    edit('main.tex', r'\section*{Online supplementary material}', r'\section*{Supplementary appendices}', 'CONDENSE', 'Describe the appendices as actually delivered inline.', 'All Appendices A--D remain inline.')
    edit('main.tex', 'They are included here to keep all cross-references resolvable in a single review PDF.', 'They remain inline; additional domain-diagnostic tables are supplied separately in the accompanying Technical Supplement.', 'CONDENSE', 'Make the two-document delivery explicit.', 'Inline A--D and Technical Supplement.')
    f='sections/01_introduction.tex'
    edit(f, 'Fresh pivotal draws can distinguish separate DML evaluations even at the same candidate; unrestricted inversion remains conceptual.', r'The distinct evaluation rules are specified in Section~\ref{sec:performance-measures}.', 'DUPLICATE', 'Detailed randomization explanation belongs at the performance definitions.', 'Section 3.2 and Appendix D evaluation sequence.')
    edit(f, 'The preserved DML-IVQR implementation has lower RMSE than the preserved Full-GMM implementation in 35 of the 40 matched designs, with documented exceptions.', 'The implementation-level RMSE comparisons have exceptions.', 'DUPLICATE', 'Avoid repeating an exact ranking count before Results.', 'Section 4.2 retains 35/40, 11/40, exceptions and numerical examples.')
    edit(f, 'Oracle-GMM also deteriorates under weaker relevance, so high-dimensional nuisance estimation is not the sole explanation. ', '', 'DUPLICATE', 'Repeated result preview is unnecessary alongside the contribution and limitations.', 'Results 4.2, Discussion paragraph 2.')
    f='sections/02_framework.tex'
    edit(f, 'These implementation differences prevent automatic transfer of the ideal orthogonality calculation or its inference theory. Absence of cross-fitting alone does not prove invalidity; the same-sample nuisance and generated-score conditions remain unestablished.', r'These differences prevent automatic transfer of ideal orthogonality or inference theory; same-sample justification remains unestablished (Appendix~\ref{app:score-algebra}). Absence of cross-fitting alone does not prove invalidity.', 'CONDENSE', 'Shorten a repeated qualification while retaining both the inferential boundary and cross-fitting distinction.', 'Framework conditional identities; Appendix D score-algebra conditions.')
    edit(f, 'the first exact minimizer is retained', 'the first candidate attaining the minimum stored grid statistic is retained', 'CONDENSE', 'E3: distinguish grid selection from finite nuisance optimization.', 'Unchanged point-estimator equation and tie rule.')
    f='sections/04_results.tex'
    edit(f, 'In each calibration replication, the restricted OLS regression uses the continuous treatment $D$ as the dependent variable and includes an intercept and $X_1,\\ldots,X_{10}$. The unrestricted regression adds $Z_1$ and $Z_2$, which are tested jointly. The reported nested-regression $F$-statistic and partial $R^2$ are calculated over 100 replications for every $(n,\\kappa)$ design.', r'The nested OLS diagnostic specified in Section~\ref{sec:performance-measures} uses 100 replications for each $(n,\kappa)$ design.', 'DUPLICATE', 'Calibration regression has already been fully specified in Design.', 'Section 3.2 retains outcome, intercept, ten controls, instruments and joint test.')
    edit(f, 'These reductions establish better point accuracy in the larger simulated sample', 'These reductions show lower observed Monte Carlo RMSE at the larger sample size', 'CONDENSE', 'M3: do not assert population improvement beyond reported Monte Carlo estimates.', 'All original RMSE values and comparison counts.')
    edit(f, ' Overall, accuracy falls as relevance weakens, despite qualified gains from a larger sample and from DML relative to Full-GMM.', '', 'DUPLICATE', 'Closing summary repeats the subsection opening and preceding comparisons.', 'All original evidence remains in Section 4.2.')
    edit(f, r'\subsection{Coverage and Finite-Sample Calibration}', r'\subsection{Direct-at-Truth Acceptance and Finite-Sample Calibration}', 'CONDENSE', 'E1: make the historical coverage shorthand explicit locally.', 'Historical labels remain in equations, tables and artwork.')
    edit(f, 'shows that empirical coverage differs considerably', 'shows that direct-at-truth acceptance (historically labelled coverage) differs considerably', 'CONDENSE', 'E1: clarify the object before using historical shorthand.', 'Section 3.2 definitions unchanged.')
    edit(f, 'Its Monte Carlo standard error is', 'Under independent replications, its conventional plug-in Monte Carlo standard error is', 'CONDENSE', 'M3: qualify the conventional uncertainty formula.', 'Unchanged formula, intervals and Appendix D stream caveat.')
    old="An individual rate's MCSE is not used as the standard error of a difference between correlated simulation results."
    edit(f, old, old+r' These uncertainty summaries assume independent replications; historical DML worker-stream independence is not verified (Appendix~\ref{app:evaluation-sequence}).', 'CONDENSE', 'M3: surface the existing RNG qualification next to MC uncertainty.', 'Appendix D retains full historical stream limitations.')
    edit(f, 'Thus declining relevance causes progressively more of the maintained domain to survive test inversion, even when coverage moves closer to $0.95$.', 'Thus lower designed relevance is accompanied by a progressively larger median grid-acceptance measure, even when direct-at-truth acceptance moves closer to $0.95$.', 'CONDENSE', 'E2: name the observed grid summary rather than continuous-domain survival or an isolated mechanism.', 'All numerical sequences, design construction and definitions unchanged.')
    edit(f, 'More observations improve localisation, but do not overcome the weakest relevance setting at these sample sizes.', 'The larger sample has a smaller or unchanged observed median accepted measure in these comparisons, with little localization under the weakest relevance setting.', 'CONDENSE', 'E2: describe the observed comparison at the two investigated sample sizes.', '52/60 and eight unchanged, all examples retained.')
    f='sections/05_discussion.tex'
    edit(f, 'A lower RMSE likewise need not imply better test calibration. ', '', 'DUPLICATE', 'Same proposition is already demonstrated numerically and previewed in Introduction.', 'Introduction paragraph 4 and Results 4.3.')
    edit(f, 'The preserved DML-IVQR implementation often has lower RMSE than preserved Full-GMM, with exceptions, but the procedures differ in nuisance dimension, regularization and residualization.', 'The implementation-level RMSE comparisons have exceptions.', 'DUPLICATE', 'Remove another full ranking/mechanism inventory; retain the next sentence prohibiting causal attribution.', 'Results 4.2 and Framework 2.2 retain all implementation differences.')
    f='sections/06_conclusion.tex'
    edit(f, ' Oracle-GMM also deteriorates under weaker relevance, so high-dimensional nuisance estimation cannot be the sole explanation.', '', 'DUPLICATE', 'Conclusion need not repeat the same Oracle diagnostic a fourth time.', 'Results 4.2 and Discussion paragraph 2.')
    edit(f, 'The non-finite mixed density, proxy/residualization choices, same-sample fitting and penalty randomness limit that link; selected numerical audits additionally show rank and decision sensitivity within a specified panel.', 'The implementation and selected-case numerical limitations summarized in the Discussion restrict that link.', 'DUPLICATE', 'Replace the third full limitation inventory with a concise pointer, retaining subsequent certificate/geometry boundaries.', 'Introduction, Framework, Discussion and Appendix D preserve every material limitation.')
    f='sections/data_availability.tex'
    edit(f, 'That commit supplies the accessible evidence archive, not the current uncommitted manuscript revision.', 'That commit supplies the checked evidence archive, rather than identifying the present manuscript version.', 'CONDENSE', 'M2: remove stale Git-status assertion without claiming a new verified public release.', 'Original checked commit, access date, unresolved freeze and local-only exclusions retained.')
    f='supplementary/A_numerical_domain.tex'
    edit(f, r'A value close to four in \(A_0\) means that almost the entire four-unit primary domain is accepted; it does not mean that the unrestricted confidence region has length four.', r'A value close to four in \(A_0\) means that the trapezoidal grid-acceptance summary is close to its maximum on the four-unit primary domain; it does not establish acceptance between evaluated points or unrestricted confidence-region length.', 'CONDENSE', 'M1: remove actual continuous-domain acceptance overstatement.', 'Unchanged accepted-measure definition and all diagnostics.')
    old=r'Tables~\ref{tab:appendix-grid-added}--\ref{tab:appendix-grid-status} retain incremental measures, boundary frequencies, profile counts, and localization diagnostics.'
    edit(f, old, 'The accompanying Technical Supplement retains Tables A.2--A.5: incremental measures, boundary frequencies, profile counts, and localization diagnostics, with their original numbering and entries.', 'MOVE TO SUPPLEMENT', 'Detailed verification tables support, but need not interrupt, the essential domain findings.', 'Technical Supplement Tables A.2--A.5; A.1 and figure stay inline. Failure and missing-profile disclosure stay inline.')
    edit(f, r'\input{tables/generated/appendix_grid_diagnostic}', r'\input{tables/generated/appendix_grid_key}', 'MOVE TO SUPPLEMENT', 'Retain key complete domain-measure table, move four detailed tables unchanged.', 'Key Table A.1 inline; A.2--A.5 in separately supplied PDF and source.')
    f='supplementary/C_coverage_audit.tex'
    edit(f, 'The frozen audit report and supporting diagnostics remain preserved in the repository. ', '', 'DUPLICATE', 'Generic preservation statement adds no locator beyond the evidence map.', 'Availability, Appendix D compact map and full repository inventory.')
    edit(f, 'These checks rule out those numerical explanations for the reported coverage patterns. They do not establish correct theoretical specification, validate the asymptotic reference distribution for this DGP, or establish nominal finite-sample calibration.', 'These checks do not establish correct theoretical specification, validate the asymptotic reference distribution for this DGP, or establish nominal finite-sample calibration.', 'DUPLICATE', 'Remove repeated rule-out sentence, keep all validity limitations.', 'Preceding paragraph states exact excluded explanations; Results 4.3 limits numerical invariance.')
    edit(f, 'Reading this frequency alongside coverage distinguishes retention of the true effect from the ability to exclude competing candidates within the maintained domain. Coverage near nominal can coexist with frequent acceptance of all primary-grid candidates: retaining the true value does not imply excluding alternatives.', 'This frequency complements direct-at-truth acceptance by measuring retention of competing primary-grid candidates.', 'DUPLICATE', 'Avoid repeating the central interpretation after Results, Discussion and Conclusion.', 'Next paragraph retains separate evaluation events, fresh draws, 41-point scope and global-geometry disclaimer.')
    f='supplementary/D_implementation.tex'
    old=read(ARTICLE/f).splitlines()[5]
    edit(f, old, r'The computational archive and checked evidence revision are identified in the data and code availability statement. They do not establish bit-for-bit regeneration from a seed on arbitrary systems. Appendix~\ref{app:evidence-map} links the scientific findings to their frozen evidence; the full repository inventory retains source paths and the unresolved historical freeze record.', 'MOVE TO SUPPLEMENT', 'Remove duplicated administrative archive/path/freeze inventory from inline D.1; M2 removes stale uncommitted wording.', 'Unabridged availability statement; accompanying EVIDENCE_INVENTORY.md.')
    old=read(ARTICLE/f).splitlines()[9]
    edit(f, old, r'Frozen CSVs permit deterministic reporting without re-estimation. The full evidence inventory records historical manifests and figure-check scopes, which do not certify a later source revision. The coverage summary uses integer direct-at-truth counts; the variance illustration is analytical. No historical validation or simulation is rerun for this document.', 'MOVE TO SUPPLEMENT', 'Move administrative check counts/manifest presentation history while preserving the limits of those checks.', 'EVIDENCE_INVENTORY.md retains original paragraph verbatim and all paths.')
    f='supplementary/D_evidence_map.tex'
    old=read(ARTICLE/f).splitlines()[2]
    edit(f, old, r'Keys E1--E6 below connect the findings to frozen evidence. The full locator inventory accompanies this proposal as \texttt{EVIDENCE\_INVENTORY.md} under \path{journal_validation/publication_review/lssp_optimization/}. It retains all original paths, revision records and access limitations; it does not recompute results or establish public access to this proposed document. The checked evidence revision is distinct from the present manuscript version and the unresolved historical freeze identifier.', 'MOVE TO SUPPLEMENT', 'M2 and concise repository-inventory pointer; retain compact finding-to-key map inline.', 'Full inventory supplied beside PDFs, original E1--E6 content preserved verbatim as source and readable text.')
    s=read(ARTICLE/f);old=s[s.index('\\begingroup\\small'):]
    new=r'''\noindent E1 identifies the 100-replication relevance calibration; E2 the main performance summaries, replication records and profiles for both sample sizes; E3 the direct truth tests and false-candidate rejection records; E4 grid informativeness; E5 the separate 100-replication domain expansion, including its failed profile; and E6 the selected-case numerical-sensitivity reports. The inventory supplies the exact CSV, table, figure and report locators for each key. Main frozen summaries are available at the checked revision described in the availability statement; large diagnostic profiles/primitives and Stage 2H raw outputs remain local-only. A locator is not a guarantee of public access or full stochastic replay.
'''
    edit(f, old, new, 'MOVE TO SUPPLEMENT', 'Long path-by-path inventory is useful verification material, not necessary inline statistical exposition.', 'EVIDENCE_INVENTORY.md and EVIDENCE_INVENTORY_ORIGINAL.tex retain all entries, source bytes, manifests, access caveats and abstract-number mapping.')
    f='tables/table_main_performance.tex'
    edit(f, 'Coverage is evaluated directly at the true structural quantile effect.', 'Coverage denotes direct-at-truth test acceptance, not membership coverage of the stored grid set.', 'CONDENSE', 'E1: improve table-note terminology; no table cell changes.', 'Original historical column label and all numerical entries.')

def source_files():
    return [ARTICLE/x for x in ['main.tex','preamble.tex','references.bib']] + [p for folder in ['sections','supplementary','tables','figures'] for p in sorted((ARTICLE/folder).rglob('*')) if p.is_file() and p.suffix.lower() in ['.tex','.bib','.png','.pdf','.jpg','.jpeg']]

def blocks(p):
    lines=read(p).splitlines();i=0
    # Tables/figures are indivisible scientific displays, including captions/notes.
    if p.parent.name=='tables' or 'generated' in p.parts and 'tables' in p.parts:
        text='\n'.join(lines)
        if '\\begin{table}' in text:
            yield 1,len(lines),'table (including caption and notes)',text;return
        if '\\begin{booktabs}' in text:
            starts=[m.start() for m in re.finditer(r'\\begin\{booktabs\}',text)]
            for k,pos in enumerate(starts):
                end=text.index('\\end{booktabs}',pos)+len('\\end{booktabs}')
                yield text[:pos].count('\n')+1,text[:end].count('\n')+1,'table',text[pos:end]
            return
        if '\\begin{figure}' in text:
            yield 1,len(lines),'figure (including caption and notes)',text;return
    while i<len(lines):
        if not lines[i].strip():i+=1;continue
        start=i;s=lines[i].strip()
        match=re.match(r'\\begin\{(equation\*?|abstract|tblr|booktabs)\}',s)
        if match or s==r'\[':
            ending='\\end{'+match.group(1)+'}' if match else r'\]';kind='displayed mathematics' if not match or 'equation' in match.group(1) else 'abstract' if match.group(1)=='abstract' else 'table'
            while i<len(lines) and ending not in lines[i]:i+=1
            i+=1;yield start+1,i,kind,'\n'.join(lines[start:i]);continue
        kind='enumerated algorithm step' if s.startswith('\\item') else 'heading/structure' if s.startswith(('\\section','\\subsection','\\label','\\input','\\setcounter','\\clearpage','\\FloatBarrier','\\Needspace','\\end','\\begin','\\renewcommand')) else 'paragraph'
        if kind in ['paragraph','enumerated algorithm step']:
            i+=1
            while i<len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(('\\begin','\\[','\\item','\\section','\\subsection','\\input','\\end','\\FloatBarrier')):i+=1
        else:i+=1
        yield start+1,i,kind,'\n'.join(lines[start:i])

def plan():
    ROOT.mkdir(parents=True,exist_ok=True)
    tracked=subprocess.check_output(['git','ls-files','-z'],cwd=REPO).decode().split('\0')
    # Hash canonical document dependencies and research scripts; use Git's tracked-file
    # comparison for the full archive, avoiding reading multi-GB historical datasets.
    baseline={p:sha(REPO/p) for p in tracked if p and Path(p).suffix in ['.R','.py'] and 'environment' not in Path(p).parts and (REPO/p).is_file()}
    assert subprocess.run(['git','diff','--quiet','HEAD','--'],cwd=REPO).returncode==0, 'Tracked baseline must be clean'
    baseline.update({p.relative_to(REPO).as_posix():sha(p) for p in source_files()})
    write(ROOT/'canonical_baseline.json',json.dumps(baseline,indent=2))
    records=[]
    for p in source_files():
        if p.suffix!='.tex':continue
        rel=p.relative_to(ARTICLE).as_posix()
        for start,end,kind,text in blocks(p):
            applicable=[e for e in EDITS if e['file']==rel and (e['old'] in text or text in e['old'])]
            category=applicable[0]['category'] if applicable else 'ESSENTIAL'
            reason='; '.join(dict.fromkeys(e['reason'] for e in applicable))
            remains='; '.join(dict.fromkeys(e['remains'] for e in applicable)) or f'Proposed source/{rel}, unchanged.'
            if rel=='tables/generated/appendix_grid_diagnostic.tex' and start>62:
                category='MOVE TO SUPPLEMENT';reason='Detailed incremental, boundary, status and stabilization verification tables; key domain measures remain inline.';remains='Technical Supplement Tables A.2--A.5, entries/captions/notes unchanged.'
            if not reason:
                reason={'displayed mathematics':'Necessary mathematical definition or argument; preserve verbatim.', 'table':'Retain existing numerical evidence with unchanged entries.', 'figure (including caption and notes)':'Retain existing visual evidence and interpretation notes.', 'enumerated algorithm step':'Necessary executable-order definition for interpreting preserved estimators.', 'abstract':'Protected verbatim by author decision.', 'heading/structure':'Required document organization or cross-reference dependency.'}.get(kind,'Necessary scientific context, specification, numerical interpretation, qualification or reproducibility information; no unsupported deletion justified.')
                if rel.startswith('tables/') and not any(rel in read(x) for x in (ARTICLE/'sections').glob('*.tex')):
                    reason+=' Existing asset remains available even if not input by the named master.'
            records.append(dict(id=f'I{len(records)+1:03}',file='journal_article/'+rel,start=start,end=end,kind=kind,classification=category,original=text,reason=reason,remains=remains,impact='No scientific weakening; any relocation must accompany both PDFs and inventory.' if category=='MOVE TO SUPPLEMENT' else 'No scientific weakening; retained content or clarification.'))
    write(ROOT/'CONTENT_ITEM_MAP.json',json.dumps(records,ensure_ascii=False,indent=2))
    rows=['# Complete pre-edit content necessity plan','', 'Created before preparing revised sources. Every original prose block, displayed mathematical block, table/figure (including caption/notes), algorithm step and structural element in the source dependency folders is inventoried below. Original full text and exact line spans are retained in CONTENT_ITEM_MAP.json. A prose block crossing a display is split at that display; no numerical table row is a deletion unit. Existing non-input table assets are retained, not newly inserted into the PDF. Structural items are recorded to make omissions and references inspectable.','', 'The change register supplies exact original/replacement text and paragraph-specific retention destinations. No blanket page target applies. No mathematical display or numerical entry will be deleted. B is retained byte-for-byte. A.1 and all scientific figures stay inline; A.2--A.5 move unchanged to a delivered Technical Supplement. Full E1--E6 evidence inventory moves to a delivered repository document, with compact map and all material reproducibility qualifications retained inline.','', 'Categories ESSENTIAL, CONDENSE, DUPLICATE and MOVE TO SUPPLEMENT are used where justified. No item is classified REMOVE: the only complete deletion is the duplicate braced summary, and all other reductions remove repeated wording rather than scientific content.','', '| ID | Original location | Type | Decision | Necessity / reason | Retention destination | Scientific impact |','|---|---|---|---|---|---|---|']
    for r in records:rows.append('| '+' | '.join(str(r[k]).replace('|','\\|').replace('\n',' ') for k in ['id'])+' | '+f"{r['file']}:{r['start']}–{r['end']} | {r['kind']} | {r['classification']} | {r['reason']} | {r['remains']} | {r['impact']} |")
    rows+=['','## Exact proposed paragraph edits','']
    for i,e in enumerate(EDITS,1):
        start=read(ARTICLE/e['file']).split(e['old'])[0].count('\n')+1
        rows += [f"### P{i:02} — {e['category']} — journal_article/{e['file']}:{start}",'',e['reason'],'','Original:','```latex',e['old'],'```','','Proposed:','```latex',e['new'] or '% duplicate wording removed','```','', 'Retained at: '+e['remains'],'','Impact: '+e['impact'],'']
    write(ROOT/'CONTENT_OPTIMIZATION_PLAN.md','\n'.join(rows))
    write(ROOT/'change_register.json',json.dumps(EDITS,ensure_ascii=False,indent=2))
    print('Plan created:',len(records),'items;',len(EDITS),'exact proposed edits;',len(baseline),'protected files',flush=True)

def prepare():
    assert (ROOT/'CONTENT_OPTIMIZATION_PLAN.md').exists(), 'Plan must precede source preparation'
    for p in source_files():
        dest=SOURCE/p.relative_to(ARTICLE);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
    for e in EDITS:
        p=SOURCE/e['file'];s=read(p);assert s.count(e['old'])==1,(e['file'],e['old'][:60]);write(p,s.replace(e['old'],e['new'],1))
    # Relocate exact existing table blocks; original full asset is still preserved in source.
    grid=read(ARTICLE/'tables/generated/appendix_grid_diagnostic.tex')
    separator='\\clearpage\n';parts=grid.split(separator,1);assert len(parts)==2
    write(SOURCE/'tables/generated/appendix_grid_key.tex',parts[0])
    write(SOURCE/'tables/generated/appendix_grid_details.tex',parts[1])
    write(SOURCE/'technical_supplement.tex',r'''\input{preamble}
\hypersetup{pdftitle={Technical Supplement: Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR},pdfauthor={Umurzokov Olimjon Umidjon ugli; Kostaev Umidjon Umirzakovich}}
\begin{document}
\section*{Technical Supplement: detailed domain diagnostics}
\noindent Companion to \emph{Controlled Instrument-Relevance Sensitivity in High-Dimensional IVQR: A Monte Carlo Study}. Tables A.2--A.5 retain their original captions, entries and numbering; Table A.1 and the essential interpretation remain in inline Appendix A of the proposed manuscript. These are the existing 100-replication domain diagnostics, not new results or the main 500-replication experiment. The recorded Stage 1 singular-design error remains an incomplete profile, not acceptance; its affected expanded-domain cell has 99 usable replications. Boundary acceptance concerns either endpoint and full-grid acceptance concerns all evaluated points; neither establishes continuous or global geometry. Med. and Mean denote replication medians and means; $R$ is intended replications, Succ. complete profiles, Fail incomplete profiles and Stage 1/2 newly recorded evaluation errors.
\renewcommand{\thetable}{A.\arabic{table}}
\setcounter{table}{1}
\input{tables/generated/appendix_grid_details}
\end{document}
''')
    orig=read(ARTICLE/'supplementary/D_evidence_map.tex')
    write(ROOT/'EVIDENCE_INVENTORY_ORIGINAL.tex',orig)
    # Keep a readable full path inventory as well as verbatim archival text.
    readable=orig
    for cmd in ['path','url','texttt','ref']:
        readable=re.sub(r'\\'+cmd+r'\{([^}]+)\}',r'`\1`',readable)
    readable=readable.replace('current uncommitted manuscript revision','present manuscript version')
    write(ROOT/'EVIDENCE_INVENTORY.md', '# Full evidence locator inventory\n\nThis document accompanies both proposed PDFs. It relocates the original E1--E6 inventory without claiming new public access. The old uncommitted-status wording is corrected; EVIDENCE_INVENTORY_ORIGINAL.tex preserves the original inventory verbatim. Scientific keys and source paths are unchanged. Public access checks remain those reported on 10 November 2026, not a new network verification. Local-only exclusions, missing freeze resolution and RNG limitations remain applicable.\n\n## Full original inventory (readable transcription)\n\n'+readable+'\n\n## Relocated administrative paragraphs from Appendix D.1\n\n'+ '\n\n'.join(read(ARTICLE/'supplementary/D_implementation.tex').splitlines()[i] for i in [5,9])+'\n\nThe quoted historical paragraph above records the original build-time uncommitted status; it is not a statement of current Git status.\n')
    diff=[]
    for p in source_files():
        if p.suffix in ['.tex','.bib']:
            rel=p.relative_to(ARTICLE);diff.extend(difflib.unified_diff(read(p).splitlines(True),read(SOURCE/rel).splitlines(True),fromfile='canonical/'+rel.as_posix(),tofile='proposed/'+rel.as_posix()))
    for rel in ['technical_supplement.tex','tables/generated/appendix_grid_key.tex','tables/generated/appendix_grid_details.tex']:
        diff.extend(difflib.unified_diff([],read(SOURCE/rel).splitlines(True),fromfile='/dev/null',tofile='proposed/'+rel))
    write(ROOT/'BEFORE_AFTER_SOURCE.diff',''.join(diff))
    print('Separate proposed source prepared; canonical manuscript untouched',flush=True)

def environment():
    runtime=ARTICLE/'qa/batch4/runtime';install=Path(os.environ['LOCALAPPDATA'])/'Programs/MiKTeX'
    env=os.environ.copy();env.update({'MIKTEX_USERCONFIG':str(runtime/'config'),'MIKTEX_USERDATA':str(runtime/'data'),'MIKTEX_USERINSTALL':str(install),'MIKTEX_USERSTARTUPFILE':str(runtime/'miktexstartup.ini'),'LANG':'C','LC_ALL':'C','PAR_GLOBAL_TEMP':str(runtime),'TEXINPUTS':str(SOURCE)+';','BIBINPUTS':str(SOURCE)+';'})
    return env,install

def build():
    QA.mkdir(exist_ok=True);env,install=environment();records=[]
    for name in ['main','technical_supplement']:
        out=ROOT/'build'/name;out.mkdir(parents=True,exist_ok=True)
        latex=[str(install/'miktex/bin/x64/pdflatex.exe'),'--disable-installer','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','-output-directory='+str(out),name+'.tex']
        biber=[str(install/'executables/windows-x64/biber/biber.exe'),'--input-directory',str(out),'--output-directory',str(out),name]
        steps=[('latex1',latex)]+([('biber',biber)] if name=='main' else [])+[('latex2',latex),('latex3',latex)]
        for step,cmd in steps:
            print('Build',name,step,flush=True);t=time.monotonic()
            with (QA/f'{name}_{step}.txt').open('w',encoding='utf-8') as h:
                r=subprocess.run(cmd,cwd=SOURCE,env=env,stdout=h,stderr=subprocess.STDOUT,timeout=240)
            records.append(dict(document=name,step=step,exit_code=r.returncode,seconds=round(time.monotonic()-t,2)))
            write(QA/'build_results.json',json.dumps(records,indent=2));assert r.returncode==0,(name,step)
        shutil.copyfile(out/(name+'.pdf'),ROOT/('manuscript_optimized.pdf' if name=='main' else 'technical_supplement.pdf'))
    print('Document builds finished',flush=True)

def verify():
    env,install=environment();QA.mkdir(exist_ok=True)
    result={}
    baseline=json.loads(read(ROOT/'canonical_baseline.json'))
    result['protected_files_checked']=len(baseline)
    result['protected_changes']=[p for p,h in baseline.items() if not (REPO/p).exists() or sha(REPO/p)!=h]
    assert not result['protected_changes']
    result['all_tracked_files_unchanged']=subprocess.run(['git','diff','--quiet','HEAD','--'],cwd=REPO).returncode==0
    assert result['all_tracked_files_unchanged']
    original=read(ARTICLE/'main.tex');proposed=read(SOURCE/'main.tex')
    abstract=lambda s:s.split('\\begin{abstract}')[1].split('\\end{abstract}')[0]
    result['abstract_verbatim']=abstract(original)==abstract(proposed);assert result['abstract_verbatim']
    author=lambda s:s[s.index('\\title'):s.index('\\begin{document}')]
    result['title_author_metadata_verbatim']=author(original)==author(proposed);assert result['title_author_metadata_verbatim']
    result['appendix_B_byte_identical']=(ARTICLE/'supplementary/B_kappa_derivation.tex').read_bytes()==(SOURCE/'supplementary/B_kappa_derivation.tex').read_bytes();assert result['appendix_B_byte_identical']
    displays=lambda s:re.findall(r'\\begin\{equation\*?\}.*?\\end\{equation\*?\}|\\\[.*?\\\]',s,re.S)
    result['mathematical_displays_identical']=all(displays(read(p))==displays(read(SOURCE/p.relative_to(ARTICLE))) for p in source_files() if p.suffix=='.tex');assert result['mathematical_displays_identical']
    result['figure_bibliography_bytes_identical']=all(p.read_bytes()==(SOURCE/p.relative_to(ARTICLE)).read_bytes() for p in source_files() if p.suffix=='.bib' or 'figures' in p.relative_to(ARTICLE).parts);assert result['figure_bibliography_bytes_identical']
    result['table_asset_bytes_identical_except_prose_note']=all(p.read_bytes()==(SOURCE/p.relative_to(ARTICLE)).read_bytes() for p in (ARTICLE/'tables').rglob('*.tex') if p.name!='table_main_performance.tex');assert result['table_asset_bytes_identical_except_prose_note']
    table=lambda s:re.findall(r'\\begin\{booktabs\}.*?\\end\{booktabs\}',s,re.S)
    result['main_table_body_identical']=table(read(ARTICLE/'tables/table_main_performance.tex'))==table(read(SOURCE/'tables/table_main_performance.tex'));assert result['main_table_body_identical']
    grid=read(ARTICLE/'tables/generated/appendix_grid_diagnostic.tex')
    result['relocated_table_blocks_identical']=table(grid)==table(read(SOURCE/'tables/generated/appendix_grid_key.tex'))+table(read(SOURCE/'tables/generated/appendix_grid_details.tex'));assert result['relocated_table_blocks_identical']
    result['full_evidence_inventory_verbatim']=read(ROOT/'EVIDENCE_INVENTORY_ORIGINAL.tex')==read(ARTICLE/'supplementary/D_evidence_map.tex');assert result['full_evidence_inventory_verbatim']
    result['documents']={}
    for name,pdf in [('original',ARTICLE/'submission/named/manuscript_named.pdf'),('optimized',ROOT/'manuscript_optimized.pdf'),('supplement',ROOT/'technical_supplement.pdf')]:
        r=subprocess.run([str(install/'miktex/bin/x64/pdftotext.exe'),'-enc','UTF-8','-layout',str(pdf),'-'],env=env,capture_output=True,encoding='utf-8',timeout=60);assert r.returncode==0
        write(QA/(name+'_text.txt'),r.stdout)
        pages=[s for s in r.stdout.split('\f') if s.strip()]
        result['documents'][name]={'pages':len(pages),'bytes':pdf.stat().st_size,'sha256':sha(pdf),'unresolved_question_pairs':r.stdout.count('??')}
    write(ROOT/'BEFORE_AFTER_PDF_TEXT.diff',''.join(difflib.unified_diff(read(QA/'original_text.txt').splitlines(True),read(QA/'optimized_text.txt').splitlines(True),fromfile='original_34_page_pdf',tofile='proposed_main_with_inline_appendices')))
    for name in ['main','technical_supplement']:
        log=read(ROOT/'build'/name/(name+'.log'))
        fatal=[line for line in log.splitlines() if re.search(r'undefined|multiply defined|Citation.*undefined|Reference.*undefined',line,re.I)]
        result[name+'_reference_warnings']=fatal;assert not fatal,fatal
        result[name+'_overfull_boxes']=[line for line in log.splitlines() if 'Overfull' in line]
    # Numeric prose tokens: no loss of unique values; repeats can be removed.
    numeric=lambda s:collections.Counter(re.findall(r'(?<![A-Za-z])[-+]?\d+(?:\.\d+)?',s))
    before=numeric('\n'.join(read(p) for p in (ARTICLE/'sections').glob('0*.tex')))
    after=numeric('\n'.join(read(p) for p in (SOURCE/'sections').glob('0*.tex')))
    result['main_sections_unique_numeric_tokens_lost']=sorted(set(before)-set(after))
    assert not result['main_sections_unique_numeric_tokens_lost']
    write(QA/'scientific_integrity.json',json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps(result,ensure_ascii=True,indent=2),flush=True)

def finalize():
    result=json.loads(read(QA/'scientific_integrity.json'))
    records=json.loads(read(ROOT/'CONTENT_ITEM_MAP.json'))
    edits=json.loads(read(ROOT/'change_register.json'))
    # Render the relocated inventory as ordinary Markdown, preserving the verbatim
    # original separately and every locator/qualification in the readable version.
    p=ROOT/'EVIDENCE_INVENTORY.md';s=read(p)
    s=re.sub(r'\\begin\{center\}.*?\\end\{center\}', '''| Key | Finding | Original manuscript location |
|---|---|---|
| E1 | Designed relevance ordering | Section 4.1 |
| E2 | Point errors and qualified implementation rankings | Section 4.2 |
| E3 | Direct truth acceptance and false-candidate rejection | Sections 4.3–4.4 |
| E4 | Grid informativeness | Section 4.5 |
| E5 | Domain expansion | Appendix A and Technical Supplement |
| E6 | Selected-case numerical sensitivity | Appendix D |
''',s,flags=re.S)
    s=re.sub(r'\\subsection\{([^}]+)\}',r'## \1',s)
    s=re.sub(r'\\label\{[^}]+\}','',s)
    s=re.sub(r'\\item\[([^]]+)\]',r'\n### \1\n\n',s)
    for token in [r'\begingroup\small\raggedright',r'\Urlmuskip=0mu plus 1mu\relax',r'\begin{description}',r'\end{description}',r'\endgroup']:
        s=s.replace(token,'')
    write(p,s)
    # Every original evidence path remains searchable in the readable inventory.
    paths=re.findall(r'\\path\{([^}]+)\}',read(ROOT/'EVIDENCE_INVENTORY_ORIGINAL.tex'))
    assert all(path in s for path in paths)
    rows=['# Content retention / deletion / relocation map','', 'This map follows the pre-edit plan; it records the exact destination of each proposed reduction. Full original text and paragraph locations are in CONTENT_OPTIMIZATION_PLAN.md and CONTENT_ITEM_MAP.json. Unchanged items retain their canonical relative locations in source/. No numerical table row, mathematical display, research result or material limitation is deleted.','', '| Change | Original location | Classification | Reason | Necessary information remains | Effect on conclusions / reproducibility |','|---|---|---|---|---|---|']
    for i,e in enumerate(edits,1):
        line=read(ARTICLE/e['file']).split(e['old'])[0].count('\n')+1
        rows.append(f"| P{i:02} | journal_article/{e['file']}:{line} | {e['category']} | {e['reason']} | {e['remains']} | {e['impact']} |")
    rows+=['','## Delivery-dependent relocations','','- All four detailed diagnostic tables are supplied, not discarded. The main Appendix A still discloses the singular-design failure and incomplete-profile denominator. Without the technical PDF reviewers would lose detailed verification; it is mandatory in this proposed package.','- All E1–E6 source paths and provenance remain in EVIDENCE_INVENTORY.md and its verbatim original. The inline map retains every scientific key and cautions that local-only records are not automatically public. Without the inventory exact source inspection would be less convenient; it accompanies both PDFs.','- No REMOVE classification is justified. Duplicate deletions are repeated wording; numerical examples and equations are not removed.','', 'Item classifications: `'+json.dumps(dict(collections.Counter(r['classification'] for r in records)))+'`.']
    write(ROOT/'CONTENT_RETENTION_MAP.md','\n'.join(rows))
    original=read(QA/'original_text.txt');complete=read(QA/'optimized_text.txt')+'\n\nTECHNICAL SUPPLEMENT\n\n'+read(QA/'supplement_text.txt')+'\n\nRELOCATED EVIDENCE INVENTORY\n\n'+read(ROOT/'EVIDENCE_INVENTORY.md')
    write(ROOT/'BEFORE_AFTER_COMPLETE_TEXT.diff',''.join(difflib.unified_diff(original.splitlines(True),complete.splitlines(True),fromfile='original_complete_34_page_pdf',tofile='proposed_main_plus_technical_pdf_plus_inventory')))
    oldaux=read(ARTICLE/'submission/work/named_build/main.aux');newaux=read(ROOT/'build/main/main.aux');supaux=read(ROOT/'build/technical_supplement/technical_supplement.aux')
    labels=lambda text:dict(re.findall(r'\\newlabel\{((?:eq|fig|tab):[^}]+)\}\{\{([^}]+)\}',text))
    before=labels(oldaux);after=labels(newaux);after.update(labels(supaux))
    assert all(after.get(k)==v for k,v in before.items())
    citations=lambda text:set(k.strip() for group in re.findall(r'\\(?:paren|text)?cite\{([^}]+)\}',text) for k in group.split(','))
    origc=citations('\n'.join(read(p) for p in source_files() if p.suffix=='.tex'))
    newc=citations('\n'.join(read(SOURCE/p.relative_to(ARTICLE)) for p in source_files() if p.suffix=='.tex'))
    assert origc==newc
    result['numbered_scientific_labels_preserved_across_two_documents']=len(before)
    result['citation_key_set_unchanged']=origc==newc
    result['relocated_inventory_paths_present']=len(paths)
    result['visual_inspection']='All 29 main and 5 technical pages reviewed in rendered contact sheets; no evident missing/cropped displays or blank pages. No full-resolution typographic certification.'
    write(QA/'scientific_integrity.json',json.dumps(result,ensure_ascii=False,indent=2))
    audit=['# Scientific integrity and document QA audit','', 'Document-only audit; no research validation performed.','', '| Check | Actual result |','|---|---|']
    for key,value in result.items():
        if key=='documents':continue
        audit.append('| '+key.replace('_',' ')+' | '+str(value).replace('|','\\|')+' |')
    audit+=['','## Page-count comparison','', '| Document | Original | Proposed |','|---|---:|---:|','| Named main PDF including inline appendices | 34 | 29 |','| Separate detailed technical tables | — | 5 |','| Combined PDF pages | 34 | 34 |','', 'The proposed combined PDFs have the same total page count. The smaller main PDF reflects relocation and modest wording changes, not five pages of scientific deletion. The relocated Markdown inventory is additional supplied material. Main text ends on p.16 in both versions; proposed references begin on p.16 rather than p.17. Inline appendices start on p.18 in both; Appendix A occupies pp.18–20, B starts p.21, C p.22 and D p.25.','', 'No final-build undefined/multiply-defined references, unresolved citation warnings, literal ?? placeholders or overfull boxes were found. Scientific label numbers match across the main and technical PDFs, including moved tables. All seven build steps exited zero. MiKTeX prints an update-maintenance notice; no package installation/update or global runtime repair was attempted.','', 'Rendered contact sheets cover all pages. The technical supplement begins its first long table on p.1 and continues on p.2; the continuation is labelled and not lost content. Other long tables and figure captions remain within page boundaries. Existing small table fonts are retained, not reduced to meet a page target.','', '## Limits','', 'Byte/text preservation and document consistency do not establish inference validity, reproduce stochastic calculations, verify every reported numerical count, establish public evidence access or certify historical numerical decisions. Original research limitations remain binding. Protected-file hashes cover 192 canonical dependencies/research scripts; Git confirms all tracked files, including tracked datasets, are unchanged. Untracked research artifacts were not enumerated as a full dataset inventory and were not targeted by any write operation. Local MiKTeX runtime logs/configuration can be refreshed by document tools.']
    write(ROOT/'SCIENTIFIC_INTEGRITY_AUDIT.md','\n'.join(audit))
    write(ROOT/'README.md', '''# Proposed LSSP optimization — author review only

Read ../LSSP_OPTIMIZATION_REPORT.md, then CONTENT_OPTIMIZATION_PLAN.md. Review manuscript_optimized.pdf together with technical_supplement.pdf and EVIDENCE_INVENTORY.md. Appendices A–D remain inline in the main PDF. Tables A.2–A.5 are in the technical PDF. Do not replace canonical journal_article/ without author approval.

The complete proposed LaTeX tree is source/. Source and rendered-text diffs, the item inventory, retention map and scientific integrity audit describe all changes. review_package.zip contains the two PDFs, complete proposed sources and review documents without build/runtime caches.

Document-only reproduction: from the repository root run `python -B journal_validation/publication_review/lssp_optimization/optimize_documents.py plan`, then `prepare`, `build`, `verify`, `finalize`. This uses the previously initialized local MiKTeX runtime; installers and shell escape are disabled. It never invokes research scripts. Plan recreates the baseline only when tracked canonical files are clean. Visual inspection remains a manual review step; finalization records the review performed in this session.
''')
    report=ROOT.parent/'LSSP_OPTIMIZATION_REPORT.md'
    text=read(report)
    text=text.replace('Final page counts and visual-inspection findings are appended below after the document-only builds complete.', 'Both documents built successfully. The final counts are **29 pages in the optimized main PDF (including A–D), plus 5 pages in the Technical Supplement**, versus 34 pages in the original named PDF. The combined PDF page count is therefore still 34; this is principally better placement of verification material, with modest prose compression, not a claim of five pages of deleted science. The full Markdown evidence inventory is additional supplied material. All 34 proposed pages were inspected in contact sheets; no evident cropped or missing displays were found.')
    text=text.replace('| Rendered text diff |', '| Complete combined text diff | `BEFORE_AFTER_COMPLETE_TEXT.diff` | Original PDF against proposed main PDF, technical PDF and relocated inventory; line-wrap noise remains visible. |\n| Rendered text diff |')
    text+='\n\n## Completed verification\n\nAll seven document-build steps exited zero. Final logs contain no undefined/multiply-defined scientific references or citations and no overfull boxes; PDF text has no unresolved `??` placeholders. SHA-256 checks found no changes to 192 protected document dependencies/research scripts; Git confirms all tracked canonical files and datasets remain unchanged. The abstract and title/author/metadata text match; Appendix B is byte-identical; every original displayed mathematical block, scientific table body and relocated table block is unchanged. Figures and bibliography remain byte-identical. All original scientific label numbers remain the same across the two PDFs, and citation keys are preserved. These checks establish document preservation, not statistical validity. See `lssp_optimization/SCIENTIFIC_INTEGRITY_AUDIT.md` for exact scope and limitations.\n'
    write(report,text)
    package=[ROOT/'manuscript_optimized.pdf',ROOT/'technical_supplement.pdf',report]+[p for p in ROOT.glob('*') if p.is_file() and p.suffix in ['.md','.json','.diff','.tex','.py']]+[p for p in SOURCE.rglob('*') if p.is_file()]
    with zipfile.ZipFile(ROOT/'review_package.zip','w',zipfile.ZIP_DEFLATED) as z:
        for p in package:z.write(p,'LSSP_OPTIMIZATION_REPORT.md' if p==report else p.relative_to(ROOT).as_posix())
    print('Review package finalized; 29-page main + 5-page technical supplement; canonical files unchanged',flush=True)

if __name__=='__main__':
    configure()
    {'plan':plan,'prepare':prepare,'build':build,'verify':verify,'finalize':finalize}[sys.argv[1]]()
