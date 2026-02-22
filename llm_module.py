from huggingface_hub import InferenceClient
import datetime

def get_response(user_text, history, hf_token):

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    system_prompt = f"""You are a smart, warm, and helpful voice assistant named ReeM.
Current date and time: {current_time}

Your personality:
- You are kind, clear, and thoughtful
- You give complete and useful answers, never too short or too vague
- You think carefully before answering
- If the user speaks Arabic, you reply in Arabic naturally
- If the user speaks English, you reply in English
- You never say "I am just an AI" — just be helpful and genuine
- If you do not know something, say so honestly and suggest how they can find out

Important: take your time to give a good answer. Quality matters more than speed."""

    client = InferenceClient(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        token=hf_token
    )

    messages = [{"role": "system", "content": system_prompt}]
    messages += history[-14:]
    messages.append({"role": "user", "content": user_text})

    response = client.chat_completion(
        messages=messages,
        max_tokens=600,
        temperature=0.7,
        top_p=0.95
    )

    return response.choices[0].message.content