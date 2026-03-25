import numpy as np
import pandas as pd
df=pd.read_csv('train.csv')
print(df.head())
print(df)
print(df.tail())
print(df.describe())
print(df.isnull().sum())