
-- CONSULTA 1
-- Temperatura média do período e maior temperatura média diária.

SELECT
    AVG(temperatura_media_c) AS temperatura_media_periodo,
    MAX(temperatura_media_c) AS maior_temperatura_media_diaria
FROM clima_diario
WHERE cidade = 'Caçapava - SP';


-- CONSULTA 2
-- Cinco dias com maior precipitação.

SELECT
    data,
    precipitacao_mm
FROM clima_diario
WHERE cidade = 'Caçapava - SP'
  AND precipitacao_mm IS NOT NULL
ORDER BY precipitacao_mm DESC, data ASC
LIMIT 5;


-- CONSULTA 3
-- Relação entre umidade e precipitação.

SELECT
    data,
    umidade_relativa_media_pct,
    precipitacao_mm
FROM clima_diario
WHERE cidade = 'Caçapava - SP'
  AND umidade_relativa_media_pct IS NOT NULL
  AND precipitacao_mm IS NOT NULL
ORDER BY data;

