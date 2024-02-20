# Movie Recommendation System

This project aims to develop a content-based movie recommendation system utilizing collaborative filtering techniques. The system suggests movies to users based on their viewing history or preferences. It combines the concepts of collaborative filtering and content-based recommendation to offer personalized suggestions to users.
## Dataset
The dataset used for this project is sourced from Google and is contained in the movie.csv file. It comprises various features such as "budget", "genres", "keywords", "original_title", "overview", "popularity", and more. The dataset consists of 4809 entries with 24 features.

## Data Preprocessing
Due to the large number of features in the dataset, only relevant features are selected for further analysis. These features include genres, director, cast, keywords, tagline, original title, and original language. Missing values in these selected features are handled using the fillna() method. Subsequently, these features and their values are combined into a single string to create a pool of feature attributes.
## Exploratory Data Analysis (EDA)
EDA involves analyzing the selected features to gain insights and ensure data integrity. The selected features are examined for any missing values and cleaned accordingly. Further analysis may involve visualizations to understand the distribution of data and relationships between features.
## Collaborative Filtering
TF-IDF vectorization is employed to represent the corpus numerically. This process converts textual data into numerical values, creating a matrix where each row represents a document and each column represents a unique term in the entire corpus. Cosine similarity is then calculated between each feature row to determine the similarity between movies. The output matrix is symmetric, with diagonal elements representing self-similarity.
## Content-based Filtering and Recommendation
To recommend movies to users, the system takes input in the form of a movie title that the user likes. It then finds similar movies based on this input. This process involves utilizing the difflib library, which provides tools for computing string similarities. The get_close_matches() function is utilized to find close matches of a user-provided movie title within a list of all movie titles, returning a list of close matches. Similarity scores are calculated for each movie, and the list of similar movies is sorted based on their similarity scores in descending order.
## User Interface
The recommendation system is integrated into a Flask-based website, along with HTML and CSS for the frontend. The website is designed to be user-friendly, allowing users to input their preferences and receive movie recommendations seamlessly.


## Dependencies

•	Python 3.x
•	Flask
•	pandas
•	numpy
•	scikit-learn
•	difflib

