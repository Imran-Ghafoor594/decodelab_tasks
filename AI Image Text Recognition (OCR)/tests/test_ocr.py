import os
import unittest

from src.ocr_engine import OCREngine


class TestOCR(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ocr = OCREngine()

    def test_engine_created(self):
        self.assertIsNotNone(self.ocr)

    def test_invalid_image(self):
        with self.assertRaises(Exception):
            self.ocr.extract_text("invalid_image.jpg")

    def test_plain_text_type(self):
        self.assertTrue(callable(self.ocr.get_plain_text))


if __name__ == "__main__":
    unittest.main()