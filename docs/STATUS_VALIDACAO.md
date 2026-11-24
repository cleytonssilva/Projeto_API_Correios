# Evidência de validação

## Estado consolidado

- Repositório publicado: **PASS**
- Branch: `main`
- Ambiente de execução real: **Windows / Python 3.12.10 / .venv**
- Validações locais determinísticas: **PASS — 5/5**
- Integração real ViaCEP: **PASS — 3/3**
- Resultado consolidado da suíte: **PASS — 8/8**
- Status final: `QA_UNIDADE3=PASS`
- GitHub Actions: **BLOCKED_BY_ACTIONS_STARTUP** — o workflow é reconhecido e cria runs, porém o job falha antes da execução de qualquer step. Esse bloqueio permanece classificado como infraestrutura de CI e não invalida a execução real local.

## Execução final validada

### Validações locais

- `test_json_deve_conter_tres_casos_com_campos_exigidos` — PASS
- `test_validacao_deve_detectar_cidade_divergente` — PASS
- `test_validacao_deve_detectar_uf_divergente` — PASS
- `test_consulta_deve_tratar_erro_string_do_viacep` — PASS
- `test_json_bruto_e_valido` — PASS

### Integração real com o ViaCEP

- `01001000` → São Paulo / SP — **PASS**
- `40010000` → Salvador / BA — **PASS**
- `30130110` → Belo Horizonte / MG — **PASS**

Tempo observado na execução final:

- camada local: aproximadamente 0,28 s;
- integração real: aproximadamente 2,06 s.

## Histórico de melhoria de QA

Uma execução anterior identificou que o caso `40020000` retornava `{"erro": "true"}` no ViaCEP.

A partir dessa falha real:

1. a massa de teste de Salvador foi corrigida para `40010000`;
2. o tratamento de `erro` passou a aceitar booleano `true` e string `"true"`;
3. foi criado um teste de regressão específico para esse comportamento;
4. o reteste completo foi executado;
5. o resultado final passou para **8/8 PASS**.

Esse ciclo demonstra detecção de defeito, diagnóstico, correção, regressão e reteste — comportamento esperado em uma prática de QA.

## Evidências do projeto

- `docs/evidencias/junit-offline.xml`: evidência da etapa local anterior.
- `reports/junit.xml`: gerado na execução real local da integração.
- `docs/evidencias/EXECUCAO_WINDOWS_PASS.md`: resumo versionado da execução final.
- Workflow: `.github/workflows/qa-unidade3.yml`.

## Veredito

`RETEST_REQUIRED=false`

`QA_UNIDADE3=PASS`

A atividade está tecnicamente validada para entrega quanto ao escopo solicitado de API e ao cenário Web em Gherkin. O GitHub Actions permanece como melhoria de infraestrutura e não como pendência funcional da atividade.
