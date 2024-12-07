# app.py
from flask import Flask, request, jsonify, send_from_directory
from query_metadata import get_metadata_title
from searchClusters import find_similar_movies_by_genre, find_similar_movies_by_summary, find_similar_movies_by_keywords
from flask_cors import CORS
import pandas as pd
import warnings

#data frame used for method calls
warnings.filterwarnings("ignore")
df = pd.read_pickle('movie_pickle.pkl')

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory(directory='./static', path='index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(directory='./static', path='favicon.ico')

@app.route('/search_results.html')
def search_results():
    return send_from_directory(directory='./static', path='search_results.html')

@app.route('/get-movie-details', methods=['POST'])
def get_movie_details():
    print("this ran")
    try:
        # Extract the index from the request's JSON payload
        data = request.get_json()
        movie_title = data.get('movieTitle')

        # Validate the movie title
        if not movie_title or not isinstance(movie_title, str):
            return jsonify({"error": "Invalid title. Please provide a non-empty string."}), 400

        # Call the function from TestScript.py
        movie_details = get_metadata_title(movie_title, df)

        if not movie_details:
            return jsonify({"error": "Movie not found"}), 404
        

        print("returning movie")

        # Return the movie details as JSON
        return jsonify(movie_details)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get-related-movies', methods=['POST'])
def get_related_movies():

    try:
        # Extract the query details from the request's JSON payload
        data = request.get_json()
        movie_title = data.get('movieTitle')
        search_type = data.get('searchType')

        # Validate the movie title
        if not movie_title or not isinstance(movie_title, str):
            return jsonify({"error": "Invalid title. Please provide a non-empty string."}), 400

        match search_type:
            case "plotSummary":
                movie_details = find_similar_movies_by_summary(movie_title, df)
            case "genre":
                movie_details = find_similar_movies_by_genre(movie_title, df)
            case "keywords":
                movie_details = find_similar_movies_by_keywords(movie_title, df)
            case _:
                movie_details = None

        print("Made it here!!!")
        print(movie_details)

        if movie_details is None:
            return jsonify({"error": "Movie not found"}), 404
        
        movie_details = movie_details.to_dict(orient="records")
        # Return the movie details as JSON
        return jsonify({"status": "success", "data": movie_details})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True, host='0.0.0.0')

