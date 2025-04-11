import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streamlit Demo", layout="wide")

# Title, markdown, and write
st.title("🌟 Streamlit Demo App")
st.markdown("Welcome to the **Streamlit demo**.")
st.write("This app showcases key features like layout, interaction, and session state.")

# Layout using columns
st.markdown("### 🔲 Columns Layout Example")
col1, col2, col3 = st.columns(3)
# col1, col2 = st.columns([2, 1])

with col1:
    st.write("This is the first column 👈")
with col2:
    st.write("This is the second column")
with col3:
    st.write("👉 This is the third column")

# Sidebar example
st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar. Use it for filters or navigation.")

# Text input and selectbox
st.markdown("### 🧑‍💻 User Input")
col1, col2 = st.columns([2, 1])

with col1:
    name = st.text_input("Enter your name:")
with col2:
    fruit = st.selectbox("Choose a fruit:", ["Apple", "Banana", "Cherry"])

if st.button("Submit"):
    st.write(f"Hello, **{name}**! You selected **{fruit}**.")
# if name:
#     st.markdown(f"<h3>Hello, <b>{name}</b>! You selected <b>{fruit}</b>.</h3>", unsafe_allow_html=True)


# Display table
st.markdown("### 📋 Table Example")
data = pd.DataFrame({
    "Fruit": ["Apple", "Banana", "Cherry"],
    "Quantity": [10, 20, 15]
})
st.table(data)
st.table(data[data["Fruit"] == fruit])
st.write(data)

# Session state + button
st.markdown("### 🔄 Session State Example")
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment Counter"):
    st.session_state.count += 1

st.write(f"🔢 Counter value: {st.session_state.count}")

