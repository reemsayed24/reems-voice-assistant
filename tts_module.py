from gtts import gTTS
from io import BytesIO

def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang, slow=False)
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer