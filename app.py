mport streamlit as st
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

# Set up the sidebar with movie selection
st.sidebar.header('Choose a movie to get recommendations')
movie_list = movies['title'].values

# Generate a unique key for the selectbox
selectbox_key = 'movie_selectbox'

selected_movie = st.sidebar.selectbox("Kindly type or select a movie from the dropdown", movie_list, key=selectbox_key)

# Add an image to the sidebar for a better visual appeal
try:
    image = Image.open('image-asset.jpeg')
except FileNotFoundError:
    url = "https://via.placeholder.com/300x400.png?text=Movie+Recommender"
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

st.sidebar.image(image, use_column_width=True)

# Show recommendations on button click
if st.sidebar.button('Show Recommendation'):
    st.markdown("### Recommended Movies")
    recommended_movie_names = recommend(selected_movie)
    for i in recommended_movie_names:
        st.write(f"🎥 {i}")

# Add a button to clear the selection (recreate the selectbox with a unique key)
if st.sidebar.button('Clear Selection'):
    st.experimental_rerun()

# Footer
st.markdown("""
---
**Movie Recommender System** - Built with Streamlit
""")
