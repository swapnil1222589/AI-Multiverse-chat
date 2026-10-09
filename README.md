🤖 AI Multiverse Chat
One chat interface. Multiple AI personalities. Powered by Google's Gemini models.

AI Multiverse Chat is a Streamlit application that lets you chat with the same AI through different personalities—from a friendly teacher to a sarcastic fitness coach. Choose a character, adjust how strongly it expresses that personality, and start a conversation.
✨ Features
- Multiple AI personalities — Friendly Teacher, Expert Hacker, Stand-up Comedian, Panicked College Student at 3 AM, 1920s Mafia Boss, and Highly Sarcastic Fitness Coach.
- Adjustable personality intensity — Tune the character's tone from 1 to 10.
- Conversational chat UI — Chat-style messages with session-based conversation history.
- Gemini-powered responses — Uses the Google Gen AI Python SDK and the gemini-2.5-flash model. 
- Simple local setup — Built with Streamlit and Python.
🧰 Tech Stack
- Python
- Streamlit — Web interface and chat experience
- Google Gen AI SDK (google-genai) — Gemini model access
🚀 Getting Started
1. Clone the repository
git clone https://github.com/swapnil1222589/AI-Multiverse-chat.git
cd AI-Multiverse-chat
2. Create and activate a virtual environment (recommended)
Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure your Gemini API key
Create a Streamlit secrets file at .streamlit/secrets.toml:
GEMINI_API_KEY = "your_gemini_api_key_here"
Get an API key from Google AI Studio.
Security: Keep your API key private. Do not commit .streamlit/secrets.toml or hard-code API keys in source files. For deployment, add GEMINI_API_KEY using your hosting platform's secrets settings.

5. Run the app
streamlit run app.py
Streamlit will print a local URL in the terminal (usually http://localhost:8501). Open it in your browser.
💬 Available Personalities
Personality	Style
Friendly Teacher	Patient, clear, and encouraging
Expert Hacker	Technical and problem-solving focused
Stand-up Comedian	Humorous and playful
Panicked College Student at 3 AM	Dramatic, stressed, and relatable
1920s Mafia Boss	Theatrical, old-school tough-guy energy
Highly Sarcastic Fitness Coach	Direct, energetic, and sarcastic


The Intensity Level slider controls how strongly the selected personality comes across.
📁 Project Structure
AI-Multiverse-chat/
├── app.py
├── requirements.txt
└── README.md
⚙️ Configuration
The application reads the API key from Streamlit secrets using GEMINI_API_KEY. Make sure this secret is configured before starting the app.
🛠️ Troubleshooting
- Missing GEMINI_API_KEY — Confirm that .streamlit/secrets.toml exists and contains the key, or configure the secret in your deployment platform.
- Dependency/import errors — Activate your virtual environment and run pip install -r requirements.txt.
- API errors or quota limits — Verify your API key, model availability, billing/quota, and Google AI Studio settings.
🗺️ Possible Next Improvements
- Add a clear-chat and conversation-export option.
- Preserve separate chat histories for each personality.
- Add more personalities and customizable system prompts.
- Improve API error handling and provide friendly error messages.
👨‍💻 Author
Swapnil Ghuge
- GitHub: @swapnil1222589
📄 License
No license is currently specified in this repository. Add a LICENSE file if you want to clarify how others may use, modify, and distribute the project.
