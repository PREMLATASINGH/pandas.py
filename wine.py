import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('wine_data.csv')
print(df.head())
print(df.info())
print(df.describe())
pd.plotting.scatter_matrix(df, figsize=(10, 10))
plt.show()
sns.pairplot(df)
plt.show()
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
