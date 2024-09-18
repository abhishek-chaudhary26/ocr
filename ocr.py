import streamlit as st
from PIL import Image
import pytesseract

# If you're on Windows, specify the path to tesseract executable (optional)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Title of the app
st.title("OCR App - Extract Text from Image")

# Instructions
st.write("Upload an image, and the app will extract text from it.")

# File uploader to upload images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    img = Image.open(uploaded_file)
    
    # Display the uploaded image in the app
    st.image(img, caption='Uploaded Image', use_column_width=True)
    st.write("Extracting text...")

    # Perform OCR on the image
    extracted_text = pytesseract.image_to_string(img)

    # Display the extracted text
    st.write("Here is the text from the image:")
    st.text(extracted_text)
