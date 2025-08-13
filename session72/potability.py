import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# --- Step 1: Data Loading and Initial Exploration ---

try:
    df = pd.read_csv('./data/water_potability.csv')
except FileNotFoundError:
    print("Error: 'water_potability.csv' not found. Please download it from the Kaggle Water Quality dataset.")
    exit()

print("--- Initial Data Info ---")
df.info()
print("\n--- Missing Values ---")
print(df.isnull().sum())
print("-" * 40)


# --- Step 2: Exploratory Data Analysis (EDA) ---

print("\n--- Starting Exploratory Data Analysis ---")

# Visualization 1: Correlation Heatmap
# This helps us see which features are most correlated with our target, 'Potability'.
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Water Quality Features', fontsize=16)
plt.savefig('heatmap_water_quality.png')
# Insight: No single feature has a very strong correlation with Potability,
# suggesting a simple model like Logistic Regression will struggle. Features like 'Sulfate',
# 'Chloramines', and 'Solids' have the highest (though still weak) correlations.

# Visualization 2: Pairplot to see relationships
# We'll look at the top 3 correlated features against Potability.
top_features = ['Sulfate', 'Chloramines', 'Solids', 'Potability']
sns.pairplot(df.dropna(), hue='Potability', vars=top_features[:-1], palette='viridis')
plt.suptitle('Pairplot of Top Features by Potability', y=1.02)
plt.savefig('pairplot_top_features.png')
# Insight: The classes are not easily separable by any single feature, confirming this is a
# complex problem that requires a more powerful model.
print("-" * 40)


# --- Step 3: Preprocessing ---

print("\n--- Starting Data Preprocessing ---")

# Define features (X) and target (y)
X = df.drop('Potability', axis=1)
y = df['Potability']

# Handle Missing Values: Use median imputation
imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(X)

# Feature Scaling:
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)

# Convert back to a DataFrame for easier use
X = pd.DataFrame(X_scaled, columns=X.columns)
print("Preprocessing complete! Features scaled and missing values imputed.")
print("-" * 40)
# --- Step 4: Model Training (Before Tuning) ---
print("\n--- Starting Model Training (Before Tuning) ---")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# We will use a more powerful model, RandomForestClassifier, which is better for complex problems.
# 'class_weight="balanced"' is crucial for imbalanced datasets like this one.
base_model = RandomForestClassifier(random_state=42, class_weight='balanced')
base_model.fit(X_train, y_train)
print("Base model training complete!")
print("-" * 40)

# --- Evaluation (Before Tuning) ---
print("\n--- Evaluation on Test Set (Before Tuning) ---")
y_pred_base = base_model.predict(X_test)
print("\nClassification Report (Before Tuning):")
print(classification_report(y_test, y_pred_base, target_names=['Not Potable', 'Potable']))

# Confusion Matrix
cm_base = confusion_matrix(y_test, y_pred_base)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_base, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Not Potable', 'Potable'],
            yticklabels=['Not Potable', 'Potable'])
plt.title('Confusion Matrix on Test Set (Before Tuning)', fontsize=16)
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.savefig('confusion_matrix_before_tuning.png')


# --- Step 5: Model Training with GridSearchCV (Hyperparameter Tuning) ---

print("\n--- Starting Model Training & Hyperparameter Tuning ---")

# 1. Define the model
# 'class_weight="balanced"' is crucial for imbalanced datasets like this one.
model = RandomForestClassifier(random_state=42, class_weight='balanced')

# 2. Define the grid of hyperparameters to search
# We'll test different numbers of trees and different tree depths.
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_leaf': [1, 2, 4]
}

# 3. Set up K-Fold Cross-Validation
cv = KFold(n_splits=5, shuffle=True, random_state=42)

# 4. Initialize GridSearchCV
# We will score based on 'f1_weighted' because accuracy is misleading here.
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=cv, scoring='f1_weighted', n_jobs=-1)

# 5. Fit GridSearchCV on the data
grid_search.fit(X_train, y_train)

print(f"Best Hyperparameters found: {grid_search.best_params_}")
print(f"Best Cross-Validation F1-Score: {grid_search.best_score_:.4f}")
print("-" * 40)


# --- Step 6: Final Evaluation (After Tuning) ---

print("\n--- Final Evaluation of the BEST Model on the Test Set (After Tuning) ---")

# The best model is automatically trained and stored
best_model = grid_search.best_estimator_

# Make predictions on the unseen test set
y_pred = best_model.predict(X_test)

# Evaluate the final model
print("\nFinal Classification Report (After Tuning):")
print(classification_report(y_test, y_pred, target_names=['Not Potable', 'Potable']))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Not Potable', 'Potable'],
            yticklabels=['Not Potable', 'Potable'])
plt.title('Confusion Matrix for Best Model on Test Set (After Tuning)', fontsize=16)
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.savefig('confusion_matrix_after_tuning.png')
