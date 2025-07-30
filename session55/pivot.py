import pandas as pd

# Using the same sales data from the previous slide
data = {
    'Store': ['A', 'A', 'B', 'B', 'A'],
    'Product': ['Apples', 'Oranges', 'Apples', 'Oranges', 'Apples'],
    'Sales': [100, 150, 200, 250, 120]
}
df = pd.DataFrame(data)

# A pivot table is the perfect tool for this question
# It reshapes the data to show Stores as rows and Products as columns
sales_pivot = df.pivot_table(index='Store', columns='Product', values='Sales', aggfunc='sum')

print(sales_pivot)