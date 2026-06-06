import streamlit as st
import os

st.set_page_config(
    page_title="EnergyPulse AI",
    page_icon="⚡",
    layout="wide"
)

# Logo
logo_path = "assets/logo.png"

if os.path.exists(logo_path):
    try:
        st.image(logo_path, width=180)
    except:
        st.warning("Logo could not be loaded")

# Title
st.title("⚡ EnergyPulse AI")
st.subheader("Smart Meter Consumption Profiler")

st.divider()

st.markdown("""
## Welcome to EnergyPulse AI

EnergyPulse AI is an AI-powered Smart Meter Consumption Profiler that helps users:

✅ Monitor Electricity Usage

✅ Predict Future Energy Consumption

✅ Detect Energy Anomalies

✅ Analyze Seasonal Consumption Patterns

✅ Identify Peak Usage Hours

✅ Generate Data-Driven Energy Insights

---

### 📊 Dashboard
View energy consumption KPIs and trends.

### 🔮 Prediction
Predict future electricity consumption using Machine Learning.

### 🚨 Anomaly Detection
Identify unusual energy usage patterns.

### 📈 Analytics
Explore monthly, hourly, and seasonal consumption trends.

### ℹ️ About
Learn about the project and technologies used.

---

### Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Plotly
- Streamlit
- Machine Learning

---



""")

st.success("✅ EnergyPulse AI Loaded Successfully")
