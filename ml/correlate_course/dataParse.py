import pandas as pd
import numpy as np

df = pd.read_excel('ml\is_valid\output.xlsx')

del df['Unnamed: 0']
df = np.array(df)

df_1 = pd.DataFrame(columns=['href', 'data', 'is_valid'], data=[i for i in df if i[-1]==1])
df_1.to_excel('ml/aaa/output.xlsx')


