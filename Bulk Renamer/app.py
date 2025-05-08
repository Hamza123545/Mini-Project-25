import os
import streamlit as st

st.title("Bulk File Renamer")

uploaded_files = st.file_uploader("Upload Files", accept_multiple_files=True)

prefix = st.text_input("Enter Prefix for Renaming:")

if uploaded_files and prefix:
    for uploaded_file in uploaded_files:
        file_path = os.path.join("/tmp", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        new_file_name = prefix + uploaded_file.name
        new_file_path = os.path.join("/tmp", new_file_name)
        os.rename(file_path, new_file_path)

        st.write(f"Renamed {uploaded_file.name} to {new_file_name}")
