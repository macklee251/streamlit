import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title='Spotify',
)

@st.cache_data
def load_data():
    # Operações pessadas
    df = pd.read_csv("/Users/macklee/Desktop/Computer science/Studies/Python/streamlit/spotify/01 Spotify.csv")
    return df

df = load_data()

st.session_state['df_spotify']=df

df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists)
df_filtered1 = df[df["Artist"] == artist]


albums = df_filtered1["Album"].value_counts().index
album = st.sidebar.selectbox("Album", albums)
df_filtered2 = df[df["Album"] == album]


col1, col2 = st.columns([.5, .5])

col1.bar_chart(df_filtered2["Stream"])
col2.line_chart(df_filtered2["Danceability"])