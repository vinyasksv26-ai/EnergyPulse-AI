import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

st.set_page_config(
    page_title="Anomaly Detection",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Anomaly Detection")

df = pd.read_csv(
    "data/smart_meter_feature_engineered.csv"
)

model = IsolationForest(
    contamination=0.01,
    random_state=42
)

df["Anomaly"] = model.fit_predict(
    df[["Global_active_power"]]
)

anomalies = df[
    df["Anomaly"] == -1
]

st.metric(
    "Anomalies Detected",
    len(anomalies)
)

fig = px.scatter(
    df.head(10000),
    x=df.head(10000).index,
    y="Global_active_power",
    color="Anomaly",
    title="Anomaly Detection"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    anomalies.head(20)
)
