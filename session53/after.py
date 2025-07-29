import pandas as pd

# --- Analysis on Cleaned, Preprocessed Data ---

# Step 1: Read the same CSV file with errors
try:
    df_clean = pd.read_csv('sales.csv')
except FileNotFoundError:
    print("Error: 'sales_data_large_errors.csv' not found.")
    exit()

# --- Step 2: Preprocessing (The "Kitchen Prep") ---
print("--- Starting Data Cleaning Process ---")

# Task 1: Remove Duplicate Rows
# We count the rows before and after to show the effect.
rows_before = len(df_clean)
df_clean = df_clean.drop_duplicates()
rows_after = len(df_clean)
print(f"Removed {rows_before - rows_after} duplicate rows.")

# Task 2: Handle Outliers
# We identify the outlier (any sale over 1000 is suspicious) and remove it.
# This is a simple filtering method for obvious errors.
outlier = df_clean[df_clean['unit_sold'] > 1000]
print(f"Found and removing outlier sale of {outlier['unit_sold'].values[0]} units for {outlier['product'].values[0]}.")
df_clean = df_clean[df_clean['unit_sold'] < 1000]


# --- Step 3: Perform the analysis on the clean data ---
print("\n--- Calculating Total Sales (After Cleaning) ---")
# Now that the data is clean, the result will reflect the true story.
correct_sales_total = df_clean.groupby('product')['unit_sold'].sum()
sorted = correct_sales_total.sort_index(ascending=False)

print("Corrected Results:")
print(sorted)

print(f"\nConclusion from the clean data: {sorted[0]} is actually outperforming {sorted[1]}.")
print("(This is the TRUE story hidden in the data!)")

