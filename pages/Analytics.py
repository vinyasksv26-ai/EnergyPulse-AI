import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Advanced Analytics")

df = pd.read_csv(
    "data/smart_meter_feature_engineered.csv"
)

peak_hour = (
    df.groupby("Hour")
    ["Global_active_power"]
    .mean()
    .idxmax()
)

peak_month = (
    df.groupby("Month")
    ["Global_active_power"]
    .mean()
    .idxmax()
)

col1,col2 = st.columns(2)

col1.metric(
    "Peak Hour",
    f"{peak_hour}:00"
)

col2.metric(
    "Peak Month",
    peak_month
)

hourly = (
    df.groupby("Hour")
    ["Global_active_power"]
    .mean()
    .reset_index()
)

fig = px.line(
    hourly,
    x="Hour",
    y="Global_active_power",
    title="Hourly Consumption Pattern"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

monthly = (
    df.groupby("Month")
    ["Global_active_power"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    monthly,
    x="Month",
    y="Global_active_power",
    title="Monthly Consumption Pattern"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
