import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# --- Step 1: Data Preprocessing ---

# Load the dataset from the Kaggle 'train.csv' file
try:
    df = pd.read_csv('./data/titanic.csv')
except FileNotFoundError:
    print("Error: 'train.csv' not found. Please download it from the Kaggle Titanic competition.")
    exit()

print("--- Initial Data Exploration ---")
df.info()
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())
print("-" * 40)

# Handle Missing Values:
# For 'Age', fill with the median.
median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)

# For 'Embarked', fill with the most common port (the mode).
mode_embarked = df['Embarked'].mode()[0]
df['Embarked'].fillna(mode_embarked, inplace=True)

# Drop 'Cabin' column due to too many missing values.
df.drop('Cabin', axis=1, inplace=True)
print("Preprocessing: Handled missing values for Age, Embarked, and dropped Cabin.")

# Encode Categorical Variables & Feature Engineering:
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df.drop(['PassengerId', 'Name', 'Ticket', 'SibSp', 'Parch'], axis=1, inplace=True)
print("Preprocessing: Encoded categorical features and created 'FamilySize'.")

# Define features (X) and target (y) BEFORE scaling
X = df.drop('Survived', axis=1)
y = df['Survived']
# Save column names before scaling (as scaler returns a numpy array)
feature_names = X.columns

# Feature Scaling:
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X = pd.DataFrame(X_scaled, columns=feature_names) # Convert back to DataFrame
print("Preprocessing: Scaled all numerical features.")
print("-" * 40)


# --- Step 2: Exploratory Data Analysis (EDA) ---

print("\n--- Starting Exploratory Data Analysis ---")
# For EDA, we'll use the preprocessed but unscaled data for easier interpretation
# We need to recreate the unscaled feature DataFrame for this
df_unscaled = df.drop('Survived', axis=1)
df_eda = df_unscaled.copy()
df_eda['Survived'] = y


# Visualization 1: Survival Rate by Gender
plt.figure(figsize=(8, 6))
# We map the encoded 'Sex' back to labels for the plot title
sns.barplot(x='Sex', y='Survived', data=df) # Using original df for unscaled Sex
plt.title('Survival Rate by Gender (0 = Male, 1 = Female)', fontsize=16)
plt.ylabel('Survival Rate')
plt.savefig('survival.png')
# Insight: This chart clearly shows that female passengers had a much higher rate of survival.

# Visualization 2: Survival Rate by Passenger Class
# Note: Pclass was not scaled as it's more of a categorical feature
plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=df) # Using original df for unscaled Pclass
plt.title('Survival Rate by Passenger Class', fontsize=16)
plt.ylabel('Survival Rate')
plt.savefig('pclass_survival.png')
# Insight: There is a strong correlation between passenger class and survival.
# First-class passengers had the highest survival rate.
print("-" * 40)

# --- Step 3: Train/Test Split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
print(f"Data split into {len(X_train)} training samples and {len(X_test)} testing samples.")
print("-" * 40)

# --- Step 4: Model Training (Before Tuning) ---
print("\n--- Starting Model Training (Before Tuning) ---")
base_model = LogisticRegression(random_state=42, max_iter=1000)
base_model.fit(X_train, y_train)
print("Base model training complete!")

# --- Evaluation (Before Tuning) ---
print("\n--- Evaluation on Test Set (Before Tuning) ---")
y_pred_base = base_model.predict(X_test)
print("\nClassification Report (Before Tuning):")
print(classification_report(y_test, y_pred_base, target_names=['Did not Survive', 'Survived']))

# Confusion Matrix
cm_base = confusion_matrix(y_test, y_pred_base)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_base, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Did not Survive', 'Survived'],
            yticklabels=['Did not Survive', 'Survived'])
plt.title('Confusion Matrix on Test Set (Before Tuning)', fontsize=16)
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.savefig('confusion_matrix_before_tuning.png')
print("-" * 40)


# --- Step 5: Model Training with GridSearchCV (Hyperparameter Tuning) ---

print("\n--- Starting Model Training & Hyperparameter Tuning ---")

# Choose the model
model = LogisticRegression(random_state=42, max_iter=1000)

# Define the grid of hyperparameters to search
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100] # C is the regularization strength
}

# Set up K-Fold Cross-Validation
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# Initialize GridSearchCV
# This will search for the best 'C' value using 5-fold cross-validation.
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=cv, scoring='accuracy')

# Fit GridSearchCV on the TRAINING data
grid_search.fit(X_train, y_train)

print(f"Best Hyperparameters found: {grid_search.best_params_}")
print(f"Best Cross-Validation Accuracy: {grid_search.best_score_ * 100:.2f}%")
print("-" * 40)


# --- Step 6: Final Evaluation (After Tuning) ---
print("\n--- Detailed Evaluation of BEST Model on a Single Test Split (After Tuning) ---")
# The best model is automatically trained on the full data and stored
best_model = grid_search.best_estimator_

# We can predict directly with the best model found by GridSearch
y_pred = best_model.predict(X_test)

print("\nClassification Report (After Tuning):")
print(classification_report(y_test, y_pred, target_names=['Did not Survive', 'Survived']))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Did not Survive', 'Survived'],
            yticklabels=['Did not Survive', 'Survived'])
plt.title('Confusion Matrix for Best Model on Test Set (After Tuning)', fontsize=16)
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.savefig('confusion_matrix_after_tuning.png')