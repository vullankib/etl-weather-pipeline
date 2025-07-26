import streamlit as st
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data/weather.db')
query = "SELECT * FROM weather"
df = pd.read_sql_query(query, conn)
conn.close()

st.title("Weather Data Visualization")

cities = df['city'].unique().tolist()
selected_city = st.selectbox("Select a city", cities)
city_df = df[df['city'] == selected_city]

st.dataframe(city_df)

# Example chart: temperature and humidity over time
if 'date' in city_df.columns:
    st.line_chart(city_df.set_index('date')[['temperature', 'humidity']])
