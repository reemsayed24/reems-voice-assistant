import whisper
import numpy as np
import soundfile as sf
from io import BytesIO

def transcribe_audio(audio_bytes):
    model = whisper.load_model("small")
    audio_array, sr = sf.read(BytesIO(audio_bytes))
    audio_float = audio_array.astype(np.float32)
    result = model.transcribe(audio_float, language=None)
    return result["text"]