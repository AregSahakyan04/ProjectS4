📝 Project Overview
A Streamlit-based web application designed to support student mental health through:
🤖 AI-powered chatbot (GPT-4) for emotional support
📊 Mood tracking with visualization
📔 Secure journaling system
🔐 User authentication

Important Note: This repository does NOT include the .env file containing the OpenAI API key required for the chatbot functionality. You will need to provide your own API key to use this feature.

🛠️ Technologies Used
Frontend: Streamlit
Backend: Python
Database: SQLite
AI: OpenAI API (GPT-4)
Styling: CSS

⚙️ Setup Instructions
Prerequisites
Python 3.8+

OpenAI API key (if using chatbot feature)

- Installation -
Clone the repository:

- bash -
git clone https://github.com/[your-username]/mental-health-companion.git
cd mental-health-companion
Install dependencies:

- bash -
pip install -r requirements.txt
Create a .env file in the root directory with your OpenAI API key:

OPENAI_API_KEY=your_api_key_here

Run the application:
bash - streamlit run 1_Home.py

⚠️ Important Notes

API Key Requirement:
The chatbot feature requires an OpenAI API key
You must provide your own key in a .env file
Never commit your .env file to version control

Data Privacy:
All user data is stored locally in mental_health.db
Passwords are hashed using SHA-256

🌟 Features
User registration and login
Light/dark theme toggle
Daily mood tracking with visualization
Private journal with date-based entries
AI-powered mental health chatbot
Local data storage (no cloud dependencies)

🙏 Acknowledgments
Streamlit for the web framework
OpenAI for the GPT API
Research in cognitive behavioral therapy and expressive writing
