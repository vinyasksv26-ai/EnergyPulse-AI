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
df = pd.read_csv(
    "data/smart_meter_small.csv"
)

# ==========================================
# KPI METRICS
# ==========================================

peak_hour = (
    df.groupby("Hour")["Global_active_power"]
    .mean()
    .idxmax()
)

peak_month = (
    df.groupby("Month")["Global_active_power"]
    .mean()
    .idxmax()
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "⚡ Peak Hour",
        f"{peak_hour}:00"
    )

with col2:
    st.metric(
        "📅 Peak Month",
        peak_month
    )

st.divider()

# ==========================================
# HOURLY ANALYSIS
# ==========================================

st.subheader("⏰ Hourly Consumption Pattern")

hourly = (
    df.groupby("Hour")["Global_active_power"]
    .mean()
    .reset_index()
)

fig1 = px.line(
    hourly,
    x="Hour",
    y="Global_active_power",
    markers=True,
    title="Average Consumption by Hour"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================================
# MONTHLY ANALYSIS
# ==========================================

st.subheader("📅 Monthly Consumption Pattern")

monthly = (
    df.groupby("Month")["Global_active_power"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    monthly,
    x="Month",
    y="Global_active_power",
    title="Average Consumption by Month"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================================
# WEEKEND VS WEEKDAY
# ==========================================

st.subheader("🏠 Weekend vs Weekday Analysis")

weekend = (
    df.groupby("Weekend")["Global_active_power"]
    .mean()
    .reset_index()
)

weekend["Weekend"] = weekend["Weekend"].replace(
    {
        0: "Weekday",
        1: "Weekend"
    }
)

fig3 = px.pie(
    weekend,
    values="Global_active_power",
    names="Weekend",
    title="Weekend vs Weekday Consumption"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.success("✅ Analytics Loaded Successfully")
