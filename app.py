import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image

# CSS for 3D-like background and app styling
page_bg_style = '''
<style>
body {
    background: linear-gradient(135deg, #89f7fe, #66a6ff); /* Gradient background */
    background-attachment: fixed; /* Keeps background fixed on scroll */
    font-family: 'Arial', sans-serif;
}

div[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle, #89f7fe, #66a6ff);
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); /* Adds a subtle 3D shadow */
    border-radius: 12px; /* Optional: Rounds the app edges for a modern look */
    padding: 20px; /* Adds padding to the app */
}

div[data-testid="stHeader"] {
    background: transparent;
}

footer {visibility: hidden;}
</style>
'''
st.markdown(page_bg_style, unsafe_allow_html=True)

# App Title and Description
st.markdown(
    "<h1 style='text-align: center; color: #FF4B4B;'>🎬 Welcome to Movie Recommendation System 🎬</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; font-size: 18px; color: #6C757D;'>Discover your next favorite movie with just a click!</p>",
    unsafe_allow_html=True,

)

# Add a visually appealing header
st.markdown(
    """
    <style>
        .stMarkdown {
            background-color: #F7F9FC;
            border: 1px solid #DDE6ED;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='stMarkdown'>✨ This app recommends movies based on your choice! ✨</div>",
    unsafe_allow_html=True,
)

# Introduction Section
st.markdown("*Welcome to Movie* Recommendation System **Your** ***Movies***.")
st.markdown(
    ''':red[Movie Recommendation] :orange[Can] :green[Suggest] :blue[You] :violet[The Best Movie] :gray[Ever] :rainbow[You Imagine].'''
)
st.markdown(
    "We can design this kind of recommendation system for your company: :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:"
)
st.markdown("**Company Partner: Shivam Kumar and Prateek Kumar**")

# Display a central image
st.image(
    "Image.jpg",  # Replace with your actual image path
    caption="Find Your Next Favorite Movie!",
    use_container_width=True
)

#2nd Poster

st.image(
    "image2.jpg",  # Replace with your actual image path
    caption="Find Your Next Favorite Movie!",
    use_container_width=True
)

# Load Movie Data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation Function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)  # Access index using i[0]
    return recommended_movies



#Testing


#Resting end


# Sidebar Layout
st.sidebar.title("🎥 Movie Recommendation")
st.sidebar.markdown("### Select Your Favorite Movie Below!")

# Sidebar Image
st.sidebar.image(
    "image2.jpg",  # Replace with your actual image path
    caption="Find Your Next Favorite Movie!",
    use_container_width=True
)

# Selectbox for Movie Selection
selected_movie_name = st.sidebar.selectbox(
    "Choose a movie you like:",
    movies['title'].values,
    help="Pick a movie, and we'll recommend others you might enjoy!"
)

# Recommendation Button and Display
if st.sidebar.button("🔍 Get Recommendations"):
    st.sidebar.markdown("### 🎉 Recommendations are Ready Below!")
    recommendations = recommend(selected_movie_name)
    for i, movie in enumerate(recommendations):
        st.markdown(f"**{i + 1}. {movie}** 🎥")
