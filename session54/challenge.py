import pandas as pd
import numpy as np

# --- 1. Data Collection ---
# Read the data from the URL into a DataFrame called 'df'.
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

print("--- Initial Investigation ---")
# Print the shape of the original DataFrame
print(f"Original shape: {df.shape}")

# Check for duplicate rows
duplicate_count = df.duplicated().sum()
print(f"Found {duplicate_count} duplicate rows.")

# Use df.info() to get a summary of the data. Pay attention to the 'Non-Null Count'.
print("\nOriginal Data Info:")
df.info()


# --- 2. Preprocessing (The First Wave of Cleaning) ---
print("\n--- Cleaning the Data... ---")

# Task 1 - Remove Duplicate Rows
# Use the .drop_duplicates() method. Use inplace=True to modify the DataFrame directly.
df.drop_duplicates(inplace=True)
print("Duplicate rows have been removed.")

# Task 2 - Remove Irrelevant Columns
# Create a list of columns you want to remove.
columns_to_drop = ['Ticket', 'Cabin', 'PassengerId']
# Use the .drop() method to remove the columns. Remember axis=1.
df = df.drop(columns=columns_to_drop, axis=1)
print("Irrelevant columns ('Ticket', 'Cabin', 'PassengerId') have been removed.")


# --- 3. Final Report ---
print("\n--- Final Report ---")
# Print the shape of the cleaned DataFrame to see the changes.
print(f"Cleaned shape: {df.shape}")

print("\n--- Final Check ---")
# Run df.info() again.
# Are the duplicate rows gone? Are the specified columns gone?
print("Cleaned Data Info:")
df.info()

print("\n--- Mission Complete! The data is now leaner and ready for the next step. ---")
