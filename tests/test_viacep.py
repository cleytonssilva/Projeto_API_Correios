from pathlib import Path

import pytest

from src.viacep_validator import carregar_casos, consultar_cep, validar_retorno

DADOS = Path(__file__).resolve().parents[1] / "dados" / "ceps.json"
CASOS = carregar_casos(DADOS)


@pytest.mark.integration
@pytest.mark.parametrize("caso", CASOS, ids=lambda caso: caso["cep"])
def test_cep_deve_retornar_cidade_e_estado_corretos(caso):
    """Validação de integração real com o ViaCEP."""
    dados = consultar_cep(caso["cep"])
    validar_retorno(caso, dados)
