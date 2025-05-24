import streamlit as st
import pickle
from PIL import Image
import requests
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .movie-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .movie-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .selected-movie {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
        color: #333;
        font-weight: bold;
    }
    
    .sidebar .stSelectbox > div > div {
        background-color: #f0f2f6;
        border-radius: 5px;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #ff6b6b, #4ecdc4);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        border-radius: 10px;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        for i in distances[1:6]:
            recommended_movie_names.append(movies.iloc[i[0]].title)
        return recommended_movie_names
    except Exception as e:
        st.error(f"Error generating recommendations: {str(e)}")
        return []

# Load the data with error handling
try:
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Required files not found: {str(e)}")
    st.stop()

# Main header
st.markdown('<h1 class="main-header">🎬 Movie Recommender System</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover your next favorite movie with AI-powered recommendations!</p>', unsafe_allow_html=True)

# Create columns for better layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("### 🎯 Select a Movie")
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Choose a movie you enjoyed:",
        movie_list,
        key='movie_selectbox',
        help="Start typing to search for your favorite movie"
    )
    
    # Display selected movie in a nice card
    if selected_movie:
        st.markdown(f'''
        <div class="selected-movie">
            🎬 Selected Movie: {selected_movie}
        </div>
        ''', unsafe_allow_html=True)

# Sidebar styling
st.sidebar.markdown("### 🎭 Movie Explorer")
st.sidebar.markdown("---")

# Load and display image in sidebar
try:
    image = Image.open('image-asset.jpeg')
except FileNotFoundError:
    try:
        url = "https://images.unsplash.com/photo-1489599808821-8a31479fbe48?w=400&h=600&fit=crop"
        response = requests.get(url, timeout=10)
        image = Image.open(BytesIO(response.content))
    except:
        # Fallback to a placeholder
        url = "https://via.placeholder.com/300x400/667eea/white?text=🎬+Movie+Recommender"
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))

st.sidebar.image(image, use_container_width=True, caption="Discover Amazing Movies!")

# Add some movie stats in sidebar
st.sidebar.markdown("### 📊 Movie Database Stats")
st.sidebar.info(f"🎬 Total Movies: {len(movies)}")
st.sidebar.success("✨ AI-Powered Recommendations")

    # Center the recommendation button
    col_left, col_center, col_right = st.columns([1, 1, 1])
    with col_center:
        get_recommendations = st.button('🔍 Get Recommendations', help="Click to get personalized movie recommendations")

# Recommendation results
if get_recommendations:
    with st.spinner('🎬 Finding perfect movies for you...'):
        recommended_movie_names = recommend(selected_movie)
        
        if recommended_movie_names:
            st.markdown("## 🌟 Recommended Movies for You")
            st.markdown(f"**Based on your interest in:** *{selected_movie}*")
            
            # Display recommendations in a nice grid
            cols = st.columns(2)
            for idx, movie in enumerate(recommended_movie_names):
                with cols[idx % 2]:
                    st.markdown(f'''
                    <div class="movie-card">
                        <h4>🎥 {movie}</h4>
                        <p>Recommended for you!</p>
                    </div>
                    ''', unsafe_allow_html=True)
            
            # Add some additional info
            st.markdown("---")
            st.markdown("### 💡 Pro Tip")
            st.info("Try selecting different movies to discover new genres and hidden gems!")
        else:
            st.error("Sorry, couldn't generate recommendations. Please try another movie.")

# Add some space
st.markdown("<br>", unsafe_allow_html=True)

# Enhanced footer
st.markdown('''
<div class="footer">
    <h3>🎬 Movie Recommender System</h3>
    <p>Powered by Machine Learning & Built with ❤️ using Streamlit</p>
    <p>🌟 Discover • Explore • Enjoy 🌟</p>
</div>
''', unsafe_allow_html=True)

# Add some fun facts or tips
with st.expander("🎭 About This Recommender"):
    st.markdown("""
    **How it works:**
    - 🤖 Uses advanced machine learning algorithms
    - 📊 Analyzes movie features and similarities
    - 🎯 Provides personalized recommendations
    - ⚡ Instant results with high accuracy
    
    **Tips for better recommendations:**
    - Try movies from different genres
    - Select movies you genuinely enjoyed
    - Explore recommendations from various time periods
    """)

# Optional: Add a feedback section
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("### 💬 Quick Feedback")
    feedback = st.radio(
        "How satisfied are you with the recommendations?",
        ["😍 Amazing!", "👍 Good", "👌 Okay", "👎 Could be better"],
        horizontal=True
    )
    if feedback:
        st.success(f"Thank you for your feedback: {feedback}")
