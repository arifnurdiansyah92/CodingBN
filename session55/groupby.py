import pandas as pd

# Our raw sales data
data = {
    'Store': ['A', 'A', 'B', 'B', 'A'],
    'Product': ['Apples', 'Oranges', 'Apples', 'Oranges', 'Apples'],
    'Sales': [100, 150, 200, 250, 120]
}
df = pd.DataFrame(data)

# Group by 'Store' and calculate the sum and mean of 'Sales' for each store
store_summary = df.groupby('Store')['Sales'].agg(['sum', 'mean'])

print(store_summary)