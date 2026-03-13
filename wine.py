import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('wine_data.csv')
print(df.head())
print(df.info())
print(df.describe())
# Visualize the distribution of wine quality
plt.figure(figsize=(10, 6))
plt.hist(df['quality'], bins=10, edgecolor='black')
plt.title('Distribution of Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Frequency')
plt.show()
