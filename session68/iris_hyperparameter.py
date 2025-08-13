import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.svm import SVC

# 1. Load Data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Define the Model and the "Grid" of Hyperparameters to test
model = SVC()
param_grid = {
    'C': [0.1, 1, 10],          # Regularization strength
    'kernel': ['linear', 'rbf'], # Type of decision boundary
    'gamma': ['scale', 'auto']   # Kernel coefficient
}

# 3. Set up K-Fold Cross-Validation
# We use StratifiedKFold to ensure each fold has a balanced number of samples from each class.
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 4. Initialize GridSearchCV
# This object will automatically perform the grid search with cross-validation.
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=cv, scoring='accuracy')

# 5. Fit the model
# This one command runs the entire process! It will test all 12 combinations (3*2*2)
# and for each one, it will run a 5-fold cross-validation. (12 * 5 = 60 total trainings)
grid_search.fit(X, y)

# 6. View the Results
print("Grid Search complete!")
print(f"The best hyperparameters found are: {grid_search.best_params_}")
print(f"The best cross-validation accuracy score is: {grid_search.best_score_:.2f}")

# The best model is automatically saved
best_model = grid_search.best_estimator_
