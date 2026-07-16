import pandas as pd

fear_greed_data = pd.read_csv(r"datasets/fear_greed_index.csv")
historical_data = pd.read_csv(r"datasets/historical_data.csv")


# Part A -->  Step 1 : Data Cleaning

print("--- Fear/Greed dataset ---\n")

print(f"No of Rows : {fear_greed_data.shape[0]}, No of Columns : {fear_greed_data.shape[1]}")
print(f"Columns : {list(fear_greed_data.columns)}")
print(f"Missing values : \n{fear_greed_data.isnull().sum()}")
print(f"Duplicates : {fear_greed_data.duplicated().sum()}")
print(fear_greed_data.dtypes)
print(fear_greed_data["classification"].unique())
print(fear_greed_data.head())

print("\n\n")
print("--- Historical dataset ---\n")
print(f"No of Rows : {historical_data.shape[0]}, No of columns : {historical_data.shape[1]}")
print(f"Columns : {list(historical_data.columns)}")
print(f"Missing values : \n{historical_data.isnull().sum()}")
print(f"Duplicates : {historical_data.duplicated().sum()}")
print(historical_data.dtypes)
print(fear_greed_data["classification"].unique())
print(historical_data.head())


# ----
# Part A -->  Step 2 : Convert TimeStamp to date
# -----

fear_greed_data['date'] = pd.to_datetime(fear_greed_data['date'])

#convert trader timestamp to date

historical_data['date'] = pd.to_datetime(historical_data['Timestamp'], unit = "ms").dt.date
historical_data['date'] = pd.to_datetime(historical_data['date'])

print("\n\n")
print("--- Fear/Greed Range ---\n")
print(f"From: {fear_greed_data['date'].min()}")
print(f"To:   {fear_greed_data['date'].max()}")
print("\n")
print("\nTrader data date range:\n")
print(f"From: {historical_data['date'].min()}")
print(f"To:   {historical_data['date'].max()}")

# merging data sets

merged = pd.merge(historical_data, fear_greed_data[['date', 'classification']], on = 'date', how = 'inner')
print(f"\nMerged dataset rows : {len(merged)}")
print(f"Columns : {list(merged.columns)}")
print(merged[['date', 'classification', 'Closed PnL']].head(10))

print(merged.columns)


# Part A : Step 3 --> Metrics

# daily PnL per trader
pnl_summary = merged.groupby("classification")["Closed PnL"].agg(
    Total_PnL = "sum",
    Average_PnL = "mean",
    Median_PnL = "median",
    Trade_Count = "count",
)
print("\n\nPnL Summary : \n")
print(pnl_summary)


# Win rate

merged['Win'] = merged['Closed PnL'] > 0
win_rate = merged.groupby("classification")["Win"].mean() * 100
print("\n\nWin Rate :\n")
print(win_rate)

# trades per day

trades_per_day = merged.groupby("date").size().reset_index(name = "trades_per_day")
print("\n\nTrades per Day :\n")
print(trades_per_day)

# long/short ratio

long_short = pd.crosstab(
    merged["classification"],
    merged["Side"]
)
print("\n\nLong Short :\n")
print(long_short)