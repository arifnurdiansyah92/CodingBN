import pandas as pd

# Create a sample DataFrame with a missing categorical value
data = {'Passenger': ['Alice', 'Bob', 'Charlie', 'David'],
        'Embarked_City': ['Southampton', 'Cherbourg', None, 'Southampton']}
df = pd.DataFrame(data)

print("--- Data with Missing City ---")
print(df)

# --- Mode Imputation ---
# 1. Find the most common city (the mode)
#    .mode()[0] gets the first mode if there are multiple.
most_common_city = df['Embarked_City'].mode()[0]
print(f"\nThe most common city is: {most_common_city}")

# 2. Fill the missing value with the mode
df['Embarked_City'] = df['Embarked_City'].fillna(most_common_city)

print("\n--- Data After Filling with Mode ---")
print(df)