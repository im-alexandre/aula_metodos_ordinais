import numpy as np
import pandas as pd
import pyperclip

df = pd.read_csv('borda_cardinal.csv', index_col='alternativas')
pyperclip.copy(df.to_latex())
print('***Dados de entrada***\n', df, '\n')

colunas = list()
for criterio in df.columns:
    ordenado = df[criterio].sort_values()
    ordenado = ordenado.reset_index()
    ordenado[criterio + '_ordem'] = ordenado.index
    ordenado.set_index('alternativas', inplace=True)
    colunas.append(ordenado[criterio + '_ordem'])

matriz_decisao = pd.concat(colunas, axis=1).applymap(lambda x: x + 1)

pyperclip.copy(matriz_decisao.to_latex())
matriz_decisao['soma'] = matriz_decisao.apply(np.sum, axis=1)
pyperclip.copy(matriz_decisao.to_latex())
print('\n*** Matriz de decisão *** \n', matriz_decisao)
