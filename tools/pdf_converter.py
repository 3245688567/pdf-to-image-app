from pdf2image import convert_from_bytes

def pdf_to_images(pdf_bytes):
    # Convert PDF bytes to list of PIL images
    images = convert_from_bytes(pdf_bytes)
    return images
