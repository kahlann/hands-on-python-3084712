import csv
# JSON utility
import json
from pprint import pprint

# Python dictionary with information about Albert Einstein
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

# Use json.dumps() to convert the dictionary to JSON - note the s on dumps!
einstein_json = json.dumps(EINSTEIN)
# Use json.loads to convert back to the dictionary
back_to_dict = json.loads(einstein_json)
# Print the json object
print(einstein_json)
# print the dictionary
pprint(back_to_dict)

# Convert the csv data to list of dictionaries, each disctionary holding data about a laureate
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# Open a new file with writing permission
with open("laureates.json", "w") as f:
    # json.dump() for files
    # convert the list of dictionaries to a json file
    json.dump(laureates, f, indent=2)
