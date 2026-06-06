import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Energy Consumption Prediction")
st.markdown("Predict future electricity consumption using Machine Learning.")

# Load Model
model = joblib.load("models/model.pkl")

col1, col2 = st.columns(2)

with col1:
    hour = st.slider("Hour", 0, 23, 12)
    day = st.slider("Day", 1, 31, 15)
    month = st.slider("Month", 1, 12, 6)

    weekend = st.selectbox(
        "Weekend",
        [0, 1],
        format_func=lambda x: "Weekend" if x == 1 else "Weekday"
    )

with col2:
    rolling_mean = st.number_input(
        "Rolling Mean",
        min_value=0.0,
        value=2.0
    )

    variance = st.number_input(
        "Variance",
        min_value=0.0,
        value=1.0
    )

    peak_ratio = st.number_input(
        "Peak Ratio",
        min_value=0.0,
        value=1.0
    )

st.divider()

if st.button("⚡ Predict Consumption"):

    input_data = pd.DataFrame({
        "Hour": [hour],
        "Day": [day],
        "Month": [month],
        "Weekend": [weekend],
        "Rolling_Mean": [rolling_mean],
        "Variance": [variance],
        "Peak_Ratio": [peak_ratio]
    })

    prediction = model.predict(input_data)[0]

    st.metric(
        "Predicted Consumption",
        f"{prediction:.2f} kWh"
    )

    if prediction < 2:
        st.success("🟢 Low Energy Demand")

    elif prediction < 5:
        st.warning("🟡 Moderate Energy Demand")

    else:
        st.error("🔴 High Energy Demand")

st.success("✅ Prediction Module Ready")
