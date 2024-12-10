import streamlit as st
import pickle
import requests
import pandas as pd
import numpy as np

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cff335047ada426f931e9b22c1cb936d&language=en-US'.format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    sorted_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]
    movies_list = [(index, float(score)) for index, score in sorted_list]
    
    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch movie cover using TMDB API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


# Load the two parts of the vectors
with open('vectors_part1.pkl', 'rb') as f:
    similarity_part1 = pickle.load(f)

with open('vectors_part2.pkl', 'rb') as f:
    similarity_part2 = pickle.load(f)

# Merge the two parts vertically
similarity = np.vstack((similarity_part1, similarity_part2))


st.title('Movie Recommendation')


selected_movie_name = st.selectbox(
    'Leveraged machine learning to create a personalized movie recommendation system. Utilized a dataset of 5000 movies from TMDB, employing techniques like data preprocessing, feature engineering, and cosine similarity to identify and give out 5 similar movies.', 
    movies['title'].values) 

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])