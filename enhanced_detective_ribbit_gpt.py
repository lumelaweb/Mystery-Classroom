import streamlit as st
from openai import OpenAI
import os

# Load OpenAI API Key securely
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Marketing Stack Matcher", page_icon="🧩")
st.title("🧩 Marketing Tool Match GPT")

# Default assistant greeting message
default_message = (
    "Hey there! 👋 I’m Marketing Tool Match GPT, created by LumelaWeb. "
    "My job is to help small business owners, solopreneurs, and consultants like you find the right marketing tools "
    "that actually fit your business — no fluff, no overwhelm.\n\n"
    "Whether you're building your first system or trying to clean up a tech mess, I help you match your goals and "
    "growth plans with tools for things like:\n\n"
    "- CRM (Customer Relationship Management)\n"
    "- Email marketing\n"
    "- Booking/calendar tools\n"
    "- Landing pages\n"
    "- Analytics\n"
    "…and more.\n\n"
    "I’m built on the same strategic approach LumelaWeb uses in their 90-Day Website Growth Blueprint. "
    "If you'd rather talk to a human, you can always book a free 30-minute call here: https://calendly.com/lumelaweb/30min\n\n"
    "Want me to help match you with the right tools? I’ll just need to ask a few quick questions. Ready to get started?"
)

# Session initialization
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": default_message}
    ]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Get user input
if user_prompt := st.chat_input("What's your first question or tell me about your business?"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=st.session_state.messages,
                )
                assistant_reply = response.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
                st.write(assistant_reply)
            except Exception as e:
                st.error(f"Oops! Something went wrong: {e}")
