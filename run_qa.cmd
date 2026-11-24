@echo off
setlocal

if not exist ".venv\Scripts\python.exe" (
  echo [0/4] Criando ambiente virtual...
  python -m venv .venv
  if errorlevel 1 exit /b 1
)

if not exist reports mkdir reports

echo [1/4] Instalando dependencias no ambiente virtual...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 exit /b 1

echo [2/4] Executando validacoes locais...
".venv\Scripts\python.exe" -m pytest -v -m "not integration"
if errorlevel 1 exit /b 1

echo [3/4] Executando integracao real com o ViaCEP...
".venv\Scripts\python.exe" -m pytest -v -m integration --junitxml=reports\junit.xml
if errorlevel 1 exit /b 1

echo [4/4] QA_UNIDADE3=PASS
