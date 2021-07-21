import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [5, 5, 5]})

print(df)

df.to_csv('results/df1.csv')
