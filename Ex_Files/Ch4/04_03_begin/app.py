import csv
try:
    from flask import Flask, render_template, request, jsonify
except:
    import os
    os.system("pip install flask")
    from flask import Flask, render_template, request, jsonify

# Instantiate an app
app = Flask(__name__)

# Get the laureates data as a list of dictionaries
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# Set the html template (make it pretty)
@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")

# Se
@app.route("/laureates/")
def laureate_list():
    # empty list to hold serach results
    results = []
    # If there is no parameter for surname in the URL, return empty list
    if not request.args.get("surname"):
        return jsonify(results)

    # If there is a surname parameter
    search_string = request.args.get("surname").lower().strip()
    # iterate over the laureates
    for laureate in laureates:
        # If there is a match, append result to the list
        if search_string in laureate["surname"].lower():
            results.append(laureate)

    # Return the jsonified results from the search
    return jsonify(results)


app.run(debug=True)
