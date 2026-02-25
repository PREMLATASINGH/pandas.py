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