import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# 1. Data Collection & Preprocessing
# We load the 'tips' dataset, which is already clean.
tips = sns.load_dataset('tips')

# Define our "feature" (X) and our "target" (y)
# We want to use the bill to predict the tip.
X = tips[['total_bill']] # Feature must be a DataFrame
y = tips['tip']          # Target is a Series

# 4. Model Selection (and data splitting)
# We choose a simple Linear Regression model.
# We also split the data, saving 20% for our final evaluation.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Training the Model
# The .fit() method teaches the model the relationship between total_bill and tip.
model = LinearRegression()
model.fit(X_train, y_train)
print("Model training complete!")

# 6. Evaluation
# We use the trained model to make predictions on the test data it has never seen.
predictions = model.predict(X_test)
error = np.sqrt(mean_squared_error(y_test, predictions)) # Use square root for interpretability
print(f"On average, the model's predictions are off by ${error:.2f}")

# --- BONUS: Let's Use Our Model! ---
# Now we can use our trained model to predict the tip for any new bill.
new_bill = [[40.00]] # A $40 bill
predicted_tip = model.predict(new_bill)
print(f"For a ${new_bill[0][0]:.2f} bill, the model predicts a tip of ${predicted_tip[0]:.2f}")
