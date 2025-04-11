import streamlit as st
import pandas as pd

st.title("📊 Bar Chart Example")

st.markdown("This page demonstrates how st.bar_chart works.")

# Chart
chart_data = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Values": [10, 20, 15]
})

st.bar_chart(chart_data.set_index("Category"))

# Mention altair
st.markdown("👉 For more customization, check out `st.altair_chart()`.")
st.write("If `st.bar_chart()` does not guess the data specification correctly, try specifying your desired chart using `st.altair_chart()`.")