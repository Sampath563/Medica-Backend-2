from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pickle

from utils.download import download_model_from_drive

app = Flask(__name__)
CORS(app)

# Model file info
MODEL_PATH = "models/ensemble_medical_model.pkl"
MODEL_FILE_ID = "15J6ieS97efmxGySE6c_9yMEbwZdMxpII"

# Ensure model folder exists
os.makedirs("models", exist_ok=True)

# Download model if not already present
if not os.path.exists(MODEL_PATH):
    print("📥 Downloading model from Google Drive...")
    download_model_from_drive(MODEL_FILE_ID, MODEL_PATH)
    print("✅ Download complete.")

# Load model using pickle
print("📦 Loading model...")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
print("✅ Model loaded successfully.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        symptoms = input_data.get('symptoms')
        age = input_data.get('age')

        # Dummy response for now — replace with actual preprocessing/prediction
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
