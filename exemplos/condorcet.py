import os
from itertools import combinations, product

import numpy as np
import pandas as pd


# Leu o arquivo csv
df = pd.read_csv('./condorcet_likert.csv', index_col='alternativas')

alternativas = list(df.index)
criterios = list(df.columns)
# print(alternativas)

alternativas_combinadas = list(combinations(alternativas, 2))

dataframes = {
    criterio: pd.DataFrame(data=0, index=alternativas, columns=alternativas)
    for criterio in criterios
}
for criterio, (alternativaA, alternativaB) in product(criterios,
                                                      alternativas_combinadas):
    if df.at[alternativaA, criterio] > df.at[alternativaB, criterio]:
        dataframes[criterio].at[alternativaA, alternativaB] = +1
        dataframes[criterio].at[alternativaB, alternativaA] = -1

    elif df.at[alternativaA, criterio] < df.at[alternativaB, criterio]:
        dataframes[criterio].at[alternativaA, alternativaB] = -1
        dataframes[criterio].at[alternativaB, alternativaA] = 1

    else:
        dataframes[criterio].at[alternativaA, alternativaB] = 0

print('')

matriz_somatorio = pd.DataFrame(sum([i.values for i in dataframes.values()]),
                                index=alternativas,
                                columns=alternativas)
os.system('clear')
print(matriz_somatorio)
print('\n\n')

def transformacao(valor):
    if valor >= 1:
        return 1
    elif valor <= -1:
        return -1
    else:
        return 0


matriz_decisao = matriz_somatorio.applymap(transformacao)

transposta = matriz_decisao.T
transposta = transposta.values * -1
valores_decisao = matriz_decisao.values + transposta

matriz_final = pd.DataFrame(valores_decisao,
                            index=alternativas,
                            columns=alternativas)
os.system('clear')
print('\n\n *** MATRIZ DE DECISÃO *** \n')
print(matriz_decisao)
matriz_condorcet = matriz_decisao.replace(-1, 0)
matriz_condorcet['Pontuação'] = matriz_condorcet.apply(np.sum, axis='columns')

os.system('clear')
matriz_condorcet

matriz_copeland = matriz_decisao.copy()
matriz_copeland['pontuação'] = matriz_condorcet.apply(np.sum, axis='columns')
matriz_copeland
