import streamlit as st
from PIL import Image, ImageFilter

st.title("Photo Manipulation")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    effect = st.selectbox("Choose an effect", ["None", "Grayscale", "Blur", "Rotate"])
    
    if effect == "Grayscale":
        image = image.convert("L")
    elif effect == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif effect == "Rotate":
        angle = st.slider("Rotation angle", 0, 360)
        image = image.rotate(angle)

    st.image(image, caption=f"Image with {effect} effect", use_container_width=True)
