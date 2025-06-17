import streamlit as st
from tools.pdf_converter import pdf_to_images
import zipfile
import io

st.set_page_config(page_title="PDF to Image Converter", layout="centered")
st.title("📄🔄🖼️ PDF to Image Converter")

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write(f"Processing **{uploaded_file.name}**...")
        pdf_bytes = uploaded_file.read()
        images = pdf_to_images(pdf_bytes)

        st.success(f"Converted {len(images)} pages from {uploaded_file.name}")

        # Create ZIP for this PDF
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
            for idx, image in enumerate(images):
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format="PNG")
                zip_file.writestr(f"page_{idx+1}.png", img_byte_arr.getvalue())
        zip_buffer.seek(0)

        # Download buttons at top and bottom for each PDF
        st.download_button(
            label=f"📦 Download {uploaded_file.name} Images ZIP (Top)",
            data=zip_buffer,
            file_name=f"{uploaded_file.name}_images.zip",
            mime="application/zip",
            key=f"download_top_{uploaded_file.name}"
        )

        for i, img in enumerate(images):
            st.image(img, caption=f"{uploaded_file.name} - Page {i + 1}", use_container_width=True)

        st.download_button(
            label=f"📦 Download {uploaded_file.name} Images ZIP (Bottom)",
            data=zip_buffer,
            file_name=f"{uploaded_file.name}_images.zip",
            mime="application/zip",
            key=f"download_bottom_{uploaded_file.name}"
        )
