# 🎙️ ReeM's Voice Assistant

A real-time AI-powered voice assistant built with Streamlit, Whisper STT, Mistral LLM, and gTTS.

---

## ✨ Features

- 🎤 **Speech to Text** — Records your voice and converts it to text using OpenAI Whisper
- 🧠 **AI Brain** — Understands your question and generates a smart response using Mistral-7B
- 🔊 **Text to Speech** — Converts the AI response back to voice using gTTS
- 💬 **Conversation Memory** — Remembers the last 14 messages for natural conversation flow
- 🌍 **Multilingual** — Supports both English and Arabic
- 🎨 **Warm UI** — Clean and comfortable design with earthy tones and burgundy accents

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Speech to Text | OpenAI Whisper (small) |
| Language Model | Mistral-7B-Instruct via HuggingFace |
| Text to Speech | gTTS |
| Deployment | Streamlit Cloud |

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/reems-voice-assistant.git
cd reems-voice-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

### 4. Add your HuggingFace token in the sidebar

Get your free token from [huggingface.co](https://huggingface.co/settings/tokens)

---

## 📁 Project Structure
```
reems-voice-assistant/
├── app.py              # Main Streamlit application
├── stt_module.py       # Speech to Text using Whisper
├── tts_module.py       # Text to Speech using gTTS
├── llm_module.py       # AI responses using Mistral
├── requirements.txt    # Project dependencies
└── README.md
```

---

## 🌐 Live Demo

[Click here to try the app](https://YOUR_APP_NAME.streamlit.app)

---

## 📌 Task Submission

This project was built as part of the **Uneeq Interns** program task:
> Implement a real-time voice assistant using STT and TTS

---

Made with 🤍 by ReeM