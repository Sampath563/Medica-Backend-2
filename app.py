from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

from utils.download import download_model_from_drive

app = Flask(__name__)
CORS(app)

MODEL_PATH = "models/ensemble_medical_model.joblib"

# Download and load model
download_model_from_drive()

print("📦 Loading model...")
model = joblib.load(MODEL_PATH)
print("✅ Model loaded successfully.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        symptoms = input_data.get('symptoms')
        age = input_data.get('age')

        # TODO: Replace this with your actual preprocessing + prediction
        # X = preprocess(symptoms, age)
        # prediction = model.predict(X)[0]
        prediction = "PredictedDisease"

        return jsonify({'prediction': prediction})
    
    except Exception as e:
        print("❌ Prediction error:", str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return "Medica backend is running!"

if __name__ == '__main__':
    app.run(debug=True)
