import streamlit as st

st.set_page_config(page_title="Creed AI", layout="centered", initial_sidebar_state="collapsed")

st.title("⚡ Creed AI Chart Assistant")
st.write("Welcome to Creed's AI Chart Assistant!")

st.success("✅ App is running successfully!")

st.subheader("Quick Test")

# Mobile-friendly input with button
col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_input("Type anything:", placeholder="Hello Creed!", key="user_input")
with col2:
    submit = st.button("Send", use_container_width=True)

if submit and user_input:
    st.write(f"You typed: {user_input}")
    st.balloons()

st.markdown("---")
st.markdown("Built by **Creed**")
