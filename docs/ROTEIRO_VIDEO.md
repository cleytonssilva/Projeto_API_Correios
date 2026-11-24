# Roteiro do vídeo - QA Unidade 3

Duração sugerida: **3 a 4 minutos**.

## 1. Contexto - 20 a 30 s

"Nesta atividade de Qualidade de Software, automatizei a validação de CEP, cidade e estado usando o ViaCEP. Contextualizei o exercício com o Projeto API Correios, no qual a qualidade do endereço é importante antes da pré-postagem."

## 2. JSON de entrada - 20 s

Mostrar `dados/ceps.json` e destacar os três registros:

- São Paulo/SP — `01001000`;
- Salvador/BA — `40010000`;
- Belo Horizonte/MG — `30130110`.

Explicar que cada objeto contém exatamente `cep`, `cidade` e `estado`.

## 3. Código - 50 a 60 s

Mostrar `src/viacep_validator.py` e explicar:

- validação de CEP com 8 dígitos;
- chamada real ao ViaCEP;
- tratamento de CEP não encontrado;
- tratamento de `erro=true` tanto booleano quanto string;
- comparação de `localidade` com `cidade`;
- comparação de `uf` com `estado`.

Mostrar rapidamente `tests/test_viacep.py` e o uso de parametrização.

## 4. Execução real - 45 s

No terminal, executar:

```powershell
.\run_qa.cmd
```

Destacar o resultado:

```text
5 passed, 3 deselected
3 passed, 5 deselected
QA_UNIDADE3=PASS
```

Explicar: "Foram cinco validações locais e três consultas reais ao ViaCEP, totalizando oito testes aprovados."

## 5. Evidência de QA - 30 s

Explicar resumidamente que uma execução anterior encontrou um CEP de Salvador que retornava `erro=true`.

Dizer:

"O teste identificou uma massa de teste inadequada. O CEP foi corrigido, o código passou a tratar também o retorno de erro como string e foi adicionado um teste de regressão. Depois disso, executei o reteste completo com 8 de 8 aprovados."

Esse é um bom ponto para demonstrar o ciclo de QA:

```text
FAIL → DIAGNÓSTICO → CORREÇÃO → REGRESSÃO → RETESTE → PASS
```

## 6. Gherkin - 30 s

Mostrar `features/login_portal_aluno.feature` e explicar:

- **Dado**: pré-condição;
- **Quando**: ação;
- **Então**: comportamento esperado.

## 7. Fechamento - 20 s

"A atividade demonstra dois tipos de qualidade: na API, validei automaticamente a consistência de CEP, cidade e estado; no cenário Web, usei Gherkin para especificar o comportamento esperado de login. No contexto do Projeto API Correios, esse mesmo princípio funciona como um gate de qualidade antes de etapas posteriores do processo de expedição."
