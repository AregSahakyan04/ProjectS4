import streamlit as st

def load_user_settings():
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""
    if "theme" not in st.session_state:
        st.session_state.theme = "Dark"
    if "reply_mode" not in st.session_state:
        st.session_state.reply_mode = "Short"
    if "name_confirmed" not in st.session_state:
        st.session_state.name_confirmed = False

def apply_theme():
    css_file = "styling/dark.css" if st.session_state.theme == "Dark" else "styling/light.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    if st.button("🚪 Logout", key="logout_button"):
        st.session_state.user = None
        st.switch_page("auth.py")

def sidebar_settings():
    with st.sidebar:
        st.markdown("## ⚙️ Settings")

        # Name section — editable only if not confirmed
        if not st.session_state.name_confirmed:
            name = st.text_input("Enter your name", value=st.session_state.user_name)
            if name and st.button("Save Name"):
                st.session_state.user_name = name
                st.session_state.name_confirmed = True
        else:
            st.markdown(f"👤 **Name:** {st.session_state.user_name}")
            if st.button("Change Name"):
                st.session_state.name_confirmed = False

        new_theme = st.radio("Theme", ["Dark", "Light"], index=0 if st.session_state.theme == "Dark" else 1)

        # Apply and rerun only if changed
        if new_theme != st.session_state.theme:
            st.session_state.theme = new_theme
            st.rerun()
