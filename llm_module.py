import requests
import datetime

def get_response(user_text, history, api_key):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    system_prompt = f"""You are a smart, warm, and helpful voice assistant named ReeM.
Current date and time: {current_time}
Keep your answers clear and helpful.
If the user speaks Arabic, reply in Arabic naturally.
If the user speaks English, reply in English.
If you do not know something, say so honestly."""

    messages = [{"role": "system", "content": system_prompt}]
    messages += history[-14:]
    messages.append({"role": "user", "content": user_text})

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": messages,
        "max_tokens": 600,
        "temperature": 0.7
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=data
    )

    result = response.json()
    return result["choices"][0]["message"]["content"]
