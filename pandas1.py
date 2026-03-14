import pandas as pd
df = pd.read_csv('wine_data.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.corr())
print(df.isnull().sum())
print(df['quality'].value_counts())