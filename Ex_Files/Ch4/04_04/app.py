import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("flName"):
        return jsonify(results)

    search_string = request.args.get("flName").lower().strip()

    # Enhance search functionality to be able to search by first or last name 
    for laureate in laureates:
        surname = laureate["surname"].lower().strip()
        fname = laureate["name"].lower().strip()
        
        if (search_string in surname) or(search_string in fname):
            results.append(laureate)

    return jsonify(results)


app.run(debug=True)
