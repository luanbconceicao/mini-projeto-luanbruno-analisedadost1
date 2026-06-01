Sobre o Projeto
Análise Exploratória de Dados (AED) aplicada a uma base real de compras do varejo com 830.000 registros. O objetivo é transformar dados brutos em informações úteis, identificando problemas, realizando limpeza e extraindo insights.

## 🗂️ Estrutura dos Arquivos

```
mini-projeto/
├── main.py
├── exploracao.py
├── transformacao.py
├── estatisticas.py
├── agrupamentos.py
├── BaseVarejo.csv
├── df_limpo.csv
├── requirements.txt
├── README.md
└── README_LuanBruno_AnaliseDadosT1.md
```

## Reflexão Teórica — ETL e Qualidade de Dados

Neste projeto, cada etapa do ETL foi aplicada:

- **Extract:** leitura do `BaseVarejo.csv` com pandas, identificando 830.000 registros e 14 colunas.
- **Transform:** remoção de colunas e linhas vazias, tratamento de duplicatas, conversão de tipos de dados (DATA para datetime) e limpeza de strings.
- **Load:** ao final, o DataFrame limpo com 733447 registros está pronto para alimentar análises mais avançadas ou dashboards.

A **qualidade de dados** é fundamental nesse processo — dados com nulos, duplicatas ou tipos incorretos geram análises incorretas.

## Insights Obtidos

**1.** A base tinha 4 colunas completamente vazias que foram removidas. 3.650 linhas estavam sem categoria e nome do produto — poderiam ser recuperadas via PR_ID, mas foram preenchidas com 'Sem Categoria' e 'Sem Nome' respectivamente.
**2.** Linhas duplicadas foram removidas (96.553 linhas). Pode haver casos onde o mesmo produto foi comprado mais de uma vez na mesma compra — sem coluna de hora ou informação do sistema gerador, optou-se pela remoção.
**3.** Existem produtos com o mesmo nome mas IDs diferentes, indicando possível inconsistência no cadastro. Não foi feito tratamento.
**4.** Clientes com 3 filhos possuem a maior média de compras (764 por cliente).
**5.** O gênero feminino realizou mais compras (382427 vs 351020 masculino).
**6.** A categoria mais vendida foi Alimentos e o produto mais vendido foi Presunto Cozido com 12719 vendas.
