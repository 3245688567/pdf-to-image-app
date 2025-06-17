import fitz  # PyMuPDF
from PIL import Image
import io

def pdf_to_images(pdf_bytes, zoom=2):  # zoom=2 means 144 DPI (2 x 72)
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    images = []

    mat = fitz.Matrix(zoom, zoom)  # zoom factor

    for page in doc:
        pix = page.get_pixmap(matrix=mat, alpha=False)  # alpha=False to get RGB image (no transparency)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        images.append(img)

    return images
