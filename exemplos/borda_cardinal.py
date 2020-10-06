import numpy as np
import pandas as pd
import pyperclip

df = pd.read_csv('borda_cardinal.csv', index_col='alternativas')
pyperclip.copy(df.to_latex())
print('***Dados de entrada***\n', df, '\n')

colunas = list()
for criterio in df.columns:
    ordenado = df[criterio].sort_values(ascending=False)
    ordenado = ordenado.reset_index()
    ordenado[criterio + '_ordem'] = ordenado.index
    ordenado.set_index('alternativas', inplace=True)
    colunas.append(ordenado[criterio + '_ordem'])

matriz_decisao = pd.concat(colunas, axis=1).applymap(lambda x: x + 1)
matriz_decisao.columns = df.columns
print(50 * '*', '\n')
print(df)
print('\n')
print(matriz_decisao)

pyperclip.copy(matriz_decisao.to_latex())
matriz_decisao['soma'] = matriz_decisao.apply(np.sum, axis=1)
matriz_decisao = matriz_decisao.sort_values(by='soma')
pyperclip.copy(matriz_decisao.to_latex())
print('\n*** Matriz de decisão *** \n', matriz_decisao)
