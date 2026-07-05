from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:
    """
    Creates TF-IDF vectors and computes cosine similarity.
    """

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.similarity_matrix = None

    def fit_transform(self, data):
        """
        Convert text features into TF-IDF vectors.
        """
        tfidf_matrix = self.vectorizer.fit_transform(data["Features"])

        self.similarity_matrix = cosine_similarity(tfidf_matrix)

        return self.similarity_matrix