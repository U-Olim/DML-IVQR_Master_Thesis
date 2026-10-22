from pathlib import Path
import hashlib, json

root = Path(__file__).resolve().parents[2]
article = root / 'journal_article'
snapshot = {}
for folder in ('thesis', 'simulation', 'Empirical_work', 'example', 'thesis_extension'):
    for p in (root / folder).rglob('*'):
        if p.is_file():
            snapshot[p.relative_to(root).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
(article / 'qa/revision_preservation_sha256.json').write_text(json.dumps(snapshot, indent=2))

p = article / 'main.tex'
s = p.read_text(encoding='utf-8')
s = s.replace(r'\author{}', r'''% Shared affiliation and individual contact details; no corresponding author.
\author{\begin{minipage}{\textwidth}\centering
\normalsize UMIDJON UMIRZAKOVICH KOSTAEV\textsuperscript{a}\\
\small ORCID: \href{https://orcid.org/0009-0000-0205-5142}{0009-0000-0205-5142}\\
Email: \href{mailto:umidjonkostaev2025@gmail.com}{umidjonkostaev2025@gmail.com}\\[0.7em]
\normalsize OLIMJON UMIDJON UGLI UMURZOKOV\textsuperscript{a}\\
\small ORCID: \href{https://orcid.org/0009-0008-0090-7100}{0009-0008-0090-7100}\\
Email: \href{mailto:olimumurzokov022@gmail.com}{olimumurzokov022@gmail.com}\\[0.7em]
\small\textsuperscript{a}Tashkent State University of Economics, Tashkent, Uzbekistan
\end{minipage}}''')
s = s.replace('implementation and reproduction details.', 'implementation notes.')
s = s.replace(' Appendix E provides the complete frozen numerical results.', '')
s = s.replace('\\input{supplementary/E_full_results}\n', '')
s = s.replace('pdftitle={High-Dimensional IVQR under Weak Instruments}', 'pdftitle={High-Dimensional IVQR under Weak Instruments},pdfauthor={UMIDJON UMIRZAKOVICH KOSTAEV; OLIMJON UMIDJON UGLI UMURZOKOV}')
p.write_text(s, encoding='utf-8')
p = article / 'supplementary/D_implementation.tex'
s = p.read_text(encoding='utf-8')
s = s.split(r'\subsection{Numerics, failures, and reproduction workflow}')[0].rstrip() + '\n'
p.write_text(s, encoding='utf-8')
(article / 'supplementary/E_full_results.tex').unlink()
p = article / 'sections/04_results.tex'
s = p.read_text(encoding='utf-8').replace(', reported in Supplementary Appendix~\\ref{app:full-results}', '')
p.write_text(s, encoding='utf-8')
