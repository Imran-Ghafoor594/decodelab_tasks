import streamlit as st
from src.recommender import MovieRecommender

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🎬 AI Movie Recommendation System")
st.write(
    "Get personalized movie recommendations using "
    "AI-based similarity matching."
)

# -----------------------------
# Load Recommender
# -----------------------------
recommender = MovieRecommender(r"F:\Internship\Decodelabs\Task-3\data\movies.csv")

movie_list = sorted(recommender.movies["Movie"].tolist())

# -----------------------------
# User Input
# -----------------------------
selected_movie = st.selectbox(
    "Select Your Favorite Movie",
    movie_list
)

top_n = st.slider(
    "Number of Recommendations",
    min_value=1,
    max_value=10,
    value=5
)

# -----------------------------
# Recommendation Button
# -----------------------------
if st.button("Recommend Movies"):

    recommendations = recommender.recommend(
        selected_movie,
        top_n
    )

    if recommendations:

        st.success("Recommendations Generated Successfully!")

        st.subheader("Recommended Movies")

        for i, movie in enumerate(recommendations, start=1):
            st.write(f"{i}. {movie}")

    else:
        st.error("No recommendations found.")