import streamlit as st
import openai

st.set_page_config(page_title="Creed AI Assistant", layout="wide")

st.title("🤖 Creed AI Assistant")
st.caption("Your personal AI assistant — by Creed")

with st.sidebar:
    st.header("🔑 API Key")
    api_key = st.text_input("OpenAI API Key", type="password")
    st.markdown("Get key from [platform.openai.com](https://platform.openai.com)")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I'm Creed AI. Ask me anything! 👋"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask Creed AI..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        if not api_key:
            response = "⚠️ Please add your OpenAI API key in the sidebar."
        else:
            try:
                openai.api_key = api_key
                completion = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                response = completion.choices[0].message.content
            except Exception as e:
                response = f"Error: {e}"
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
