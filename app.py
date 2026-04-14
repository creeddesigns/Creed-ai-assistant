import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Creed AI", layout="wide")

st.title("🤖 Creed AI Assistant")
st.caption("Your real AI assistant — powered by Google Gemini")

# Sidebar for API key
with st.sidebar:
    st.header("🔑 API Key Required")
    api_key = st.text_input("Enter your Gemini API Key", type="password", 
                           help="Get free key from aistudio.google.com")
    if api_key:
        genai.configure(api_key=api_key)
        st.success("✅ AI Ready!")
    
    st.markdown("---")
    st.markdown("**How to get API key:**")
    st.markdown("1. Go to [aistudio.google.com](https://aistudio.google.com)")
    st.markdown("2. Sign in with Google")
    st.markdown("3. Click 'Get API key'")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm Creed AI — a real intelligent assistant. Ask me anything! 📊✨"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

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
                model = genai.GenerativeModel('gemini-1.5-flash')
                chat = model.start_chat(history=[])
                ai_response = chat.send_message(prompt)
                response = ai_response.text
            except Exception as e:
                response = f"Error: {str(e)}\n\nMake sure your API key is correct."
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
