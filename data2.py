import pandas as pd
data={
    "Name":["A","B","C","D"],
    "Department":["IT","HR","IT","FINANCE"],
    "Salary":[40000,50000,45000,60000],
    "Experience":[2,5,3,7]
  
}
df=pd.DataFrame(data)
print(df)
df["Salary"]=df["Salary"].apply(lambda x:x*1.10)
print(df)
df["Category"]=df["Salary"].apply(lambda x:"high"if x>50000 else"low")
print(df)
pd.pivot_table(df,values="Salary",index="Department",aggfunc=["mean","sum"])
print(df)
df1=df["Department"]=df["Department"].replace("IT","TECH")
print(df1)