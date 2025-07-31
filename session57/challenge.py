import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
tips = sns.load_dataset('tips')

# Check data types and for any missing values
print("--- Data Info ---")
tips.info()

print("\n--- Descriptive Statistics ---")
# Get summary statistics for numerical columns
print(tips.describe())

# Set up a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot histogram for total_bill
sns.histplot(tips['total_bill'], kde=True, ax=axes[0])
axes[0].set_title('Distribution of Total Bill')

# Plot histogram for tip
sns.histplot(tips['tip'], kde=True, ax=axes[1])
axes[1].set_title('Distribution of Tips')

plt.show()

# Create a scatter plot with a regression line to show the trend
sns.lmplot(x='total_bill', y='tip', data=tips, height=6)
plt.title('Relationship Between Total Bill and Tip')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='time', y='tip', data=tips)
plt.title('Tips by Meal Time (Lunch vs. Dinner)')
plt.xlabel('Meal Time')
plt.ylabel('Tip ($)')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='tip', data=tips, order=['Thur', 'Fri', 'Sat', 'Sun'])
plt.title('Tips by Day of the Week')
plt.xlabel('Day')
plt.ylabel('Tip ($)')
plt.show()

# Use a scatter plot and hue to see the relationship with total_bill included
sns.lmplot(x='total_bill', y='tip', hue='smoker', data=tips, height=6)
plt.title('Tipping by Smokers vs. Non-Smokers')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='size', y='tip', data=tips)
plt.title('Tips by Party Size')
plt.xlabel('Number of People in Group')
plt.ylabel('Tip ($)')
plt.show()
