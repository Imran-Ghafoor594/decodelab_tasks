import unittest

from src.recommender import MovieRecommender


class TestMovieRecommender(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.recommender = MovieRecommender("data/movies.csv")

    def test_movie_exists(self):
        recommendations = self.recommender.recommend("Inception")

        self.assertTrue(len(recommendations) > 0)

    def test_movie_not_found(self):
        recommendations = self.recommender.recommend("ABC XYZ")

        self.assertEqual(recommendations, [])

    def test_top_three(self):
        recommendations = self.recommender.recommend(
            "Inception",
            top_n=3
        )

        self.assertEqual(len(recommendations), 3)

    def test_return_type(self):
        recommendations = self.recommender.recommend("Titanic")

        self.assertIsInstance(recommendations, list)


if __name__ == "__main__":
    unittest.main()