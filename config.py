import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
PROXY_URL = os.getenv("INSTAGRAM_PROXY")

# Safety limits to avoid bans
MAX_LIKES_PER_DAY = 30
MAX_COMMENTS_PER_DAY = 10
MAX_FOLLOWS_PER_DAY = 10
MAX_UNFOLLOWS_PER_DAY = 10

# Time delays (in seconds)
MIN_DELAY = 30
MAX_DELAY = 60
