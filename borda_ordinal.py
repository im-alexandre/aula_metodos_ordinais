import numpy as np
import pandas as pd

df = pd.read_csv('./borda_ordinal.csv', index_col='alternativas')

df['soma'] = df.apply(np.sum, axis=1)
df = df.sort_values(by='soma')

print(df)
print(f'A melhor alternativa é {df.index[0]}')
