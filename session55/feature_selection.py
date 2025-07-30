import pandas as pd

# Our available ingredients (all columns)
data = {
    'product_id': [101, 102, 103, 104],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'units_sold': [35, 150, 80, 45],
    'warehouse_location': ['North', 'South', 'North', 'East']
}
df = pd.DataFrame(data)

print("--- All Available Features ---")
print(df)

# The Chef's Decision: We only need 'product_name' and 'units_sold' for our sales report.
# The other columns are irrelevant for this specific recipe.
features_to_select = ['product_name', 'units_sold']

# Create a new DataFrame with ONLY the selected features
df_selected = df[features_to_select]

print("\n--- Only The Selected, Important Features ---")
print(df_selected)
