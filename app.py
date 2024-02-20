import difflib
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
movies = pd.read_csv("movies.csv")
selected_features = ['genres', 'director', 'cast', 'keywords', 'tagline', 'original_title', 'original_language']
for feature in selected_features:
    movies[feature] = movies[feature].fillna('')

required_features = movies['genres'] + ' ' + movies['director'] + ' ' + movies['cast'] + ' ' + movies['keywords'] + ' ' + movies['tagline'] + ' ' + movies['original_title']
vectorizer = TfidfVectorizer()
vector_features = vectorizer.fit_transform(required_features)
similarity = cosine_similarity(vector_features)

@app.route('/')
def home():
    return render_template("interface.html")

@app.route('/mov_rec',methods = ['POST'])
def mov_rec():
    user_title = request.form.get('INPUT')
    print(user_title)
    if user_title is None or user_title.strip() == '':
        return render_template("interface.html", output="No input provided")

    close_match = difflib.get_close_matches(user_title, movies['title'].tolist())

    if not close_match:
        return render_template("interface.html", output="No matching movie found")

    best_match = close_match[0]
    movie_index = movies[movies['title'] == best_match]['index'].values[0]
    similarity_scores = list(enumerate(similarity[movie_index]))
    sorted_similar_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:10]

    recommended_movies = []
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies.iloc[index]['title']
        recommended_movies.append(title_from_index)

    return render_template("interface.html", output=recommended_movies)

if __name__ == "__main__":
    app.run(debug=True)
