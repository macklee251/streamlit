import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Button
primary_btn = st.button('Primary', type='primary')
secondary_btn = st.button('Secondary', type='secondary')

if primary_btn:
    st.write('Primary button clicked!')
if secondary_btn:
    st.write('Secondary button clicked!')
st.divider()

# Checkbox
checkbox = st.checkbox('Check me out')
if checkbox:
    st.write('Checkbox on!')
else:
    st.write('Checkbox off!')

st.divider()


st.divider()


st.divider()


st.divider()


st.divider()


st.divider()


st.divider()
