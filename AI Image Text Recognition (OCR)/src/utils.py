import os


def save_text(text, output_file):

    os.makedirs(
        os.path.dirname(output_file),
        exist_ok=True
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)


def print_results(results):

    print("\nDetected Text\n")

    for i, item in enumerate(results, start=1):

        print(f"{i}. {item['text']}")
        print(f"   Confidence: {item['confidence']}")