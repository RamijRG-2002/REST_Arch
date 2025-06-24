from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

@app.route("/baishik")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route('/predict', methods = ['POST'])
def get_Prediction():
    data = request.get_json()
    print(data["sepal_length"])
    return jsonify({"message":"JSON data received", "data":data})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)