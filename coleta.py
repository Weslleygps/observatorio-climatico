
import json
from datetime import datetime
from pathlib import Path

import requests


# Configurações do projeto
CIDADE = "Caçapava - SP"
LATITUDE = -23.10
LONGITUDE = -45.71

DATA_INICIO = "2026-10-20"
DATA_FIM = "2026-11-18"

URL_API = "https://archive-api.open-meteo.com/v1/archive"

PASTA_DADOS = Path("dados/brutos")
ARQUIVO_JSON = PASTA_DADOS / "clima_original.json"


def coletar_dados():
    PASTA_DADOS.mkdir(parents=True, exist_ok=True)

    parametros = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "start_date": DATA_INICIO,
        "end_date": DATA_FIM,
        "daily": (
            "temperature_2m_mean,"
            "precipitation_sum,"
            "relative_humidity_2m_mean"
        ),
        "timezone": "America/Sao_Paulo",
        "temperature_unit": "celsius",
        "precipitation_unit": "mm"
    }

    print("Consultando a API Open-Meteo...")

    try:
        resposta = requests.get(
            URL_API,
            params=parametros,
            timeout=30
        )

        resposta.raise_for_status()
        dados_api = resposta.json()

        if "daily" not in dados_api:
            raise ValueError("A API não retornou os dados diários.")

        # Preserva a resposta original e os parâmetros da coleta.
        registro = {
            "cidade": CIDADE,
            "parametros": parametros,
            "data_coleta": datetime.now().isoformat(),
            "api_response": dados_api
        }

        with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
            json.dump(
                registro,
                arquivo,
                ensure_ascii=False,
                indent=4
            )

        quantidade = len(dados_api["daily"]["time"])

        print("\nColeta realizada com sucesso!")
        print(f"Cidade: {CIDADE}")
        print(f"Registros recebidos: {quantidade}")
        print(f"Arquivo original: {ARQUIVO_JSON}")

    except requests.exceptions.RequestException as erro:
        print(f"Erro na comunicação com a API: {erro}")
        raise

    except (ValueError, KeyError) as erro:
        print(f"Erro nos dados recebidos: {erro}")
        raise


if __name__ == "__main__":
    coletar_dados()
