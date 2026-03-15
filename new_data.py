import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data
def preprocess_data(data):
    # Example preprocessing steps
    data = data.dropna()  # Remove missing values
    data['date'] = pd.to_datetime(data['date'])  # Convert date column to datetime
    return data
def main():
    file_path = r"C:\Users\Prema\Downloads\All+Data+&+Resources (1)\All Data & Resources\Day 1\Data\sales2017_raw.csv"  # Path to your data file
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    print(processed_data.head())  # Display the first few rows of the processed data
df=pd.read_csv('wine_data.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.corr())
print(df.isnull().sum())
pd.plotting.scatter_matrix(df, figsize=(10, 10))
plt.show()
sns.heatmap(df.corr(), annot=True, cmap='coolwarm',)
plt.show()

