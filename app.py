import streamlit as st
from tools.pdf_converter import pdf_to_images
import zipfile
import io

st.set_page_config(page_title="PDF to Image Converter", layout="centered")
st.title("📄🔄🖼️ PDF to Image Converter")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.info("Processing PDF...")
    images = pdf_to_images(uploaded_file.read())

    st.success(f"Converted {len(images)} pages.")

    # Create ZIP in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
        for idx, image in enumerate(images):
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format="PNG")
            zip_file.writestr(f"page_{idx+1}.png", img_byte_arr.getvalue())
    zip_buffer.seek(0)

    # --- TOP Download Button ---
    st.download_button(
        label="📦 Download All Images as ZIP",
        data=zip_buffer,
        file_name="converted_images.zip",
        mime="application/zip",
        key="download_top"
    )

    # Show images
    for i, img in enumerate(images):
        st.image(img, caption=f"Page {i + 1}", use_container_width=True)

    # --- BOTTOM Download Button ---
    st.download_button(
        label="📦 Download All Images as ZIP",
        data=zip_buffer,
        file_name="converted_images.zip",
        mime="application/zip",
        key="download_bottom"
    )
