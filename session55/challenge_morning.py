import pandas as pd
import numpy as np

# --- Data Setup ---
# This block creates the complex customer DataFrame for the challenge.
customer_data = {
    'customer_id': [f'CUST-{1000+i}' for i in range(12)],
    'age': [28, 35, 42, 21, 35, 55, 28, 42, 35, 21, 28, 55],
    'gender': ['Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female'],
    'region': ['Urban', 'Suburban', 'Urban', 'Rural', 'Suburban', 'Urban', 'Suburban', 'Urban', 'Rural', 'Rural', 'Urban', 'Suburban'],
    'signup_date': ['2023-01-15', '2022-05-20', '2023-11-10', '2024-02-01', '2022-05-20', '2021-09-30', '2023-01-15', '2023-11-10', '2024-03-12', '2024-02-01', '2023-08-01', '2021-09-30'],
    'last_purchase_details': [
        '2025-07-10:$85.50', '2025-06-25:$210.00', '2025-07-20:$45.25', '2025-05-01:$15.00',
        '2025-07-22:$350.75', '2025-07-01:$120.00', '2025-07-18:$95.00', '2025-07-21:$60.50',
        '2025-06-10:$25.00', np.nan, '2025-07-15:$40.00', '2025-07-11:$110.25'
    ],
    'total_sessions': [58, 120, 95, 30, 135, 250, 62, 105, 45, 33, 75, 280],
    'last_device_used': ['Mobile', 'Desktop', 'Desktop', 'Mobile', 'Mobile', 'Desktop', 'Tablet', 'Desktop', 'Mobile', 'Mobile', 'Tablet', 'Desktop'],
    'is_premium_member': [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    'satisfaction_score': [4, 5, 3, 4, 5, 5, np.nan, 2, 3, np.nan, 4, 5]
}
customer_df = pd.DataFrame(customer_data)


# --- Task 1: Regional Satisfaction Report (GroupBy) ---
print("--- SOLUTION FOR TASK 1 ---")
# Calculate the median and fill missing values
median_score = customer_df['satisfaction_score'].median()
customer_df['satisfaction_score'].fillna(median_score, inplace=True)

# Group by region and aggregate
regional_report = customer_df.groupby('region').agg(
    average_satisfaction_score=('satisfaction_score', 'mean'),
    total_sessions=('total_sessions', 'sum')
)
print(regional_report)
print("\n" + "="*50 + "\n")


# --- Task 2: Advanced Purchase Analysis (Feature Engineering) ---
print("--- SOLUTION FOR TASK 2 ---")
# Define a function to parse the messy column
def parse_purchase_details(detail_string):
    if pd.isna(detail_string):
        return pd.NA, pd.NA
    
    date_str, amount_str = detail_string.split(':$')
    amount = float(amount_str)
    
    analysis_date = pd.to_datetime('2025-07-30')
    purchase_date = pd.to_datetime(date_str)
    days_since = (analysis_date - purchase_date).days
    
    return days_since, amount

# Apply the function and create two new columns
customer_df[['days_since_last_purchase', 'last_purchase_amount']] = customer_df['last_purchase_details'].apply(
    lambda x: pd.Series(parse_purchase_details(x))
)
print("DataFrame with new engineered features (days_since_last_purchase, last_purchase_amount):")
print(customer_df[['customer_id', 'days_since_last_purchase', 'last_purchase_amount']].head())
print("\n" + "="*50 + "\n")


# --- Task 3: Machine Learning Prep (Feature Selection & Encoding) ---
print("--- SOLUTION FOR TASK 3 ---")
# Feature Selection
features_to_select = [
    'age', 'gender', 'region', 'total_sessions', 'last_device_used', 
    'is_premium_member', 'satisfaction_score', 'days_since_last_purchase', 'last_purchase_amount'
]
model_df = customer_df[features_to_select].copy()

# Handle missing values in the selected data before encoding/modeling
model_df['days_since_last_purchase'].fillna(model_df['days_since_last_purchase'].median(), inplace=True)
model_df['last_purchase_amount'].fillna(model_df['last_purchase_amount'].median(), inplace=True)

# One-Hot Encoding
model_df_encoded = pd.get_dummies(model_df, columns=['gender', 'region', 'last_device_used'], drop_first=True)

print("Encoded DataFrame for Modeling (First 5 Rows):")
print(model_df_encoded.head())
print("\n" + "="*50 + "\n")


# --- Task 4: Device and Region Engagement (Pivot Table) ---
print("--- SOLUTION FOR TASK 4 ---")
# Create the pivot table
engagement_pivot = customer_df.pivot_table(
    values='total_sessions',
    index='region',
    columns='last_device_used',
    aggfunc='mean'
)
print(engagement_pivot)
print("\n" + "="*50 + "\n")