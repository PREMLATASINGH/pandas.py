import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Age":[23,21,25,28],
    "Salary":[40000,50000,45000,60000]
}
df=pd.DataFrame(data)
print(df)
df["Bonus"]=df["Salary"]*0.10
print(df)
df["Salary"]=df["Salary"]+5000
print(df)