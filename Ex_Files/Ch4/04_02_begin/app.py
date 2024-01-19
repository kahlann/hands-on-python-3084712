import csv
# Import Flask - quick way to get an application working on the web
# render_templates allows rendering of html file
# jsonify takes data structures and returns them as JSON
try:
    from flask import Flask, render_template, jsonify
except:
    import os
    os.system("pip install flask")
    from flask import Flask, render_template, jsonify

# Instantiate a Flask object
app = Flask(__name__)

# Use csv reader to get laureates data as a list of dictionaries
with open("laureates.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# render using an html file
@app.route("/")
def index():
    return render_template("index.html")

# Get the laureats data as JSON
@app.route("/laureates/")
def laureate():
    return jsonify(laureates)

# Run the app
app.run(debug=True)


