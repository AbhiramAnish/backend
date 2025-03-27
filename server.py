from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

from reportGeneration import ReportGeneration
rG = ReportGeneration()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all routes for development

# Function to safely load ML models
def load_model(path):
    try:
        with open(path, "rb") as model_file:
            return pickle.load(model_file)
    except Exception as e:
        print(f"❌ Error loading model {path}: {e}")
        return None

model1 = load_model("random_forest_model.pkl")  
model2 = load_model("mark_1_Landslide2.pkl")  

print(f"✅ Model 1 Type: {type(model1)}")
print(f"✅ Model 2 Type: {type(model2)}")

@app.route("/", methods=["GET"])
def home():
    return "Flask backend is running!"

@app.route("/predict", methods=["POST"])
def predict():
    if model1 is None or model2 is None:
        print("❌ One or both ML models failed to load!")
        return jsonify({"error": "One or both ML models are missing"}), 500  

    data = request.get_json()
    print(f"📥 Received Data: {data}")  # Log incoming data
    
    if not data or "weather" not in data:
        print("❌ Invalid input format")
        return jsonify({"error": "Invalid input"}), 400

    weather_features = data["weather"]
    
    if not isinstance(weather_features, list) or len(weather_features) != 3:
        print(f"❌ Invalid input shape: {weather_features}")
        return jsonify({"error": "Weather data must be a list of 3 numerical values"}), 400
    
    try:
        # Convert input for model1 (expects 3 features)
        weather_array1 = np.array(weather_features, dtype=float).reshape(1, -1)
        print(f"✅ Model 1 Input Shape: {weather_array1.shape}")
        print("\n\t",weather_array1,"\n")

        # Directly providing static inputs to model2 (expects 4 features)
        weather_array2 = np.array([1, 2, 3, 4], dtype=float).reshape(1, -1)  # Hardcoded for now
        print(f"✅ Model 2 Input Shape: {weather_array2.shape}")

        # Directly adding 4th static input to weather_array1 and giving to model2 (expects 4 features)
        weather_array3 = np.append(weather_array1,10.5).reshape(1, -1)
        print(f"✅ Model 2 2nd Input Shape: {weather_array3.shape}")

        # Get predictions
        prediction1 = model1.predict(weather_array1)[0]
        prediction2 = model2.predict(weather_array3)[0]

        print(f"✅ Prediction 1: {prediction1}, Prediction 2: {prediction2}")

        # print(type(data))
        # print(weather_features)
        # Save to CSV
        rG.generateReport([{"feature1": weather_features[0], 
                            "feature2": weather_features[1], 
                            "feature3": weather_features[2]}], 
                          prediction1, prediction2, 'output1.csv')

        return jsonify({
            "prediction1": str(prediction1),
            "prediction2": str(prediction2)
        })
    except Exception as e:
        print(f"❌ Prediction failed: {e}")
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Debug mode enabled
