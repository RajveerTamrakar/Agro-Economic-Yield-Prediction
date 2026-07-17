import streamlit as st
import pandas as pd
import joblib

st.title("🚜 Farmer Income Predictor")

# Ask the user for the data
total_land = st.number_input("Total Land For Agriculture (Hectares)", value=2.5)
non_agri_inc = st.number_input("Non-Agriculture Income (₹)", value=50000)
agro_econ_score = st.slider("Agro-Economic Score", 0.0, 100.0, 50.0)
access_score = st.slider("Market Access Score", -100.0, 100.0, -10.0)

if st.button("Predict Income"):
    # Load your saved model
    model = joblib.load("agro_model.pkl")

    # Put the inputs into a tiny table for the model
    input_data = pd.DataFrame([{
        'Total_Land_For_Agriculture': total_land,
        'Non_Agriculture_Income': non_agri_inc,
        'agro_econ_score': agro_econ_score,
        'access_score': access_score
    }])

    # Predict!
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Farmer Income: ₹{max(0, prediction):,.2f}")
