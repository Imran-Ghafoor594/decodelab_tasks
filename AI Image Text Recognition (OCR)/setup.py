from setuptools import setup, find_packages

setup(
    name="ai-image-text-recognition",
    version="1.0.0",
    author="Imran Ghafoor",
    description="AI OCR using EasyOCR",

    packages=find_packages(),

    install_requires=[
        "easyocr",
        "opencv-python",
        "numpy",
        "pillow",
        "streamlit",
        "pandas"
    ],

    python_requires=">=3.9"
)