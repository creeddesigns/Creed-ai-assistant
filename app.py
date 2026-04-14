import streamlit as st

st.set_page_config(page_title="Creed AI", layout="wide")

st.title("🤖 Creed AI Assistant")
st.caption("Your assistant — by Creed")

# Simple responses that actually work
responses = {
    "hi": "Hello! I'm Creed. How can I help you today?",
    "hello": "Hi there! Ready to create some charts?",
    "how are you": "I'm great! Ready to help you with data and charts.",
    "chart": "I can help you create bar charts, line charts, and pie charts. Just tell me your data!",
    "help": "I can help with charts, data analysis, and answering questions. What do you need?",
    "bye": "Goodbye! Come back anytime.",
}

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I'm Creed. Ask me about charts or just say hi! 👋"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.chat_message("assistant"):
        reply = "I'm Creed! I'm learning to be an AI assistant. For now, try asking about charts, data, or saying hello!"
        
        # Check for keywords
        lower_input = user_input.lower()
        for key, response in responses.items():
            if key in lower_input:
                reply = response
                break
        
        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
