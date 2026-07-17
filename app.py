import streamlit as st
import pandas as pd

st.title("🚜 Farmer Income Insights Dashboard")
st.write("Welcome to Rajveer's Agro-Economic Analytics App!")

# Automatically load the dataset from your GitHub folder behind the scenes
@st.cache_data
def load_data():
    return pd.read_csv("Agro Dataset.csv")

try:
    df = load_data()
    
    # Show data overview
    st.subheader("📊 Dataset Overview")
    st.write(f"This application is directly analyzing {df.shape[0]} records of agricultural profiles across multiple data features.")
    st.dataframe(df.head(10))
    
    # Simple dynamic filtering
    st.subheader("🔍 Filter Data by Region")
    if 'REGION' in df.columns:
        regions = df['REGION'].unique()
        selected_region = st.selectbox("Select a Region to filter:", regions)
        filtered_df = df[df['REGION'] == selected_region]
        st.write(f"Showing data for {selected_region} region:")
        st.dataframe(filtered_df.head(20))
        
except FileNotFoundError:
    st.error("Could not automatically locate 'Agro Dataset.csv' in the repository. Please make sure the filename matches exactly.")
