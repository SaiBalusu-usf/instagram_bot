import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# Safety limits to avoid bans
MAX_LIKES_PER_DAY = 50
MAX_COMMENTS_PER_DAY = 20
MAX_FOLLOWS_PER_DAY = 20
MAX_UNFOLLOWS_PER_DAY = 20

# Time delays (in seconds)
MIN_DELAY = 5
MAX_DELAY = 15
