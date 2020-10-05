from itertools import combinations, product

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import pyperclip

df = pd.read_csv('./condorcet_likert.csv', index_col='alternativas')
print('*** Dados de entrada ***\n')
print(df)
pyperclip.copy(df.to_latex())

alternativas = list(df.index)
criterios = list(df.columns)
# print(alternativas)

alternativas_combinadas = list(combinations(alternativas, 2))
# print(list(alternativas_combinadas))

dataframes = {
    criterio: pd.DataFrame(data=0, index=alternativas, columns=alternativas)
    for criterio in criterios
}
for criterio, (alternativaA, alternativaB) in product(criterios,
                                                      alternativas_combinadas):
    if df.at[alternativaA, criterio] > df.at[alternativaB, criterio]:
        dataframes[criterio].at[alternativaA, alternativaB] = +1
    elif df.at[alternativaA, criterio] < df.at[alternativaB, criterio]:
        dataframes[criterio].at[alternativaA, alternativaB] = -1
    else:
        dataframes[criterio].at[alternativaA, alternativaB] = 0

with open('condorcet.tex', 'w') as tex:
    for criterio, dataframe in dataframes.items():
        tex.write(criterio)
        tex.write(dataframe.to_latex())

print('')

matriz_decisao = pd.DataFrame(sum([i.values for i in dataframes.values()]),
                              index=alternativas,
                              columns=alternativas)
pyperclip.copy(matriz_decisao.to_latex())


def transformacao(valor):
    if valor >= 1:
        return 1
    elif valor <= -1:
        return -1
    else:
        return 0


print('\n\n *** MATRIZ DE DECISÃO *** \n')
matriz_decisao = matriz_decisao.applymap(transformacao)
print(matriz_decisao)
transposta = matriz_decisao.T
transposta = transposta.values * -1
valores_decisao = matriz_decisao.values + transposta

matriz_final = pd.DataFrame(valores_decisao,
                            index=alternativas,
                            columns=alternativas)
G = nx.DiGraph()
G.add_nodes_from(alternativas)

for i, j in list(product(alternativas, alternativas)):
    if matriz_final.at[i, j] == 1:
        G.add_weighted_edges_from([
            (i, j, 1),
        ])

nx.draw(G, node_size=6000, with_labels=True, node_shape='s')
plt.show()
