import requests
import pandas as pd

API_KEY = "AIzaSyAvB7Ms8ckImIS57I0uSrUTq83lN8EDM4Y"
REGION_CODE = "IN"

url = "https://www.googleapis.com/youtube/v3/videoCategories"

params = {
    "part": "snippet",
    "regionCode": REGION_CODE,
    "key": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

categories = []
for item in data["items"]:
    categories.append({
        "category_id": item["id"],
        "category_name": item["snippet"]["title"]
    })

df_cat = pd.DataFrame(categories)
df_cat.to_csv("categories.csv", index=False)

print("✅ Categories saved to categories.csv")
