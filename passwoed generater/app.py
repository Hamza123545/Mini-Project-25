import streamlit as st
import random
import string

st.title("Password Generator")

length = st.slider("Password length", 6, 32, 12)
include_special = st.checkbox("Include special characters", value=True)

if st.button("Generate Password"):
    chars = string.ascii_letters + string.digits
    if include_special:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    st.code(password, language='text')
