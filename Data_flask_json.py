from flask import Flask, jsonify
import json

app = Flask(__name__)

# Backend file containing data
DATA_FILE = "data.json"

@app.route("/api", methods=["GET"])
def get_data():
    try:
        # Open and read the JSON file
        with open(DATA_FILE, "r") as f:
            data = json.load(f)   # Convert JSON -> Python list/dict
    except FileNotFoundError:
        # If file not found, return empty list
        data = []
    return jsonify(data)  # Flask will return JSON response

if __name__ == "__main__":
    app.run(debug=True)
