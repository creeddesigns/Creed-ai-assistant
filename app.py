import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.set_page_config(page_title="Creed AI Charts", layout="wide")

st.title("📊 Creed AI Chart Generator")
st.caption("Create beautiful charts instantly — by Creed")

# Sidebar for chart options
with st.sidebar:
    st.header("📈 Chart Settings")
    chart_type = st.selectbox("Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])
    st.markdown("---")
    st.markdown("### Quick Examples")
    st.markdown("- Sales by month")
    st.markdown("- Product performance")
    st.markdown("- Survey results")

# Main area - two tabs
tab1, tab2 = st.tabs(["📝 Enter Data", "📁 Upload File"])

# Tab 1: Manual data entry
with tab1:
    st.subheader("Enter your data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        labels = st.text_area("Labels (one per line)", "Apples\nBananas\nOranges")
    with col2:
        values = st.text_area("Values (one per line)", "30\n50\n20")
    
    if st.button("✨ Create Chart", type="primary", use_container_width=True):
        try:
            # Parse data
            label_list = [l.strip() for l in labels.split("\n") if l.strip()]
            value_list = [float(v.strip()) for v in values.split("\n") if v.strip()]
            
            if len(label_list) == len(value_list):
                # Create chart
                fig, ax = plt.subplots(figsize=(8, 5))
                
                if chart_type == "Bar Chart":
                    ax.bar(label_list, value_list, color='steelblue')
                    ax.set_ylabel("Values")
                elif chart_type == "Line Chart":
                    ax.plot(label_list, value_list, marker='o', linewidth=2, markersize=8)
                    ax.set_ylabel("Values")
                else:  # Pie Chart
                    ax.pie(value_list, labels=label_list, autopct='%1.1f%%')
                
                ax.set_title(f"{chart_type} - Creed AI", fontsize=14, fontweight='bold')
                st.pyplot(fig)
                st.success(f"✅ {chart_type} created successfully!")
            else:
                st.error(f"Number of labels ({len(label_list)}) doesn't match values ({len(value_list)})")
        except Exception as e:
            st.error(f"Error: {e}. Please check your numbers.")

# Tab 2: File upload
with tab2:
    st.subheader("Upload CSV or Excel file")
    
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx', 'xls'])
    
    if uploaded_file:
        try:
            # Read file
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success(f"✅ Loaded {len(df)} rows and {len(df.columns)} columns")
            st.dataframe(df.head())
            
            # Let user choose columns
            st.subheader("Select columns for chart")
            col1, col2 = st.columns(2)
            
            with col1:
                x_column = st.selectbox("X-axis (labels)", df.columns)
            with col2:
                y_column = st.selectbox("Y-axis (values)", df.columns)
            
            if st.button("Generate from File", type="primary"):
                fig, ax = plt.subplots(figsize=(8, 5))
                
                if chart_type == "Bar Chart":
                    ax.bar(df[x_column], df[y_column], color='coral')
                    plt.xticks(rotation=45)
                elif chart_type == "Line Chart":
                    ax.plot(df[x_column], df[y_column], marker='s', linewidth=2)
                    plt.xticks(rotation=45)
                else:
                    ax.pie(df[y_column], labels=df[x_column], autopct='%1.1f%%')
                
                ax.set_title(f"{chart_type}: {y_column} by {x_column}", fontsize=12)
                st.pyplot(fig)
                
        except Exception as e:
            st.error(f"Error reading file: {e}")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by **Creed** | Create charts with your data instantly")
