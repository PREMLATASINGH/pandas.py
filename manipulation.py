import pandas as pd
df=pd.read_csv('data.csv')
print(df)
print(df.head(5))
print(df.columns)
print(df.tail(5))
print(df.describe())
print(df.dtypes)