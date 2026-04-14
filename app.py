import streamlit as st
import requests
import json

st.set_page_config(page_title="Creed AI", layout="wide")

st.title("🤖 Creed AI Assistant")
st.caption("Your real AI assistant — by Creed")

# Sidebar for API key
with st.sidebar:
    st.header("🔑 API Key Required")
    api_key = st.text_input("Enter your Gemini API Key", type="password", 
                           help="Get free key from aistudio.google.com")
    
    if api_key:
        st.success("✅ API Key ready!")
    
    st.markdown("---")
    st.markdown("**Get your free API key:**")
    st.markdown("[aistudio.google.com](https://aistudio.google.com)")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm Creed AI — a real intelligent assistant. Ask me anything! 📊✨"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Function to call Gemini API
def call_gemini(prompt, api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Chat input
if prompt := st.chat_input("Ask Creed AI anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate AI response
    with st.chat_message("assistant"):
        if not api_key:
            response = "⚠️ Please add your Gemini API key in the sidebar first.\n\nGet one free at [aistudio.google.com](https://aistudio.google.com)"
        else:
            try:
                response = call_gemini(prompt, api_key)
            except Exception as e:
                response = f"Error: {str(e)}"
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
