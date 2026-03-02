import pandas as pd
from io import StringIO
Data='{"employee_name":"prema","email":"singh@gmail.com","job_profile":[{"title1":"team_lead","title2":"data_analyst"}]}'
df=pd.read_json(StringIO(Data))
print(df)
print(type(df))