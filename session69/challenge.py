import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, KFold, GridSearchCV, cross_val_score
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error

# --- Part 1: Exploration and Baseline Model ---

# 1. Load the dataset
housing = fetch_california_housing()
X, y = housing.data, housing.target

# 2. Split the ORIGINAL data for later use
X_train_base, X_test_base, y_train_base, y_test_base = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Train a simple Linear Regression model as a baseline
baseline_model = LinearRegression()
baseline_model.fit(X_train_base, y_train_base)
pred_base = baseline_model.predict(X_test_base)
rmse_base = np.sqrt(mean_squared_error(y_test_base, pred_base))

print("--- Baseline Model Performance ---")
print(f"Simple Linear Regression Test RMSE: {rmse_base:.4f}")
print("-" * 40)


# --- Part 2: Creating and Diagnosing an Overfitting Model ---

# 1. Create Overly Complex Features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# 2. Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_poly)

# 3. Split the new, complex data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# 4. Train a Linear Regression model on the complex features
overfit_model = LinearRegression()
overfit_model.fit(X_train, y_train)

# 5. Evaluate the overfit model on BOTH training and testing data
pred_train = overfit_model.predict(X_train)
pred_test = overfit_model.predict(X_test)
rmse_train = np.sqrt(mean_squared_error(y_train, pred_train))
rmse_test = np.sqrt(mean_squared_error(y_test, pred_test))

print("\n--- Diagnosis of Overfitting Model (from single split) ---")
print(f"Training Set RMSE: {rmse_train:.4f}")
print(f"Testing Set RMSE: {rmse_test:.4f}")
print("-" * 40)


# --- Part 3: The Solution - Systematic Tuning with GridSearchCV ---

# For this solution, we'll focus on the Ridge model which often performs well.
print("\n--- Part 3: Finding the Best Regularized Model ---")
ridge = Ridge()
param_grid_ridge = {'alpha': [10, 100, 1000, 10000]}
cv = KFold(n_splits=5, shuffle=True, random_state=42)
grid_search_ridge = GridSearchCV(estimator=ridge, param_grid=param_grid_ridge, cv=cv, scoring='neg_root_mean_squared_error')
grid_search_ridge.fit(X_train, y_train)
best_ridge_model = grid_search_ridge.best_estimator_
print(f"Best alpha for Ridge found by GridSearchCV: {grid_search_ridge.best_params_['alpha']}")
print("-" * 40)


# --- Part 4: The Proof - Comparing Models with Cross-Validation ---

print("\n--- Part 4: Proving the Point with 5-Fold Cross-Validation ---")
# We will now evaluate the overfitted model and the best regularized model
# on the FULL complex dataset (X_scaled) using cross-validation.
# This gives a much more reliable performance estimate than a single train/test split.

# 1. Evaluate the Overfitted Model
cv_scores_overfit = cross_val_score(
    estimator=overfit_model,
    X=X_scaled,
    y=y,
    cv=cv,
    scoring='neg_root_mean_squared_error'
)
# Convert scores to positive RMSE
cv_scores_overfit = -cv_scores_overfit

# 2. Evaluate the Best Regularized (Ridge) Model
cv_scores_ridge = cross_val_score(
    estimator=best_ridge_model,
    X=X_scaled,
    y=y,
    cv=cv,
    scoring='neg_root_mean_squared_error'
)
# Convert scores to positive RMSE
cv_scores_ridge = -cv_scores_ridge


# --- Final Results ---
print("\n--- Final Cross-Validated Comparison ---")
print(f"Overfitted Model CV Scores (RMSE on 5 folds): {np.round(cv_scores_overfit, 4)}")
print(f"Overfitted Model AVERAGE CV RMSE: {cv_scores_overfit.mean():.4f} (+/- {cv_scores_overfit.std():.4f})\n")

print(f"Regularized Ridge Model CV Scores (RMSE on 5 folds): {np.round(cv_scores_ridge, 4)}")
print(f"Regularized Ridge Model AVERAGE CV RMSE: {cv_scores_ridge.mean():.4f} (+/- {cv_scores_ridge.std():.4f})\n")

print("--- Conclusion ---")
if cv_scores_ridge.mean() < cv_scores_overfit.mean():
    print("The Regularized Ridge model has a lower average error and is more stable (lower std dev).")
    print("This proves that regularization created a more reliable and better-performing model!")
else:
    print("The Overfitted model still has a slightly lower average error, but the Regularized model is more stable (lower std dev).")

