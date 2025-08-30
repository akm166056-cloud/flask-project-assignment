import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev")

# Get MongoDB Atlas URI from .env (use the proper var name)
MONGODB_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGODB_URI)

# Database & collection
db = client["todo_db"]
items = db["items"]

@app.route("/")
def index():
    return redirect(url_for("todo"))

@app.route("/todo", methods=["GET"])
def todo():
    # Renders frontend To-Do form (todo.html must exist in templates/)
    return render_template("todo.html")

@app.route("/submittodoitem", methods=["POST"])
def submittodoitem():
    # Accept from form (HTML) or JSON (API POST)
    item_name = request.form.get("itemName") or (request.json and request.json.get("itemName"))
    item_desc = request.form.get("itemDescription") or (request.json and request.json.get("itemDescription"))

    if not item_name:
        return jsonify({"error": "itemName is required"}), 400

    doc = {"itemName": item_name, "itemDescription": item_desc or ""}
    items.insert_one(doc)

    # Return JSON if API call, else redirect to frontend
    if request.is_json:
        return jsonify({"status": "ok", "saved": doc}), 201

    flash("To-Do item saved!")
    return redirect(url_for("todo"))

@app.route("/api", methods=["GET"])
def api_list():
    # List all items in JSON (exclude _id)
    docs = list(items.find({}, {"_id": 0}))
    return jsonify(docs)

if __name__ == "__main__":
    app.run(debug=True)
