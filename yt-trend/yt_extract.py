import requests
import pandas as pd

# --- Replace with your API key ---
API_KEY = "AIzaSyAvB7Ms8ckImIS57I0uSrUTq83lN8EDM4Y"
REGION_CODE = "IN"  # You can change to "US", "UK", etc.

# YouTube API endpoint for trending videos
url = "https://www.googleapis.com/youtube/v3/videos"

# API parameters
params = {
    "part": "snippet,statistics",
    "chart": "mostPopular",
    "maxResults": 50,        # You can increase up to 50
    "regionCode": REGION_CODE,
    "key": API_KEY
}

# Request data
response = requests.get(url, params=params)
data = response.json()

# Extract important fields
videos = []
for item in data["items"]:
    videos.append({
        "video_id": item["id"],
        "title": item["snippet"]["title"],
        "channel_title": item["snippet"]["channelTitle"],
        "category_id": item["snippet"]["categoryId"],
        "published_at": item["snippet"]["publishedAt"],
        "view_count": item["statistics"].get("viewCount", 0),
        "like_count": item["statistics"].get("likeCount", 0),
        "comment_count": item["statistics"].get("commentCount", 0)
    })

# Convert to DataFrame
df = pd.DataFrame(videos)

# Save as CSV
df.to_csv("raw_data.csv", index=False)

print("✅ Data saved to raw_data.csv successfully!")
