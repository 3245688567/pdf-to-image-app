import streamlit as st
from tools.pdf_converter import pdf_to_images

st.set_page_config(page_title="PDF to Image Converter", layout="centered")
st.title("📄🔄🖼️ PDF to Image Converter")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.info("Processing PDF...")
    images = pdf_to_images(uploaded_file.read())
    
    st.success(f"Converted {len(images)} pages.")
    
    for i, img in enumerate(images):
        st.image(img, caption=f"Page {i + 1}", use_column_width=True)
