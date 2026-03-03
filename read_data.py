import pandas as pd
from io import StringIO
Data='{"employee_name":"prema","email":"singh@gmail.com","job_profile":[{"title1":"team_lead","title2":"data_analyst"}]}'
df=pd.read_json(StringIO(Data))
print(df)
print(type(df))
df1=df.to_json(orient='index')
print(df1)
print(type(df1))
print(df['employee_name'])
print(df['email'])
print(df['job_profile'])
print(df['job_profile'][0])
print(df['job_profile'][0]['title1'])