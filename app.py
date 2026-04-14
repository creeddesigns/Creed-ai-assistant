import streamlit as st
import requests

st.set_page_config(page_title="Creed AI Assistant", layout="wide")

st.title("🤖 Creed AI Assistant")
st.caption("Your real AI assistant — by Creed")

with st.sidebar:
    st.header("🔑 API Key")
    api_key = st.text_input("Gemini API Key", type="password")
    if api_key:
        st.success("✅ Key received")
    st.markdown("[Get free API key](https://aistudio.google.com)")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I'm Creed AI. Ask me anything! 👋"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

def ask_gemini(prompt, key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={key}"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    r = requests.post(url, json=payload)
    if r.status_code == 200:
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    return f"Error {r.status_code}: {r.text}"

user_input = st.chat_input("Ask Creed AI...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Creed is thinking..."):
            if not api_key:
                response = "⚠️ Please add your Gemini API key in the sidebar."
            else:
                response = ask_gemini(user_input, api_key)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
