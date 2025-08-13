import dask.dataframe as dd

# Dask reads the data by pointing to it, not loading it all.
ddf = dd.read_csv('large_dataset.csv')

# This line does NOT calculate the mean yet.
# It just adds 'calculate the mean' to the task plan.
mean_value_task = ddf['column_name'].mean()

# The .compute() command triggers the actual calculation.
# Dask reads the data and computes the mean in parallel.
final_mean = mean_value_task.compute()

print(f"The final mean is: {final_mean}")