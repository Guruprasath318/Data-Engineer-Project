import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 YouTube Trending Data Dashboard")

# ✅ Load Data (use raw string)
df = pd.read_csv(r"D:\Data Engineer Project\final_yt_data.csv")

# Top 10 videos
st.subheader("Top 10 Trending Videos")
top10 = df.nlargest(10, 'view_count')[['title', 'channel_title', 'view_count']]
st.dataframe(top10)

# Chart 1: Most Viewed Videos
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(y='title', x='view_count', data=top10, ax=ax, palette='viridis')
ax.set_title("Top 10 Most Viewed Videos")
st.pyplot(fig)

# Chart 2: Category Engagement
st.subheader("Average Engagement by Category")
cat_engage = df.groupby('category_name')['engagement_ratio'].mean().reset_index()
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x='category_name', y='engagement_ratio', data=cat_engage, palette='magma', ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# Chart 3: Views vs Likes Scatter
st.subheader("Views vs Likes Correlation")
fig3, ax3 = plt.subplots()
sns.scatterplot(x='view_count', y='like_count', data=df, alpha=0.6, ax=ax3)
ax3.set_title("Views vs Likes Relationship")
st.pyplot(fig3)
