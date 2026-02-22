import streamlit as st
from audio_recorder_streamlit import audio_recorder
from stt_module import transcribe_audio
from tts_module import text_to_speech
from llm_module import get_response

st.set_page_config(
    page_title="ReeM's Voice Assistant",
    page_icon="🎙️",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@300;400;500&display=swap');

    html, body, .stApp {
        background-color: #f5f0eb;
        font-family: 'Inter', sans-serif;
    }

    section[data-testid="stSidebar"] {
        background-color: #ede8e2;
        border-right: 1px solid #d6cfc7;
    }

    h1 {
        font-family: 'Playfair Display', serif;
        color: #6b2737;
        font-size: 2.2rem;
        margin-bottom: 0;
    }

    .subtitle {
        color: #9e8f83;
        font-size: 0.85rem;
        margin-top: 2px;
        margin-bottom: 24px;
        font-weight: 300;
        letter-spacing: 0.05em;
    }

    .user-msg {
        background-color: #e8e0d8;
        color: #3a2f2a;
        padding: 14px 18px;
        border-radius: 16px 16px 4px 16px;
        margin: 8px 0;
        font-size: 0.95rem;
        line-height: 1.6;
        border-left: 3px solid #c4a882;
    }

    .ai-msg {
        background-color: #6b2737;
        color: #f9f4ef;
        padding: 14px 18px;
        border-radius: 16px 16px 16px 4px;
        margin: 8px 0;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .status-box {
        background-color: #ede8e2;
        border: 1px solid #d6cfc7;
        border-radius: 12px;
        padding: 14px 18px;
        color: #6b5c52;
        font-size: 0.9rem;
        margin-top: 12px;
    }

    .stButton > button {
        background-color: #6b2737;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 8px 20px;
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        transition: background 0.2s;
    }

    .stButton > button:hover {
        background-color: #85303f;
    }

    .stSelectbox label, .stTextInput label {
        color: #6b5c52;
        font-size: 0.85rem;
    }

    div[data-testid="stAudio"] {
        margin-top: 10px;
    }

    .empty-state {
        color: #b0a398;
        font-size: 0.9rem;
        font-style: italic;
        text-align: center;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)


# Header
st.markdown("<h1>🎙️ ReeM's Voice Assistant</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Whisper STT &nbsp;·&nbsp; Mistral LLM &nbsp;·&nbsp; gTTS</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    hf_token = st.text_input("HuggingFace Token", type="password", placeholder="hf_xxxxxxxxxxxx")
    lang = st.selectbox("Voice Response Language", ["en", "ar"])
    st.markdown("---")
    if st.button("🗑️ Clear Conversation"):
        st.session_state.history = []
        st.session_state.chat_log = []
        st.rerun()
    st.markdown("---")
    st.markdown('<p style="color:#b0a398; font-size:0.8rem;">Made with 🤍 by ReeM</p>', unsafe_allow_html=True)

# Session state
if "history" not in st.session_state:
    st.session_state.history = []
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# Layout
left, right = st.columns([1, 2], gap="large")

with left:
    st.markdown("#### 🎤 Speak")
    audio_bytes = audio_recorder(
        text="Click & Speak",
        recording_color="#6b2737",
        neutral_color="#c4a882",
        icon_size="2x"
    )

    if audio_bytes and hf_token:
        st.audio(audio_bytes, format="audio/wav")

        with st.spinner("Listening..."):
            user_text = transcribe_audio(audio_bytes)

        st.markdown(f'<div class="status-box">🗣️ <b>You said:</b><br>{user_text}</div>', unsafe_allow_html=True)

        with st.spinner("ReeM is thinking..."):
            ai_reply = get_response(user_text, st.session_state.history, hf_token)

        st.session_state.history.append({"role": "user", "content": user_text})
        st.session_state.history.append({"role": "assistant", "content": ai_reply})
        st.session_state.chat_log.append(("user", user_text))
        st.session_state.chat_log.append(("ai", ai_reply))

        with st.spinner("Generating voice..."):
            audio_reply = text_to_speech(ai_reply, lang=lang)

        st.audio(audio_reply, format="audio/mp3", autoplay=True)

    elif audio_bytes and not hf_token:
        st.warning("Please add your HuggingFace token in the sidebar.")

with right:
    st.markdown("#### 💬 Conversation")
    if not st.session_state.chat_log:
        st.markdown('<p class="empty-state">No conversation yet.<br>Click the mic and start talking 🎙️</p>', unsafe_allow_html=True)
    for role, msg in st.session_state.chat_log:
        if role == "user":
            st.markdown(f'<div class="user-msg">👤 &nbsp;{msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="ai-msg">🤍 &nbsp;{msg}</div>', unsafe_allow_html=True)
```

---

### requirements.txt
```
streamlit
openai-whisper
gtts
huggingface_hub
audio-recorder-streamlit
soundfile
numpy
torch