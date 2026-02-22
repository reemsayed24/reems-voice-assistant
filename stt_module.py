import requests

def transcribe_audio(audio_bytes, api_key):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    files = {
        "file": ("audio.wav", audio_bytes, "audio/wav"),
        "model": (None, "whisper-large-v3"),
    }
    response = requests.post(
        "https://api.groq.com/openai/v1/audio/transcriptions",
        headers=headers,
        files=files
    )
    result = response.json()
    return result.get("text", "Could not transcribe. Please try again.")
