import pandas as pd
import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="yt_project"
)

query = "SELECT * FROM trend_videos"
df = pd.read_sql(query, connection)

connection.close()

print(df.head())
