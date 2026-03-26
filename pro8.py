import numpy as np
import pandas as pd
df=pd.read_csv('netflix_titles.csv')
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.fillna(0))