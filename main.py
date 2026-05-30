# MINI PROJETO 
# Aluno: Luan Bruno de Melo Conceição
# Turma: Analise de dados T1

# ============================================================
# PARTE 1: Importação dos dados e informações da tabela
# ============================================================

import pandas as pd
import numpy as np
from exploracao import explorar
from transformacao import *
from estatisticas import desc_col_num_filhos

# Carregamento da base de dados
df = pd.read_csv('BaseVarejo.csv', sep=';')

# Chamada da função explorar para impressão das imformações do Data Frame
explorar(df)

# =========================================================================
# PARTE 2: Transformação de Strings, Datetime e remoção de colunas vazias
# =========================================================================

df = remover_espacos(df) # Chamando a função remover_espacos para tratar os espaços das colunas strings

print("\n=== CONTAGEM E CONVERSÃO DE STRINGS QUE REPRESENTAM NULOS  ===")
df = conversor_nulos(df) 

print("\n=== CONTAGEM DE VALORES NULOS POR COLUNA ===")
print(df.isnull().sum())

print("\n=== REMOÇÃO DE COLUNAS COM TODOS OS VALORES NULOS ===")
df = remover_colunas_vazias(df)

print("\n=== CONVERSÃO DA COLUNA DATA DE STRING PARA DATETIME ===")
df['DATA'] = converter_data(df['DATA'])

print("\n=== REMOÇÃO DE DUPLICATAS ===")
df = remover_duplicatas(df)

print("\n=== PRIMEIRAS 5 LINHAS APÓS A LIMPEZA ===")
print(df.head(5))

# =========================================================================
# PARTE 3: Estatísticas Descritivas coluna número de filhos
# =========================================================================
print("\n=== ESTATÍSTICAS DESCRITIVAS: NÚMERO DE FILHOS (CL_FHL) ===")
desc_col_num_filhos(df)
