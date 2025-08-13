import pandas as pd
import numpy as np
import random
import time
import os

def create_dummy_chunk(chunk_id, num_rows_per_chunk):
    """Generates a single chunk of realistic-looking dummy data."""
    
    start_id = chunk_id * num_rows_per_chunk
    
    data = {
        'transaction_id': range(start_id, start_id + num_rows_per_chunk),
        'user_id': np.random.randint(10000, 50000, size=num_rows_per_chunk),
        'transaction_amount': np.random.uniform(5.0, 500.0, size=num_rows_per_chunk).round(2),
        'product_category': np.random.choice(
            ['Electronics', 'Clothing', 'Groceries', 'Home Goods', 'Books', 'Toys'],
            size=num_rows_per_chunk,
            p=[0.2, 0.2, 0.3, 0.15, 0.1, 0.05] # Probabilities for each category
        ),
        'timestamp': pd.to_datetime(np.random.randint(1609459200, 1640995199, size=num_rows_per_chunk), unit='s'), # Random dates in 2021
        'is_fraudulent': np.random.choice([0, 1], size=num_rows_per_chunk, p=[0.99, 0.01]) # 1% of transactions are fraudulent
    }
    
    # Introduce some missing values to make it realistic
    df = pd.DataFrame(data)
    for _ in range(int(num_rows_per_chunk * 0.02)): # Make 2% of rows have a missing amount
        df.loc[random.randint(0, num_rows_per_chunk-1), 'transaction_amount'] = np.nan
        
    return df

def generate_large_csv(filename, total_rows, chunk_size):
    """Generates a large CSV file by creating and appending chunks."""
    
    print(f"Starting to generate '{filename}' with {total_rows:,} rows...")
    start_time = time.time()
    
    # Ensure the file doesn't exist from a previous run
    if os.path.exists(filename):
        os.remove(filename)
        
    num_chunks = total_rows // chunk_size
    
    for i in range(num_chunks):
        chunk = create_dummy_chunk(chunk_id=i, num_rows_per_chunk=chunk_size)
        
        # The first chunk writes the header, subsequent chunks append without the header
        is_first_chunk = (i == 0)
        chunk.to_csv(filename, mode='a', header=is_first_chunk, index=False)
        
        # Progress indicator
        if (i + 1) % 10 == 0:
            print(f"  ... {i+1}/{num_chunks} chunks written")
            
    end_time = time.time()
    file_size = os.path.getsize(filename) / (1024 * 1024) # in MB
    
    print("\n--- Generation Complete! ---")
    print(f"File '{filename}' created successfully.")
    print(f"Total rows: {total_rows:,}")
    print(f"File size: {file_size:.2f} MB")
    print(f"Time taken: {end_time - start_time:.2f} seconds")


# --- Main execution ---
if __name__ == "__main__":
    # --- Parameters to Customize ---
    
    # Set the total number of rows you want in the final file.
    # 5,000,000 rows is a good starting point for a large file (~500-600 MB).
    TOTAL_ROWS = 50000000
    
    # Set the number of rows to generate in memory at one time.
    # 100,000 is a safe number for most computers.
    CHUNK_SIZE = 1000000
    
    # Set the desired filename.
    FILENAME = "large_transactions_dataset.csv"
    
    generate_large_csv(FILENAME, TOTAL_ROWS, CHUNK_SIZE)

