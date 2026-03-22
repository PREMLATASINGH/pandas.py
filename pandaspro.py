import pandas as pd
import matplotlib.pyplot as plt
data={
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve','Frank','Grace','Heidi','Ivan','Judy'],
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.info())
print(df.describe())
print(df.tail())
pd.plotting.scatter_matrix(df, figsize=(10, 10))
plt.show()
plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
df1=df[df['Age']>40]
print(df1)
new_row = pd.DataFrame([{'Name':'Karl','Age':75,'City':'Austin'}])
df1 = pd.concat([df1, new_row], ignore_index=True)
print(df1)
removed_row = df1[df1['Name'] == 'David']
df1 = df1[df1['Name'] != 'David']
print(df1)
print(removed_row)
print(df1.head())
print(df.apply(lambda x: x['Age']*2 if x['Age'] > 40 else x['Age'], axis=1))
print(type(df))



