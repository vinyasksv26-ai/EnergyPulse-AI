import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Electricity Consumption Prediction")

model = joblib.load("models/model.pkl")

col1, col2 = st.columns(2)

with col1:
    hour = st.slider("Hour", 0, 23, 12)
    day = st.slider("Day", 1, 31, 15)
    month = st.slider("Month", 1, 12, 6)
    weekend = st.selectbox(
        "Weekend",
        [0,1]
    )

with col2:
    rolling_mean = st.number_input(
        "Rolling Mean",
        value=2.0
    )

    variance = st.number_input(
        "Variance",
        value=1.0
    )

    peak_ratio = st.number_input(
        "Peak Ratio",
        value=1.0
    )

if st.button("Predict Consumption"):

    input_data = pd.DataFrame({
        "Hour":[hour],
        "Day":[day],
        "Month":[month],
        "Weekend":[weekend],
        "Rolling_Mean":[rolling_mean],
        "Variance":[variance],
        "Peak_Ratio":[peak_ratio]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Consumption: {prediction:.2f} kWh"
    )

    if prediction < 2:
        st.info("Low Demand")
    elif prediction < 5:
        st.warning("Medium Demand")
    else:
        st.error("High Demand")
