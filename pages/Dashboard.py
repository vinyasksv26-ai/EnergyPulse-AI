import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("data/smart_meter_small.csv")

st.title("📊 Energy Analytics Dashboard")

# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "⚡ Total Records",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "📈 Peak Consumption",
        f"{df['Global_active_power'].max():.2f} kWh"
    )

with col3:
    st.metric(
        "📊 Average Consumption",
        f"{df['Global_active_power'].mean():.2f} kWh"
    )

with col4:
    st.metric(
        "🔋 Minimum Consumption",
        f"{df['Global_active_power'].min():.2f} kWh"
    )

st.divider()

# ==========================================
# CONSUMPTION TREND
# ==========================================

st.subheader("⚡ Electricity Consumption Trend")

fig1 = px.line(
    df.head(5000),
    y="Global_active_power",
    title="Consumption Trend"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ==========================================
# MONTHLY ANALYSIS
# ==========================================

st.subheader("📅 Monthly Average Consumption")

monthly = (
    df.groupby("Month")["Global_active_power"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    monthly,
    x="Month",
    y="Global_active_power",
    title="Monthly Consumption"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ==========================================
# WEEKEND VS WEEKDAY
# ==========================================

st.subheader("🏠 Weekend vs Weekday Usage")

weekend = (
    df.groupby("Weekend")["Global_active_power"]
    .mean()
    .reset_index()
)

weekend["Weekend"] = weekend["Weekend"].replace(
    {0: "Weekday", 1: "Weekend"}
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

# ==========================================
# SEASONAL ANALYSIS
# ==========================================

if "Season" in df.columns:

    st.subheader("🌦 Seasonal Consumption")

    season = (
        df.groupby("Season")["Global_active_power"]
        .mean()
        .reset_index()
    )

    fig4 = px.bar(
        season,
        x="Season",
        y="Global_active_power",
        title="Seasonal Average Consumption"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.success("✅ Dashboard Loaded Successfully")
