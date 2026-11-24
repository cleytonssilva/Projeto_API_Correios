# Relatório de Entrega - Qualidade de Software (QA) - Unidade 3

**Projeto:** Projeto API Correios - Recorte acadêmico de QA  
**Aluno:** Cleyton Santiago  
**Repositório-alvo:** `cleytonssilva/Projeto_API_Correios`

## 1. Objetivo

Implementar a atividade prática da Unidade 3 por meio de automação de teste de API com o ViaCEP e especificação de um cenário Web em Gherkin.

A atividade foi contextualizada com o Projeto API Correios: CEP, cidade e UF são tratados como dados críticos de endereço e devem ser validados antes que um registro avance para etapas posteriores de expedição.

## 2. Requisito acadêmico - API

A entrada contém três campos:

```json
{
  "cep": "01001000",
  "cidade": "São Paulo",
  "estado": "SP"
}
```

O arquivo `dados/ceps.json` contém três casos. O teste consulta `https://viacep.com.br/ws/{CEP}/json/` e compara:

- `localidade` x `cidade` esperada;
- `uf` x `estado` esperado;
- CEP retornado x CEP consultado.

## 3. Estratégia de QA

Foram separados dois níveis de teste:

### 3.1 Validação determinística

Testa localmente a estrutura do JSON e comprova que a regra detecta cidade/UF divergentes.

### 3.2 Teste de integração

Realiza chamada real ao ViaCEP. Se o serviço retornar dado diferente do esperado, CEP inexistente ou erro HTTP, o teste falha.

Essa separação reduz falsos diagnósticos: uma indisponibilidade externa não invalida a lógica local, e uma lógica correta não é confundida com uma integração realmente comprovada.

## 4. Casos de teste

| CEP | Cidade esperada | UF | Resultado esperado |
|---|---|---|---|
| 01001000 | São Paulo | SP | PASS |
| 40020000 | Salvador | BA | PASS |
| 30130110 | Belo Horizonte | MG | PASS |

## 5. Critérios de aceite

A entrega é considerada aprovada quando:

- o JSON possui exatamente os campos `cep`, `cidade`, `estado`;
- existem três casos de entrada;
- todos os CEPs possuem 8 dígitos;
- a consulta real ao ViaCEP responde sem erro;
- cidade e UF retornadas coincidem com os dados esperados;
- o cenário Gherkin de login está presente e legível;
- a suíte é executável por Pytest;
- existe automação em CI para repetição dos testes.

## 6. Atividade Web - Gherkin

O cenário `features/login_portal_aluno.feature` especifica o login com credenciais válidas no Portal do Aluno, descrevendo pré-condições, ações e resultado esperado em linguagem Gherkin.

## 7. Integração com o Projeto API Correios

O recorte acadêmico não modifica o fluxo produtivo do projeto. Ele demonstra um uso significativo de QA aplicado ao tratamento de dados de endereço: uma inconsistência entre CEP, cidade e UF deve ser detectada antes de o dado alimentar etapas operacionais posteriores.

Assim, o teste funciona conceitualmente como um **quality gate de endereço**.

## 8. Execução e evidências

Execução local:

```bash
python -m pytest -v
```

Execução automatizada:

- GitHub Actions: `.github/workflows/qa-unidade3.yml`;
- artefato gerado: `reports/junit.xml`.

## 9. Limites e transparência

O teste de integração depende de conectividade com o ViaCEP. A documentação oficial do serviço informa que o CEP deve possuir 8 dígitos; formato inválido resulta em HTTP 400 e CEP válido inexistente retorna `erro: true`.

A suíte implementada trata o formato antes da chamada e transforma CEP não encontrado em falha explícita.

## 10. Conclusão

A atividade atende ao enunciado e adiciona práticas de QA relevantes: dados externos, assertions explícitas, parametrização, separação de testes locais e de integração, mensagens de diagnóstico, execução repetível e CI.

O resultado é uma entrega acadêmica pequena, mas executável, auditável e conectada a um cenário real de qualidade de dados no Projeto API Correios.
