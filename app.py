import streamlit as st
import pickle
from PIL import Image
import requests
from io import BytesIO

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

# Load the data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set up the app header and layout
st.title('🎬 Movie Recommender System')
st.markdown("## Find your next favorite movie!")

# Initialize session state variables
if "selected_movie" not in st.session_state:
    st.session_state["selected_movie"] = ""
if "recommended_movies" not in st.session_state:
    st.session_state["recommended_movies"] = []

# Sidebar setup
st.sidebar.header('Choose a movie to get recommendations')
movie_list = movies['title'].values

# Clear selection logic
def clear_selection():
    st.session_state["selected_movie"] = ""
    st.session_state["recommended_movies"] = []

# Movie selection dropdown
selected_movie = st.sidebar.selectbox(
    "Kindly type or select a movie from the dropdown",
    [""] + list(movie_list),  # Add an empty option for clearing
    key="selected_movie"
)

# Add an image to the sidebar
try:
    image = Image.open('image-asset.jpeg')
except FileNotFoundError:
    url = "https://via.placeholder.com/300x400.png?text=Movie+Recommender"
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

st.sidebar.image(image, use_column_width=True)

# Show recommendations on button click
if st.sidebar.button("Show Recommendation") and selected_movie:
    st.session_state["recommended_movies"] = recommend(selected_movie)

# Clear output on button click
if st.sidebar.button("Clear Selection"):
    clear_selection()

# Display recommendations if available
if st.session_state["recommended_movies"]:
    st.markdown("### Recommended Movies")
    for movie in st.session_state["recommended_movies"]:
        st.write(f"🎥 {movie}")

# Footer
st.markdown("""
---
**Movie Recommender System** - Built with Streamlit
""")
