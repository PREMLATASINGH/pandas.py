import pandas as pd
import matplotlib.pyplot as plt
df={'product_id':['p001','p002','p003','p004','p005','p006','p007','p008','p009','p010'],
    'product_name':['wireless mouse','laptop','keyboard','monitor','printer','webcam','headphones','speakers','external hard drive','usb flash drive'],
    'category':['electronics','electronics','electronics','electronics','electronics','electronics','electronics','electronics  ','electronics','electronics'],
    'unit':[10,5,15,8,3,12,20,7,4,25],
    'price':[25.99,999.99,49.99,199.99,149.99,89.99,59.99,129.99,79.99,19.99],
    'sales':[259.90,4999.95,749.85,1599.92,449.97,1079.88,1199.80,909.93,319.96,499.75],'units_sold':[10,5,15,8,3,12,20,7,4,25],''
    'region':['North America','Europe','Asia','North America','Europe','Asia','North America','Europe','Asia','North America']}
df=pd.DataFrame(df)
print(df)
print(df.head())
print(df.info())