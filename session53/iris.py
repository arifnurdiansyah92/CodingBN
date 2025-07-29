import pandas as pd
import numpy as np
from scipy import stats

# 1. Data Collection (The Shopping Trip)
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
data = pd.read_csv(url)

# 2. Kitchen Prep: Remove Duplicates
data = data.drop_duplicates()

# 3. Kitchen Prep: Handle Outliers (using a statistical method)
numeric_data = data.select_dtypes(include=[np.number])
z_scores = np.abs(stats.zscore(numeric_data))
data = data[(z_scores < 3).all(axis=1)]

# 4. Kitchen Prep: Normalize Data (Cut to the same size)
numeric_cols = data.select_dtypes(include=[np.number]).columns
data[numeric_cols] = (data[numeric_cols] - data[numeric_cols].min()) / (data[numeric_cols].max() - data[numeric_cols].min())

print("Clean and Normalized Data:")
print(data.head())