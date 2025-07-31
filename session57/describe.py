import pandas as pd
import seaborn as sns

# Load the famous Titanic dataset
titanic = sns.load_dataset('titanic')

# Get the summary statistics
print(titanic.describe())