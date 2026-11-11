"""Compile and inspect a byte-identical snapshot of corrected canonical LaTeX; document-only."""
from pathlib import Path
import hashlib, json, os, re, shutil, subprocess, sys, time

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
ARTICLE=REPO/'journal_article'
SOURCE=ROOT/'source'
BUILD=ROOT/'build'
QA=ROOT/'qa'
INSTALL=Path(os.environ['LOCALAPPDATA'])/'Programs/MiKTeX'
RUNTIME=ARTICLE/'qa/batch4/runtime'

def read(p):return p.read_text(encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8',newline='\n')
def env():
    e=os.environ.copy();e.update({'MIKTEX_USERCONFIG':str(RUNTIME/'config'),'MIKTEX_USERDATA':str(RUNTIME/'data'),'MIKTEX_USERINSTALL':str(INSTALL),'MIKTEX_USERSTARTUPFILE':str(RUNTIME/'miktexstartup.ini'),'LANG':'C','LC_ALL':'C','PAR_GLOBAL_TEMP':str(RUNTIME),'TEXINPUTS':str(SOURCE)+';','BIBINPUTS':str(SOURCE)+';'})
    return e
def gitdiff():return subprocess.check_output(['git','diff','HEAD','--binary','--'],cwd=REPO)

def compile_document():
    for p in [SOURCE,BUILD,QA]:p.mkdir(parents=True,exist_ok=True)
    files=[ARTICLE/x for x in ['main.tex','preamble.tex','references.bib']]
    files += [p for folder in ['sections','supplementary','tables','figures'] for p in sorted((ARTICLE/folder).rglob('*')) if p.is_file() and p.suffix.lower() in ['.tex','.bib','.pdf','.png','.jpg','.jpeg']]
    manifest={p.relative_to(ARTICLE).as_posix():sha(p) for p in files}
    historical={p.relative_to(REPO).as_posix():sha(p) for p in ARTICLE.rglob('*.pdf')}
    write(QA/'source_manifest.json',json.dumps(manifest,indent=2))
    write(QA/'historical_pdf_hashes.json',json.dumps(historical,indent=2))
    (QA/'prebuild_tracked.diff').write_bytes(gitdiff())
    for p in files:
        target=SOURCE/p.relative_to(ARTICLE);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
    old=subprocess.check_output(['git','show','HEAD:journal_article/main.tex'],cwd=REPO)
    abstract=lambda b:b.split(b'\\begin{abstract}')[1].split(b'\\end{abstract}')[0].replace(b'\r\n',b'\n')
    assert abstract(old)==abstract((SOURCE/'main.tex').read_bytes())
    latex=[str(INSTALL/'miktex/bin/x64/pdflatex.exe'),'--disable-installer','-no-shell-escape','-interaction=nonstopmode','-halt-on-error','-file-line-error','-recorder','-output-directory='+str(BUILD),'main.tex']
    biber=[str(INSTALL/'executables/windows-x64/biber/biber.exe'),'--input-directory',str(BUILD),'--output-directory',str(BUILD),'main']
    records=[]
    for step,command in [('latex1',latex),('biber',biber),('latex2',latex),('latex3',latex)]:
        print('Starting',step,flush=True);start=time.monotonic()
        with (QA/(step+'.txt')).open('w',encoding='utf-8') as h:r=subprocess.run(command,cwd=SOURCE,env=env(),stdout=h,stderr=subprocess.STDOUT,timeout=240)
        records.append(dict(step=step,exit_code=r.returncode,seconds=round(time.monotonic()-start,2),command=command))
        write(QA/'build_results.json',json.dumps(records,indent=2));assert r.returncode==0,step
        print(step,'passed',flush=True)
    shutil.copyfile(BUILD/'main.pdf',ROOT/'manuscript_canonical_corrected.pdf')

def audit():
    result={}
    manifest=json.loads(read(QA/'source_manifest.json'))
    assert all(sha(ARTICLE/p)==h and sha(SOURCE/p)==h for p,h in manifest.items())
    result['canonical_dependencies_and_snapshot_byte_identical']=len(manifest)
    mathblocks=lambda s:re.findall(r'\\begin\{equation\*?\}.*?\\end\{equation\*?\}|\\\[.*?\\\]',s,re.S)
    tables=lambda s:re.findall(r'\\begin\{booktabs\}.*?\\end\{booktabs\}',s,re.S)
    for rel in manifest:
        if not rel.endswith('.tex'):continue
        old=subprocess.check_output(['git','show','HEAD:journal_article/'+rel],cwd=REPO).decode()
        new=read(SOURCE/rel)
        assert mathblocks(old)==mathblocks(new),rel
        if rel.startswith('tables/'):assert tables(old)==tables(new),rel
    result['displayed_math_and_scientific_table_bodies_match_historical_source']=True
    assert gitdiff()==(QA/'prebuild_tracked.diff').read_bytes()
    result['tracked_working_tree_diff_unchanged']=True
    history=json.loads(read(QA/'historical_pdf_hashes.json'))
    assert all(sha(REPO/p)==h for p,h in history.items())
    result['existing_historical_pdfs_preserved']=len(history)
    main=read(SOURCE/'main.tex')
    assert '\\input{tables/generated/appendix_grid_diagnostic}' in read(SOURCE/'supplementary/A_numerical_domain.tex')
    assert '\\input{supplementary/D_evidence_map}' in read(SOURCE/'supplementary/D_implementation.tex')
    includes=re.findall(r'\\input\{([^}]+)\}',main)
    result['canonical_main_inclusion_order']=includes
    expected=['sections/01_introduction','sections/02_framework','sections/03_design','sections/04_results','sections/05_discussion','sections/06_conclusion','supplementary/A_numerical_domain','supplementary/B_kappa_derivation','supplementary/C_coverage_audit','supplementary/D_implementation']
    assert [i for i in includes if i in expected]==expected
    result['all_sections_appendices_full_tables_and_inventory_inline']=True
    aux=read(BUILD/'main.aux');oldaux=read(ARTICLE/'submission/work/named_build/main.aux')
    labels=lambda s:dict(re.findall(r'\\newlabel\{((?:eq|tab|fig):[^}]+)\}\{\{([^}]+)\}',s))
    before,after=labels(oldaux),labels(aux)
    assert before==after,(set(before)-set(after),set(after)-set(before))
    result['all_scientific_labels_and_numbers_match_historical']=len(after)
    result['equation_labels']=sum(k.startswith('eq:') for k in after)
    result['table_labels']=sum(k.startswith('tab:') for k in after)
    result['figure_labels']=sum(k.startswith('fig:') for k in after)
    log=read(BUILD/'main.log');blg=read(BUILD/'main.blg')
    bad=[s for s in (log+'\n'+blg).splitlines() if re.search(r'undefined|multiply defined|Empty bibliography|Please.*rerun|Label\(s\) may have changed|^!|>\s*ERROR\s*-|^.*(?:LaTeX|Package \S+) Error:',s,re.I)]
    result['unresolved_reference_citation_or_bibliography_warnings']=bad;assert not bad,bad
    result['overfull_boxes']=[s for s in log.splitlines() if 'Overfull' in s];assert not result['overfull_boxes']
    result['other_latex_warning_lines']=[s for s in log.splitlines() if 'Warning' in s]
    result['underfull_boxes']=[s for s in log.splitlines() if 'Underfull' in s]
    bbl=read(BUILD/'main.bbl')
    cites=set(re.findall(r'\\abx@aux@cite\{[^}]+\}\{([^}]+)\}',aux))
    entries=set(re.findall(r'\\entry\{([^}]+)\}',bbl))
    assert cites and cites<=entries
    result['cited_bibliography_keys_resolved']=sorted(cites)
    recorder=read(BUILD/'main.fls')
    # Recursively traverse only the canonical master dependencies, then require recorder evidence.
    visited=set()
    def walk(rel):
        if rel in visited:return
        visited.add(rel);s=read(SOURCE/rel)
        for target in re.findall(r'\\input\{([^}]+)\}',s):walk(target+'.tex')
    walk('main.tex')
    normalized_recorder=recorder.replace('\\','/')
    assert all(rel in normalized_recorder for rel in visited)
    graphics=set()
    for rel in visited:graphics.update(re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}',read(SOURCE/rel)))
    assert all(rel in normalized_recorder and (SOURCE/rel).is_file() for rel in graphics)
    result['recursive_tex_inputs_recorded']=sorted(visited)
    result['all_referenced_graphics_recorded']=sorted(graphics)
    assert 'lssp_optimization' not in recorder
    result['optimized_sources_used']=False
    pdf=ROOT/'manuscript_canonical_corrected.pdf'
    for name,args in [('pdfinfo',['pdfinfo.exe','-enc','UTF-8',str(pdf)]),('text',['pdftotext.exe','-enc','UTF-8','-layout',str(pdf),'-'])]:
        r=subprocess.run([str(INSTALL/'miktex/bin/x64'/args[0])]+args[1:],env=env(),capture_output=True,timeout=60);assert r.returncode==0
        try:decoded=r.stdout.decode('utf-8')
        except UnicodeDecodeError:
            assert name=='pdfinfo', 'PDF text must decode as UTF-8'
            decoded=r.stdout.decode('cp1251')
        write(QA/(name+'.txt'),decoded)
    text=read(QA/'text.txt');pages=[p for p in text.split('\f') if p.strip()]
    result['page_count']=len(pages);result['pdf_bytes']=pdf.stat().st_size;result['pdf_sha256']=sha(pdf)
    assert '??' not in text
    result['literal_unresolved_question_pairs']=0
    # Source-level numeric and math preservation is established by identical snapshot hashes;
    # formatting and label resolution are document checks, not research validation.
    oldmain=subprocess.check_output(['git','show','HEAD:journal_article/main.tex'],cwd=REPO).decode()
    abstract=lambda s:s.split('\\begin{abstract}')[1].split('\\end{abstract}')[0]
    result['abstract_verbatim_against_historical_source']=abstract(oldmain)==abstract(main)
    assert result['abstract_verbatim_against_historical_source']
    write(QA/'verification.json',json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps(result,ensure_ascii=True,indent=2),flush=True)

def render():
    from PIL import Image,ImageDraw
    r=subprocess.run([str(INSTALL/'miktex/bin/x64/pdftoppm.exe'),'-r','65','-gray','-png',str(ROOT/'manuscript_canonical_corrected.pdf'),str(QA/'page')],env=env(),capture_output=True,timeout=180);assert r.returncode==0
    files=sorted(QA.glob('page-*.png'))
    for start in range(0,len(files),12):
        canvas=Image.new('RGB',(1000,1110),'#d0d0d0');draw=ImageDraw.Draw(canvas)
        for j,p in enumerate(files[start:start+12]):
            im=Image.open(p).convert('RGB');im.thumbnail((236,337));x=j%4*250+7;y=j//4*370+23;canvas.paste(im,(x,y));draw.text((x,y-17),p.stem,fill='black')
        canvas.save(QA/f'contact-{start//12+1}.png')
    print('Rendered',len(files),'pages',flush=True)

if __name__=='__main__':{'build':compile_document,'audit':audit,'render':render}[sys.argv[1]]()
