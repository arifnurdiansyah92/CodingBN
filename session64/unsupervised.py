import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# Load the dataset (we will only use the features, X)
iris = load_iris()
X = iris.data

# We tell the model to find 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Train the model and get the cluster assignment for each data point
clusters = kmeans.fit_predict(X)

# Let's visualize the results
# We create a DataFrame to hold our data and the new cluster labels
df = pd.DataFrame(X, columns=iris.feature_names)
df['found_cluster'] = clusters
df['true_species'] = iris.target # Add the true labels just for our comparison

# Plot the clusters the algorithm found
plt.figure(figsize=(10,7))
sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', hue='found_cluster', palette='viridis', s=100)
plt.title('Clusters Found by K-Means Algorithm')
plt.show()
