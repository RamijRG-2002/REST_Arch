import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

# 🔹 User provides the Iris dataset (CSV)
df = pd.read_csv('iris.csv')  # Ensure iris.csv is in the same directory

# 🔹 Separate features and target using iloc
X = df.iloc[:, :-1]   # all columns except the last
y = df.iloc[:, -1]    # last column (target)

# 🔹 Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔹 Create SVM model
model = SVC(kernel='linear')  # You can try 'rbf', 'poly', etc.

# 🔹 Train model
model.fit(X_train, y_train)

# 🔹 Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# 🔹 Save model using joblib
joblib.dump(model, 'svm_iris_model.pkl')
print("Model saved as 'svm_iris_model.pkl'")
