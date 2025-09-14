import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler

# Load model and dataset
model = joblib.load("flood_app/flood_hazard_model.pkl")
df = pd.read_csv("new_cleaned_flood_data.csv")

# Title and description
st.title("🌊 Flood Hazard Risk Predictor")
st.markdown("Predict flood hazard category based on district-level flood indicators.")

# Sidebar inputs
st.sidebar.header("📥 Input Parameters")
hazard_index = st.sidebar.slider("Flood Hazard Index", int(df["Flood_Hazard_Index"].min()), int(df["Flood_Hazard_Index"].max()), int(df["Flood_Hazard_Index"].mean()))
inundated_area = st.sidebar.slider("Inundated Area (Ha)", int(df["Inundated_Area_Ha"].min()), int(df["Inundated_Area_Ha"].max()), int(df["Inundated_Area_Ha"].mean()))
hazard_pct = st.sidebar.slider("Flood Hazard (%)", int(df["Flood_Hazard_Pct"].min()), int(df["Flood_Hazard_Pct"].max()), int(df["Flood_Hazard_Pct"].mean()))

# Normalize input using MinMaxScaler fitted on original data
scaler = MinMaxScaler()
scaler.fit(df[["Flood_Hazard_Index", "Inundated_Area_Ha", "Flood_Hazard_Pct"]])

user_input = pd.DataFrame({
    "Flood_Hazard_Index": [hazard_index],
    "Inundated_Area_Ha": [inundated_area],
    "Flood_Hazard_Pct": [hazard_pct]
})


# Scale and keep as DataFrame with correct columns
scaled_array = scaler.transform(user_input)
scaled_input = pd.DataFrame(scaled_array, columns=user_input.columns)

# Predict
prediction = model.predict(scaled_input)[0]

# Display result
st.subheader("🧠 Predicted Hazard Category")
st.success(f"**{prediction}**")

# Optional: Show sample data
with st.expander("📊 View Sample Data"):
    st.dataframe(df.head())
