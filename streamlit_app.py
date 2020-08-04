import streamlit as st

"""
# Trivial Streamlit App

This is the most basic Streamlit app _ever_!
"""

v = st.slider("Choose a value", 0, 100)

"You selected:", v
