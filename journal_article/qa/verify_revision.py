from pathlib import Path
import hashlib, json, re

article = Path(__file__).resolve().parents[1]
root = article.parent
snapshot = json.loads((article / 'qa/revision_preservation_sha256.json').read_text())
changed = [name for name, digest in snapshot.items()
           if not (root / name).is_file() or hashlib.sha256((root / name).read_bytes()).hexdigest() != digest]
text = (article / 'qa/article_text.txt').read_text(encoding='utf-8')
pages = text.split('\f')
if not pages[-1].strip():
    pages.pop()
log = (article / 'main.log').read_text(errors='replace')
expected = ['UMIDJON UMIRZAKOVICH KOSTAEV', 'OLIMJON UMIDJON UGLI UMURZOKOV',
            '0009-0000-0205-5142', '0009-0008-0090-7100',
            'umidjonkostaev2025@gmail.com', 'olimumurzokov022@gmail.com',
            'Tashkent State University of Economics, Tashkent, Uzbekistan']
checks = {
    'page_count': len(pages),
    'all_author_details_present': all(x in pages[0] for x in expected),
    'author_order_correct': pages[0].index(expected[0]) < pages[0].index(expected[1]),
    'affiliation_printed_once': text.count(expected[-1]) == 1,
    'no_empty_pages': all(re.sub(r'\s|\d', '', p) for p in pages),
    'deleted_headings_absent': all(x not in text for x in ['Numerics, failures, and reproduction workflow', 'Complete Frozen Numerical Results']),
    'deleted_appendix_reference_absent': 'app:full-results' not in '\n'.join(p.read_text(encoding='utf-8') for p in article.rglob('*.tex')),
    'clean_latex_log': not re.search(r'undefined|multiply defined|Overfull|Rerun to get|Label\(s\) may have changed', log, re.I),
    'preserved_file_count': len(snapshot),
    'changed_preserved_files': changed,
}
(article / 'qa/revision_validation.json').write_text(json.dumps(checks, indent=2))
print(json.dumps(checks, indent=2))
assert len(pages) == 28 and not changed
assert all(checks[k] for k in ['all_author_details_present', 'author_order_correct', 'affiliation_printed_once', 'no_empty_pages', 'deleted_headings_absent', 'deleted_appendix_reference_absent', 'clean_latex_log'])
