from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

app = Flask(__name__)

# Load .env file
load_dotenv()

# Get username and password from env
username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
cluster  = os.getenv("MONGO_CLUSTER")  # e.g., cluster0.i0dfks1.mongodb.net

# Safely encode the password
encoded_password = quote_plus(password)

# Build URI
uri = f"mongodb+srv://{username}:{encoded_password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(uri)
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for("success"))
        except Exception as e:
            error = str(e)
    return render_template("form.html", error=error)

@app.route("/success")
def success():
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)
