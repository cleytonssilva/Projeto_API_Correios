# Projeto API Correios - QA Unidade 3

Entrega prática da disciplina **Qualidade de Software (QA) - Unidade 3**, contextualizada com o projeto `Projeto_API_Correios`.

## Status da entrega

**QA_UNIDADE3=PASS — 8/8 testes validados em execução real no Windows**

- 5 testes locais/determinísticos: **PASS**
- 3 testes reais contra o ViaCEP: **PASS**
- cenário Web em Gherkin: **ENTREGUE**
- execução isolada em `.venv`: **VALIDADA**
- GitHub Actions: workflow publicado, com bloqueio de startup do runner separado do resultado funcional

## Objetivo

Automatizar a validação de que um CEP consultado no ViaCEP retorna **cidade** e **estado/UF** coerentes com um JSON de entrada contendo exatamente os três campos exigidos: `cep`, `cidade` e `estado`.

O exercício foi conectado a um problema real do fluxo de expedição: **dados de endereço inconsistentes não devem avançar silenciosamente para uma etapa de pré-postagem**.

## Escopo entregue

- `dados/ceps.json`: 3 casos de entrada;
- `src/viacep_validator.py`: consulta e regras de validação;
- `tests/test_viacep.py`: teste de integração real com ViaCEP;
- `tests/test_dados_entrada.py`: testes determinísticos da estrutura e das regras;
- `features/login_portal_aluno.feature`: cenário Gherkin solicitado para login;
- `.github/workflows/qa-unidade3.yml`: automação de CI;
- `docs/RELATORIO_ENTREGA_QA_UNIDADE3.md`: relatório acadêmico;
- `docs/ROTEIRO_VIDEO.md`: roteiro objetivo para o vídeo de entrega;
- `docs/STATUS_VALIDACAO.md`: veredito técnico consolidado;
- `docs/evidencias/EXECUCAO_WINDOWS_PASS.md`: evidência final resumida.

## Pré-requisitos

- Python 3.11 ou superior;
- acesso à internet para o teste de integração com `https://viacep.com.br`.

## Execução no Windows

### Opção recomendada — sem alterar a ExecutionPolicy

Não é necessário ativar a `.venv`:

```powershell
git pull
.\run_qa.cmd
```

O script:

1. usa/cria a `.venv`;
2. instala as dependências dentro do ambiente isolado;
3. executa os testes locais;
4. executa os testes reais contra o ViaCEP;
5. gera `reports/junit.xml`;
6. encerra com `QA_UNIDADE3=PASS` quando tudo passa.

## Execução manual

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v -m "not integration"
.\.venv\Scripts\python.exe -m pytest -v -m integration --junitxml=reports\junit.xml
```

## Casos validados

| CEP | Cidade | UF | Resultado |
|---|---|---|---|
| 01001000 | São Paulo | SP | PASS |
| 40010000 | Salvador | BA | PASS |
| 30130110 | Belo Horizonte | MG | PASS |

## Critério de aprovação

Para cada registro do JSON, a automação exige:

1. CEP no formato de 8 dígitos;
2. resposta HTTP válida;
3. CEP localizado;
4. `localidade` igual à `cidade` esperada;
5. `uf` igual ao `estado` esperado.

Qualquer divergência causa **FAIL** com mensagem explícita.

## Cenário Web em Gherkin

O arquivo `features/login_portal_aluno.feature` descreve o login válido no Portal do Aluno utilizando `Dado / Quando / Então`, conforme solicitado na atividade.

## Relação com o Projeto API Correios

O uso do ViaCEP representa um **quality gate de dados**: antes de um endereço alimentar etapas posteriores, a automação verifica se CEP, cidade e UF são coerentes.

## Evidência final

A execução real em Windows resultou em:

```text
5 passed, 3 deselected
3 passed, 5 deselected
QA_UNIDADE3=PASS
```

O histórico de validação, incluindo a detecção e correção de uma massa de teste inválida, está documentado em `docs/STATUS_VALIDACAO.md`.
