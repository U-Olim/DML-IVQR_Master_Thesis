"""Read-only document/ZIP integrity inspection and PDF rendering; not statistical validation."""
from pathlib import Path
import csv, hashlib, io, json, os, re, subprocess, sys, zipfile
from PIL import Image, ImageDraw
ROOT = Path(__file__).resolve().parent
ARTICLE = ROOT.parent
RUNTIME = ARTICLE / 'qa/batch4/runtime'
env = os.environ.copy()
env.update({'MIKTEX_USERCONFIG': str(RUNTIME / 'config'), 'MIKTEX_USERDATA': str(RUNTIME / 'data'),
            'MIKTEX_USERINSTALL': str(Path(os.environ['LOCALAPPDATA']) / 'Programs/MiKTeX'),
            'MIKTEX_USERSTARTUPFILE': str(RUNTIME / 'miktexstartup.ini')})
terms = ['umurzokov', 'kostaev', 'olimumurzokov022', 'umidjonkostaev2025', 'orcid.org/0009',
         '0009-0008-0090-7100', '0009-0000-0205-5142', 'Tashkent State University',
         'github.com', 'U-Olim', 'DML-IVQR_Master_Thesis', '15b8b4dc', 'ac9a9cca', '0f4188ca']
for variant in (sys.argv[1:] or ['named', 'review', 'supplement']):
    pdf = ROOT / ('review/supplementary_tables_review.pdf' if variant == 'supplement' else variant + '/manuscript_' + variant + '.pdf')
    out = ROOT / 'qa' / variant
    out.mkdir(parents=True, exist_ok=True)
    jobs = [('info', ['pdfinfo', '-enc', 'UTF-8', str(pdf)]), ('xmp', ['pdfinfo', '-meta', str(pdf)]),
            ('urls', ['pdfinfo', '-url', str(pdf)]), ('attachments', ['pdfdetach', '-list', str(pdf)]),
            ('text_console', ['pdftotext', '-enc', 'UTF-8', '-layout', str(pdf), str(out / 'text.txt')]),
            ('render_console', ['pdftoppm', '-r', '75', '-gray', '-png', str(pdf), str(out / 'page')])]
    for label, cmd in jobs:
        with (out / (label + '.txt')).open('w', encoding='utf-8') as h:
            result = subprocess.run(cmd, env=env, stdout=h, stderr=subprocess.STDOUT, timeout=180)
        assert result.returncode == 0, (variant, label, result.returncode)
        print(variant, label, 'done', flush=True)
    text = (out / 'text.txt').read_text(encoding='utf-8')
    pages = [p for p in text.split('\f') if p.strip()]
    scans = ['text', 'info', 'xmp', 'urls', 'attachments']
    leaks = {label: [t for t in terms if t.lower() in (out / (label + '.txt')).read_text(encoding='utf-8', errors='replace').lower()] for label in scans}
    # Utilities can log local installation paths on initialization. Metadata/URI output is still reviewed explicitly.
    if variant != 'named':
        assert not any(leaks.values()), leaks
    pngs = sorted(out.glob('page-*.png'))
    for start in range(0, len(pngs), 12):
        canvas = Image.new('RGB', (1000, 1110), '#d0d0d0'); draw = ImageDraw.Draw(canvas)
        for j, path in enumerate(pngs[start:start+12]):
            im = Image.open(path).convert('RGB'); im.thumbnail((236, 337))
            x, y = (j % 4) * 250 + 7, (j // 4) * 370 + 23
            canvas.paste(im, (x, y)); draw.text((x, y-17), path.stem, fill='black')
        canvas.save(out / ('contact-%s.png' % (start // 12 + 1)))
    result = {'variant': variant, 'pdf': str(pdf.relative_to(ROOT)), 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
              'bytes': pdf.stat().st_size, 'pages': len(pages), 'rendered_pages': len(pngs),
              'question_pairs': text.count('??'), 'blank_pages': [i+1 for i,p in enumerate(text.split('\f')[:-1]) if not p.strip()],
              'identity_scan': leaks, 'destination_audit': 'Direct utility enumeration stalled; compiled bookmark sources inspected separately. No exhaustive object/JavaScript audit claimed.'}
    (out / 'audit.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result), flush=True)
