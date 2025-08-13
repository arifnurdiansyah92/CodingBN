import pandas as pd

df = pd.read_csv('verylarge_transactions_dataset.csv')
print(df.describe())