import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About EnergyPulse AI")

st.markdown("""
## Smart Meter Consumption Profiler

EnergyPulse AI is an intelligent energy analytics platform that helps users:

- Forecast electricity consumption
- Detect unusual energy usage
- Analyze seasonal patterns
- Monitor peak consumption periods
- Generate energy insights using Machine Learning

### Technologies Used

- Python
- Pandas
- Scikit-Learn
- Plotly
- Streamlit

### Developed By

Vinyas K S  
4VM24CS047  
Vidya Vikas Institute of Engineering and Technology

### Project Goal

To help consumers understand and optimize electricity usage through data-driven analytics and predictive modeling.
""")

st.success("✅ About Page Loaded Successfully")
