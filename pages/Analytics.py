import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Advanced Analytics")

# Load Dataset
df = pd.read_csv("smart_meter_small.csv")

st.write("Dataset Shape:", df.shape)

# Peak Hour
peak_hour = (
    df.groupby("Hour")["Global_active_power"]
    .mean()
    .idxmax()
)

# Peak Month
peak_month = (
    df.groupby("Month")["Global_active_power"]
    .mean()
    .idxmax()
)

col1, col2 = st.columns(2)

with col1:
    st.metric("⚡ Peak Hour", f"{peak_hour}:00")

with col2:
    st.metric("📅 Peak Month", str(peak_month))

# Hourly Analysis
hourly = (
    df.groupby("Hour")["Global_active_power"]
    .mean()
    .reset_index()
)

fig1 = px.line(
    hourly,
    x="Hour",
    y="Global_active_power",
    title="Hourly Consumption Pattern"
)

st.plotly_chart(fig1, use_container_width=True)

# Monthly Analysis
monthly = (
    df.groupby("Month")["Global_active_power"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    monthly,
    x="Month",
    y="Global_active_power",
    title="Monthly Consumption Pattern"
)

st.plotly_chart(fig2, use_container_width=True)

st.success("✅ Analytics Loaded Successfully")
