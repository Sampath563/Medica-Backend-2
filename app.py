from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from huggingface_hub import hf_hub_download

app = Flask(__name__)
CORS(app)

# Download model from Hugging Face Hub
MODEL_REPO = "Sampath563/medica-model"
MODEL_FILENAME = "ensemble_medical_model.pkl"

print("📥 Downloading model from Hugging Face Hub...")
model_path = hf_hub_download(repo_id=MODEL_REPO, filename=MODEL_FILENAME)
print("✅ Model downloaded.")

print("📦 Loading model...")
model = joblib.load(model_path)
print("✅ Model loaded successfully.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        symptoms = data.get("symptoms")
        age = data.get("age")

        # TODO: Replace this with real preprocessing and model.predict
        prediction = "PredictedDisease"
        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return "Medica backend is running!"

if __name__ == '__main__':
    app.run(debug=True)
