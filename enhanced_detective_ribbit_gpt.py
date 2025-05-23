
import streamlit as st
import openai
import random

# Set up the OpenAI API key from secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page config
st.set_page_config(page_title="Detective Ribbit 🐸", page_icon="🐸")

# Mystery prompts to rotate through
mysteries = [
    "Who stole the last donut from the teacher's lounge? 🍩",
    "Why are there muddy footprints on the ceiling? 👣",
    "Who hid all the whiteboard markers in the hamster cage? 🐹",
    "Why is the class goldfish wearing sunglasses? 🕶️🐟",
    "Who turned all the cafeteria trays upside down? 🍽️",
    "Why is the school mascot wearing a tutu? 🐯🩰",
    "Who put googly eyes on all the pencils? 👀✏️"
]

# Initialize messages and random mystery
if "messages" not in st.session_state:
    st.session_state.selected_mystery = random.choice(mysteries)
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are Detective Ribbit, a silly frog detective who solves classroom mysteries with the help of 4th and 5th graders. "
                "You make funny guesses, ask for silly clues, and encourage creativity. Every case is wild and includes goofy suspects like staplers, bananas, or invisible hamsters. "
                "You always end messages with a funny frog sound or pun (e.g. 'Ribbit-ribbit, I’m on it!'). Make it fun, interactive, and never too scary. Ask one question at a time."
            )
        },
        {
            "role": "assistant",
            "content": (
                f"🎩🐸 Welcome to the Detective Ribbit Mystery Agency! I'm Detective Ribbit, the finest froggy investigator this side of the swamp.\n\n"
                f"Today's mystery: *{st.session_state.selected_mystery}*\n\n"
                "Was it the janitor's pet raccoon? A sneaky backpack? Or maybe… the principal’s office chair?!\n\n"
                "What’s your first clue, detective? Ribbit-ribbit, let’s hop to it!"
            )
        }
    ]

# Display chat
for msg in st.session_state.messages:
    st.markdown(f"**{msg['role'].capitalize()}**: {msg['content']}")

# Handle input with toggle to reset text
if "input_toggle" not in st.session_state:
    st.session_state.input_toggle = 0

input_key = f"user_input_{st.session_state.input_toggle}"
user_input = st.text_input("What do you think happened?", key=input_key)

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4",
        messages=st.session_state.messages
    )

    assistant_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

    st.session_state.input_toggle += 1
    st.experimental_rerun()
