# Relatório de Entrega - Qualidade de Software (QA) - Unidade 3

**Projeto:** Projeto API Correios - Recorte acadêmico de QA  
**Aluno:** Cleyton Santiago  
**Repositório:** `cleytonssilva/Projeto_API_Correios`  
**Status final:** `QA_UNIDADE3=PASS`

## 1. Objetivo

Implementar a atividade prática da Unidade 3 por meio de automação de teste de API com o ViaCEP e especificação de um cenário Web em Gherkin.

A atividade foi contextualizada com o Projeto API Correios: CEP, cidade e UF são tratados como dados críticos de endereço e devem ser validados antes que um registro avance para etapas posteriores de expedição.

## 2. Requisito acadêmico - API

A entrada contém exatamente três campos:

```json
{
  "cep": "01001000",
  "cidade": "São Paulo",
  "estado": "SP"
}
```

O arquivo `dados/ceps.json` possui três casos e o teste consulta `https://viacep.com.br/ws/{CEP}/json/`.

São comparados:

- CEP retornado x CEP consultado;
- `localidade` x `cidade` esperada;
- `uf` x `estado` esperado.

## 3. Estratégia de QA

A suíte foi separada em dois níveis.

### 3.1 Validação determinística

Verifica:

- estrutura do JSON;
- presença dos três casos;
- regra de divergência de cidade;
- regra de divergência de UF;
- tratamento do retorno de CEP inexistente quando o campo `erro` chega como string.

### 3.2 Integração real

Executa chamadas reais ao ViaCEP e valida os dados recebidos.

Essa separação permite distinguir defeitos de regra, problemas da massa de teste e falhas externas de infraestrutura.

## 4. Casos de teste validados

| CEP | Cidade esperada | UF | Resultado real |
|---|---|---|---|
| 01001000 | São Paulo | SP | PASS |
| 40010000 | Salvador | BA | PASS |
| 30130110 | Belo Horizonte | MG | PASS |

## 5. Resultado da execução final

Ambiente:

- Windows;
- Python 3.12.10;
- Pytest 8.3.5;
- ambiente virtual `.venv`.

Resultado:

```text
5 passed, 3 deselected
3 passed, 5 deselected
QA_UNIDADE3=PASS
```

Total efetivamente validado: **8 testes PASS**.

## 6. Evidência de melhoria

Durante uma execução anterior, o CEP `40020000` retornou `{"erro": "true"}`.

O teste detectou a inconsistência e o processo de QA resultou em:

1. diagnóstico da massa de teste;
2. substituição por `40010000`;
3. melhoria do código para reconhecer `erro` booleano ou string;
4. criação de teste de regressão;
5. reteste completo;
6. resultado final 8/8 PASS.

Esse ciclo evidencia a aplicação prática de QA, pois a falha não foi ocultada: foi usada para melhorar tanto os dados quanto a robustez da automação.

## 7. Atividade Web - Gherkin

O arquivo `features/login_portal_aluno.feature` especifica o login com credenciais válidas no Portal do Aluno, descrevendo pré-condição, ação e resultado esperado em linguagem Gherkin.

## 8. Critérios de aceite

A atividade foi considerada aprovada porque:

- o JSON possui exatamente `cep`, `cidade` e `estado`;
- existem três casos;
- os CEPs possuem 8 dígitos;
- a consulta real ao ViaCEP foi executada;
- cidade e UF retornadas coincidiram com os dados esperados;
- o cenário Gherkin está versionado;
- a suíte é executável por Pytest;
- a execução é reproduzível por `run_qa.cmd`;
- o resultado final foi `QA_UNIDADE3=PASS`.

## 9. GitHub Actions

O workflow `.github/workflows/qa-unidade3.yml` está publicado. No momento da validação, o GitHub criou os runs, mas os jobs encerraram antes da execução de qualquer step.

Esse comportamento foi classificado separadamente como **BLOCKED_BY_ACTIONS_STARTUP** e não altera o resultado funcional obtido em execução real local.

## 10. Conclusão

A atividade atende ao enunciado e demonstra práticas relevantes de Qualidade de Software: teste orientado por dados, assertions explícitas, integração com serviço externo, tratamento de falhas, regressão, reteste, ambiente isolado e documentação de evidências.

O resultado final é uma entrega acadêmica executável, auditável e contextualizada com um cenário real do Projeto API Correios.
