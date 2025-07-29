import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Sample data with missing values from the PDF
data = {'Age': [25, 30, None, 22, None, 28],
        'Salary': [50000, 60000, 55000, None, 52000, 58000]}
df = pd.DataFrame(data)

# First, we find the missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing Age with the MEDIAN (safer choice)
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# Fill missing Salary with the MEAN
mean_salary = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(mean_salary)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Let's use the cleaned DataFrame from before
# Standardization (Z-Score Glasses)
scaler_std = StandardScaler()
df['Age_standardized'] = scaler_std.fit_transform(df[['Age']])

# Min-Max Scaling (0-to-1 Glasses)
scaler_mm = MinMaxScaler()
df['Age_minmax'] = scaler_mm.fit_transform(df[['Age']])

print(df)
