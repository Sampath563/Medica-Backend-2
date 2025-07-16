from flask import Flask, request, jsonify
from flask_cors import CORS
from huggingface_hub import hf_hub_download
import joblib
import os

app = Flask(__name__)
CORS(app)

# Set custom cache directory to /tmp (safe for Hugging Face Spaces)
os.environ["HF_HOME"] = "/tmp"

# Download model from Hugging Face Hub
print("📥 Downloading model from Hugging Face Hub...")
model_path = hf_hub_download(
    repo_id="Sampath563/medica-model",
    filename="ensemble_medical_model.pkl",
    cache_dir="/tmp"  # ✅ prevent permission error
)

# Load the model
print("📦 Loading model...")
model = joblib.load(model_path)
print("✅ Model loaded successfully.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Dummy prediction for now
        prediction = "PredictedDisease"
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "Medica backend running on Hugging Face Spaces"

if __name__ == '__main__':
    app.run(debug=True)
