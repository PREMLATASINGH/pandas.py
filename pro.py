import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df={'student':['Alice','Bob','Charlie','David','Eve'],
    'age':[20,21,19,22,20],
    'grade':[85,90,78,92,88],
    'city':['New York','Los Angeles','Chicago','Houston','Phoenix']}
df=pd.DataFrame(df)
print(df)
plt.hist(df['age'], bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
sns.barplot(x='student', y='grade', data=df)
plt.title('Student Grades')
plt.xlabel('Student')
plt.ylabel('Grade')
plt.show()
sns.scatterplot(x='age', y='grade', data=df)
plt.title('Age vs Grade')
plt.xlabel('Age')
plt.ylabel('Grade')
plt.show()
