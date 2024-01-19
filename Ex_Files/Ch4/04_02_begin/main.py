import csv
# Import Flask - quick way to get an application working on the web
try:
    from flask import Flask, render_template, jsonify
except:
    import os
    os.system("pip install flask")
    from flask import Flask, render_template, jsonify

# Instantiate a Flask object
app = Flask(__name__)

# Define a route using decorator - function
@app.route("/")
def hello():
    return "Hello, World!"

# Run
app.run(debug=True)