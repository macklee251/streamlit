import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt


# Line Plot
df1 = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.dataframe(df1)
st.line_chart(df1)

a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = a**2
df2 = pd.DataFrame(np.transpose([a, b]))
df2 = df2.set_index(0)
df2.rename(columns={0: "x", 1: "y=x^2"}, inplace=True)

st.dataframe(df2)
st.line_chart(df2)


# Area chart
st.area_chart(df2)


# Bar chart
st.bar_chart(df2)