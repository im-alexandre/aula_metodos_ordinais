import os
import numpy as np
import pandas as pd

os.system('clear')

df = pd.read_csv('borda_cardinal.csv', index_col='alternativas')

print('\n***Dados de entrada***\n', df, '\n')

df['criterio1'].rank()
# df['criterio1'].rank(ascending=False)

def ranking(coluna):
    return coluna.rank(ascending=False)

print('')

os.system('clear')
df.apply(ranking, axis='index')

matriz_decisao = df.apply(ranking, axis='index')

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html

os.system('clear')
matriz_decisao.apply(np.sum, axis='columns')

matriz_decisao['soma'] = matriz_decisao.apply(np.sum, axis='columns')
matriz_decisao.sort_values(by='soma', inplace=True)

os.system('clear')
matriz_decisao
