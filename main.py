from idlelib import history

import pandas as pd

fear_greed_data = pd.read_csv(r"datasets/fear_greed_index.csv")
historical_data = pd.read_csv(r"datasets/historical_data.csv")


# Part A -->  Step 1 : Data Cleaning

print("--- Fear/Greed dataset ---\n")

print(f"No of Rows : {fear_greed_data.shape[0]}, No of Columns : {fear_greed_data.shape[1]}")
print(f"Columns : {list(fear_greed_data.columns)}")
print(f"Missing values : \n{fear_greed_data.isnull().sum()}")
print(f"Duplicates : {fear_greed_data.duplicated().sum()}")
print(fear_greed_data.head())

print("\n\n")
print("--- Historical dataset ---\n")
print(f"No of Rows : {historical_data.shape[0]}, No of columns : {historical_data.shape[1]}")
print(f"Columns : {list(historical_data.columns)}")
print(f"Missing values : \n{historical_data.isnull().sum()}")
print(f"Duplicates : {historical_data.duplicated().sum()}")
print(historical_data.head())
