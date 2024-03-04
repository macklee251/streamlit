import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "year": ["2023", "2024", "2025"],
    "col1": ["new_value1", "new_value4", "new_value7"],
    "col2": ["new_value2", "new_value5", "new_value8"],
    "col3": ["new_value3", "new_value6", "new_value9"]
})

# We can use st.dataframe or st.write to display a dataframe
st.dataframe(df)
st.write(df)

st.table(df)

st.metric(label="Metric label", value=123, delta=0.5, delta_color="inverse")