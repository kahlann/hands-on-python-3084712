# csv library for reading and manipulating csv data
import csv
# Fancy print module - nicer formatting
from pprint import pprint

# Set a basic csv variable
# Want to read this into a dictionary/JSON (more useful) like format
EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

# Dictionary - more similar to JSON format (JavaScript)
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

# Looks at each line in the file, closes the file when finished
# Read-only, open the laureates.csv file as a variable named f
with open("laureates.csv", "r") as f:
    # set reader object to be a csv.DictReader instantaited with the laureates file, f
    reader = csv.DictReader(f)
    # The list of laureates is the DictReader object turned into a list
    laureates = list(reader)

# For each laureate in the list
for laureate in laureates:
    # If we hit Einstein entry
    if laureate["surname"] == "Einstein":
        # Print the information about that laureate
        pprint(laureate)
        break
