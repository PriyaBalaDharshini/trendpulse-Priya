import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

# Fix date columns (important)
df["publishedAt"] = pd.to_datetime(df["publishedAt"], errors="coerce")
df["date"] = df["publishedAt"].dt.date
df["hour"] = df["publishedAt"].dt.hour


# 1. Top Sources (Bar Chart)

top_sources = df["source_name"].value_counts().head(5)

plt.figure()
top_sources.plot(kind="bar")
plt.title("Top 5 News Sources")
plt.xlabel("Source")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. Articles per Day (Line Chart)

articles_per_day = df["date"].value_counts().sort_index()

plt.figure()
articles_per_day.plot(kind="line", marker="o")
plt.title("Articles Published Per Day")
plt.xlabel("Date")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 3. Articles by Hour (Bar Chart)

articles_by_hour = df["hour"].value_counts().sort_index()

plt.figure()
articles_by_hour.plot(kind="bar")
plt.title("Articles Published by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Articles")
plt.tight_layout()
plt.show()


# 4. Title Length Distribution (Histogram)

df["title_length"] = df["title"].astype(str).apply(len)

plt.figure()
df["title_length"].plot(kind="hist", bins=10)
plt.title("Title Length Distribution")
plt.xlabel("Title Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()