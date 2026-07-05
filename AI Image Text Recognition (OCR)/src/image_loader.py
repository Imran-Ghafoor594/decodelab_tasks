import os
from PIL import Image


class ImageLoader:

    @staticmethod
    def load_image(image_path):
        """
        Load and validate image.
        """

        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")

        return Image.open(image_path)