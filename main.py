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
from agrupamentos import *

# Carregamento da base de dados
df = pd.read_csv('BaseVarejo.csv', sep=';')

# Chamada da função explorar para impressão das imformações do Data Frame
explorar(df)

# =========================================================================
# PARTE 2 e 3: Transformação de Strings, Datetime e remoção de colunas vazias
# =========================================================================

df = remover_espacos(df) # Chamando a função remover_espacos para tratar os espaços das colunas strings

# Conversão de células preenchidas com NULL, N/A ou vazias para np.nan para que possam ser detectadas pelo método isnull()
df = conversor_nulos(df) 

print("\n=== CONTAGEM DE VALORES NULOS POR COLUNA ===")
print(df.isnull().sum())


# Conversão de valores nulos nas colunas de categoria produto e nome produto para "sem categoria" e "sem nome" respectivamente.
print("\n=== TRATAMENTO DE VALORES NULOS ===")
df['PR_CAT'] = df['PR_CAT'].apply(verificar_nulo, args=('PR_CAT',))
df['PR_NOME'] = df['PR_NOME'].apply(verificar_nulo, args=('PR_NOME',))
    
print(f"Linhas preenchidas com 'Sem Categoria' e 'Sem Nome': {(df['PR_CAT'] == 'Sem Categoria').sum()}")

# Função para remover valores nulos
df = remover_colunas_vazias(df)

print("\n=== CONTAGEM DE VALORES NULOS POR COLUNA ===")
df = df.reset_index(drop=True) # reindexação das linhas após limpeza
print(df.isnull().sum())


# Função para converter a data de string para datetime
df['DATA'] = converter_data(df['DATA'])

# Função para remover linhas que possuem todos os valores iguais, deixando apenas a primeira
df = remover_duplicatas(df)

print("\n=== NÚMERO DE REGISTROS E COLUNAS APÓS LIMPEZA ===")
print(f"Tamanho: {df.shape[0]} linhas e {df.shape[1]} colunas")

# =========================================================================
# PARTE 4: Estatísticas Descritivas coluna número de filhos
# =========================================================================
desc_col_num_filhos(df)

# =========================================================================
# PARTE 5: Exploração de agrupamentos
# =========================================================================

# Função para retornar o número de compras por gênero
num_compras_genero(df)

# Função para retornar o número de compras por quantidade de filho
num_compras_filho(df)

# Função para retornar o número de vendas por categoria e o produto mais vendido 
cat_pr_vendas(df)

# =========================================================================
# Criação do arquivo novo após limpeza dos dados
# =========================================================================
df.to_csv('df_limpo.csv', index=False)

print("\n=== CONCLUSÕES ===")
print("1. A base continha 4 colunas completamente vazias que foram removidas. 3650 linhas estavam sem os valores de categorias e nome do produto preenchidas, poderia ser feito um preenchimento correto já que possuiam o valor de ID produto, mas foram preenchidas com 'Sem Categoria' e 'Sem Nome' respectivamente")
print("2. Linhas duplicadas foram removidas, porém pode haver casos onde o mesmo produto foi comprado mais de uma vez na mesma compra. Sem uma coluna de hora ou informação do sistema gerador, optou-se pela remoção.")
print("3. Existem produtos com o mesmo nome mas IDs diferentes, o que pode indicar inconsistência no cadastro. Não foi feito tratamento.")
print("4. Clientes com 3 filhos são os que mais realizam compras (764 por cliente).")
print("5. O gênero com mais compras foi o Feminino, com 382427 vs 351020 masculino")
print("6. A categoria de produtros mais comprada foi a de Alimentos e o produto mais vendido foi Presunto Cozido com 12719 vendas.")