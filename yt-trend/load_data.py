import pandas as pd
import mysql.connector

# Step 1: Read cleaned CSV
df = pd.read_csv("cleaned_data.csv")

# Step 2: Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",        # change if your username is different
    password="root",
    database="yt_project"
)

cursor = connection.cursor()

# Step 3: Insert data row by row
for _, row in df.iterrows():
    sql = """
    INSERT INTO trend_videos
    (void_id, title, channel_title, category_name, published_at, view_count, like_count, comment_count, engagement_ratio)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        row['void_id'], row['title'], row['channel_title'], row['category_name'],
        row['published_at'], row['view_count'], row['like_count'],
        row['comment_count'], row['engagement_ratio']
    )

    # ✅ Move execute() inside the loop
    cursor.execute(sql, values)

# ✅ Commit once after all rows are inserted
connection.commit()

cursor.close()
connection.close()

print("✅ All rows from cleaned_data.csv have been loaded into MySQL successfully!")
