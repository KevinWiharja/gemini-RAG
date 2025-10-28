import requests
import streamlit as st
import os

st.set_page_config(
    page_title="Brew Haven Assistant",
    page_icon="☕",
    layout="centered"
)

API_BASE = os.getenv("API_URL", "http://127.0.0.1:8000")
API_ENDPOINT = f"{API_BASE}/chat"

def get_bot_response(user_input):
    request_body = {
        "query": user_input
    }

    try:
        response = requests.post(API_ENDPOINT, json=request_body)
        if response.status_code == 200:
            try:
                data = response.json()
                return data.get("answer", "Sorry, the API returned unexpected data.")
            except requests.exceptions.JSONDecodeError:
                return response.text
        else:
            return f"❌ API Error: Failed to get response (Status: {response.status_code})."
    except requests.exceptions.ConnectionError:
        return "❌ Connection Error: Ensure the FastAPI server is running."
    except Exception as e:
        return f"❌ An unexpected error occurred: {str(e)}"


if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Welcome to Brew Haven Assistant. How can I help you with company information?"
    })


st.title("☕ Brew Haven Assistant")
st.markdown("RAG-powered assistant for your company documents.")


if st.button("New Chat"):
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Welcome to Brew Haven Assistant. How can I help you with company information?"
    })
    st.rerun()

st.divider()


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if user_prompt := st.chat_input("Ask something about Brew Haven..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.write(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching for the answer..."):
            response = get_bot_response(user_prompt)
            st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})