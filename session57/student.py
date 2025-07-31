import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create a simple dataset of student performance
# We'll create a dictionary and then convert it to a pandas DataFrame.
data = {
    'Math_Score': [85, 92, 78, 65, 88, 72, 95, 68, 75, 81],
    'Science_Score': [90, 88, 75, 68, 92, 70, 98, 70, 78, 85],
    'Hours_Studied': [4, 5, 3, 2, 4.5, 2.5, 6, 2.2, 3.5, 4],
    'Attendance_Pct': [95, 98, 90, 80, 92, 85, 100, 82, 88, 91],
    'Sleep_Hours': [7, 7.5, 6, 8, 7, 6.5, 8, 5.5, 7, 7.5]
}

df = pd.DataFrame(data)

# 2. Calculate the correlation matrix
# The .corr() method calculates the relationship between each numerical column.
# A value of 1 means a perfect positive correlation.
# A value of -1 means a perfect negative correlation.
# A value of 0 means no correlation.
correlation_matrix = df.corr()

# 3. Create the heatmap
# We use seaborn's heatmap function to visualize the correlation matrix.
plt.figure(figsize=(10, 8)) # Set the size of the figure for better readability

sns.heatmap(
    correlation_matrix, 
    annot=True,        # This shows the correlation values on the heatmap
    cmap='coolwarm',   # This is the color scheme (cool for negative, warm for positive)
    fmt=".2f",         # Format the numbers to two decimal places
    linewidths=.5      # Add lines between the cells
)

# Add a title to the plot
plt.title('Correlation Heatmap of Student Performance Factors', fontsize=16)

# Display the plot
plt.show()

# How to interpret this heatmap:
# - Look for strong red colors: This indicates a strong positive correlation.
#   For example, 'Hours_Studied' has a very strong positive correlation with both
#   'Math_Score' (0.97) and 'Science_Score' (0.96), which makes sense.
# - Look for strong blue colors: This would indicate a strong negative correlation.
#   In this dataset, there are no strong negative correlations.
# - Look for light colors (close to white): This indicates a weak or no correlation.
#   For example, 'Sleep_Hours' has a very weak correlation with most other factors.
