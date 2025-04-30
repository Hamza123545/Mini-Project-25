import streamlit as st
import qrcode
import cv2
from PIL import Image
import numpy as np
import io

st.title("QR Code Generator / Decoder")

option = st.selectbox("Choose an option", ("Generate QR Code", "Decode QR Code"))

if option == "Generate QR Code":
    text = st.text_input("Enter text to generate QR code:")
    if text:
        qr = qrcode.make(text)

        
        img_byte_arr = io.BytesIO()
        qr.save(img_byte_arr)
        img_byte_arr.seek(0)

       
        st.image(img_byte_arr, caption="Generated QR Code", use_container_width=True)

elif option == "Decode QR Code":
    uploaded_file = st.file_uploader("Upload a QR code image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        image = np.array(image)
        detector = cv2.QRCodeDetector()
        value, pts, qr_code = detector(image)
        if value:
            st.write(f"Decoded Text: {value}")
        else:
            st.write("No QR Code detected.")
