import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev")

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = MongoClient(MONGODB_URI)
db = client["todo_db"]
items = db["items"]

@app.route("/")
def index():
    return redirect(url_for("todo"))

@app.route("/todo", methods=["GET"])
def todo():
    return render_template("todo.html")

@app.route("/submittodoitem", methods=["POST"])
def submittodoitem():
    # Accept from form or JSON
    item_name = request.form.get("itemName") or (request.json and request.json.get("itemName"))
    item_desc = request.form.get("itemDescription") or (request.json and request.json.get("itemDescription"))

    if not item_name:
        return jsonify({"error": "itemName is required"}), 400

    doc = {"itemName": item_name, "itemDescription": item_desc or ""}

    items.insert_one(doc)

    # If called via JSON, return JSON; otherwise redirect back to the form
    if request.is_json:
        return jsonify({"status": "ok", "saved": doc}), 201

    flash("To-Do item saved!")
    return redirect(url_for("todo"))

@app.route("/api", methods=["GET"])
def api_list():
    # convenience: list items as JSON
    docs = list(items.find({}, {"_id": 0}))
    return jsonify(docs)

if __name__ == "__main__":
    app.run(debug=True)
