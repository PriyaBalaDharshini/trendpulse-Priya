import pandas as pd
import json
import random

# load data
with open("raw_data.json", "r") as file:
    data = json.load(file)

articles = data["articles"]
print(articles)

cleaned_data = []

for article in articles:
    cleaned_data.append(
        {
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "urlToImage": article.get("urlToImage"),
            "publishedAt": article.get("publishedAt"),
            "content": article.get("content"),
            "source_id": article.get("source", {}).get("id"),
            "source_name": article.get("source", {}).get("name"),
        }
    )

df = pd.DataFrame(cleaned_data)

print(df.isna().sum())

df_copy = df.copy()

df_copy = df_copy.fillna({
    "urlToImage": "Not Available"
})

# Fill source_id with random IDs
df_copy["source_id"] = df_copy["source_id"].apply(
    lambda x: f"id_{random.randint(1000, 9999)}" if pd.isna(x) else x
)

df_copy["publishedAt"] = pd.to_datetime(df_copy["publishedAt"], errors="coerce")
df_copy["date"] = df_copy["publishedAt"].dt.date
df_copy["hour"] = df_copy["publishedAt"].dt.hour

df_copy.to_csv("cleaned_data.csv", index=False)

print("Data cleaned and saved as cleaned_data.csv")
print("Total records:", len(df_copy))
print(df_copy)