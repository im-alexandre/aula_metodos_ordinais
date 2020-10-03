import numpy as np
import pandas as pd

df = pd.read_csv('borda_cardinal.csv', index_col='alternativas')
print('***Dados de entrada***\n', df, '\n')

colunas = list()
for criterio in df.columns:
    ordenado = df[criterio].sort_values()
    ordenado = ordenado.reset_index()
    ordenado[criterio + '_ordem'] = ordenado.index
    ordenado.set_index('alternativas', inplace=True)
    colunas.append(ordenado[criterio + '_ordem'])

matriz_decisao = pd.concat(colunas, axis=1).applymap(lambda x: x + 1)

matriz_decisao['soma'] = matriz_decisao.apply(np.sum, axis=1)
print('\n*** Matriz de decisão *** \n', matriz_decisao)
