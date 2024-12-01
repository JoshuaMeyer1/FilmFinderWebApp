# app.py
from flask import Flask, request, jsonify, send_from_directory
from TestScript import get_row_by_index
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

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

if __name__ == '__main__':
    app.run(debug=True)