import streamlit as st
import pandas as pd
import requests

st.title("🌍 Global Migration Dashboard")

# Fetch data from API
response = requests.get("http://localhost:8000/migration")
data = pd.DataFrame(response.json())

st.dataframe(data)

st.subheader("Top Destination Countries")
top_dest = data.groupby("destination")["count"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_dest)
