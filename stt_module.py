import requests
import time

def transcribe_audio(audio_bytes, hf_token):
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
    headers = {"Authorization": f"Bearer {hf_token}"}
    
    for attempt in range(5):
        response = requests.post(API_URL, headers=headers, data=audio_bytes)
        
        if response.status_code == 200:
            try:
                result = response.json()
                if "text" in result:
                    return result["text"]
            except Exception:
                pass
        
        if response.status_code == 503:
            time.sleep(10)
            continue
            
        time.sleep(5)
    
    return "Could not transcribe. Please try again."
