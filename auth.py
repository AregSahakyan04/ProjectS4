import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))
from database import init_db, register_user, login_user

st.set_page_config(page_title="Login", layout="centered")

hide_sidebar = """
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
"""

st.markdown(hide_sidebar, unsafe_allow_html=True)

# Initialize DB
init_db()

if "user" in st.session_state and st.session_state.user:
    st.switch_page("pages/1_Home.py")  # Automatically redirect if logged in

# Session user tracker
if "user" not in st.session_state:
    st.session_state.user = None

# If already logged in, go to home
if st.session_state.user:
    st.success(f"Welcome back, {st.session_state.user}!")
    st.markdown("[Go to Home 🧠](Home)")
    st.stop()

# Login/Register UI
st.title("🔐 Welcome to Mental Health Companion")
mode = st.radio("Choose an option", ["Login", "Register"])

if mode == "Login":
    st.subheader("Log in to your account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login", key="login_button"):
        if login_user(username, password):
            st.session_state.user = username
            st.rerun()  # 🔁 Forces refresh so user is logged in immediately
        else:
            st.error("Invalid username or password.")

else:
    st.subheader("Create a new account")
    new_username = st.text_input("Create Username")
    new_email = st.text_input("Email")
    new_password = st.text_input("Create Password", type="password")

    if st.button("Register", key="register_button"):
        if new_username and new_email and new_password:
            if register_user(new_username, new_email, new_password):
                st.success("✅ Account created successfully! You can now log in.")
            else:
                st.error("⚠️ Username or email already exists.")
        else:
            st.warning("Please fill in all fields.")
