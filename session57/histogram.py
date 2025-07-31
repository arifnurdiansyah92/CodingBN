import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.histplot(data=titanic, x='age', bins=30, kde=True)
plt.title('Distribution of Passenger Ages')
plt.show()
