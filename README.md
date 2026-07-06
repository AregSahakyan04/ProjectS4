# Mental Health Companion

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

A Streamlit web app that supports student mental health through:

- 🤖 AI-powered chatbot (GPT-4) for emotional support
- 📊 Mood tracking with visualization
- 📔 Secure journaling system
- 🔐 User authentication (bcrypt-hashed passwords)

## Setup

**Prerequisites:** Python 3.8+, an OpenAI API key (only needed for the chatbot feature).

1. Clone the repository:
   ```bash
   git clone https://github.com/AregSahakyan04/mental-health-companion.git
   cd mental-health-companion
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   streamlit run auth.py
   ```

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** SQLite
- **AI:** OpenAI API (GPT-4)
- **Charts:** Matplotlib

## Notes

- The `.env` file is not included in this repository — you must supply your own OpenAI API key to use the chatbot feature.
- All user data is stored locally in `mental_health.db` (no cloud dependency).
- Passwords are hashed with **bcrypt** (salted, adaptive cost) rather than raw SHA-256, to avoid the rainbow-table weaknesses of unsalted fast hashes.

## Features

- User registration and login
- Light/dark theme toggle
- Daily mood tracking with visualization
- Private journal with date-based entries
- AI-powered mental health chatbot
- Local data storage (no cloud dependencies)

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [OpenAI](https://openai.com/) for the GPT API
