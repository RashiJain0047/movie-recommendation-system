import streamlit as st
import pickle
import pandas as pd

# 1. Load the data models exported from your notebook
# Note: Using 'movie_list.pkl' to match your actual file!
movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# 2. Define the recommendation function logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    # Fetch top 5 similar movies
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# 3. Build the Streamlit Web UI Layout
st.title('Movie Recommender System')

# Dropdown menu containing all movie titles
selected_movie_name = st.selectbox(
    'Type or select a movie to get recommendations:',
    movies['title'].values
)

# Recommend Button Action
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    
    # Display recommendations cleanly using 5 columns
    cols = st.columns(5)
    for index, col in enumerate(cols):
        with col:
            st.text(recommendations[index])