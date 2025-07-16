from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pickle
import gdown

app = Flask(__name__)
CORS(app)

# Model config
MODEL_PATH = "models/ensemble_medical_model.pkl"
MODEL_FILE_ID = "15J6ieS97efmxGySE6c_9yMEbwZdMxpII"
MODEL_URL = f"https://drive.google.com/uc?id={MODEL_FILE_ID}"

# Ensure model directory exists
os.makedirs("models", exist_ok=True)

# Download model if missing
if not os.path.exists(MODEL_PATH):
    print("📥 Downloading model from Google Drive...")
    gdown.download(MODEL_URL, MODEL_PATH, quiet=False)
    print("✅ Download complete.")

# Load model using pickle
print("📦 Loading model...")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
print("✅ Model loaded successfully.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        symptoms = data.get('symptoms')
        age = data.get('age')

        # Dummy return, replace with actual model.predict
        return jsonify({'prediction': "PredictedDisease"})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return "Medica backend is running!"

if __name__ == '__main__':
    app.run(debug=True)
