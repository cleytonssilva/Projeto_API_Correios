$ErrorActionPreference = "Stop"

Write-Host "[1/3] Instalando dependencias..."
python -m pip install -r requirements.txt

Write-Host "[2/3] Executando validacoes locais..."
python -m pytest -v -m "not integration"

Write-Host "[3/3] Executando integracao real com o ViaCEP..."
python -m pytest -v -m integration --junitxml=reports/junit.xml

Write-Host "QA_UNIDADE3=PASS"
