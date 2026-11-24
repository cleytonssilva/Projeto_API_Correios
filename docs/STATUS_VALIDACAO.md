# Evidência de validação

## Estado consolidado

- Repositório publicado: **PASS**
- Branch: `main`
- Validações locais determinísticas: **PASS** — 4 testes executados com sucesso.
- Estrutura do JSON: **PASS** — 3 casos com os campos `cep`, `cidade` e `estado`.
- Regra de detecção de divergência de cidade: **PASS**.
- Regra de detecção de divergência de UF: **PASS**.
- Consulta externa de referência ao ViaCEP para `01001000`: **CONFIRMADA** — São Paulo/SP.
- Teste de integração ViaCEP no ambiente de preparação: **BLOCKED_BY_NETWORK** — falha de resolução DNS para `viacep.com.br`.
- GitHub Actions: **BLOCKED_BY_ACTIONS_STARTUP** — o workflow é reconhecido e cria runs, porém o job falha antes da execução de qualquer step; re-run apresentou o mesmo comportamento.
- A falha de startup do GitHub Actions não é classificada como defeito funcional da suíte de testes.

## Evidências

- `docs/evidencias/junit-offline.xml`: 4 testes locais com sucesso.
- Workflow publicado em `.github/workflows/qa-unidade3.yml`.
- Execução GitHub Actions mais recente analisada: run `45298437782`, tentativa 2, conclusão `failure`, sem steps executados.
- Commit da publicação completa antes desta atualização: `df13e85980895dfa21f41dc2e4413fd733f940a2`.

## Próxima validação operacional

Para concluir a prova de integração automatizada, executar a suíte em um ambiente com acesso normal ao ViaCEP:

```powershell
python -m pip install -r requirements.txt
python -m pytest -v -m integration
```

Resultado esperado:

- `01001000` → São Paulo / SP
- `40010000` → Salvador / BA
- `30130110` → Belo Horizonte / MG

A atividade permanece executável localmente e o bloqueio de CI está classificado separadamente como infraestrutura de GitHub Actions.
