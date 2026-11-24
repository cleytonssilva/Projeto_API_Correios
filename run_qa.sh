#!/usr/bin/env bash
set -euo pipefail
python -m pip install -r requirements.txt
python -m pytest -v -m "not integration"
python -m pytest -v -m integration --junitxml=reports/junit.xml
echo "QA_UNIDADE3=PASS"
