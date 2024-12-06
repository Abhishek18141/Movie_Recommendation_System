🎬 Movie Recommender System
This project is a simple Movie Recommender System built with Streamlit, which allows users to select a movie and receive recommendations for similar movies. The system uses precomputed similarity data and movie metadata stored in pickle files.

🛠️ Features
Interactive and user-friendly interface built using Streamlit.
Dropdown for selecting a movie to get recommendations.
Display of top 5 recommended movies based on similarity.
Clear selection functionality to reset recommendations.
Sidebar with an optional movie poster for better visual appeal.
🚀 How to Run the Project
Prerequisites
Python 3.8 or higher installed on your machine.
Required Python libraries (listed in requirements.txt).
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/Movie_Recommend_System.git
cd Movie_Recommend_System
Install Dependencies
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate    # For Linux/MacOS
venv\Scripts\activate       # For Windows
Install required Python packages:

bash
Copy code
pip install -r requirements.txt
Add Necessary Files
Ensure the following files are present in the project directory:

movie_list.pkl: Contains movie titles and metadata.
similarity.pkl: Contains precomputed similarity scores.
If these files are missing, refer to the Dataset and Model section below to regenerate them.

Run the Application
bash
Copy code
streamlit run app.py
📂 Project Structure
bash
Copy code
Movie_Recommend_System/
├── app.py               # Main Streamlit application
├── movie_list.pkl       # Pickle file containing movie metadata
├── similarity.pkl       # Pickle file containing similarity scores
├── image-asset.jpeg     # Sidebar movie poster (optional)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

📜 Dataset and Model
Dataset: The system uses a dataset of movie titles and metadata.
Replace movie_list.pkl with your dataset or regenerate it using pandas.
Similarity Computation: Precomputed similarity scores (e.g., cosine similarity) are saved in similarity.pkl.
Ensure these files are properly created and saved before running the app.
Example to regenerate the pickle files:

python
Copy code
import pandas as pd
import pickle

# Example movie data
data = {'title': ['Movie1', 'Movie2', 'Movie3']}
movies = pd.DataFrame(data)

# Save movies to pickle
with open('movie_list.pkl', 'wb') as f:
    pickle.dump(movies, f)

# Example similarity matrix
similarity = [[1.0, 0.8, 0.6], [0.8, 1.0, 0.5], [0.6, 0.5, 1.0]]

# Save similarity to pickle
with open('similarity.pkl', 'wb') as f:
    pickle.dump(similarity, f)

🖼️ Example Screenshots
Main Interface:
![Screenshot (22)](https://github.com/user-attachments/assets/f7fcdf11-e3b6-47ea-b85a-cbd3289f30ee)

🛠️ Technologies Used
Streamlit: For building the web app interface.
Python: For backend logic and data handling.
Pandas: For data processing.
Pickle: For saving and loading precomputed data.

👩‍💻 Future Enhancements
Add more sophisticated recommendation algorithms (e.g., collaborative filtering).
Integrate real-time data from external APIs (e.g., TMDb or IMDb).
Allow users to provide feedback on recommendations to improve accuracy.

📧 Contact
If you have any questions or feedback, feel free to reach out!

Name: Abhishek Pandey
Email: abhishekpandey88201@gmail.com
GitHub: Abhishek18141
