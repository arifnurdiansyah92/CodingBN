import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# 1. Create a sample dataset of Coding BN participants
# 0 = Female, 1 = Male
data = {
    'Coding_Experience_Years': [1, 2, 2.5, 4, 1, 3, 5, 6, 4.5, 5.5, 2, 3.5],
    'Pre_Course_Score':        [60, 75, 70, 85, 80, 88, 90, 95, 92, 98, 55, 78],
    'Gender':                  [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

X = df[['Coding_Experience_Years', 'Pre_Course_Score']]
y = df['Gender']

# Scale the features for SVM
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Train the SVM model
# We use a linear kernel to find a straight-line boundary
svm_model = SVC(kernel='linear', C=1.0)
svm_model.fit(X_scaled, y)

# 3. Visualize the Decision Boundary and Margins
plt.figure(figsize=(12, 8))
# Plot the data points
sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=y, s=150, palette={0:'purple', 1:'orange'}, style=y, markers={0:'o', 1:'s'})

# Create the grid to plot the decision boundary
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50),
                     np.linspace(ylim[0], ylim[1], 50))
Z = svm_model.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot the decision boundary and the margins
ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

# Highlight the support vectors
ax.scatter(svm_model.support_vectors_[:, 0], svm_model.support_vectors_[:, 1], s=300,
           linewidth=1, facecolors='none', edgecolors='k', label='Support Vectors')

plt.title('SVM Decision Boundary with Maximum Margin')
plt.xlabel('Coding Experience (Scaled)')
plt.ylabel('Pre-Course Score (Scaled)')
plt.legend()
plt.show()
