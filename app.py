import streamlit as st
import random

st.set_page_config(page_title="Creed AI", layout="wide")

st.title("🤖 Creed AI Assistant")
st.caption("Your AI assistant — by Creed")

# Simple responses for demo
responses = [
    "That's interesting! Tell me more about your data.",
    "I can help you create charts from that information.",
    "Would you like me to analyze trends in your data?",
    "Great question! Let me think about that...",
    "I'm learning to be a better AI assistant. What else would you like to know?"
]

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm Creed. Ask me anything about charts, data, or just say hi! 👋"}
    ]

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Ask Creed AI anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        response = f"**Creed AI:** {random.choice(responses)}\n\n> You said: *{prompt}*\n\nSoon I'll have full AI capabilities! For now, try asking me about charts or data."
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with info
with st.sidebar:
    st.header("📊 Features Coming")
    st.markdown("""
    - ✅ Chat interface (working now)
    - 🔜 Real AI (Gemini/OpenAI)
    - 🔜 Chart generation
    - 🔜 CSV data analysis
    - 🔜 Voice input
    """)
    st.success("App is running correctly!")
