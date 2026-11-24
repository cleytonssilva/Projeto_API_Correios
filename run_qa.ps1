$ErrorActionPreference = "Stop"

$PythonVenv = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $PythonVenv)) {
    Write-Host "[0/4] Criando ambiente virtual..."
    python -m venv .venv
}

New-Item -ItemType Directory -Force -Path (Join-Path $PSScriptRoot "reports") | Out-Null

Write-Host "[1/4] Instalando dependencias no ambiente virtual..."
& $PythonVenv -m pip install -r requirements.txt

Write-Host "[2/4] Executando validacoes locais..."
& $PythonVenv -m pytest -v -m "not integration"

Write-Host "[3/4] Executando integracao real com o ViaCEP..."
& $PythonVenv -m pytest -v -m integration --junitxml=reports/junit.xml

Write-Host "[4/4] QA_UNIDADE3=PASS"
