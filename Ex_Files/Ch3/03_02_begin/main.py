import csv
# datetime module for easy-to-work-with datastructures for dates, times
from datetime import datetime
from pprint import pprint

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        print("============")
        # get the year of award as a datetime object
        year_date = datetime.strptime(laureate["year"], "%Y")
        # get the year, month, day of their birthday as a datetime object
        born_date = datetime.strptime(laureate["born"], "%Y-%m-%d")
        # Caluclate the age at which they were awarded the prize by extracting the year information from the datetime objects
        print("age:", year_date.year - born_date.year)
        break
