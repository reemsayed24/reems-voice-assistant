import requests
from io import BytesIO

def transcribe_audio(audio_bytes, hf_token):
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
    headers = {"Authorization": f"Bearer {hf_token}"}
    response = requests.post(API_URL, headers=headers, data=audio_bytes)
    result = response.json()
    if "text" in result:
        return result["text"]
    else:
        return "Could not transcribe audio. Please try again."
