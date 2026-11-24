# Projeto API Correios - QA Unidade 3

Entrega prática da disciplina **Qualidade de Software (QA) - Unidade 3**, contextualizada com o projeto `Projeto_API_Correios`.

## Objetivo

Automatizar a validação de que um CEP consultado no ViaCEP retorna **cidade** e **estado/UF** coerentes com um JSON de entrada contendo exatamente os três campos exigidos: `cep`, `cidade` e `estado`.

O exercício foi conectado a um problema real do fluxo de expedição: **dados de endereço inconsistentes não devem avançar silenciosamente para uma etapa de pré-postagem**.

## Escopo entregue

- `dados/ceps.json`: 3 casos de entrada;
- `src/viacep_validator.py`: consulta e regras de validação;
- `tests/test_viacep.py`: teste de integração real com ViaCEP;
- `tests/test_dados_entrada.py`: testes determinísticos da estrutura e das regras;
- `features/login_portal_aluno.feature`: cenário Gherkin solicitado para login;
- `.github/workflows/qa-unidade3.yml`: execução automatizada no GitHub Actions;
- `docs/RELATORIO_ENTREGA_QA_UNIDADE3.md`: relatório acadêmico;
- `docs/ROTEIRO_VIDEO.md`: roteiro objetivo para o vídeo de entrega.

## Pré-requisitos

- Python 3.11 ou superior;
- acesso à internet para o teste de integração com `https://viacep.com.br`.

## Execução no Windows

### Opção recomendada — sem alterar a ExecutionPolicy do PowerShell

Não é necessário ativar a `.venv`. O arquivo `run_qa.cmd` cria o ambiente virtual se necessário e usa diretamente o Python isolado:

```powershell
git pull
.\run_qa.cmd
```

Execução equivalente, passo a passo:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v -m "not integration"
.\.venv\Scripts\python.exe -m pytest -v -m integration --junitxml=reports\junit.xml
```

### PowerShell script

Se a política local permitir scripts, também pode ser usado:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\run_qa.ps1
```

O `Bypass` acima vale somente para esse processo do PowerShell e não altera permanentemente a política do computador.

## Execução manual

Validações locais:

```bash
python -m pytest -v -m "not integration"
```

Integração real com ViaCEP:

```bash
python -m pytest -v -m integration
```

Execução completa:

```bash
python -m pytest -v
```

## Critério de aprovação

Para cada registro do JSON, a automação exige:

1. CEP no formato de 8 dígitos;
2. HTTP sem erro na chamada ao ViaCEP;
3. CEP encontrado;
4. `localidade` igual à `cidade` esperada;
5. `uf` igual ao `estado` esperado.

Qualquer divergência causa **FAIL** com mensagem explícita.

## Cenário Web em Gherkin

O arquivo `features/login_portal_aluno.feature` descreve o cenário de autenticação válida no Portal do Aluno usando `Dado / Quando / Então`, conforme solicitado na atividade.

## Relação com o Projeto API Correios

O uso do ViaCEP neste exercício representa um **quality gate de dados**: antes de um endereço alimentar processos posteriores, a automação verifica se CEP, cidade e UF são coerentes. A atividade acadêmica preserva seu escopo original, mas demonstra uma aplicação realista de QA em um fluxo de expedição.

## Evidência

O workflow `QA Unidade 3 - ViaCEP` executa os testes a cada `push`, `pull_request` ou acionamento manual e publica o JUnit XML como artefato.
