import cv2


class ImageProcessor:

    @staticmethod
    def preprocess(image_path):
        """
        Preprocess image for better OCR accuracy.
        """

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError("Unable to read image.")

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Reduce noise
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        # Apply threshold
        processed = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        return processed