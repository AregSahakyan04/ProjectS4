import streamlit as st
import sqlite3
from datetime import date, datetime
from settings import load_user_settings, sidebar_settings, apply_theme

st.set_page_config(page_title="Daily Journal", layout="centered")

# 🔐 Redirect to login if not logged in
if "user" not in st.session_state or st.session_state.user is None:
    st.switch_page("auth")

st.title("📓 Your Daily Journal")

# 📅 Date selector
selected_date = st.date_input("Choose a date", value=date.today())

load_user_settings()
apply_theme()
sidebar_settings()

# 💾 Save entry to DB (NEW: does not overwrite)
def save_entry(username, entry_date, text):
    conn = sqlite3.connect("mental_health.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO journal (username, entry_date, entry, timestamp) VALUES (?, ?, ?, ?)",
        (username, entry_date, text, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()

# 📤 Retrieve all entries for date
def load_entries(username, entry_date):
    conn = sqlite3.connect("mental_health.db")
    c = conn.cursor()
    c.execute(
        "SELECT entry, timestamp FROM journal WHERE username=? AND entry_date=? ORDER BY timestamp ASC",
        (username, entry_date)
    )
    rows = c.fetchall()
    conn.close()
    return rows

# Input box
note = st.text_area("Write your thoughts or reflections:", height=200)

# Save button
if st.button("Save Entry"):
    if note.strip():
        save_entry(st.session_state.user, str(selected_date), note.strip())
        st.success("✅ Entry saved.")
        st.rerun()

# Show all entries for selected date
entries = load_entries(st.session_state.user, str(selected_date))
if entries:
    st.markdown("### 📖 Entries for this day:")
    for entry, timestamp in entries:
        st.markdown(f"🕒 *{timestamp}*")
        st.info(entry)
else:
    st.info("No entries for this date yet.")
