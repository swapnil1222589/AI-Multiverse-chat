import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Multiverse Chat",
    page_icon="🤖",
    layout="centered"
)

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]                 
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

avatars = {
    "Friendly Teacher": "👩‍🏫",
    "Expert Hacker": "💻",
    "Stand-up Comedian": "😂",
    "Panicked College Student at 3 AM": "😱",
    "1920s Mafia Boss": "🕴️",
    "Highly Sarcastic Fitness Coach": "🏋️"
}

bot_avatar = avatars.get(personality, "🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(
        message["role"],
        avatar=bot_avatar if message["role"] == "assistant" else None
    ):
        st.write(message["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    instructions = f"""
You are acting as: {personality}

Intensity Level: {intensity}/10

Rules:
- Stay completely in character.
- Higher intensity means a stronger personality.
- Never break character.
- Give useful, engaging responses.
"""

    conversation = instructions + "\n\n"

    for message in st.session_state.messages:
        conversation += f"{message['role']}: {message['content']}\n"

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=conversation
        )

        answer = response.text or "I couldn't generate a response."

        with st.chat_message("assistant", avatar=bot_avatar):
            st.write(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        st.error(f"Gemini API error: {e}")
