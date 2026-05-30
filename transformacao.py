import pandas as pd
import numpy as np

# Função para remover espaços no inicio e fim dos valores das colunas strings
# Caso tenha algum valor apenas com espaço, ele ficará vazio e será convertido para np.nan na função conversor_nulos()
def remover_espacos(df):
  for coluna in df.columns:
    if df[coluna].dtype == 'object':
      df[coluna] = df[coluna].str.strip()
      
  return df

# Conversão de células preenchidas com NULL, N/A ou vazias para np.nan para que possam ser detectadas pelo método isnull()
def conversor_nulos(df):
  print(f"Numero de nulos antes do replace de nulos: {df.isnull().sum().sum()}")
  df = df.replace({'NULL': np.nan, 'N/A': np.nan, '': np.nan})
  print(f"Numero de nulos depois do replace de nulos: {df.isnull().sum().sum()}")

  return df

# Foi descidido remover os valores nulos, pois são 3 colunas onde todos os valores inclusive o nome da coluna estão com os valores vazios
def remover_colunas_vazias(df):
  print(f"Número de colunas antes: {len(df.columns)}")
  df = df.dropna(axis=1, how='all')
  print(f"Número de colunas depois: {len(df.columns)}")
  print(f"Número de valores nulos no Data Frame: {df.isnull().sum().sum()}")

  return df

def converter_data(series_data):
  print(f"Tipo da coluna antes: {series_data.dtype}")
  series_data = pd.to_datetime(series_data, format='%d/%m/%Y')
  print(f"Tipo da coluna depois: {series_data.dtype}")
  
  return series_data

#Função para remover linhas que possuem todos os valores iguais, deixando apenas a primeira
def remover_duplicatas(df):
  print(f"Número de linhas antes do tratamento de duplicatas: {df.shape[0]}")
  df = df.drop_duplicates()
  print(f"Número de linhas após do tratamento de duplicatas: {df.shape[0]}")

  return df