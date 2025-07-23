# Normal Way to Install is pip install <module>
# Or path/to/python -m pip install <module>

import numpy as np
import pandas as pd

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
# Perform element-wise operations
arr_squared = arr ** 2
print("Squared:", arr_squared)
# Create a 2D array (matrix)
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:\n", matrix)
# Matrix addition
matrix_sum = matrix + 10
print("Matrix + 10:\n", matrix_sum)

# Generate an array of random numbers
random_arr = np.random.rand(5)
print("Random array:", random_arr)
# Calculate mean, median, and standard deviation
mean_val = np.mean(random_arr)
median_val = np.median(random_arr)
std_dev = np.std(random_arr)
print(f"Mean: {mean_val:.2f}, Median: {median_val:.2f}, Std Dev: {std_dev:.2f}")

# A list of numbers
number = [1, 2, 3, 4, 5]
# Loop through the list and perform an operation
for i in range(len(number)):
    number[i] = number[i] * 2  # Double each number
print("Doubled numbers:", number)

# NumPy array operations
numbers_array = np.array([1, 2, 3, 4, 5])
numbers_array = numbers_array * 2  # Double each element in the array
print("Doubled numbers:", numbers_array)

# Data for our table
data = {
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25, 30, 35],
  'City': ['New York', 'Chicago', 'Houston']
}

# Create the DataFrame
df = pd.DataFrame(data)
print(df)

# Display under 30s
under_30s = df[df['Age'] < 30]
print("People under 30:\n", under_30s)