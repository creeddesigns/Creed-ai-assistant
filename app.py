import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Creed AI Assistant", layout="wide")

st.title("🤖 Creed AI Assistant")
st.caption("Your personal AI assistant — like having Creed with you always")

# Sidebar for API key
with st.sidebar:
    st.header("🔑 Configuration")
    api_key = st.text_input("Gemini API Key", type="password", 
                           help="Get free key from aistudio.google.com")
    
    if api_key:
        genai.configure(api_key=api_key)
        st.success("✅ API key configured!")
    
    st.markdown("---")
    st.markdown("### Features coming soon:")
    st.markdown("- 📊 Chart creation")
    st.markdown("- 📁 Data analysis")
    st.markdown("- 💡 Smart insights")

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm Creed AI. Ask me anything about data, charts, or just chat with me! 👋"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask Creed AI anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Creed is thinking..."):
            if not api_key:
                response = "⚠️ Please add your Gemini API key in the sidebar first. Get one free at aistudio.google.com"
            else:
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    chat = model.start_chat(history=[])
                    ai_response = chat.send_message(prompt)
                    response = ai_response.text
                except Exception as e:
                    response = f"Error: {str(e)}"
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
