import streamlit as st
import pandas as pd
import plotly.express as px
import google.generativeai as genai
import json
import re

st.set_page_config(page_title="Creed Chart Assistant", layout="wide")

st.title("📊 Creed AI Chart Assistant")
st.caption("Generate charts from natural language — by Creed")

with st.sidebar:
    st.header("🔑 API Key")
    api_key = st.text_input("Gemini API Key", type="password")
    st.markdown("Get your free key from [Google AI Studio](https://aistudio.google.com/)")

tab1, tab2 = st.tabs(["✨ Text to Chart", "📁 Data Upload"])

with tab1:
    st.subheader("Describe your chart")
    prompt = st.text_area("Example: Bar chart: Apples 30, Bananas 50, Oranges 20")
    
    if st.button("Generate Chart", type="primary"):
        if not api_key:
            st.error("Please enter your API key")
        elif not prompt:
            st.warning("Please describe your chart")
        else:
            with st.spinner("Creed AI is working..."):
                try:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(f"""
                    Extract chart data from: "{prompt}"
                    Return ONLY JSON: {{"type":"bar","labels":["A","B"],"values":[10,20],"title":"My Chart"}}
                    """)
                    text = re.sub(r'```json\n?|```\n?', '', response.text.strip())
                    data = json.loads(text)
                    df = pd.DataFrame({'x': data['labels'], 'y': data['values']})
                    if data['type'] == 'bar':
                        fig = px.bar(df, x='x', y='y', title=data.get('title', prompt))
                    elif data['type'] == 'line':
                        fig = px.line(df, x='x', y='y', title=data.get('title', prompt))
                    elif data['type'] == 'pie':
                        fig = px.pie(df, names='x', values='y', title=data.get('title', prompt))
                    else:
                        fig = px.scatter(df, x='x', y='y', title=data.get('title', prompt))
                    st.plotly_chart(fig, use_container_width=True)
                    st.success("✅ Chart ready!")
                except Exception as e:
                    st.error(f"Error: {e}. Try: 'Bar chart: A 10, B 20'")

with tab2:
    st.subheader("Upload CSV or Excel")
    file = st.file_uploader("Choose file", type=['csv', 'xlsx'])
    if file:
        df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
        st.dataframe(df.head())
        x = st.selectbox("X axis", df.columns)
        y = st.selectbox("Y axis", df.columns)
        if st.button("Make Chart"):
            st.plotly_chart(px.bar(df, x=x, y=y), use_container_width=True)

st.markdown("---")
st.markdown("Built with ❤️ by **Creed**")
