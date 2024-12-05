# app.py
from flask import Flask, request, jsonify, send_from_directory
from TestScript import get_row_by_index
from query_metadata import get_metadata_title
from flask_cors import CORS
import pandas as pd

#data frame used for method calls
df = pd.read_csv('movieData.csv')

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory(directory='./static', path='index.html')

@app.route('/get-row', methods=['POST'])
def get_row():
    try:
        # Extract the index from the request's JSON payload
        data = request.get_json()
        index = data.get('index')

        if index is None or not isinstance(index, int):
            return jsonify({"error": "Invalid index. Please provide an integer."}), 400

        # Call the function from TestScript.py
        row = get_row_by_index(index)

        return jsonify({"row": row})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get-movie-details', methods=['POST'])
def get_movie_details():
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
        
        # Return the movie details as JSON
        return jsonify({
            "plotSummary": movie_details["plotSummary"],
            "keywords": movie_details["keywords"],
            "genre": movie_details["genre"]
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')