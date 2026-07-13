import streamlit as st
import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"  # Replace with your Gemini API key
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Multiverse Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Multiverse Chat")
st.caption("Talk with different AI personalities powered by Gemini")

st.sidebar.title("⚙️ App Settings")

personality = st.sidebar.selectbox(
    "Choose AI Personality",
    [
        "Friendly Teacher",
        "Expert Hacker",
        "Stand-up Comedian",
        "Panicked College Student at 3 AM",
        "1920s Mafia Boss",
        "Highly Sarcastic Fitness Coach"
    ]
)

intensity = st.sidebar.slider(
    "Intensity Level",
    min_value=1,
    max_value=10,
    value=5
)

if personality == "Friendly Teacher":
    bot_avatar = "👩‍🏫"
elif personality == "Expert Hacker":
    bot_avatar = "💻"
elif personality == "Stand-up Comedian":
    bot_avatar = "😂"
elif personality == "Panicked College Student at 3 AM":
    bot_avatar = "😱"
elif personality == "1920s Mafia Boss":
    bot_avatar = "🕴️"
elif personality == "Highly Sarcastic Fitness Coach":
    bot_avatar = "🏋️"
else:
    bot_avatar = "🤖"

user_input = st.text_input("Type your message...")

if st.button("SEND"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        ai_instructions = f"""
You are acting as: {personality}

Intensity Level: {intensity}/10

Rules:
- Stay completely in character.
- The higher the intensity, the more dramatic and realistic your personality becomes.
- Never break character.
- Give detailed and engaging responses.
- Respond naturally like a real person.
"""
        final_prompt = ai_instructions + "\n\nUser: " + user_input
        response = model.generate_content(final_prompt)

        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("assistant", avatar=bot_avatar):
            st.write(response.text)
