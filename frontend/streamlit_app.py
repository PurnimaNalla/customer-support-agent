import streamlit as st
from backend.agent import support_agent

st.title("Customer Support Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.write(msg)

user_input = st.chat_input("Ask your question")

if user_input:

    st.session_state.messages.append(
        ("user", user_input)
    )

    try:
        bot_reply = support_agent(user_input)

    except Exception as e:
        bot_reply = f"Error: {e}"

    st.session_state.messages.append(
        ("assistant", bot_reply)
    )

    st.rerun()