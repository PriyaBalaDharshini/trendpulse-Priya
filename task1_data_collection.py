import requests
import json

API_KEY = "a787e8ed0c5f4d23b98a25d1f09ae9e8"
url = f"https://newsapi.org/v2/everything?q=technology&language=en&sortBy=publishedAt&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()
print("Total Article: ", data["totalResults"])

with open("raw_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Raw response saved")
