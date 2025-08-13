import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# Define Cars dataset directly
data = pd.read_csv('cars.csv')
cars = pd.DataFrame(data)

# Assuming the dataset has columns: 'speed', 'doors', and 'type'
# 'type' is the target variable (categorical), and 'speed' and 'doors' are features
X_clf = cars[['speed', 'doors', 'seats']]
y_clf = cars['type']

# Split data
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42)

# Train Logistic Regression model
clf = LogisticRegression(max_iter=1500)
clf.fit(X_train_clf, y_train_clf)

# Predict
y_pred_clf = clf.predict(X_test_clf)

# Evaluate
accuracy = accuracy_score(y_test_clf, y_pred_clf)
print("Classification - Cars Dataset")
print(f"Accuracy: {accuracy:.2f}")

# Visualization: Confusion Matrix
cm = confusion_matrix(y_test_clf, y_pred_clf, labels=clf.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix - Cars Classification')
plt.savefig('cars_confusion_matrix.png')

# Optional: Pairplot of Cars features colored by type
cars_df = X_clf.copy()
cars_df['type'] = y_clf
sns.pairplot(cars_df, hue='type', diag_kind='kde')
plt.suptitle('Cars Dataset Feature Pairplot', y=1.02)
plt.savefig('cars.png')

# Function to predict car type for a new dataset
def predict_car_type_from_file(input_file, output_file):
    try:
        # Load the new dataset (without 'type' column)
        new_data = pd.read_csv(input_file)

        # Ensure the required columns are present
        if not {'speed', 'doors', 'seats'}.issubset(new_data.columns):
            print("Input file must contain 'speed' and 'doors' and 'seats' columns.")
            return

        # Predict the type using the trained model
        new_data['type'] = clf.predict(new_data[['speed', 'doors', 'seats']])

        # Save the new dataset with predictions to a file
        new_data.to_csv(output_file, index=False)
        print(f"Predictions saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
predict_car_type_from_file('new_cars.csv', 'predicted_cars.csv')
