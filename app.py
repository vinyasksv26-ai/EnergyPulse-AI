import streamlit as st

st.set_page_config(
    page_title="EnergyPulse AI",
    page_icon="⚡",
    layout="wide"
)

# Logo and Title
col1, col2 = st.columns([1, 4])

with col1:
    st.image("assets/logo.png", width=150)

with col2:
    st.title("⚡ EnergyPulse AI")
    st.subheader("Smart Meter Consumption Profiler")

st.divider()

st.markdown("""
## Welcome to EnergyPulse AI

EnergyPulse AI is an intelligent Smart Meter Consumption Profiler that helps users:

✅ Monitor Electricity Usage

✅ Predict Future Energy Consumption

✅ Detect Energy Anomalies

✅ Analyze Seasonal Consumption Patterns

✅ Identify Peak Usage Hours

✅ Generate Data-Driven Energy Insights

---

### Features

📊 Dashboard  
View real-time energy analytics and KPIs.

🔮 Prediction  
Predict future electricity consumption using Machine Learning.

🚨 Anomaly Detection  
Detect unusual energy usage patterns automatically.

📈 Analytics  
Explore monthly, hourly, and seasonal consumption trends.

ℹ️ About  
Learn about the project, technologies, and objectives.

---

### Technologies Used

- Python
- Pandas
- Scikit-Learn
- Plotly
- Streamlit
- Machine Learning

""")

st.success("✅ EnergyPulse AI Loaded Successfully")
