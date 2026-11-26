
# Observatório Climático Local

Projeto Integrador Extensionista 2 – Ciência de Dados
Universidade de Marília (UNIMAR)

## Integrante

- Weslley Gonçalves Pinheiro Soares

## Público-alvo

Estudantes e professores da comunidade escolar de Caçapava (SP).

## Objetivo

Analisar o comportamento histórico da temperatura, precipitação e umidade relativa em Caçapava, contribuindo para o planejamento de atividades ao ar livre e para a conscientização sobre o clima local.

## Fonte dos dados

Open-Meteo Historical Weather API:
https://open-meteo.com/en/docs/historical-weather-api

Os dados são históricos e provenientes de modelos meteorológicos, não devendo ser apresentados como medições diretas de uma estação meteorológica local.

## Recorte

- Localidade: Caçapava (SP).
- Coordenadas: latitude -23.10 e longitude -45.71 (aproximadas).
- Período: 30 dias consecutivos, conforme configurado em coleta.py.
- Temperatura média diária (°C).
- Precipitação diária acumulada (mm).
- Umidade relativa média diária (%).

## Tecnologias

- Python
- Requests
- pandas
- DuckDB
- SQL
- Git e GitHub

## Estrutura

```text
observatorio-climatico/
├── coleta.py
├── banco.py
├── analisar.py
├── consultas.sql
├── requirements.txt
├── README.md
├── .gitignore
├── dados/
│   ├── brutos/
│   ├── tratados/
│   └── observatorio.duckdb
└── docs/
    └── escopo-1/
        └── AE1/
```

## Preparação do ambiente

Clone o repositório:

```bash
git clone https://github.com/Weslleygps/observatorio-climatico.git
cd observatorio-climatico
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Execução

1. Configure as datas de 30 dias em coleta.py.
2. Execute a coleta:

```bash
python coleta.py
```

3. Trate os dados e gere o banco:

```bash
python banco.py
```

4. Execute as análises:

```bash
python analisar.py
```

## Indicadores

- Temperatura média do período (°C).
- Precipitação acumulada no período (mm).
- Umidade relativa média do período (%).

## Limitações

Os dados são provenientes de modelos meteorológicos históricos. Eles representam estimativas para a região e não necessariamente medições diretas em uma estação localizada no município.

A análise descreve o período selecionado e não constitui previsão meteorológica.

## Status

- [x] Ambiente configurado.
- [x] Repositório GitHub criado.
- [ ] Coleta de dados.
- [ ] Tratamento e validação.
- [ ] Banco DuckDB.
- [ ] Consultas SQL e indicadores.
- [ ] Relatório técnico.


      
## AE2 – Desenho da solução

Esta etapa apresenta o planejamento técnico do Observatório Climático Local.

**Localidade:** Caçapava – SP

**Período:** 20/10/2026 a 18/11/2026

**Variáveis:**
- Temperatura média diária (°C)
- Precipitação diária (mm)
- Umidade relativa média (%)

**Tecnologias:**
- Open-Meteo API
- Python e Requests
- pandas
- DuckDB e SQL
- Streamlit
- GitHub

**Documentação da AE2:**

Os documentos, o diagrama do fluxo e o wireframe estão disponíveis em:

`docs/escopo-1/AE2-2/`

