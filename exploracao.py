import pandas as pd
import numpy as np

# Função para realizar a exploração do Data Frame criado a aprtir do arquivo BaseVarejo.csv
def explorar(df):
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