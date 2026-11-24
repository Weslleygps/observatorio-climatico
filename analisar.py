
import duckdb

conexao = duckdb.connect(
    "dados/observatorio.duckdb",
    read_only=True
)

print("\n1. INDICADORES DO PERÍODO")

print(conexao.execute("""
    SELECT
        ROUND(AVG(temperatura_media_c), 2)
            AS temperatura_media,
        ROUND(SUM(precipitacao_mm), 2)
            AS precipitacao_total,
        ROUND(AVG(umidade_relativa_media_pct), 2)
            AS umidade_media
    FROM clima_diario
    WHERE cidade = 'Caçapava - SP'
""").df().to_string(index=False))


print("\n2. DIAS MAIS CHUVOSOS")

print(conexao.execute("""
    SELECT data, precipitacao_mm
    FROM clima_diario
    WHERE cidade = 'Caçapava - SP'
    ORDER BY precipitacao_mm DESC
    LIMIT 5
""").df().to_string(index=False))


print("\n3. MAIOR TEMPERATURA MÉDIA DIÁRIA")

print(conexao.execute("""
    SELECT data, temperatura_media_c
    FROM clima_diario
    WHERE cidade = 'Caçapava - SP'
    ORDER BY temperatura_media_c DESC
    LIMIT 1
""").df().to_string(index=False))


print("\n4. RELAÇÃO ENTRE UMIDADE E PRECIPITAÇÃO")

print(conexao.execute("""
    SELECT
        ROUND(
            CORR(
                umidade_relativa_media_pct,
                precipitacao_mm
            ), 3
        ) AS correlacao
    FROM clima_diario
    WHERE cidade = 'Caçapava - SP'
      AND umidade_relativa_media_pct IS NOT NULL
      AND precipitacao_mm IS NOT NULL
""").df().to_string(index=False))


conexao.close()
