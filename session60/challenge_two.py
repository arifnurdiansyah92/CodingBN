import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- Part 1: Loading Data with ALL Necessary Columns ---

# Define the path to your downloaded dataset file.
# NOTE: Replace '2008.csv' with the actual path to your file.
file_path = '2008.csv' 

# Define a chunk size.
chunk_size = 1_000_000

# CRITICAL FIX: We must include the delay reason columns in our list to load them.
cols_to_keep = [
    'Year', 'Month', 'DayofMonth', 'DayOfWeek', 'DepTime', 'CRSDepTime',
    'ArrTime', 'CRSArrTime', 'UniqueCarrier', 'FlightNum', 'TailNum',
    'ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay', 'DepDelay',
    'Origin', 'Dest', 'Distance', 'Cancelled', 'Diverted',
    # --- ADDED THESE COLUMNS ---
    'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay'
]

# Create an iterator to read the large CSV file in chunks
try:
    chunk_iterator = pd.read_csv(
        file_path,
        chunksize=chunk_size,
        usecols=cols_to_keep,
        encoding='latin1'
    )
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    print("Please make sure the dataset is in the same directory or provide the full path.")
    # Exit gracefully if the file isn't found
    exit()


# Process each chunk and store the cleaned versions in a list
list_of_chunks = []
print("Starting to process the large file in chunks...")

for i, chunk in enumerate(chunk_iterator):
    print(f"Processing chunk {i+1}...")
    # Filter out flights that were not cancelled or diverted.
    chunk = chunk[(chunk['Cancelled'] == 0) & (chunk['Diverted'] == 0)]
    list_of_chunks.append(chunk)

# Concatenate all the processed chunks into a single DataFrame
print("Concatenating all chunks into a final DataFrame...")
df = pd.concat(list_of_chunks, ignore_index=True)

print("Finished loading and initial filtering.")
print("-" * 40)


# --- Part 2: Analysis - Bar Chart for the Direct Answer ---

# Define the delay columns
delay_columns = ['CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']

# Fill any NaN values in these columns with 0, as NaN means no delay of that type.
df[delay_columns] = df[delay_columns].fillna(0)

# Calculate the sum of delay minutes for each category
total_delays = df[delay_columns].sum()

# Sort the values to make the chart clearer
total_delays = total_delays.sort_values(ascending=False)

# Create a bar chart for a clear, direct answer
plt.figure(figsize=(12, 7))
total_delays.plot(kind='bar', color='skyblue')
plt.title('Total Delay Minutes by Cause', fontsize=16)
plt.ylabel('Total Minutes (in tens of millions)')
plt.xlabel('Reason for Delay')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print("--- Total Delay Minutes by Cause ---")
print(total_delays)
print("-" * 40)


# --- Part 3: Analysis - Heatmap for Deeper Insights ---

# Now we can create the heatmap because the columns exist in our DataFrame.
# This heatmap shows the relationship between the delay types themselves.
delay_correlation = df[delay_columns].corr()

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    delay_correlation,
    annot=True,        # Show the correlation values
    cmap='coolwarm',   # Use a color scheme that highlights positive/negative correlation
    fmt=".2f"          # Format numbers to two decimal places
)
plt.title('Correlation Heatmap of Delay Types', fontsize=16)
plt.show()

