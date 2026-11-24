
import json
from pathlib import Path

import duckdb
import pandas as pd


CIDADE = "Caçapava - SP"

ARQUIVO_JSON = Path("dados/brutos/clima_original.json")
ARQUIVO_CSV = Path("dados/tratados/clima_tratado.csv")
ARQUIVO_BANCO = Path("dados/observatorio.duckdb")


def carregar_json():
    if not ARQUIVO_JSON.exists():
        raise FileNotFoundError(
            "Arquivo JSON não encontrado. Execute coleta.py primeiro."
        )

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def tratar_dados(registro):
    dados = registro["api_response"]["daily"]

    df = pd.DataFrame({
        "data": dados["time"],
        "temperatura_media_c": dados["temperature_2m_mean"],
        "precipitacao_mm": dados["precipitation_sum"],
        "umidade_relativa_media_pct": dados[
            "relative_humidity_2m_mean"
        ]
    })

    # Conversão dos tipos
    df["data"] = pd.to_datetime(
        df["data"], errors="coerce"
    )

    colunas_numericas = [
        "temperatura_media_c",
        "precipitacao_mm",
        "umidade_relativa_media_pct"
    ]

    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(
            df[coluna], errors="coerce"
        )

    # Identificação de problemas
    if df["data"].isna().any():
        raise ValueError("Existem datas inválidas.")

    if df["data"].duplicated().any():
        raise ValueError("Existem datas duplicadas.")

    # Confere a cobertura do período
    parametros = registro["parametros"]

    inicio = pd.Timestamp(parametros["start_date"])
    fim = pd.Timestamp(parametros["end_date"])

    datas_esperadas = pd.date_range(inicio, fim, freq="D")

    if len(datas_esperadas) != 30:
        raise ValueError(
            "O período configurado não possui exatamente 30 dias."
        )

    if not df["data"].sort_values().reset_index(drop=True).equals(
        pd.Series(datas_esperadas, name="data")
    ):
        raise ValueError(
            "A cobertura de datas está incompleta ou fora do período."
        )

    # Validação dos valores
    if (df["precipitacao_mm"].dropna() < 0).any():
        raise ValueError("Precipitação negativa encontrada.")

    umidade = df["umidade_relativa_media_pct"].dropna()

    if ((umidade < 0) | (umidade > 100)).any():
        raise ValueError("Umidade fora do intervalo de 0 a 100%.")

    # Valores ausentes permanecem como ausentes.
    print("\nResumo da qualidade dos dados:")
    print("Registros:", len(df))
    print("Duplicidades:", df["data"].duplicated().sum())
    print("\nValores ausentes:")
    print(df.isna().sum())

    # Adiciona identificação da localidade
    df.insert(0, "cidade", CIDADE)

    return df


def salvar_csv(df):
    ARQUIVO_CSV.parent.mkdir(
        parents=True, exist_ok=True
    )

    df.to_csv(
        ARQUIVO_CSV,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"\nCSV tratado salvo em: {ARQUIVO_CSV}")


def salvar_duckdb(df):
    ARQUIVO_BANCO.parent.mkdir(
        parents=True, exist_ok=True
    )

    conexao = duckdb.connect(str(ARQUIVO_BANCO))

    try:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS clima_diario (
                cidade VARCHAR NOT NULL,
                data DATE NOT NULL,
                temperatura_media_c DOUBLE,
                precipitacao_mm DOUBLE,
                umidade_relativa_media_pct DOUBLE,
                PRIMARY KEY (cidade, data)
            )
        """)

        # Remove os registros do mesmo período antes de inserir.
        # Isso permite executar o processo novamente sem duplicar dados.
        data_inicio = df["data"].min().date()
        data_fim = df["data"].max().date()

        conexao.execute(
            """
            DELETE FROM clima_diario
            WHERE cidade = ?
            AND data BETWEEN ? AND ?
            """,
            [CIDADE, data_inicio, data_fim]
        )

        conexao.register("dados_temporarios", df)

        conexao.execute("""
            INSERT INTO clima_diario
            SELECT
                cidade,
                CAST(data AS DATE),
                temperatura_media_c,
                precipitacao_mm,
                umidade_relativa_media_pct
            FROM dados_temporarios
        """)

        conexao.unregister("dados_temporarios")

        total = conexao.execute("""
            SELECT COUNT(*)
            FROM clima_diario
            WHERE cidade = ?
        """, [CIDADE]).fetchone()[0]

        print(f"Registros armazenados no DuckDB: {total}")

    finally:
        conexao.close()


def main():
    registro = carregar_json()
    df = tratar_dados(registro)

    salvar_csv(df)
    salvar_duckdb(df)

    print("\nProcessamento finalizado com sucesso!")


if __name__ == "__main__":
    main()
