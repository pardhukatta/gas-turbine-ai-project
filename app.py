import streamlit as st
import pandas as pd
import joblib

model = joblib.load("rf_model.pkl")

st.title("🔥 Gas Turbine Emission Prediction")

AT = st.number_input("Ambient Temperature")
AP = st.number_input("Ambient Pressure")
AH = st.number_input("Ambient Humidity")
AFDP = st.number_input("Air Filter DP")
GTEP = st.number_input("Exhaust Pressure")
TIT = st.number_input("Turbine Inlet Temp")
TAT = st.number_input("Turbine After Temp")
CDP = st.number_input("Compressor Discharge Pressure")

if st.button("Predict NOX"):
    input_data = pd.DataFrame([[AT, AP, AH, AFDP, GTEP, TIT, TAT, CDP]],
                             columns=['AT','AP','AH','AFDP','GTEP','TIT','TAT','CDP'])

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted NOX: {prediction:.2f}")

    # ✅ NOW prediction exists → safe to use
    if prediction > 80:
        st.error("⚠️ High Pollution Risk")
    elif prediction > 50:
        st.warning("⚠️ Moderate Pollution")
    else:
        st.success("✅ Safe Emission Level")