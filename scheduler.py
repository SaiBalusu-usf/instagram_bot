import schedule
import time
from client import InstagramBot

class BotScheduler:
    def __init__(self, bot: InstagramBot):
        self.bot = bot

    def job_upload_photo(self, photo_path, caption):
        print(f"Executing scheduled upload: {photo_path}")
        self.bot.upload_photo(photo_path, caption)

    def job_upload_reel(self, video_path, caption):
        print(f"Executing scheduled reel: {video_path}")
        self.bot.upload_reel(video_path, caption)

    def job_like_hashtags(self, hashtag, amount):
        print(f"Executing scheduled like: #{hashtag}")
        self.bot.like_hashtag_posts(hashtag, amount)

    def schedule_daily_upload(self, time_str, photo_path, caption, is_reel=False):
        if is_reel:
            schedule.every().day.at(time_str).do(self.job_upload_reel, photo_path, caption)
            print(f"Scheduled daily Reel upload at {time_str}")
        else:
            schedule.every().day.at(time_str).do(self.job_upload_photo, photo_path, caption)
            print(f"Scheduled daily Photo upload at {time_str}")

    def schedule_golden_hour_post(self, photo_path, caption):
        # Golden hour approximation (e.g., 5 PM or 6 PM)
        # Ideally this would calculate based on sunset, but fixed for MVP
        golden_time = "17:30"
        schedule.every().day.at(golden_time).do(self.job_upload_photo, photo_path, caption)
        print(f"Scheduled Golden Hour post at {golden_time}")

    def schedule_engagement(self, time_str, hashtag, amount):
        schedule.every().day.at(time_str).do(self.job_like_hashtags, hashtag, amount)
        print(f"Scheduled engagement at {time_str}")

    def run_pending(self):
        schedule.run_pending()
