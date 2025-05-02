import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file with API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def display_chat(history):
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for sender, msg in history:
        class_name = "user-msg" if sender == "You" else "bot-msg"
        st.markdown(f'<div class="{class_name}"><strong>{sender}:</strong> {msg}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def get_ai_response(user_input):
    try:
        # Build message list from chat history
        messages = [{"role": "system", "content": "You are a compassionate mental health assistant. Be calm, kind, and helpful."}]

        for sender, msg in st.session_state.chat_history:
            role = "user" if sender == "You" else "assistant"
            messages.append({"role": role, "content": msg})

        messages.append({"role": "user", "content": user_input})

        # Send request to GPT-4o-mini
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Fast and smart
            messages=messages
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Error: {str(e)}"
