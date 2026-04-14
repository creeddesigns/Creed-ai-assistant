import streamlit as st
import requests

st.set_page_config(page_title="Creed AI Assistant", layout="wide")

st.title("🤖 Creed AI Assistant")
st.caption("Your real AI assistant — powered by Google Gemini")

# Sidebar for API key
with st.sidebar:
    st.header("🔑 API Key")
    api_key = st.text_input("Enter your Gemini API Key", type="password", 
                           help="Get free key from aistudio.google.com")
    
    if api_key:
        st.success("✅ AI Ready!")
    
    st.markdown("---")
    st.markdown("### How to get your free API key:")
    st.markdown("1. Go to [aistudio.google.com](https://aistudio.google.com)")
    st.markdown("2. Sign in with Google")
    st.markdown("3. Click 'Get API key'")
    st.markdown("4. Copy and paste here")
    st.markdown("---")
    st.markdown("### Features:")
    st.markdown("- 💬 Real AI conversations")
    st.markdown("- 📊 Chart creation (ask me)")
    st.markdown("- 📁 Data analysis")
    st.markdown("- 🧠 Smart insights")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm Creed AI. Ask me anything — data, charts, coding, or just chat! 👋"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to call Gemini API
def call_gemini(prompt, api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
    
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
        return f"Error: {response.status_code}. Please check your API key."

# Chat input
user_input = st.chat_input("Ask Creed AI anything...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Creed is thinking..."):
            if not api_key:
                response = "⚠️ Please enter your Gemini API key in the sidebar first.\n\nGet one free at [aistudio.google.com](https://aistudio.google.com)"
            else:
                try:
                    response = call_gemini(user_input, api_key)
                except Exception as e:
                    response = f"Error: {str(e)}"
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})       
