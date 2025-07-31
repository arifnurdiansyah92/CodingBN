import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
corr = titanic.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Titanic Features')
plt.show()
