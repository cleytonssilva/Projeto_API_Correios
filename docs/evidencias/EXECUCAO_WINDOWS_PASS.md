# Execução real no Windows — PASS

## Ambiente

- Sistema: Windows
- Python: 3.12.10
- Pytest: 8.3.5
- Execução: `run_qa.cmd`
- Isolamento: `.venv`

## Resultado

### Testes locais

```text
collected 8 items / 3 deselected / 5 selected
5 passed, 3 deselected
```

### Integração real ViaCEP

```text
01001000 -> PASSED
40010000 -> PASSED
30130110 -> PASSED
3 passed, 5 deselected
```

### Veredito

```text
QA_UNIDADE3=PASS
```

**Total: 8/8 testes aprovados.**

## Observação

Esta evidência resume a execução real informada no terminal do ambiente Windows. O arquivo `reports/junit.xml` é gerado localmente pela etapa de integração e não é versionado por padrão.
