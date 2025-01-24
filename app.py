import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Jeffandy's Movie Recommendations")
selectvalue=st.selectbox("Select a movie from the dropdown", movies_list)
# selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=05dbc130fc2a1bd6ea7133ec27b37abb&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data ['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
  index= movies[movies['title']==movie].index[0]
  distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
  recommendation=[]
  recommendation_poster=[]
  for i in distance[1:6]:
    movies_id = movies.iloc[i[0]].id
    recommendation.append(movies.iloc[i[0]].title)
    recommendation_poster.append(fetch_poster(movies_id))
  return recommendation, recommendation_poster


if st.button("Share Recommendations!"):
    movie_names, movie_poster  = recommend(selectvalue)
    col1, col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_names[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_names[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_names[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_names[4])
        st.image(movie_poster[4])