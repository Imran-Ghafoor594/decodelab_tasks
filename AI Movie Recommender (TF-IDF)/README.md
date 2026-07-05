# AI Movie Recommendation System

A simple AI-powered Movie Recommendation System built with **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. This project recommends movies based on similarity between movie genres and languages using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## Project Overview

The goal of this project is to recommend movies according to a user's favorite movie. Instead of random suggestions, the system analyzes movie features and finds similar movies using AI-based similarity matching.

This project was developed as part of an Artificial Intelligence Internship assignment.

---

## Features

- AI-based recommendation system
- TF-IDF feature extraction
- Cosine Similarity matching
- Clean and modular Python code
- Streamlit web interface
- Command-line interface
- Unit testing included
- Easy to extend with larger datasets

---

## Project Structure

```
AI-Recommendation-System/
│
├── data/
│   └── movies.csv
│
├── outputs/
│   └── recommendations.txt
│
├── src/
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── recommender.py
│   ├── utils.py
│   └── __init__.py
│
├── tests/
│   └── test_recommender.py
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Imran-Ghafoor594/decodelab_tasks.git
```

Move into the project directory:

```bash
cd AI-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  Run the Command Line Version

```bash
python main.py
```

---

## Run the Streamlit Web App

```bash
streamlit run app.py
```

---

##  Run Unit Tests

```bash
python -m unittest tests/test_recommender.py
```

or

```bash
pytest
```

---

## Sample Output

```
Enter your favorite movie:

Inception

Recommended Movies:

1. Interstellar
2. The Dark Knight
3. Avengers Endgame
4. John Wick
5. Gladiator
```

---

## Future Improvements

- Content-based recommendation
- Collaborative filtering
- User authentication
- Movie posters
- TMDB API integration
- Deep Learning recommendation models
- Hybrid recommendation engine

---

## Contributing

Contributions are welcome. Feel free to fork this repository and submit pull requests.

---

## License

This project is licensed under the MIT License.

---

##  Author

**Imran Ghafoor**
***| AI & ML Enthusiast |***
