import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="yt_project"
)

df = pd.read_sql("select * from trend_videos",conn)
conn.close()

df.to_csv("final_yt_data.csv",index=False)
print("final dataset exported to csv")
