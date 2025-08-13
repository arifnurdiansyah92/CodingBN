import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- Part 1: Loading and Initial Cleaning with Chunking ---

# Define the path to your downloaded dataset file.
# NOTE: Replace '2008.csv' with the actual path to your file.
file_path = '2008.csv' 

# Define a chunk size. 1 million rows is a good starting point.
chunk_size = 1_000_000

# We will read the file in chunks and only keep the columns we need for our analysis.
# This is a crucial memory-saving technique.
cols_to_keep = [
    'Year', 'Month', 'DayofMonth', 'DayOfWeek', 'DepTime', 'CRSDepTime',
    'ArrTime', 'CRSArrTime', 'UniqueCarrier', 'FlightNum', 'TailNum',
    'ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay', 'DepDelay',
    'Origin', 'Dest', 'Distance', 'Cancelled', 'Diverted'
]

# Create an iterator to read the large CSV file in chunks
chunk_iterator = pd.read_csv(
    file_path,
    chunksize=chunk_size,
    usecols=cols_to_keep,
    encoding='latin1' # This can help with potential reading errors
)

# Process each chunk and store the cleaned versions in a list
list_of_chunks = []
print("Starting to process the large file in chunks...")

for i, chunk in enumerate(chunk_iterator):
    print(f"Processing chunk {i+1}...")
    # For this analysis, we are interested in flights that were not cancelled or diverted.
    chunk = chunk[(chunk['Cancelled'] == 0) & (chunk['Diverted'] == 0)]
    list_of_chunks.append(chunk)

# Concatenate all the processed chunks into a single DataFrame
print("Concatenating all chunks into a final DataFrame...")
df = pd.concat(list_of_chunks, ignore_index=True)

print("Finished loading and initial filtering.")
print(f"The final DataFrame has {len(df)} rows.")
print("-" * 40)


# --- Part 2: In-Depth Cleaning and Feature Engineering ---

print("Starting in-depth cleaning and feature engineering...")

# Handle missing values for key delay columns.
# A common assumption is that if delay is not reported, it was 0.
df['ArrDelay'] = df['ArrDelay'].fillna(0)
df['DepDelay'] = df['DepDelay'].fillna(0)

# Feature Engineering: Create a boolean 'IsDelayed' column.
# The industry standard often considers a flight delayed if it arrives 15 or more minutes late.
df['IsDelayed'] = (df['ArrDelay'] > 15).astype(int)

# Feature Engineering: Convert 'DepTime' to hour of the day for analysis.
# We fill any potential NaNs first, convert to string, pad with zeros, then take the first 2 chars.
df['Hour'] = df['DepTime'].fillna(0).astype(int).astype(str).str.zfill(4).str[:2]

print("Finished cleaning and feature engineering.")
print(df[['ArrDelay', 'DepDelay', 'IsDelayed', 'Hour']].head())
print("-" * 40)


# --- Part 3: Exploratory Data Analysis (EDA) ---

print("Starting Exploratory Data Analysis...")

# Visualization 1: Delays by Month
plt.figure(figsize=(12, 7))
sns.countplot(x='Month', data=df, hue='IsDelayed', palette=['#22c55e', '#ef4444'])
plt.title('Total Flights and Delays by Month', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Number of Flights')
plt.legend(title='Status', labels=['On Time', 'Delayed'])
plt.show()
# Insight: The winter months (December, January, February) and summer months (June, July)
# appear to have a higher number of delays.

# Visualization 2: Delays by Day of the Week
plt.figure(figsize=(12, 7))
sns.countplot(x='DayOfWeek', data=df, hue='IsDelayed', palette=['#22c55e', '#ef4444'])
plt.title('Total Flights and Delays by Day of the Week', fontsize=16)
plt.xlabel('Day of the Week (1=Monday, 7=Sunday)')
plt.ylabel('Number of Flights')
plt.legend(title='Status', labels=['On Time', 'Delayed'])
plt.show()
# Insight: Weekdays, especially Friday (5), seem to experience more delays than weekends.

# Visualization 3: Delays by Airline Carrier
# Calculate delay rate per carrier to be fair to smaller airlines
carrier_delays = df.groupby('UniqueCarrier')['IsDelayed'].value_counts(normalize=True).unstack()
carrier_delays.rename(columns={0: 'OnTime_Rate', 1: 'Delay_Rate'}, inplace=True)
carrier_delays = carrier_delays.sort_values('Delay_Rate', ascending=False)

plt.figure(figsize=(15, 8))
carrier_delays['Delay_Rate'].plot(kind='bar', color='skyblue')
plt.title('Proportion of Delayed Flights by Airline Carrier', fontsize=16)
plt.xlabel('Airline Carrier')
plt.ylabel('Proportion of Flights Delayed')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# Insight: There is a significant variation in delay rates among different carriers.
# Some airlines have a much higher proportion of delayed flights than others.

# Visualization 4: Delays by Hour of the Day
delay_by_hour = df.groupby('Hour')['IsDelayed'].mean() # Calculate the mean delay rate for each hour

plt.figure(figsize=(14, 7))
delay_by_hour.plot(kind='line', marker='o', color='purple')
plt.title('Average Delay Rate by Departure Hour', fontsize=16)
plt.xlabel('Hour of the Day (24-hour format)')
plt.ylabel('Proportion of Flights Delayed')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.xticks(np.arange(0, 25, 1))
plt.show()
# Insight: The delay rate is very low in the early morning and increases steadily throughout the day,
# peaking in the late evening. This suggests delays have a cascading effect.

# --- Your Task: Complete this code ---

# 1. Calculate Q1, Q3, and IQR for the 'ArrDelay' column
Q1 = df['ArrDelay'].quantile(0.25)
Q3 = df['ArrDelay'].quantile(0.75)
IQR = Q3 - Q1

# 2. Calculate the outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 3. Create a new DataFrame that excludes the outliers
df_no_outliers = df[(df['ArrDelay'] >= lower_bound) & (df['ArrDelay'] <= upper_bound)]

# 4. Create a 'before and after' visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.boxplot(x=df['ArrDelay'], ax=axes[0])
axes[0].set_title('Before Outlier Removal')

sns.boxplot(x=df_no_outliers['ArrDelay'], ax=axes[1])
axes[1].set_title('After Outlier Removal')

plt.show()

print(f"Original dataset size: {len(df)}")
print(f"New dataset size without outliers: {len(df_no_outliers)}")
