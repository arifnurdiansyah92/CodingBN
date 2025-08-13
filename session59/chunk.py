import pandas as pd

# Define the size of each chunk (e.g., 100,000 rows)
chunk_size = 100000

# Create an iterator that reads the CSV in chunks
data_chunks = pd.read_csv('large_transactions_dataset.csv', chunksize=chunk_size)

# Loop through each chunk and process it
for chunk in data_chunks:
    # Perform your operations on the small chunk here
    # For example, let's just print the number of rows in each chunk
    print(f"Processing a chunk with {len(chunk)} rows...")
    # cleaned_chunk = chunk.dropna() # Example operation