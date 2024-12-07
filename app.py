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
        movieTitle = data.get('movieTitle')

        # Validate the movie title
        if not movieTitle or not isinstance(movieTitle, str):
            return jsonify({"error": "Invalid title. Please provide a non-empty string."}), 400

        # Call the function from TestScript.py
        movieDetails = get_metadata_title(movieTitle, df)

        if not movieDetails:
            return jsonify({"error": "Movie not found"}), 404
        

        print("returning movie")

        # Return the movie details as JSON
        return jsonify(movieDetails)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get-related-movies', methods=['POST'])
def get_related_movies():

    try:
        # Extract the query details from the request's JSON payload
        data = request.get_json()
        movieTitle = data.get('movieTitle')
        searchType = data.get('searchType')

        # Validate the movie title
        if not movieTitle or not isinstance(movieTitle, str):
            return jsonify({"error": "Invalid title. Please provide a non-empty string."}), 400

        match searchType:
            case "plotSummary":
                movieDetails = find_similar_movies_by_summary(movieTitle, df)
            case "genre":
                movieDetails = find_similar_movies_by_genre(movieTitle, df)
            case "keywords":
                movieDetails = find_similar_movies_by_keywords(movieTitle, df)
            case _:
                movieDetails = None

        print("Made it here!!!")
        print(movieDetails)

        if movieDetails is None:
            return jsonify({"error": "Movie not found"}), 404
        
        movieDetails = movieDetails.to_dict(orient="records")
        # Return the movie details as JSON
        return jsonify({"status": "success", "data": movieDetails})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True, host='0.0.0.0')

