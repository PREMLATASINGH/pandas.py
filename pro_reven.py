import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('Revenue-Report.csv')
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.isnull().sum())
total_sales = df['Sales Rep'].sum()
print("Total Sales:", total_sales)