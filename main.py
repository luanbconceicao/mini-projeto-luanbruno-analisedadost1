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
print(f"Numero de nulos antes do replace de nulos: {df.isnull().sum().sum()}")
df_limpo = df.replace({'NULL': np.nan, 'N/A': np.nan, '': np.nan})
print(f"Numero de nulos depois do replace de nulos: {df.isnull().sum().sum()}")

print("\n=== CONTAGEM DE VALORES NULOS POR COLUNA ===")
print(df.isnull().sum())

# Foi descidido remover os valores nulos, pois são 3 colunas onde todos os valores inclusive o nome da coluna estão com os valores vazios
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

# =========================================================================
# PARTE 3: Estatísticas Descritivas coluna número de filhos
# =========================================================================
print("\n=== ESTATÍSTICAS DESCRITIVAS: NÚMERO DE FILHOS (CL_FHL) ===")

def desc_col_num_filhos(df):

# Fiz os cálculos estatísticos separadamente solicitados para a coluna de Número de Filhos
  media = df['CL_FHL'].mean()
  mediana = df['CL_FHL'].median()
  desvio_padrao = df['CL_FHL'].std()
  moda = df['CL_FHL'].mode()[0]
  minimo = df['CL_FHL'].min()
  maximo = df['CL_FHL'].max()
  contagem = df['CL_FHL'].count()
  quartil1 = df['CL_FHL'].quantile(0.25)
  quartil3 = df['CL_FHL'].quantile(0.75)
  

  print(f"Média: {media:.2f} filho(s)")
  print(f"Mediana: {mediana} filho(s)")
  print(f"Desvio Padrão: {desvio_padrao:.2f}")
  print(f"Moda: {moda}")
  print(f"Mínimo de filhos: {minimo} filhos")
  print(f"Máximo: {maximo} filhos")
  print(f"Contagem: {contagem}")
  print(f"1° Quartil (25%): {quartil1}")
  print(f"2° Quartil (50%): {mediana}")
  print(f"3° Quartil (75%): {quartil3}")


desc_col_num_filhos(df)
