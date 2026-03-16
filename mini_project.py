import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
print(df.head())
print(df)
print(df.info())
print(df.describe())
print (df.isnull().sum())
df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'])
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)