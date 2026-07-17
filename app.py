import streamlit as st
import pandas as pd

st.title("🚜 Farmer Income Insights Dashboard")
st.write("Welcome to Rajveer's Agro-Economic Analytics App!")

# Upload the CSV directly on the web app
uploaded_file = st.file_uploader("Upload your Agro Dataset CSV file to view insights", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Show data overview
    st.subheader("📊 Dataset Overview")
    st.write(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns successfully.")
    st.dataframe(df.head(10))
    
    # Simple dynamic filtering
    st.subheader("🔍 Filter Data by Region")
    if 'REGION' in df.columns:
        regions = df['REGION'].unique()
        selected_region = st.selectbox("Select a Region to filter:", regions)
        filtered_df = df[df['REGION'] == selected_region]
        st.write(f"Showing data for {selected_region} region:")
        st.dataframe(filtered_df.head(20))
    else:
        st.warning("Could not find a 'REGION' column in this CSV file.")
