from instagrapi import Client

from instagrapi.exceptions import LoginRequired, TwoFactorRequired
import os
import time
import random
from config import PROXY_URL, MIN_DELAY, MAX_DELAY

class InstagramBot:
    def __init__(self, username, password):
        self.client = Client()
        if PROXY_URL:
            print(f"Setting proxy: {PROXY_URL}")
            self.client.set_proxy(PROXY_URL)
        
        self.username = username
        self.password = password
        self.session_file = f"{username}_session.json"

    def random_sleep(self):
        """
        Sleeps for a random duration between MIN_DELAY and MAX_DELAY.
        Adds a small Gaussian variation for more human-like behavior.
        """
        delay = random.uniform(MIN_DELAY, MAX_DELAY)
        print(f"Sleeping for {delay:.2f} seconds...")
        time.sleep(delay)

    def login(self):
        """
         precise login flow to avoid re-login if session is valid.
        """
        if os.path.exists(self.session_file):
            print(f"Loading session from {self.session_file}")
            self.client.load_settings(self.session_file)
        
        try:
            self.client.login(self.username, self.password)
            print("Logged in successfully.")
            self.client.dump_settings(self.session_file)
        except TwoFactorRequired:
            code = input("2FA Code required: ")
            self.client.two_factor_login(code)
            print("Logged in successfully (2FA).")
            self.client.dump_settings(self.session_file)
        except Exception as e:
            print(f"Login failed: {e}")
            if os.path.exists(self.session_file):
                print("Session file might be corrupted. Deleting and retrying...")
                os.remove(self.session_file)
                self.login() # Retry once

    def upload_photo(self, photo_path, caption):
        """
        Uploads a photo to the feed.
        """
        if not os.path.exists(photo_path):
            print(f"Error: File not found {photo_path}")
            return

        print(f"Uploading {photo_path}...")
        try:
            media = self.client.photo_upload(photo_path, caption)
            print(f"Photo uploaded successfully. Media ID: {media.pk}")
            return media
        except Exception as e:
            print(f"Failed to upload photo: {e}")

    def upload_reel(self, video_path, caption):
        """
        Uploads a video as a Reel.
        """
        if not os.path.exists(video_path):
            print(f"Error: File not found {video_path}")
            return

        print(f"Uploading Reel {video_path}...")
        try:
            media = self.client.clip_upload(video_path, caption)
            print(f"Reel uploaded successfully. Media ID: {media.pk}")
            return media
        except Exception as e:
            print(f"Failed to upload reel: {e}")

    def upload_story(self, media_path, is_video=False):
        """
        Uploads a photo or video to Stories.
        """
        if not os.path.exists(media_path):
            print(f"Error: File not found {media_path}")
            return

        print(f"Uploading Story {media_path}...")
        try:
            if is_video:
                media = self.client.video_upload_to_story(media_path)
            else:
                media = self.client.photo_upload_to_story(media_path)
            
            print(f"Story uploaded successfully. Media ID: {media.pk}")
            return media
        except Exception as e:
            print(f"Failed to upload story: {e}")

    def like_hashtag_posts(self, hashtag, amount=5):
        """
        Likes top/recent posts from a hashtag.
        """
        print(f"Liking {amount} posts for #{hashtag}...")
        try:
            medias = self.client.hashtag_medias_top(hashtag, amount=amount)
            # You can also use hashtag_medias_recent, but top is safer for bots usually
            
            for media in medias:
                try:
                    self.client.media_like(media.id)
                    print(f"Liked post {media.id} by {media.user.username}")
                    self.random_sleep()
                except Exception as e:
                    print(f"Failed to like post {media.id}: {e}")
        except Exception as e:
            print(f"Error fetching hashtag medias: {e}")

    def comment_on_post(self, media_id, comment_text):
        """
        Comments on a specific post.
        """
        print(f"Commenting on {media_id}...")
        try:
            comment = self.client.media_comment(media_id, comment_text)
            print(f"Commented: {comment.text}")
            return comment
        except Exception as e:
            print(f"Failed to comment: {e}")
