import praw
import os
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv()

# Initialize Reddit instance
def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT")
    )

# Scrape posts and comments of a user
def scrape_user_content(username, limit=100):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    posts = []
    comments = []

    try:
        for submission in user.submissions.new(limit=limit):
            posts.append(f"[POST] {submission.title} - {submission.selftext[:300]}")
    except Exception as e:
        print(f"Error fetching posts: {e}")

    try:
        for comment in user.comments.new(limit=limit):
            comments.append(f"[COMMENT] {comment.body[:300]}")
    except Exception as e:
        print(f"Error fetching comments: {e}")

    return posts + comments
