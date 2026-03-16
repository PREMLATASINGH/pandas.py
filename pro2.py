import pandas as pd
import matplotlib.pyplot as plt
df={'product':['freeze','vegetable','dairy','meat','grain','bakery','fruit','snacks','condiments','beverages','other'],
    'sales':[100,150,200,250,300,350,400,450,500,550,600],
    'profit':[20,30,40,50,60,70,80,90,100,110,120],
    'category':['food','food','food','food','food','food','food','food','food','beverage','other']}
df=pd.DataFrame(df)
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())