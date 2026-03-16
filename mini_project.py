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
average_sales = df['Sales'].mean()
print("Average Sales:", average_sales)
df['month'] = df['Date'].dt.month
monthly_sales = df.groupby('month')['Sales'].sum()
print(monthly_sales)