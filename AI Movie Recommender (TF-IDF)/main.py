from src.preprocessing import DataPreprocessor
from src.recommender import MovieRecommender
from src.utils import save_recommendations

processor = DataPreprocessor(r"F:\Internship\Decodelabs\Task-3\data\movies.csv")

movies = processor.preprocess()

recommender = MovieRecommender(r"F:\Internship\Decodelabs\Task-3\data\movies.csv")

movie = input("Enter your favorite movie: ")

recommendations = recommender.recommend(movie)

if recommendations:

    print("\nRecommended Movies:\n")

    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie}")

    save_recommendations(
        recommendations,
        r"F:\Internship\Decodelabs\Task-3\outputs\recommendations.txt"
    )

else:
    print("Movie not found in dataset.")

print(movies.head())