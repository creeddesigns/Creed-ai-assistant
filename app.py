import streamlit as st

st.set_page_config(page_title="Creed AI", layout="centered")

st.title("📊 Creed AI Chart Assistant")
st.write("Welcome to Creed's AI Chart Assistant!")

st.success("✅ App is running successfully!")

st.subheader("Quick Test")
user_input = st.text_input("Type anything:", placeholder="Hello Creed!")
if user_input:
    st.write(f"You typed: {user_input}")

st.markdown("---")
st.markdown("Built by **Creed**")
