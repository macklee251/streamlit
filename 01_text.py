import streamlit as st
import pandas as pd

# Title
st.title("This is a title")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Markdown
st.markdown("##### This is a markdown")

# Caption
st.caption("This is a caption")

# Code block
st.code("""import pandas as pd
df = pd.DataFrame()""")

# Preformatted text
st.text("This is a preformatted text")

# Latex
st.latex(r"y = x^2")

# Divider
st.text("Text above divider")
st.divider()
st.text("Text below divider")

st.write("some text")