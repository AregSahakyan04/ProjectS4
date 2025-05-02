import streamlit as st
from mood_tracker import log_mood, show_mood_chart
from utils import save_chat_to_file
from settings import load_user_settings, sidebar_settings, apply_theme

st.set_page_config(page_title="Mood Tracker", layout="centered")

load_user_settings()
sidebar_settings()
apply_theme()

st.title("📊 Mood Tracker")

if "mood_log" not in st.session_state:
    st.session_state.mood_log = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

mood = st.slider("How are you feeling?", 1, 10, value=5)

col1, col2 = st.columns(2)
if col1.button("Log Mood"):
    log_mood(st.session_state.mood_log, mood)
if col2.button("Show Mood Chart"):
    show_mood_chart(st.session_state.mood_log)

st.markdown("---")
st.markdown("### 💾 Save Chat Log")
if st.button("Save Chat Log"):
    save_chat_to_file(st.session_state.chat_history)
    st.success("Chat saved to chat_log.txt!")
