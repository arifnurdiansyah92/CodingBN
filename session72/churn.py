import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# --- Step 1: Data Loading & Initial Exploration ---

# Load the dataset from the Kaggle 'BankChurners.csv' file
# NOTE: You may need to rename the file provided by Kaggle.
try:
    df = pd.read_csv('./data/BankChurners.csv')
except FileNotFoundError:
    print("Error: 'BankChurners.csv' not found. Please download it from the Kaggle 'Credit Card Customers' dataset.")
    exit()

# Drop unnecessary columns at the end of the file and the client number
df = df.iloc[:, :-2]
df = df.drop('CLIENTNUM', axis=1)

print("--- Initial Data Info ---")
df.info()

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())
print("-" * 40)


# --- Step 2: Data Preprocessing ---

print("\n--- Starting Data Preprocessing ---")

# Encode the Target Variable:
# Convert the target 'Attrition_Flag' into a numerical format (0 and 1).
df['Attrition_Flag'] = df['Attrition_Flag'].map({'Existing Customer': 0, 'Attrited Customer': 1})
print("Encoded target variable 'Attrition_Flag'.")

# Identify categorical and numerical features
categorical_features = df.select_dtypes(include=['object']).columns
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns.drop('Attrition_Flag')

# Encode Categorical Features:
# We will use one-hot encoding for the other categorical columns.
df = pd.get_dummies(df, columns=categorical_features, drop_first=True)
print("Encoded categorical features using one-hot encoding.")

# Feature Scaling:
# We will scale all numerical features.
scaler = StandardScaler()
df[numerical_features] = scaler.fit_transform(df[numerical_features])
print("Scaled numerical features.")
print("-" * 40)


# --- Step 3: Exploratory Data Analysis (EDA) ---

print("\n--- Starting Exploratory Data Analysis ---")
# Reload original data for accurate EDA before scaling/encoding
df_eda = pd.read_csv('./data/BankChurners.csv').iloc[:, :-2]

# Visualization 1: Churn Rate
plt.figure(figsize=(8, 6))
sns.countplot(x='Attrition_Flag', data=df_eda)
plt.title('Customer Churn Distribution', fontsize=16)
plt.savefig('churn_distribution.png')
# Insight: This is an imbalanced dataset. Most customers are 'Existing Customers',
# which means our model's accuracy might be high, but we need to check precision/recall.

# Visualization 2: Churn by Gender
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', hue='Attrition_Flag', data=df_eda)
plt.title('Churn Distribution by Gender', fontsize=16)
plt.savefig('churn_distribution_by_gender.png')
# Insight: A higher proportion of females have churned compared to males.
print("-" * 40)


# --- Step 4: Model Training ---

print("\n--- Starting Model Training ---")
# Define your features (X) and your target (y)
X = df.drop('Attrition_Flag', axis=1)
y = df['Attrition_Flag']

# Perform a train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Data split into {len(X_train)} training samples and {len(X_test)} testing samples.")

# Choose and train a classification model
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)
print("Model training complete!")
print("-" * 40)


# --- Step 5: Model Evaluation (Before Tuning) ---

print("\n--- Starting Model Evaluation (Before Tuning) ---")
# Make predictions on your test set
y_pred = model.predict(X_test)

# 1. Accuracy Score
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# 2. Classification Report
print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred, target_names=['Existing Customer', 'Attrited Customer']))

# 3. Confusion Matrix
print("\n--- Confusion Matrix ---")
cm = confusion_matrix(y_test, y_pred)
# Visualize it
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Existing Customer', 'Attrited Customer'],
            yticklabels=['Existing Customer', 'Attrited Customer'])
plt.title('Confusion Matrix (Before Tuning)', fontsize=16)
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.savefig('confusion_matrix_before_tuning.png')


# --- Step 6: Model Training with KFold Cross Validation & Hyperparameter Tuning ---

print("\n--- Starting Model Training & Hyperparameter Tuning ---")

# 1. Define the model
model_tuned = LogisticRegression(random_state=42, max_iter=1000)

# 2. Define the grid of hyperparameters to search
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],
    'solver': ['liblinear'] # liblinear is good for smaller datasets and supports L1/L2
}

# 3. Set up K-Fold Cross-Validation
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# 4. Initialize GridSearchCV
grid_search = GridSearchCV(estimator=model_tuned, param_grid=param_grid, cv=cv, scoring='accuracy', n_jobs=-1)

# 5. Fit GridSearchCV on the training data
grid_search.fit(X_train, y_train)

print(f"Best Hyperparameters found: {grid_search.best_params_}")
print(f"Best Cross-Validation Accuracy: {grid_search.best_score_ * 100:.2f}%")
print("-" * 40)


# --- Step 7: Final Evaluation (After Tuning) ---

print("\n--- Final Evaluation of the BEST Model on the Test Set (After Tuning) ---")

# The best model is automatically trained and stored
best_model = grid_search.best_estimator_

# Make predictions on the unseen test set
y_pred_tuned = best_model.predict(X_test)

# Evaluate the final model
# 1. Accuracy Score
accuracy_tuned = accuracy_score(y_test, y_pred_tuned)
print(f"Tuned Model Accuracy: {accuracy_tuned * 100:.2f}%")

# 2. Classification Report
print("\nFinal Classification Report (After Tuning):")
print(classification_report(y_test, y_pred_tuned, target_names=['Existing Customer', 'Attrited Customer']))

# 3. Confusion Matrix
cm_tuned = confusion_matrix(y_test, y_pred_tuned)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_tuned, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Existing Customer', 'Attrited Customer'],
            yticklabels=['Existing Customer', 'Attrited Customer'])
plt.title('Confusion Matrix for Best Model on Test Set (After Tuning)', fontsize=16)
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.savefig('confusion_matrix_after_tuning.png')