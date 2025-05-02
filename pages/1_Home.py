import streamlit as st

st.set_page_config(page_title="Mental Health Chat", layout="centered")

from chat import get_ai_response, display_chat
from settings import load_user_settings, sidebar_settings, apply_theme

if "user" not in st.session_state or st.session_state.user is None:
    st.switch_page("auth.py")

# Load global settings
load_user_settings()
sidebar_settings()
apply_theme()

# Greeting using name
st.title(f"🧠 Hello, {st.session_state.user_name}! Mental Health Companion is here to help you")

# Session state setup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_message" not in st.session_state:
    st.session_state.user_message = ""
if "clear_input" not in st.session_state:
    st.session_state.clear_input = False
if st.button("🔄 Reset Conversation"):
    st.session_state.chat_history = []
    st.rerun()

# Clear input after send
if st.session_state.clear_input:
    st.session_state.user_message = ""
    st.session_state.clear_input = False

# Chat input
user_input = st.text_input("Type your message", key="user_message")
if st.button("Send") and user_input:
    response = get_ai_response(user_input)  # ← DialoGPT replaces rule-based
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))
    st.session_state.clear_input = True
    st.rerun()

with st.sidebar:
    if st.button("🚪 Logout"):
        st.session_state.user = None
        st.rerun()

# Chat display
st.markdown("### 💬 Conversation")
display_chat(st.session_state.chat_history)


