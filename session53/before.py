import pandas as pd

# --- Analysis on Raw, Messy Data ---

# Step 1: Read the CSV file with errors
# This file contains duplicate entries and a massive outlier.
try:
    df_raw = pd.read_csv('sales.csv')
    print("--- Raw Data Preview (First 5 Rows) ---")
    print(df_raw.head())
except FileNotFoundError:
    print("Error: 'sales.csv' not found.")
    print("Please make sure the CSV file is in the same folder as your script.")
    exit()

# Step 2: Perform the analysis directly on the messy data
print("\n--- Calculating Total Sales (Before Cleaning) ---")
# We group by product and sum the units sold.
# The calculation will be heavily skewed by the outlier and duplicates.
biased_sales_total = df_raw.groupby('product')['unit_sold'].sum()

print("Biased Results:")
print(biased_sales_total)

print("\nConclusion from this data: Laptop A is outperforming Laptop B by a massive margin!")
print("(This conclusion is WRONG due to bad data.)")

