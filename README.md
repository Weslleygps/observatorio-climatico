# observatorio-climatico
# Observatório Climático Local

Projeto Integrador Extensionista 2 – Ciência de Dados
Universidade de Marília (UNIMAR) · Prof. Luiz Henrique

## Integrantes
- Weslley Gonçalves Pinheiro Soares 

## Público-alvo
Estudantes e professores da comunidade escolar da localidade analisada.

## Necessidade trabalhada
Compreender as variações de temperatura e chuva ao longo do mês,
para apoiar o planejamento de atividades ao ar livre e a conscientização
sobre o clima local, usando dados que a comunidade consiga interpretar
facilmente.

## Problema investigado
Como o clima se comportou na localidade nos últimos 30 dias, e que
informações seriam úteis para o público escolhido?

## Localidade e período
- **Localidade:** Caçapava (SP)
- **Período:** 30 dias consecutivos (de 20/10/2026 a 20/11/2026)

## Recorte do projeto
- Uma localidade e trinta dias consecutivos
- Três variáveis meteorológicas: temperatura média diária (°C),
  precipitação diária (mm) e umidade relativa média (%)
- Uma tabela principal
- Três perguntas analíticas
- Três indicadores (KPIs) e dois gráficos

## Perguntas analíticas
1. Qual foi a temperatura máxima do período e em qual dia ocorreu?
2. Quais foram os dias mais chuvosos?
3. Existe relação entre a umidade e a precipitação?

## Indicadores (KPIs)
- Temperatura média do período (°C)
- Total de precipitação no período (mm)
- Umidade média do período (%)

## Gráficos
- Tendência da temperatura média diária (linha)
- Precipitação diária (barras)

## Ferramentas
| Ferramenta | Responsabilidade |
|---|---|
| Open-Meteo API | Fonte dos dados meteorológicos |
| Python + Requests | Coleta dos dados |
| Pandas | Limpeza e organização dos dados |
| DuckDB + SQL | Armazenamento e consultas analíticas |
| Streamlit | Painel de visualização |
| Git + GitHub | Versionamento e colaboração |

## Estrutura do repositório
projeto/
├── README.md
├── requirements.txt
├── .gitignore
├── coleta.py        # solicita dados à API Open-Meteo
├── banco.py         # conexão e persistência (DuckDB)
├── app.py           # painel Streamlit
├── consultas.sql    # consultas SQL
├── dados/
└── docs/

## Instruções de execução
1. Clone o repositório:
   git clone https://github.com/SEU-USUARIO/observatorio-climatico.git
2. Crie e ative o ambiente virtual:
   python -m venv .venv
   .venv\Scripts\activate        (Windows)
   source .venv/bin/activate     (Linux/Mac)
3. Instale as dependências:
   pip install -r requirements.txt
4. Teste o ambiente:
   python teste_ambiente.py

## Status
- [x] Ambiente configurado
- [x] Repositório criado
- [x] README inicial
- [ ] Coleta de dados (Aula 2)
- [ ] Banco de dados e consultas SQL
- [ ] Painel e relatório final
