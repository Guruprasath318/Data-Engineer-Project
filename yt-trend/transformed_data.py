import pandas as pd

# Read both CSV files
df_videos = pd.read_csv("raw_data.csv")
df_categories = pd.read_csv("categories.csv")

# Convert category_id to string (to match data type)
df_videos["category_id"] = df_videos["category_id"].astype(str)
df_categories["category_id"] = df_categories["category_id"].astype(str)

# Merge both datasets
df_merged = df_videos.merge(df_categories, on="category_id", how="left")

# Clean up data
df_merged["published_at"] = pd.to_datetime(df_merged["published_at"])
df_merged["view_count"] = pd.to_numeric(df_merged["view_count"], errors="coerce")
df_merged["like_count"] = pd.to_numeric(df_merged["like_count"], errors="coerce")
df_merged["comment_count"] = pd.to_numeric(df_merged["comment_count"], errors="coerce")

# Add a new metric column: engagement ratio
df_merged["engagement_ratio"] = (df_merged["like_count"] + df_merged["comment_count"]) / df_merged["view_count"]

# Save cleaned data
df_merged.to_csv("cleaned_data.csv", index=False)

print("✅ Cleaned data saved to cleaned_data.csv")
