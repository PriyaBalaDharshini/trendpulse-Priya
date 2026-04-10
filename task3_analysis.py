import pandas as pd
from collections import Counter

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

print("===== DATA ANALYSIS =====")

# 1. Basic info
print("\nTotal Articles:", len(df))
print("\nColumns:\n", df.columns)

# 2. Top sources
top_sources = df["source_name"].value_counts().head(5)
print("\nTop 5 Sources:\n", top_sources)

# 3. Articles per day
articles_per_day = df["date"].value_counts().sort_index()
print("\nArticles per Day:\n", articles_per_day)

# 4. Articles by hour
articles_by_hour = df["hour"].value_counts().sort_index()
print("\nArticles by Hour:\n", articles_by_hour)

# 5. Title length
df["title_length"] = df["title"].astype(str).apply(len)
print("\nAverage Title Length:", df["title_length"].mean())

# 6. Keyword analysis
ai_count = df["title"].str.contains("AI", case=False).sum()
print("\nArticles mentioning 'AI':", ai_count)

# 7. Common words
all_titles = " ".join(df["title"])
words = all_titles.split()

common_words = Counter(words).most_common(10)
print("\nMost Common Words:\n", common_words)