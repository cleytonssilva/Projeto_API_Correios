import json
from pathlib import Path

import pytest

from src.viacep_validator import carregar_casos, validar_retorno

DADOS = Path(__file__).resolve().parents[1] / "dados" / "ceps.json"


def test_json_deve_conter_tres_casos_com_campos_exigidos():
    casos = carregar_casos(DADOS)
    assert len(casos) == 3
    for caso in casos:
        assert set(caso) == {"cep", "cidade", "estado"}


def test_validacao_deve_detectar_cidade_divergente():
    caso = {"cep": "01001000", "cidade": "São Paulo", "estado": "SP"}
    retorno_incorreto = {"cep": "01001-000", "localidade": "Campinas", "uf": "SP"}

    with pytest.raises(AssertionError, match="Cidade divergente"):
        validar_retorno(caso, retorno_incorreto)


def test_validacao_deve_detectar_uf_divergente():
    caso = {"cep": "01001000", "cidade": "São Paulo", "estado": "SP"}
    retorno_incorreto = {"cep": "01001-000", "localidade": "São Paulo", "uf": "RJ"}

    with pytest.raises(AssertionError, match="UF divergente"):
        validar_retorno(caso, retorno_incorreto)


def test_json_bruto_e_valido():
    with DADOS.open(encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    assert isinstance(dados, list)
