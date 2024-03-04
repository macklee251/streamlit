import streamlit as st
import pandas as pd
import webbrowser

st.markdown("# FIFA 2023 official dataset!")
st.sidebar.markdown("Desenvolvido por [Macklee](wwww.mackhughes.com)")

btn = st.button("Acesse of dados do kaggle")

if btn:
    webbrowser.open("https://www.kaggle.com/")
    
st.markdown("Este é um conjunto de dados oficial do FIFA 2023, que contém informações valiosas sobre jogadores, times, estatísticas de partidas e muito mais. Com base nesses dados, é possível realizar análises detalhadas e extrair insights interessantes sobre o mundo do futebol. O conjunto de dados é uma fonte confiável para pesquisadores, analistas e entusiastas do esporte. Explore as informações disponíveis e mergulhe no fascinante universo do futebol com o FIFA 2023 official dataset!")