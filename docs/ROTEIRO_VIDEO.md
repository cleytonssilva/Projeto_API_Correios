# Roteiro do vídeo - QA Unidade 3

Duração sugerida: 3 a 4 minutos.

## 1. Contexto - 20 a 30 s

"Nesta atividade de Qualidade de Software, automatizei a validação de CEP, cidade e estado usando o ViaCEP. Contextualizei o exercício com o Projeto API Correios, no qual a qualidade do endereço é importante antes da pré-postagem."

## 2. JSON de entrada - 20 s

Mostrar `dados/ceps.json` e destacar que cada objeto contém somente `cep`, `cidade` e `estado`.

## 3. Código - 60 s

Mostrar `src/viacep_validator.py` e explicar:
- validação de 8 dígitos;
- chamada HTTP ao ViaCEP;
- tratamento de CEP não encontrado;
- comparação de `localidade` com `cidade`;
- comparação de `uf` com `estado`.

Depois mostrar `tests/test_viacep.py` e o uso de `pytest.mark.parametrize`.

## 4. Execução - 40 s

Executar:

```powershell
.\run_qa.ps1
```

ou:

```powershell
python -m pytest -v
```

Mostrar os casos com `PASSED`.

## 5. Gherkin - 30 s

Mostrar `features/login_portal_aluno.feature` e explicar rapidamente:
- Dado: pré-condição;
- Quando: ação;
- Então: resultado esperado.

## 6. Fechamento - 20 s

"A automação permite detectar divergências de endereço de forma repetível e objetiva. O mesmo princípio pode atuar como gate de qualidade antes de etapas posteriores de um processo de expedição."
