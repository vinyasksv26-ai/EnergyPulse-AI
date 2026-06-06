import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="EnergyPulse AI",
    page_icon="⚡",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

col1, col2 = st.columns([1, 4])

with col1:
    st.image("logo.png", width=180)

with col2:
    st.title("⚡ EnergyPulse AI")
    st.markdown("### Smart Meter Consumption Profiler")
    st.caption("AI-Powered Energy Analytics & Forecasting Platform")

st.divider()

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
## 🚀 Welcome to EnergyPulse AI

EnergyPulse AI is an intelligent energy monitoring and analytics platform
designed to help consumers, utility providers, and smart-city initiatives
optimize electricity usage through Machine Learning and Data Analytics.

### 🎯 Project Objectives

- Forecast future electricity consumption
- Detect unusual energy usage patterns
- Analyze hourly and seasonal trends
- Monitor peak energy demand periods
- Generate actionable energy insights
""")

# ==========================================
# FEATURES
# ==========================================

st.subheader("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.info("""
### 📊 Dashboard
- Real-time KPIs
- Consumption trends
- Monthly analysis
- Seasonal insights
""")

    st.info("""
### 🔮 Prediction
- Machine Learning based forecasting
- Future energy demand estimation
- Smart consumption planning
""")

with col2:
    st.info("""
### 🚨 Anomaly Detection
- Detect abnormal usage patterns
- Identify energy spikes
- Improve energy efficiency
""")

    st.info("""
### 📈 Analytics
- Hourly consumption analysis
- Peak usage identification
- Advanced energy insights
""")

# ==========================================
# PROJECT METRICS
# ==========================================

st.subheader("📌 Project Highlights")

c1, c2, c3, c4 = st.columns(4)

c1.metric("ML Model", "Random Forest")
c2.metric("Dataset Size", "50,000 Records")
c3.metric("Features", "19")
c4.metric("Accuracy", "99%+")

# ==========================================
# TECHNOLOGY STACK
# ==========================================

st.subheader("🛠 Technology Stack")

st.markdown("""
- **Python**
- **Pandas**
- **NumPy**
- **Scikit-Learn**
- **Plotly**
- **Streamlit**
- **Machine Learning**
""")

# ==========================================
# HOW TO USE
# ==========================================

st.subheader("📖 How To Use")

st.success("""
1. Open Dashboard to view energy insights.
2. Use Prediction to forecast consumption.
3. Explore Anomaly Detection for unusual patterns.
4. Analyze trends in Analytics.
5. Read project details in About.
""")

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown("""



🏆 Hackathon Project | Energy Analytics using Machine Learning
""")
