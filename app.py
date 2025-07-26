import streamlit as st
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data/weather.db')
query = "SELECT * FROM weather"
df = pd.read_sql_query(query, conn)
conn.close()

st.title("Weather Data Visualization")
st.dataframe(df)

# Example chart: temperature and humidity over time
if 'date' in df.columns:
    st.line_chart(df.set_index('date')[['temperature', 'humidity']])
