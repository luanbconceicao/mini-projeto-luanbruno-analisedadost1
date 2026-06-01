import pandas as pd
import numpy as np

# Função para remover espaços no inicio e fim dos valores das colunas strings
# Caso tenha algum valor apenas com espaço, ele ficará vazio e será convertido para np.nan na função conversor_nulos()
def remover_espacos(df):
  for coluna in df.columns:
    if df[coluna].dtype == 'object':
      df[coluna] = df[coluna].str.strip()
      
  return df

def conversor_nulos(df):
  print("\n=== CONTAGEM E CONVERSÃO DE STRINGS QUE REPRESENTAM NULOS  ===")
  print(f"Numero de nulos antes do replace de nulos: {df.isnull().sum().sum()}")
  df = df.replace({'NULL': np.nan, 'N/A': np.nan, '#N/D': np.nan , '': np.nan})
  print(f"Numero de nulos depois do replace de nulos: {df.isnull().sum().sum()}")

  return df

# Função que verifica que o valor é nulo, caso seja, o if a qual coluna pertense para preencher 'Sem Categoria' ou 'Sem Nome'
def verificar_nulo(valor, coluna):
    if pd.isna(valor):
        if coluna == 'PR_CAT':
            return 'Sem Categoria'
        else:
            return 'Sem Nome'
    else:
        return valor
    
# Foi descidido remover os valores nulos restantes, pois são 3 colunas onde todos os valores inclusive o nome da coluna estão com os valores vazios.
def remover_colunas_vazias(df):
    print("\n=== REMOÇÃO DE COLUNAS COM TODOS OS VALORES NULOS ===")
    print(f"Número de colunas antes: {len(df.columns)}")
    df = df.dropna(axis=1, how='all')
    print(f"Número de colunas depois: {len(df.columns)}")

    print(f"Número de valores nulos restantes: {df.isnull().sum().sum()}")
    return df

def converter_data(series_data):
  print("\n=== CONVERSÃO DA COLUNA DATA DE STRING PARA DATETIME ===")
  print(f"Tipo da coluna antes: {series_data.dtype}")
  series_data = pd.to_datetime(series_data, format='%d/%m/%Y')
  print(f"Tipo da coluna depois: {series_data.dtype}")
  
  return series_data

def remover_duplicatas(df):
  print("\n=== REMOÇÃO DE DUPLICATAS ===")
  print(f"Número de linhas antes do tratamento de duplicatas: {df.shape[0]}")
  df = df.drop_duplicates()
  print(f"Número de linhas após do tratamento de duplicatas: {df.shape[0]}")

  return df