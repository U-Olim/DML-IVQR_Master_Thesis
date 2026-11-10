"""Document-only Batch 4 build; never invokes research scripts or package installers."""
from pathlib import Path
import configparser, json, os, subprocess, time
ARTICLE = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
RUNTIME = OUT / 'runtime'
INSTALL = Path(os.environ['LOCALAPPDATA']) / 'Programs' / 'MiKTeX'
ORIGINAL_CONFIG = Path(os.environ['APPDATA']) / 'MiKTeX' / 'miktex' / 'config' / 'miktex.ini'
for folder in [OUT, RUNTIME / 'config' / 'miktex' / 'config', RUNTIME / 'data']:
    folder.mkdir(parents=True, exist_ok=True)
original = configparser.ConfigParser()
original.read(ORIGINAL_CONFIG)
config = configparser.ConfigParser()
config.optionxform = str
config['Core'] = {key: original.get('Core', key) for key in ['LastUserMaintenance', 'NoRegistry', 'SharedSetup'] if original.has_option('Core', key)}
config['MPM'] = {'AutoInstall': '0'}
with (RUNTIME / 'config' / 'miktex' / 'config' / 'miktex.ini').open('w') as handle:
    config.write(handle)
startup = RUNTIME / 'miktexstartup.ini'
startup.write_text('[Paths]\nUserConfig=' + str(RUNTIME / 'config') + '\nUserData=' + str(RUNTIME / 'data') + '\nUserInstall=' + str(INSTALL) + '\n[Setup]\nVersion=25.12\n')
env = os.environ.copy()
env.update({'MIKTEX_USERCONFIG': str(RUNTIME / 'config'), 'MIKTEX_USERDATA': str(RUNTIME / 'data'), 'MIKTEX_USERINSTALL': str(INSTALL), 'MIKTEX_USERSTARTUPFILE': str(startup), 'LANG': 'C', 'LC_ALL': 'C', 'PAR_GLOBAL_TEMP': str(RUNTIME), 'TEXINPUTS': str(OUT) + ';' + str(ARTICLE) + ';', 'BIBINPUTS': str(ARTICLE) + ';'})
latex = [str(INSTALL / 'miktex/bin/x64/pdflatex.exe'), '--disable-installer', '-no-shell-escape', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory=' + str(OUT), 'main.tex']
biber = [str(INSTALL / 'executables/windows-x64/biber/biber.exe'), '--input-directory', str(OUT), '--output-directory', str(OUT), 'main']
records = []
for name, command in [('latex1', latex), ('biber', biber), ('latex2', latex), ('latex3', latex)]:
    print('Starting', name, flush=True)
    started = time.monotonic()
    with (OUT / (name + '.txt')).open('w', encoding='utf-8') as log:
        process = subprocess.Popen(command, cwd=OUT, env=env, stdout=log, stderr=subprocess.STDOUT)
        try:
            code = process.wait(timeout=240)
        except subprocess.TimeoutExpired:
            process.kill()
            code = 'TIMEOUT'
    records.append({'step': name, 'command': command, 'exit_code': code, 'seconds': round(time.monotonic() - started, 2)})
    (OUT / 'build_results.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
    print(name, 'exit:', code, flush=True)
    if code != 0:
        raise SystemExit(1)
print('Document-only build sequence finished.', flush=True)
