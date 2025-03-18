from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

import SMS
obj = SMS.sms()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load ML model
model = pickle.load(open("random_forest_model.pkl", "rb"))

@app.route("/", methods=["GET"])  # Root route to check if backend is live
def home():
    return "Flask backend is running!"

@app.route("/predict", methods=["POST"])  # Ensure this route exists
def predict():
    data = request.json
    if not data or "weather" not in data:
        return jsonify({"error": "Invalid input"}), 400  # Handle missing data

    weather_features = np.array(data["weather"]).reshape(1, -1)
    prediction = model.predict(weather_features)[0]
    obj.msg(prediction)
    return jsonify({"prediction": str(prediction)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Allow external connections

