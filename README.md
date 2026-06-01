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

Insights Obtidos

1. A base tinha 4 colunas completamente vazias que foram removidas. 3.650 linhas estavam sem categoria e nome do produto — poderiam ser recuperadas via PR_ID, mas foram removidas por representarem menos de 1% do total.
2. Linhas duplicadas foram removidas (96.131 linhas). Pode haver casos onde o mesmo produto foi comprado mais de uma vez na mesma compra — sem coluna de hora ou informação do sistema gerador, optou-se pela remoção.
3. Existem produtos com o mesmo nome mas IDs diferentes, indicando possível inconsistência no cadastro. Não foi feito tratamento.
4. Clientes com 3 filhos possuem a maior média de compras (760 por cliente).
5. O gênero feminino realizou mais compras (380.735 vs 349.484 masculino).
6. A categoria mais vendida foi Alimentos e o produto mais vendido foi Presunto Cozido com 12.719 vendas.
