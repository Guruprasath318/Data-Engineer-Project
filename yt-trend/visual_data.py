import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Connect to MySQL and load data into DataFrame
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="yt_project"
)

query = "SELECT * FROM trend_videos"
df = pd.read_sql(query, connection)
connection.close()

print("✅ Data loaded successfully!")
print(df.head())

# Step 2: Visualization

# Top 10 most viewed videos
top10 = df.nlargest(10, 'view_count')

plt.figure(figsize=(10,6))
sns.barplot(y='title', x='view_count', data=top10, palette='viridis')
plt.title('Top 10 Most Viewed Videos')
plt.xlabel('Views')
plt.ylabel('Video Title')
plt.tight_layout()
plt.show()

# Category-wise average engagement ratio
category_engagement = df.groupby('category_name')['engagement_ratio'].mean().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(x='category_name', y='engagement_ratio', data=category_engagement, palette='magma')
plt.title('Average Engagement Ratio by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
