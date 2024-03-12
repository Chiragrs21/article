import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


df = pd.read_csv('data.csv')

def information(value):
  
    input_title = value

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['title'].values.astype('U'))

    input_tfidf = vectorizer.transform([input_title])

# Compute cosine similarity between input title and dataset titles
    cosine_similarities = cosine_similarity(
        input_tfidf, tfidf_matrix).flatten()

    most_similar_index = np.argmax(cosine_similarities)


    most_similar_row = df.iloc[most_similar_index]

    return most_similar_row
