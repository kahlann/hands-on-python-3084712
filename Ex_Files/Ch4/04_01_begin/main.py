# Import requests module (install if necessary)
try:
    import requests
except:
    import os
    os.system("pip install requests")
    import requests

# Get data from worldbank API
response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

# Get data from the last 20 years
last_twenty_years = response.json()[1][:20]

# Iterate over the years
for year in last_twenty_years:
    # Set display width (formatting)
    display_width = year["value"] // 10_000_000
    # Print the date, then the above value number of = signs (like a bar chart)
    print(year["date"], "="* display_width)