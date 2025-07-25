import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 1. Prepare your data in a Pandas DataFrame
data = pd.DataFrame({'day': [1, 2, 3, 4, 5], 'sales': [10, 15, 12, 18, 22]})

# 2. Tell Seaborn what you want to see (just one line!)
sns.scatterplot(x='day', y='sales', data=data)

# 3. Show the result
plt.show() # We still use plt.show() to display the plot
