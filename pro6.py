import pandas as pd 
import numpy as np
data={
    "product":["laptop","phone","chair","table","laptop"],
    "category":["tech","tech","furniture","furniture","tech"],
    "quantity":[1,2,3,1,2],
    "price":[1200,800,150,300,1200],
    "cost":[900,500,100,200,900],
    "region":["east","west","east","south","west"],
    "date":['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-01']

}
df=pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Data Cleaning
print("\nData Cleaning:")
print("Null values per column:")
print(df.isnull().sum())

# Check for duplicates
print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")
if df.duplicated().sum() > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")

# Strip whitespace from string columns
string_cols = df.select_dtypes(include=['object']).columns
for col in string_cols:
    df[col] = df[col].str.strip()

# Ensure categories are consistent
df['category'] = df['category'].str.lower()

print("\nData types:")
print(df.dtypes)

df["date"]=pd.to_datetime(df["date"])
print("date:",df["date"])
df["total_sales"]=np.multiply(df["quantity"],df["price"])
df['profit']=np.multiply(df["quantity"],(df["price"]-df['cost']))
print(df)
print("total profit:", df["profit"].sum())
