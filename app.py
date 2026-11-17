import pandas as pd
import streamlit as st
from detector import analyze_logs, load_logs

st.set_page_config(page_title="CyberShield | Security Monitor", page_icon="🛡️", layout="wide")
st.title("🛡️ CyberShield")
st.caption("A defensive security log analyzer for learning and portfolio demonstrations.")

uploaded = st.file_uploader("Upload an authentication or network CSV log", type=["csv"])
source = uploaded if uploaded else "data/sample_logs.csv"

try:
    logs = load_logs(source)
    alerts = analyze_logs(logs)
    c1, c2, c3 = st.columns(3)
    c1.metric("Log events", len(logs))
    c2.metric("Alerts", len(alerts))
    c3.metric("High severity", int((alerts["severity"] == "High").sum()) if not alerts.empty else 0)

    st.subheader("Security alerts")
    if alerts.empty:
        st.success("No suspicious patterns detected in this dataset.")
    else:
        st.dataframe(alerts, use_container_width=True, hide_index=True)
        st.download_button("Download alerts CSV", alerts.to_csv(index=False), "cybershield_alerts.csv", "text/csv")

    st.subheader("Event summary")
    if "event_type" in logs.columns:
        st.bar_chart(logs["event_type"].value_counts())
    st.subheader("Raw log events")
    st.dataframe(logs, use_container_width=True, hide_index=True)
except Exception as exc:
    st.error(f"Could not analyze the supplied CSV: {exc}")
    st.info("See README.md for the required CSV columns and sample format.")
