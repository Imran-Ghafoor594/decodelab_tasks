# DecodeLabs — AI Internship Projects

A collection of 4 AI/ML projects built during the **DecodeLabs Artificial Intelligence Internship**. Each project lives in its own folder with its own README, code, and dependencies — this file gives an overview of all of them together.

**Author:** Imran Ghafoor · *AI & ML Enthusiast*

---

## Projects

| # | Project | Description | Tech Stack |
|---|---------|-------------|------------|
| 1 | [Rule-Based AI Chatbot](./rule-based-AI-chatbot) | A simple rule-based chatbot with a knowledge-base dictionary, predefined intents, and fallback responses. | Python |
| 2 | [AI Movie Recommender (TF-IDF)](./AI-movie-recommender-using-tfidf) | Recommends movies using TF-IDF vectorization and Cosine Similarity on genre/language features. CLI + Streamlit web app. | Python, Pandas, Scikit-learn, Streamlit |
| 3 | [AI Image Text Recognition](./image-text-recognition) | OCR app that extracts text from images using EasyOCR, with confidence scores and a Streamlit interface. | Python, EasyOCR, OpenCV, Streamlit |
| 4 | [Iris Flower Classifier (KNN)](./flower-classifier-using-knn) | Classifies Iris flower species using the K-Nearest Neighbors algorithm, with full evaluation metrics. | Python, Scikit-learn, Jupyter |

---

## Repository Structure

```
Decodelabs/
│
├── rule-based-AI-chatbot/
│   ├── chatbot.py
│   ├── requirements.txt
│   └── README.md
│
├── AI-movie-recommender-using-tfidf/
│   ├── src/
│   ├── data/
│   ├── app.py
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── image-text-recognition/
│   ├── src/
│   ├── app.py
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── flower-classifier-using-knn/
│   ├── notebooks/
│   ├── data/
│   ├── requirements.txt
│   └── README.md
│
└── README.md   ← you are here
```

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/Imran-Ghafoor594/decodelab_tasks.git
cd decodelab_tasks
```

Each project is self-contained. Move into the project folder you want to run and install its dependencies:

```bash
cd <project-folder>
pip install -r requirements.txt
```

Then follow the **Run** instructions in that project's own README.

---

## Tech Stack Overview

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, EasyOCR, OpenCV, Pillow
- **Interfaces:** Streamlit (web apps), CLI, Jupyter Notebook
- **Concepts covered:** Rule-based systems, NLP (TF-IDF, Cosine Similarity), Computer Vision (OCR), Classical ML (KNN)

---

## About DecodeLabs Internship

These projects were completed as part of the **DecodeLabs Artificial Intelligence Internship**, covering practical, hands-on tasks across NLP, computer vision, and classical machine learning.

---

## License

Individual projects are licensed under the MIT License where noted. See each project folder for details.

## Author

**Imran Ghafoor**
*AI & ML Enthusiast*
