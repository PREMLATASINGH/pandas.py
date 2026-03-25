import pandas as pd 
import numpy as np
data={
    "product":["laptop","phone","chair","table","laptop"],
    "category":["tech","tech","fruniture","furniture","tech"],
    "quantity":[1,2,3,1,2],
    "price":[1200,800,150,300,1200],
    "cost":[900,500,100,200,900],
    "region":["east","west","east","south","west"],
    "date":['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-01']

}
df=pd.DataFrame(data)
print(df)
print(df.isnull().sum())
df["date"]=pd.to_datetime(df["date"])