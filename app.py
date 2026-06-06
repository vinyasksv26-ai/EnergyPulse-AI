import streamlit as st

st.set_page_config(
    page_title="EnergyPulse AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Logo
try:
    st.sidebar.image("assets/logo.png", width=120)
except:
    pass

st.title("⚡ EnergyPulse AI")
st.subheader("Smart Meter Consumption Profiler")

st.markdown("""
### Welcome to EnergyPulse AI

An AI-powered energy analytics platform that helps:

- 🔮 Predict electricity consumption
- 🚨 Detect abnormal usage patterns
- 📈 Analyze seasonal demand
- ⚡ Identify peak load behavior
- 📊 Visualize smart meter insights

### Features

- Dashboard Analytics
- Energy Consumption Prediction
- Anomaly Detection
- Seasonal & Monthly Analysis
- Smart Energy Insights

Use the sidebar to navigate between modules.
""")

st.success("System Ready")
