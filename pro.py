import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df={'student':['Alice','Bob','Charlie','David','Eve'],
    'age':[20,21,19,22,20],
    'grade':[85,90,78,92,88],
    'city':['New York','Los Angeles','Chicago','Houston','Phoenix']}
df=pd.DataFrame(df)
print(df)