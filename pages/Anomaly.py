import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

st.set_page_config(
    page_title="Anomaly Detection",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Energy Anomaly Detection")

# Load Dataset
df = pd.read_csv(
    "data/smart_meter_small.csv"
)

# Train Isolation Forest
model = IsolationForest(
    contamination=0.01,
    random_state=42
)

df["Anomaly"] = model.fit_predict(
    df[["Global_active_power"]]
)

# Extract anomalies
anomalies = df[
    df["Anomaly"] == -1
]

# KPI
st.metric(
    "🚨 Anomalies Detected",
    len(anomalies)
)

st.divider()

# Scatter Plot
fig = px.scatter(
    df.head(10000),
    x=df.head(10000).index,
    y="Global_active_power",
    color="Anomaly",
    title="Anomaly Detection Analysis"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Show anomaly records
st.subheader("⚠️ Detected Anomalies")

st.dataframe(
    anomalies.head(20),
    use_container_width=True
)

st.success("✅ Anomaly Detection Loaded Successfully")
