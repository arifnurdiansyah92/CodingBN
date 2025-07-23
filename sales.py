import pandas as pd
import numpy as np

# Step 1: Create the Raw Data
sales_data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    'Units Sold': [35, 150, 80, 45, 200],
    'Price Per Unit': [1200, 25, 75, 300, 50]
}

# Step 2: Build a Pandas DataFrame
print("--- Initial DataFrame ---")
df = pd.DataFrame(sales_data)
print(df)

# Step 3: Calculate with NumPy
# Extract columns as NumPy arrays for fast calculations
units_sold_array = np.array(df['Units Sold'])
price_array = np.array(df['Price Per Unit'])

# Perform element-wise multiplication to get revenue for each product
total_revenue_array = units_sold_array * price_array

# Step 4: Update the DataFrame
# Add the new revenue data as a column in our DataFrame
df['Total Revenue'] = total_revenue_array
print("\n--- DataFrame with Total Revenue ---")
print(df)

# Step 5: Analyze the Data
print("\n--- Sales Analysis ---")

# Use Pandas to calculate the grand total revenue
grand_total_revenue = df['Total Revenue'].sum()
print(f"Grand Total Revenue: ${grand_total_revenue:,.2f}")

# Find the best-selling product by revenue
best_product = df[df['Total Revenue'] == df['Total Revenue'].max()]
print("\nBest Performing Product by Revenue:")
print(best_product)