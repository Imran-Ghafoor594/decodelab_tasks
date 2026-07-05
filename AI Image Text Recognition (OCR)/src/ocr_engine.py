import cv2
import easyocr
import tempfile

from src.image_processer import ImageProcessor


class OCREngine:

    def __init__(self, languages=["en"]):
        self.reader = easyocr.Reader(languages)

    def extract_text(self, image_path):

        processed_image = ImageProcessor.preprocess(image_path)

        with tempfile.NamedTemporaryFile(
            suffix=".png",
            delete=False
        ) as temp:

            cv2.imwrite(temp.name, processed_image)

            results = self.reader.readtext(temp.name)

        extracted = []

        for _, text, confidence in results:

            extracted.append({
                "text": text,
                "confidence": round(confidence, 2)
            })

        return extracted

    def get_plain_text(self, image_path):

        results = self.extract_text(image_path)

        return "\n".join(
            item["text"]
            for item in results
        )