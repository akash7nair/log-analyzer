import streamlit as st
from datetime import datetime, timedelta
from analyzer import LogAnalyzer 

st.set_page_config(page_title="Log Analyzer")
st.title("Log Analysis Dashboard")

log_file = st.file_uploader("Upload log file", type=['log'])  
if log_file:
    analyzer = LogAnalyzer(log_file.name)  
    with open(log_file.name, 'wb') as f:  
        f.write(log_file.getbuffer())  

time_range = st.select_slider(
    "Analysis timeframe",
    options=["1h", "6h", "24h", "Custom"])

if st.button("Analyze"):  
    end_time = datetime.now()
    if time_range == "1h":  
        start_time = end_time - timedelta(hours=1)  
    elif time_range == "6h":  
        start_time = end_time - timedelta(hours=6)
    else:
        start_time = end_time - timedelta(days=1)


    results = analyzer.analyze_timeframe(start_time, end_time)
    
    #results = LogAnalyzer.analyze_timeframe(start_time, end_time)
    st.metric("Total Entries", results['total_entries'])
    st.metric("Errors Found", results['error_count'])
    st.metric("Unique Messages", results['unique_messages'])