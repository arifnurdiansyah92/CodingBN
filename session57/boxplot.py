import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.boxplot(data=titanic, x='pclass', y='fare')
plt.title('Fare Distribution by Passenger Class')
plt.ylim(0, 300) # Limit y-axis to see the boxes clearly
plt.show()
