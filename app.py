import streamlit as st
import pandas as pd

st.set_page_config(page_title="Farmer Income Insights Dashboard", page_icon="🚜")

st.title("🚜 Farmer Income Insights Dashboard")
st.write("Welcome to Rajveer's Agro-Economic Analytics App!")

uploaded_file = st.file_uploader("Upload your Trilytics Dataset CSV file to view insights", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Dataset Overview")
    st.write(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns successfully.")
    st.dataframe(df.head(10))

    st.subheader("🔍 Filter Data by Region")
    if 'REGION' in df.columns:
        regions = df['REGION'].unique()
        selected_region = st.selectbox("Select a Region to filter:", regions)
        filtered_df = df[df['REGION'] == selected_region]
        st.write(f"Showing data for {selected_region} region:")
        st.dataframe(filtered_df.head(20))
    else:
        st.warning("No 'REGION' column found in the uploaded file.")
