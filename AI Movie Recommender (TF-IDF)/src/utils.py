import os


def save_recommendations(recommendations, output_file):
    """
    Save recommendations to a text file.
    """

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as file:
        for movie in recommendations:
            file.write(movie + "\n")

    print(f"Recommendations saved to {output_file}")