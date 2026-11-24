# Evidência de validação do ambiente de preparação

- Validações locais: **PASS** - 4 testes executados com sucesso.
- Teste de integração ViaCEP neste ambiente: **BLOCKED_BY_NETWORK** - falha de resolução DNS para `viacep.com.br`.
- A falha não é classificada como defeito funcional do teste; o código permanece configurado para chamada real ao ViaCEP.
- Execução real prevista: PowerShell local com internet ou GitHub Actions após publicação no repositório.

Arquivos de evidência:
- `reports/junit-offline.xml`
- `reports/junit-integration-attempt.xml`
- `reports/integration-attempt.txt`
