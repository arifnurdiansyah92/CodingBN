import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Part 1: Data Cleaning & Preparation ---

# Step 1: Load Data and Initial Inspection
print("--- Initial Data Loading and Inspection ---")
titanic = sns.load_dataset('titanic')
print("Initial missing values:")
print(titanic.isnull().sum())
print("-" * 30)

# Step 2: Handle Missing 'age'
# Calculate the median age
median_age = titanic['age'].median()
# Fill missing age values with the median
titanic['age'].fillna(median_age, inplace=True)
print(f"Missing 'age' values filled with median age: {median_age:.2f}")

# Step 3: Handle Missing 'deck'
# Drop the 'deck' column as it has too many missing values
titanic.drop('deck', axis=1, inplace=True)
print("'deck' column dropped.")

# Step 4: Handle Missing 'embark_town'
# Find the most common embarkation town (the mode)
mode_embark_town = titanic['embark_town'].mode()[0]
# Fill missing values with the mode
titanic['embark_town'].fillna(mode_embark_town, inplace=True)
print(f"Missing 'embark_town' values filled with mode: {mode_embark_town}")

# Step 5: Feature Engineering - Create 'FamilySize'
# Create the 'FamilySize' column
titanic['FamilySize'] = titanic['sibsp'] + titanic['parch'] + 1
print("'FamilySize' column created.")

# Final check for missing values to confirm cleaning is complete
print("\nFinal missing values check after cleaning:")
print(titanic.isnull().sum())
print("-" * 30)


# --- Part 2: Open-Ended Visual Exploration ---

print("\n--- Starting Visual Exploration ---")

# Visualization 1: Survival by Gender
# This chart shows the absolute number of male and female passengers who survived and who did not.
plt.figure(figsize=(8, 6))
sns.countplot(x='sex', hue='survived', data=titanic)
plt.title('Survival Count by Gender', fontsize=16)
plt.xlabel('Gender')
plt.ylabel('Number of Passengers')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()
# Insight: A vastly larger number of women survived compared to men, who had a very high casualty rate.


# Visualization 2: Survival by Passenger Class
# This plot compares the proportion of survivors in each passenger class.
plt.figure(figsize=(10, 7))
sns.countplot(x='pclass', hue='survived', data=titanic)
plt.title('Survival Count by Passenger Class', fontsize=16)
plt.xlabel('Passenger Class')
plt.ylabel('Number of Passengers')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()
# Insight: First-class passengers had a much higher survival rate than third-class passengers,
# where the majority did not survive.


# Visualization 3: Age Distribution of Survivors vs. Non-Survivors
# This plot overlays the age distributions for those who survived and those who did not.
plt.figure(figsize=(12, 7))
sns.kdeplot(data=titanic, x='age', hue='survived', fill=True, common_norm=False)
plt.title('Age Distribution by Survival Status', fontsize=16)
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend(title='Survived', labels=['Yes', 'No'])
plt.show()
# Insight: Children (passengers with a low age) had a noticeably higher survival peak compared to other age groups.
# For adults, the survival rate was lower, especially for those in the young adult range (20-40).


# Visualization 4: Survival by Family Size
# This plot explores how the size of a passenger's family related to their survival.
plt.figure(figsize=(12, 7))
sns.countplot(x='FamilySize', hue='survived', data=titanic)
plt.title('Survival Count by Family Size', fontsize=16)
plt.xlabel('Family Size')
plt.ylabel('Number of Passengers')
plt.legend(title='Survived', labels=['No', 'Yes'])
plt.show()
# Insight: Passengers traveling alone (FamilySize of 1) had a very low survival rate.
# Small families (2-4 members) had a better chance of survival than those who were alone or in very large families.
