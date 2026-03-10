import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os
import pickle
from datetime import datetime, timedelta

st.set_page_config(
    page_title="🌍 Earthquake Risk Tracker",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
.metric-card {background:#1e1e2e;padding:20px;border-radius:10px;border-left:4px solid #e74c3c;}
.stMetric {background:#1e1e2e;padding:10px;border-radius:8px;}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🌍 Earthquake Risk Tracker")
st.markdown("**Geospatial ML Pipeline** | USGS Data | DBSCAN + Random Forest + ARIMA")
st.markdown("*UMass Dartmouth MS Data Science Thesis | [harshmalviya.com](https://harshmalviya.com)*")
st.divider()

# ── Key Metrics ───────────────────────────────────────────────────────────────
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("RF Accuracy",       "71.6%",  "+38.6% vs random")
col2.metric("DBSCAN Silhouette", "0.64",   "vs K-Means 0.48")
col3.metric("Clusters Found",    "104",    "eps=0.045")
col4.metric("Events Analyzed",   "27,696", "USGS 1988-2022")
col5.metric("ARIMA p-value",     "0.0003", "Stationary ✅")
st.divider()

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.header("🔧 Controls")
page = st.sidebar.radio("Navigate", [
    "🔮 Live Predictor",
    "📊 Model Results",
    "🗺️ Interactive Map",
    "📈 About"
])

# ── Page: Live Predictor ──────────────────────────────────────────────────────
if page == "🔮 Live Predictor":
    st.header("🔮 Live Earthquake Risk Predictor")
    st.markdown("Enter location parameters to predict earthquake risk category.")

    col1, col2, col3 = st.columns(3)
    with col1:
        latitude  = st.number_input("Latitude",     -90.0,  9
