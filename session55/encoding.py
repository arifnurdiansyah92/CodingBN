import pandas as pd

# Our data with a text category
data = {'Gender': ['Male', 'Female', 'Female', 'Male']}
df = pd.DataFrame(data)

# The easiest way to do One-Hot Encoding is with pandas.get_dummies()
df_encoded = pd.get_dummies(df, columns=['Gender'])

print(df_encoded)