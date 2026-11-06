import pandas as pd

pd.set_option('display.max_columns', None)

print("Reading transaction data...")

df = pd.read_csv("Data/Transactions.csv")

print("\nOriginal Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["amount"] = df["amount"].fillna(df["amount"].mean())

print("\nCleaned Data:")
print(df)

df.to_csv("Data/cleaned_transactions.csv", index=False)

print("\nCleaned file saved successfully!")