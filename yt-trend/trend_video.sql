CREATE TABLE trend_videos(
    void_id VARCHAR(50),
    title TEXT,
    channel_title VARCHAR(300),
    category_name VARCHAR(100),
    published_at DATETIME,
    view_count BIGINT,
    like_count BIGINT,
    comment_count BIGINT,
    engagement_ratio FLOAT
);

SELECT COUNT(*) FROM trend_videos;
SELECT * FROM trend_videos LIMIT 5;


