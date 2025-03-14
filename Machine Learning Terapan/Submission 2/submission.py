# -*- coding: utf-8 -*-
"""Submission (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QYpLLNfC3usaZTR3orNnc-f94e3JYv9G

# Import Library
"""

import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from wordcloud import WordCloud
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from scipy.sparse import save_npz
import warnings
warnings.filterwarnings('ignore')

"""# Load Data"""

df = pd.read_csv('data/netflix_data.csv')

df.info()

"""### Cek data apakah ada missing value

terdapat missing value pada kolom director, cast, country, date_added, rating, duration

"""

df.isna().sum()

"""mengisi missing value dengan string kosong"""

df.fillna('', inplace=True)

"""# EDA

Jumlah film yang dirilis per tahun
"""

movie_counts = df['release_year'].value_counts().sort_index()
fig = go.Figure(data=go.Bar(x=movie_counts.index, y=movie_counts.values))
fig.update_layout(
    plot_bgcolor='rgb(17, 17, 17)',
    paper_bgcolor='rgb(17, 17, 17)',
    font_color='white',
    title='Number of Movies Released Each Year',
    xaxis=dict(title='Year'),
    yaxis=dict(title='Number of Movies')
)
fig.update_traces(marker_color='white')
fig.show()

"""Distribusi film berdasarkan negara

"""

top_countries = df['country'].value_counts().head(10)

fig = px.treemap(names=top_countries.index, parents=["" for _ in top_countries.index], values=top_countries.values)

fig.update_layout(
    plot_bgcolor='rgb(17, 17, 17)',
    paper_bgcolor='rgb(17, 17, 17)',
    font_color='white',
    title='Top Countries with Highest Number of Movies',
)
fig.show()

"""# Data Processing"""

new_df = df[['title', 'type', 'director', 'cast', 'rating', 'listed_in', 'description']]
new_df.set_index('title', inplace=True)

new_df.head()

"""membuat class untuk memproses teks"""

class TextCleaner:
    def separate_text(self, texts):
        unique_texts = set()
        for text in texts.split(','):
            unique_texts.add(text.strip().lower())
        return ' '.join(unique_texts)

    def remove_space(self, texts):
        return texts.replace(' ', '').lower()

    def remove_punc(self, texts):
        texts = texts.lower()
        texts = texts.translate(str.maketrans('', '', string.punctuation))
        return ' '.join(texts.split())

    def clean_text(self, texts):
        texts = self.separate_text(texts)
        texts = self.remove_space(texts)
        texts = self.remove_punc(texts)
        return texts

cleaner = TextCleaner()

new_df['type']        = new_df['type'].apply(cleaner.remove_space)
new_df['director']    = new_df['director'].apply(cleaner.separate_text)
new_df['cast']        = new_df['cast'].apply(cleaner.separate_text)
new_df['rating']      = new_df['rating'].apply(cleaner.remove_space)
new_df['listed_in']   = new_df['listed_in'].apply(cleaner.separate_text)
new_df['description'] = new_df['description'].apply(cleaner.remove_punc)

"""# Feature Extraction (TF-IDF)

Menggabungkan fitur teks menjadi Bag of Words (BoW)
"""

new_df['BoW'] = new_df.apply(lambda row: ' '.join(row.dropna().values), axis=1)
new_df.drop(new_df.columns[:-1], axis=1, inplace=True)

new_df.head()

"""Menerapkan TF-IDF Vectorizer"""

tfid = TfidfVectorizer()
tfid_matrix = tfid.fit_transform(new_df['BoW'])

"""Menghitung Cosine Similarity antar judul


"""

cosine_sim = cosine_similarity(tfid_matrix, tfid_matrix)
cosine_sim

final_data = df[['title', 'type']]

final_data.head()

"""# Sistem Rekomendasi

Membuat class untuk mencari film atau tv show yang mirip
"""

import re
class FlixHub:
    def __init__(self, df, cosine_sim):
        self.df = df
        self.cosine_sim = cosine_sim

    def recommendation(self, title, total_result=5, threshold=0.5):
        idx = self.find_id(title)
        self.df['similarity'] = self.cosine_sim[idx]
        sort_df = self.df.sort_values(by='similarity', ascending=False)[1:total_result+1]

        movies = sort_df['title'][sort_df['type'] == 'Movie']
        tv_shows = sort_df['title'][sort_df['type'] == 'TV Show']

        similar_movies = []
        similar_tv_shows = []

        for i, movie in enumerate(movies):
            similar_movies.append('{}. {}'.format(i+1, movie))

        for i, tv_show in enumerate(tv_shows):
            similar_tv_shows.append('{}. {}'.format(i+1, tv_show))

        return similar_movies, similar_tv_shows

    def find_id(self, name):
        for index, string in enumerate(self.df['title']):
            if re.search(name, string):
                return index
        return -1

flix_hub = FlixHub(final_data, cosine_sim)
movies, tv_shows = flix_hub.recommendation('Back to 1989', total_result=10, threshold=0.5)

print('Similar Movie(s) list:')
for movie in movies:
    print(movie)

print('\nSimilar TV_show(s) list:')
for tv_show in tv_shows:
    print(tv_show)

flix_hub = FlixHub(final_data, cosine_sim)
movies, tv_shows = flix_hub.recommendation('Stranger Things', total_result=10, threshold=0.5)

print('Similar Movie(s) list:')
for movie in movies:
    print(movie)

print('\nSimilar TV_show(s) list:')
for tv_show in tv_shows:
    print(tv_show)



def evaluate_recommendation(flix_hub, title, ground_truth, total_result=10):
    recommended_movies, recommended_tv_shows = flix_hub.recommendation(title, total_result)

    recommended = set([rec.split('. ')[1] for rec in recommended_movies + recommended_tv_shows])
    relevant = set(ground_truth)  

    true_positives = len(recommended & relevant)
    precision = true_positives / len(recommended) if recommended else 0
    recall = true_positives / len(relevant) if relevant else 0

    return precision, recall

ground_truth_movies = ["Ant-Man and the Wasp", "Equilibrium"]  
ground_truth_tv_shows = ["Miss in Kiss", "When I See You Again", "Way Back into Love", "Beyond Stranger Things"]  
ground_truth = ground_truth_movies + ground_truth_tv_shows

precision, recall = evaluate_recommendation(flix_hub, "Stranger Things", ground_truth)
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")