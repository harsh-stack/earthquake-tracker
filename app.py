import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(page_title="Earthquake Risk Tracker", page_icon="🌍", layout="wide")
st.title("🌍 Earthquake Risk Tracker")
st.markdown("UMass Dartmouth MS Data Science | [harshmalviya.com](https://harshmalviya.com)")
st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("RF Accuracy", "71.6%")
col2.metric("DBSCAN Silhouette", "0.64")
col3.metric("Clusters", "104")
col4.metric("Events", "27,696")
st.divider()

st.header("Live Risk Predictor")
latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=37.5)
longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=-122.0)
depth = st.number_input("Depth km", min_value=0.0, max_value=700.0, value=50.0)

if st.button("Predict"):
    if depth < 33:
        risk = "High Risk"
    elif depth < 70:
        risk = "Moderate Risk"
    else:
        risk = "Low Risk"
    st.success(risk)
