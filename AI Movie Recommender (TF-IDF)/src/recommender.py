import pandas as pd

from src.preprocessing import DataPreprocessor
from src.simmilarity import SimilarityEngine


class MovieRecommender:

    def __init__(self, dataset_path):
        self.processor = DataPreprocessor(dataset_path)
        self.engine = SimilarityEngine()

        self.movies = self.processor.preprocess()
        self.similarity_matrix = self.engine.fit_transform(self.movies)

    def recommend(self, favorite_movie, top_n=5):

        favorite_movie = favorite_movie.lower()

        movie_indices = pd.Series(
            self.movies.index,
            index=self.movies["Movie"].str.lower()
        )

        if favorite_movie not in movie_indices:
            return []

        idx = movie_indices[favorite_movie]

        similarity_scores = list(enumerate(self.similarity_matrix[idx]))

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        similarity_scores = similarity_scores[1:top_n + 1]

        recommendations = []

        for i, score in similarity_scores:
            recommendations.append(self.movies.iloc[i]["Movie"])

        return recommendations