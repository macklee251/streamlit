import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title='Spotify',
)

df = pd.read_csv("/Users/macklee/Desktop/Computer science/Studies/Python/streamlit/01 Spotify.csv")
df.set_index("Track", inplace=True)

st.bar_chart(df[df["Stream"] > 1000000000]["Stream"])

