import streamlit as st

st.title("📄 Session State & Reset")

st.markdown("This page demonstrates how session state persists across pages.")

if "count" not in st.session_state:
    st.session_state.count = 0

st.write(f"Current counter value: **{st.session_state.count}**")

if st.button("Reset Counter"):
    st.session_state.count = 0
    st.rerun()
