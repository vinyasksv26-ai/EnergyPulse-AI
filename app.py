import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="EnergyPulse AI",
    page_icon="⚡",
    layout="wide"
)

# Load Logo
try:
    logo = Image.open("assets/logo.png")

    col1, col2 = st.columns([1, 4])

    with col1:
        st.image(logo, width=150)

    with col2:
        st.title("⚡ EnergyPulse AI")
        st.subheader("Smart Meter Consumption Profiler")

except Exception as e:
    st.title("⚡ EnergyPulse AI")
    st.subheader("Smart Meter Consumption Profiler")
    st.warning(f"Logo not loaded: {e}")

st.divider()

st.markdown("""
## Welcome to EnergyPulse AI

### Features

📊 Dashboard
- Energy consumption trends
- KPI monitoring

🔮 Prediction
- Machine Learning based forecasting

🚨 Anomaly Detection
- Detect unusual power usage

📈 Analytics
- Monthly and hourly analysis

ℹ️ About
- Project information

