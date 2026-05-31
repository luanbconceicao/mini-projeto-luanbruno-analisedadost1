import pandas as pd


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
  
  print("\n=== ESTATÍSTICAS DESCRITIVAS: NÚMERO DE FILHOS (CL_FHL) ===")
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
