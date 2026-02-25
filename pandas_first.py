import pandas as pd
# Create a sample DataFrame
data = {    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}
df = pd.DataFrame(data)     
# Display the first few rows of the DataFrame
print(df.head())
data1=[1,2,3,4,5]
s=pd.Series(data1)
print(s)
print(type(s))
data2={'a':1,'b':2,'c':3}
s1=pd.Series(data2) 
print(s1)
print(type(s1))
print(s1['a'])
data3=[10,20,30,40,50]
index=['a','b','c','d','e']
s2=pd.Series(data3,index=index)
print(s2)
print(s2['c'])
data4={
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df1=pd.DataFrame(data4)
print(df1)
print(type(df1))
print(df1['Name'])
print(df1[['Name','City']])