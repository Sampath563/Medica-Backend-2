from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

from utils.download import download_model_from_drive

app = Flask(__name__)
CORS(app)

# Load model
MODEL_PATH = "models/ensemble_medical_model.joblib"
MODEL_FILE_ID = "1KjygXsSIGGVp6c9UVhdU9_rNCV6GQlWy"

os.makedirs("models", exist_ok=True)

if not os.path.exists(MODEL_PATH):
    print("📥 Downloading model from Google Drive...")
    download_model_from_drive(MODEL_FILE_ID, MODEL_PATH)

print("📦 Loading model...")
model = joblib.load(MODEL_PATH)
print("✅ Model loaded successfully.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        symptoms = input_data.get('symptoms')
        age = input_data.get('age')

        # X = preprocess(symptoms, age)
        prediction = "PredictedDisease"  # Replace with: model.predict(X)
        return jsonify({'prediction': prediction})
    
    except Exception as e:
        print("❌ Prediction error:", str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return "Medica backend is running!"

if __name__ == '__main__':
    app.run(debug=True)
