import streamlit as st
import pandas as pd
import joblib
import os
from geopy.distance import geodesic

# ==========================
# Load model & encoders
# ==========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "fraud_detection_model.jb"))
encoders = joblib.load(os.path.join(BASE_DIR, "label_encoder.jb"))

# ==========================
# Utility
# ==========================
def calculate_distance(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).km

# ==========================
# UI
# ==========================
st.set_page_config(page_title="Fraud Detection System")
st.title("💳 Fraud Detection System")
st.write("Enter transaction details")

merchant = st.text_input("Merchant")
category = st.text_input("Category")
amount = st.number_input("Amount", min_value=0.0)

lat = st.number_input("Customer Latitude", format="%.6f")
lon = st.number_input("Customer Longitude", format="%.6f")
merch_lat = st.number_input("Merchant Latitude", format="%.6f")
merch_lon = st.number_input("Merchant Longitude", format="%.6f")

hour = st.slider("Hour", 0, 23, 12)
day = st.slider("Day", 1, 31, 15)
month = st.slider("Month", 1, 12, 6)

gender = st.selectbox("Gender", ["Male", "Female"])
cc_num = st.text_input("Credit Card Number")

# ==========================
# Prediction
# ==========================
if st.button("Check for Fraud"):

    if not all([merchant, category, cc_num]):
        st.warning("Please fill all required fields")
    else:
        distance = calculate_distance(lat, lon, merch_lat, merch_lon)

        df = pd.DataFrame([{
            "merchant": merchant,
            "category": category,
            "amt": amount,
            "distance": distance,
            "hour": hour,
            "day": day,
            "month": month,
            "gender": gender,
            "cc_num": hash(cc_num) % 100
        }])

        for col in ["merchant", "category", "gender"]:
            try:
                df[col] = encoders[col].transform(df[col])
            except ValueError:
                df[col] = -1

        prediction = model.predict(df)[0]

        if prediction == 1:
            st.error("🚨 Fraudulent Transaction")
        else:
            st.success("✅ Legitimate Transaction")
