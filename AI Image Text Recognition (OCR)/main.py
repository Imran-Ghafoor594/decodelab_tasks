from src.image_loader import ImageLoader
from src.ocr_engine import OCREngine
from src.utils import save_text
from src.config import OUTPUT_FILE


def main():

    image_path = input("Enter image path: ")

    try:

        ImageLoader.load_image(image_path)

        ocr = OCREngine()

        results = ocr.extract_text(image_path)

        print("\nDetected Text\n")

        for item in results:

            print(
                f"{item['text']} "
                f"(Confidence: {item['confidence']})"
            )

        text = ocr.get_plain_text(image_path)

        save_text(text, OUTPUT_FILE)

        print("\nText saved successfully.")
        print(f"Output File: {OUTPUT_FILE}")

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()