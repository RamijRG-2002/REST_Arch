import sqlite3
import pandas as pd
import time
import os

def display_predictions():
    while True:
        try:
            # Clear the screen (works on Windows and Unix-based systems)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Connect to SQLite database
            conn = sqlite3.connect('iris_predictions.db')
            cursor = conn.cursor()

            # Fetch all records
            cursor.execute('SELECT * FROM predictions')
            rows = cursor.fetchall()

            # If there are records, display them using pandas
            if rows:
                df = pd.DataFrame(rows, columns=[
                    'ID', 'Timestamp', 'Sepal Length', 'Sepal Width',
                    'Petal Length', 'Petal Width', 'Prediction'
                ])
                print("🌸 Iris Flower Predictions (Updated Every 30s):\n")
                print("Press Ctrl+C to exit at any time.\n")
                print(df.to_string(index=False))
            else:
                print("No predictions found in the database.")

            conn.close()
            
            # Wait 30 seconds before refreshing
            time.sleep(30)

        except KeyboardInterrupt:
            print("\nExiting display...")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            break

if __name__ == "__main__":
    display_predictions()
