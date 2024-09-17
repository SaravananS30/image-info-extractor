import streamlit as st
from PIL import Image
import google.generativeai as genai
import os

# Configure Google Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set the model and generation config
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flask",  # You can choose the model variant
    generation_config=generation_config,
)

# Streamlit App Title
st.set_page_config(page_title="AI Image Info Extractor", page_icon=":camera_with_flash:", layout="centered")

st.title("AI Image Info Extractor :camera_with_flash:")
st.write("Upload an image and ask any questions related to it!")


# Upload Image section
uploaded_file = st.file_uploader("Choose an image file...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Text Input for asking a question about the image
    question = st.text_input("Ask a question about this image:")

    if st.button("Ask AI"):
        if question:
            with st.spinner("Processing your request..."):
                # AI Querying based on image and question
                try:
                    response = model.generate_content([question, img])
                    st.success("AI Response:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error occurred: {str(e)}")
        else:
            st.error("Please enter a question.")
else:
    st.write("Please upload an image to proceed.")
