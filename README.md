# Iris Species Prediction API

This project demonstrates a simple REST API using Flask for predicting the species of iris flowers using a pre-trained machine learning model. The API receives flower measurements via a POST request and returns the predicted species. The project also includes an example of how to test the API using Postman.

## Project Structure

```
.
├── flask_quickstart.py      # Basic Flask app (demo endpoint)
├── model_predict.py         # Main API with ML prediction
├── svm_iris_model.pkl       # Pre-trained SVM model for iris prediction
├── requirements.txt         # Python dependencies
├── output.png               # Postman screenshot (API test example)
└── env/                     # (Optional) Python virtual environment
```

---

## 1. Setup Instructions

### Prerequisites

- Python 3.7+
- `pip` (Python package manager)
- (Optional) Postman for API testing

### 1.1. Clone the Repository

```bash
git clone <your-repo-url>
cd Flask_Tut
```

### 1.2. Create a Virtual Environment (Recommended)

```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate
```

### 1.3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Running the API Server

The main API is implemented in `model_predict.py`. It loads a pre-trained SVM model and exposes a `/predict` endpoint.

### Start the Server

```bash
python model_predict.py
```

The server will start at `http://0.0.0.0:5000` (or `http://127.0.0.1:5000`).

---

## 3. API Usage

### Endpoint

- **URL:** `/predict`
- **Method:** `POST`
- **Content-Type:** `application/json`
- **Request Body Example:**

```json
{
  "sepal_length": 5.1,
  "sepal_width": 4.2,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

### Response Example

```json
{
  "input_data": {
    "sepal_length": 5.1,
    "sepal_width": 4.2,
    "petal_length": 1.4,
    "petal_width": 0.2
  },
  "message": "Prediction successful",
  "prediction": "setosa"
}
```

---

## 4. Testing with Postman

You can use Postman to send a POST request to the API. Refer to the included screenshot (`output.png`) for a visual guide.

**Steps:**

1. Open Postman and create a new POST request to `http://127.0.0.1:5000/predict`.
2. Set the request body to `raw` and select `JSON`.
3. Enter the sample JSON data as shown above.
4. Click **Send**.
5. You should receive a response with the predicted species and the input data.

![Postman Example](output.png)

---

## 5. Project Details

- **flask_quickstart.py:** A basic Flask app with a demo endpoint (`/ramij`) and a simple `/predict` endpoint that echoes received JSON (for learning purposes).
- **model_predict.py:** The main API. Loads a pre-trained SVM model (`svm_iris_model.pkl`) and exposes a `/predict` endpoint. Accepts iris measurements, predicts the species, and returns the result as JSON.
- **svm_iris_model.pkl:** The serialized machine learning model trained on the Iris dataset.
- **requirements.txt:** Lists all Python dependencies required to run the project.

---

## 6. Notes

- Ensure `svm_iris_model.pkl` is present in the project directory.
- The API will return an error if any required field is missing or if the input format is incorrect.
- The included Postman screenshot (`output.png`) shows a successful prediction request and response.

---

## 7. References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)

---
