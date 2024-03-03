# import libraries
import streamlit as st
from streamlit_embedcode import github_gist

# Add code from a GitHub Gist
st.title("Add code from a GitHub Gist")
st.write("You can add code from a GitHub Gist using the `streamlit_embedcode` library.")

link = "https://gist.github.com/gak92/1d5c5fd9db6956c6dd9da66a6a385b9f"

st.write("Here is the code from the Gist:")
github_gist(link)