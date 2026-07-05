import pandas as pd


class DataPreprocessor:
    """
    Handles loading and preprocessing of the movie dataset.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """
        Load dataset from CSV file.
        """
        self.data = pd.read_csv(self.file_path)
        return self.data

    def clean_data(self):
        """
        Remove missing values and duplicate rows.
        """
        self.data = self.data.dropna()
        self.data = self.data.drop_duplicates()

        self.data["Genre"] = self.data["Genre"].str.strip()
        self.data["Language"] = self.data["Language"].str.strip()

        return self.data

    def create_features(self):
        """
        Combine important columns into a single feature.
        """
        self.data["Features"] = (
            self.data["Genre"] + " " +
            self.data["Language"]
        )

        return self.data

    def preprocess(self):
        """
        Complete preprocessing pipeline.
        """
        self.load_data()
        self.clean_data()
        self.create_features()
        return self.data