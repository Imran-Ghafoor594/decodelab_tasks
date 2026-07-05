import tempfile

import pandas as pd
import streamlit as st
from PIL import Image

from src.config import OUTPUT_FILE
from src.image_loader import ImageLoader
from src.ocr_engine import OCREngine
from src.utils import save_text

# ----------------------------------
# Page Config
# ----------------------------------

st.set_page_config(
    page_title="AI Image Text Recognition",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Image Text Recognition")
st.write("Extract text from images using EasyOCR")

st.divider()


# ----------------------------------
# Load OCR Model
# ----------------------------------

@st.cache_resource
def load_ocr():
    return OCREngine()


ocr = load_ocr()


# ----------------------------------
# Upload Image
# ----------------------------------

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file)

    left, right = st.columns(2)

    with left:

        st.subheader("Uploaded Image")

        st.image(
            image,
            use_container_width=True
        )

    # Save temporary image

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    ) as temp:

        image.save(temp.name)

        image_path = temp.name

    if st.button("Extract Text"):

        try:

            # Validate Image
            ImageLoader.load_image(image_path)

            # OCR
            results = ocr.extract_text(image_path)

            text = ocr.get_plain_text(image_path)

            save_text(
                text,
                OUTPUT_FILE
            )

            with right:

                st.subheader("Extracted Text")

                st.text_area(
                    "",
                    text,
                    height=300
                )

            if results:

                st.subheader("Confidence Scores")

                df = pd.DataFrame(results)

                st.dataframe(
                    df,
                    use_container_width=True
                )

            st.download_button(
                "Download Text",
                data=text,
                file_name="extracted_text.txt",
                mime="text/plain"
            )

            st.success("OCR Completed Successfully!")

        except Exception as e:

            st.error(f"Error: {e}")