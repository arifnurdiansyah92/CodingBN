import pandas as pd

# Read Dataset
df = pd.read_csv('sales.csv')

# Print Top 5 Data
print(df.head())
sales_laptop_a = df[df['product'] == 'Laptop A']
sales_laptop_b = df[df['product'] == 'Laptop B']