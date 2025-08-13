import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate some noisy data where the true pattern is a line
np.random.seed(42)
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 3 * X.squeeze() + np.random.randn(100) * 10 # Added more noise

# For demonstration, let's add polynomial features to allow overfitting
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=15)
X_poly = poly.fit_transform(X)

# Split the complex data
X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.5, random_state=42)

# Train three models
linear_model = LinearRegression()
ridge_model = Ridge(alpha=0.1) # Ridge with some regularization
lasso_model = Lasso(alpha=0.1, max_iter=10000) # Lasso with some regularization

linear_model.fit(X_train, y_train)
ridge_model.fit(X_train, y_train)
lasso_model.fit(X_train, y_train)

# Make predictions
y_pred_linear = linear_model.predict(X_test)
y_pred_ridge = ridge_model.predict(X_test)
y_pred_lasso = lasso_model.predict(X_test)

# Plot the results
plt.figure(figsize=(14, 8))
plt.scatter(X, y, color='black', s=10, label='Original Data')
plt.plot(np.sort(X_test[:, 1]), y_pred_linear[np.argsort(X_test[:, 1])], color='red', label=f'Linear (Overfit) MSE: {mean_squared_error(y_test, y_pred_linear):.2f}')
plt.plot(np.sort(X_test[:, 1]), y_pred_ridge[np.argsort(X_test[:, 1])], color='blue', label=f'Ridge (alpha=1.0) MSE: {mean_squared_error(y_test, y_pred_ridge):.2f}')
plt.plot(np.sort(X_test[:, 1]), y_pred_lasso[np.argsort(X_test[:, 1])], color='green', label=f'Lasso (alpha=0.1) MSE: {mean_squared_error(y_test, y_pred_lasso):.2f}')

plt.title('Effect of Regularization on an Overfitting Model')
plt.ylim(-15, 45)
plt.legend()
plt.show()