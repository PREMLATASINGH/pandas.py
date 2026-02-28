import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Department":["IT","HR","IT","FINANCE"],
    "Salary":[40000,50000,45000,60000],
    "Experience":[2,5,3,7]
  
}
df=pd.DataFrame(data)
print(df)
df1=df["Salary"]=df["Salary"].apply(lambda x:x*1.10)
print(df1)