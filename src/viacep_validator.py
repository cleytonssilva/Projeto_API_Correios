from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import requests

VIACEP_BASE_URL = "https://viacep.com.br/ws/{cep}/json/"
CEP_PATTERN = re.compile(r"^\d{8}$")
REQUIRED_FIELDS = {"cep", "cidade", "estado"}


def carregar_casos(caminho: str | Path) -> list[dict[str, str]]:
    """Carrega e valida a estrutura mínima exigida para os casos de teste."""
    path = Path(caminho)
    with path.open(encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    if not isinstance(dados, list) or not dados:
        raise ValueError("O arquivo JSON deve conter uma lista não vazia de casos.")

    casos: list[dict[str, str]] = []
    for indice, caso in enumerate(dados, start=1):
        if not isinstance(caso, dict):
            raise ValueError(f"Caso {indice}: esperado um objeto JSON.")
        if set(caso.keys()) != REQUIRED_FIELDS:
            raise ValueError(
                f"Caso {indice}: os campos devem ser exatamente {sorted(REQUIRED_FIELDS)}."
            )
        if not CEP_PATTERN.fullmatch(str(caso["cep"])):
            raise ValueError(f"Caso {indice}: CEP deve possuir exatamente 8 dígitos.")
        if not str(caso["cidade"]).strip():
            raise ValueError(f"Caso {indice}: cidade não pode ser vazia.")
        if not re.fullmatch(r"[A-Z]{2}", str(caso["estado"])):
            raise ValueError(f"Caso {indice}: estado deve ser uma UF com 2 letras maiúsculas.")
        casos.append(
            {
                "cep": str(caso["cep"]),
                "cidade": str(caso["cidade"]).strip(),
                "estado": str(caso["estado"]).strip(),
            }
        )
    return casos


def _resposta_indica_cep_inexistente(dados: dict[str, Any]) -> bool:
    """Normaliza as formas conhecidas de retorno do campo 'erro' do ViaCEP."""
    valor = dados.get("erro")
    if valor is True:
        return True
    if isinstance(valor, str) and valor.strip().lower() == "true":
        return True
    return False


def consultar_cep(cep: str, timeout: int = 10) -> dict[str, Any]:
    """Consulta o ViaCEP e devolve o JSON da resposta."""
    if not CEP_PATTERN.fullmatch(cep):
        raise ValueError("CEP inválido: informe exatamente 8 dígitos.")

    resposta = requests.get(
        VIACEP_BASE_URL.format(cep=cep),
        timeout=timeout,
        headers={"User-Agent": "Projeto-API-Correios-QA-Unidade3/1.0"},
    )
    resposta.raise_for_status()
    dados = resposta.json()

    if _resposta_indica_cep_inexistente(dados):
        raise AssertionError(f"CEP {cep} não encontrado pelo ViaCEP.")

    return dados


def validar_retorno(caso: dict[str, str], dados: dict[str, Any]) -> None:
    """Valida CEP, cidade/localidade e UF retornados pelo serviço."""
    cep_retornado = str(dados.get("cep", "")).replace("-", "")
    cidade_retornada = str(dados.get("localidade", "")).strip()
    uf_retornada = str(dados.get("uf", "")).strip()

    assert cep_retornado == caso["cep"], (
        f"CEP divergente: esperado {caso['cep']}, retornado {cep_retornado or '<vazio>'}."
    )
    assert cidade_retornada == caso["cidade"], (
        f"Cidade divergente para o CEP {caso['cep']}: "
        f"esperado '{caso['cidade']}', retornado '{cidade_retornada}'."
    )
    assert uf_retornada == caso["estado"], (
        f"UF divergente para o CEP {caso['cep']}: "
        f"esperado '{caso['estado']}', retornado '{uf_retornada}'."
    )
