# MINI PROJETO 
# Aluno: Luan Bruno de Melo Conceição
# Turma: Analise de dados T1

# ============================================================
# PARTE 1: Importação dos dados e informações da tabela
# ============================================================

import pandas as pd
import numpy as np

# Carregamento da base de dados
df = pd.read_csv('BaseVarejo.csv', sep=';')

print("\n=== PRIMEIRAS 5 LINHAS ===")
print(df.head(5))

print("\n=== NÚMERO DE REGISTROS E COLUNAS ===")
print(f"Tamanho: {df.shape[0]} linhas e {df.shape[1]} colunas")

print("\n=== NOMES DAS COLUNAS ===")
print(df.columns.tolist())

print("\n=== TIPOS DE DADOS POR COLUNA ===")
for coluna in df.columns:
  tipo = str(df[coluna].dtype)
  print(f"Coluna {coluna} é do tipo {tipo}")
  

print("\n=== RESUMO GERAL ===")
print(df.info())

# =========================================================================
# PARTE 2: Transformação de Strings, Datetime e remoção de colunas vazias
# =========================================================================

# Removendo espaços no inicio e fim dos valores das colunas strings
# Caso tenha algum valor apenas com espeço, será convertido para np.nan ná próxima etapa
for coluna in df.columns:
  if df[coluna].dtype == 'object':
    df[coluna] = df[coluna].str.strip()

# Conversão de células preenchidas com NULL, N/A ou vazias para np.nan para que possam ser detectadas pelo método isnull()
# Não precisou ser convertido nenhuma celular para np.nan
print("\n=== CONTAGEM E CONVERSÃO DE STRINGS QUE REPRESENTAM NULOS  ===")
df_limpo = df.replace({'NULL': np.nan, 'N/A': np.nan, '': np.nan})
print(f"Numero de nulos antes do replace de nulos: {df.isnull().sum().sum()}")
print(f"Numero de nulos depois do replace de nulos: {df_limpo.isnull().sum().sum()}")

print("\n=== CONTAGEM DE VALORES NULOS POR COLUNA ===")
print(df.isnull().sum())

# Removendo colunas vazias
print("\n=== REMOÇÃO DE COLUNAS COM TODOS OS VALORES NULOS ===")
print(f"Número de colunas antes: {len(df.columns)}")
df = df.dropna(axis=1, how='all')
print(f"Número de colunas depois: {len(df.columns)}")
print(f"Número de valores nulos no Data Frame: {df.isnull().sum().sum()}")

print("\n=== CONVERSÃO DA COLUNA DATA DE STRING PARA DATETIME ===")
print(f"Tipo da coluna antes: {df['DATA'].dtype}")
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
print(f"Tipo da coluna depois: {df['DATA'].dtype}")

print("\n=== REMOÇÃO DE DUPLICATAS ===")
print(f"Número de linhas antes do tratamento de duplicatas: {df.shape[0]}")
df = df.drop_duplicates()
print(f"Número de linhas após do tratamento de duplicatas: {df.shape[0]}")


print("\n=== PRIMEIRAS 5 LINHAS APÓS A LIMPEZA ===")
print(df.head(5))