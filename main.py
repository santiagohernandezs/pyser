import streamlit as st

st.title('Pyser')

st.file_uploader('Upload a file', type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
