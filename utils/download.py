import requests
import os

# Your Drive File ID
FILE_ID = "1KjygXsSIGGVp6c9UVhdU9_rNCV6GQlWy"
DESTINATION = "models/ensemble_medical_model.joblib"

def download_model_from_drive(file_id="1KjygXsSIGGVp6c9UVhdU9_rNCV6GQlWy", destination="models/ensemble_medical_model.joblib"):
    if not os.path.exists("models"):
        os.makedirs("models")

    if os.path.exists(destination):
        print("✅ Model already exists.")
        return

    print("📥 Downloading model from Google Drive...")

    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    
    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)
    print("✅ Download complete.")


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:  # filter out keep-alive chunks
                f.write(chunk)
