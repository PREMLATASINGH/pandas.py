import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('wine_data.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.corr())
print(df.isnull().sum())
pd.plotting.scatter_matrix(df, figsize=(10, 10))
plt.show()

