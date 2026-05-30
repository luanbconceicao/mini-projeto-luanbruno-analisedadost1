import pandas as pd

def num_compras_genero(df):
  print("\n=== NÚMERO DE COMPRAS POR GÊNERO ===")
  agrupamento = df.groupby('CL_GENERO')['CO_ID'].count()

  print(f"Número mulheres: {agrupamento['F']}")
  print(f"Número por homens: {agrupamento['M']}")

def num_compras_filho(df):
  print("\n=== NÚMERO DE COMPRAS POR QUANTIDADE DE FILHOS ===")
  agrupamento = df.groupby('CL_FHL')['CO_ID'].count()
  print(agrupamento)

def cat_pr_vendas(df):
  print("\n=== CATEGORIAS E PRODUTO COM MAIOR NÚMERO DE VENDAS ===")

  agrupamento_cat = df.groupby('PR_CAT')['CO_ID'].count()
  agrupamento_produto = df.groupby('PR_NOME')['CO_ID'].count()

  print(agrupamento_cat)

  print(f"\nO produto mais vendido foi o {agrupamento_produto.idxmax()}, com {agrupamento_produto.max()} vendas.")
