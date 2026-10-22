$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
try {
    foreach ($step in @('latex', 'biber', 'latex', 'latex')) {
        if ($step -eq 'biber') { & biber main }
        else { & pdflatex -interaction=nonstopmode -halt-on-error main.tex }
        if ($LASTEXITCODE -ne 0) { throw "Article build failed at $step." }
    }
} finally { Pop-Location }
