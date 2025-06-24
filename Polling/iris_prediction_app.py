import joblib
import sqlite3
from datetime import datetime
import uuid
import pandas as pd
# ✅ Load the SVM model correctly using joblib
model = joblib.load('svm_iris_model.pkl')

# Create SQLite database and table
def create_database():
    conn = sqlite3.connect('iris_predictions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id TEXT PRIMARY KEY,
            timestamp TEXT,
            sepal_length REAL,
            sepal_width REAL,
            petal_length REAL,
            petal_width REAL,
            prediction TEXT
        )
    ''')
    conn.commit()
    return conn

def get_user_input():
    while True:
        try:
            sepal_length = float(input("Enter sepal length (cm): "))
            sepal_width = float(input("Enter sepal width (cm): "))
            petal_length = float(input("Enter petal length (cm): "))
            petal_width = float(input("Enter petal width (cm): "))
            return [sepal_length, sepal_width, petal_length, petal_width]
        except ValueError:
            print("Please enter valid numeric values!")

def main():
    # Initialize database
    conn = create_database()
    cursor = conn.cursor()
    
    print("Welcome to Iris Flower Prediction App!")
    print("Press Ctrl+C to exit at any time.")
    
    while True:
        try:
            # Get user input
            features = get_user_input()
            
            # Make prediction
            feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
            features_df = pd.DataFrame([features], columns=feature_names)
            prediction = model.predict(features_df)[0]
            
            # Generate unique ID and timestamp
            prediction_id = str(uuid.uuid4())
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Store in database
            cursor.execute('''
                INSERT INTO predictions (id, timestamp, sepal_length, sepal_width, 
                                         petal_length, petal_width, prediction)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (prediction_id, timestamp, features[0], features[1], 
                  features[2], features[3], prediction))
            conn.commit()
            
            # Print prediction
            print(f"\nPrediction: {prediction}")
            print(f"Prediction ID: {prediction_id}")
            print(f"Timestamp: {timestamp}\n")
            
        except KeyboardInterrupt:
            print("\nExiting program...")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    
    conn.close()

if __name__ == "__main__":
    main()
