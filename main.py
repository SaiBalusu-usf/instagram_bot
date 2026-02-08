import os
import time
from dotenv import load_dotenv
from client import InstagramBot
from scheduler import BotScheduler
from hashtags import SmartHashtags

def main():
    load_dotenv()
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")

    if not username or not password:
        print("Please set INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD in .env file")
        return

    bot = InstagramBot(username, password)
    scheduler = BotScheduler(bot)

    hashtags_gen = SmartHashtags()

    print("--- Instagram Automation Tool v2.0 (Photographer Edition) ---")
    print("1. Login only")
    print("2. Immediate Photo Upload")
    print("3. Immediate Reel Upload")
    print("4. Immediate Story Upload")
    print("5. Generate Smart Hashtags")
    print("6. Start Scheduler (Loop)")
    
    choice = input("Enter choice: ")

    if choice == '1':
        bot.login()
    
    elif choice == '2':
        bot.login()
        path = input("Enter photo path: ")
        base_caption = input("Enter caption: ")
        category = input("Enter category (portrait, landscape, street, bnw, general): ")
        tags = hashtags_gen.get_hashtags(category)
        final_caption = f"{base_caption}\n.\n.\n{tags}"
        print(f"Generated Caption:\n{final_caption}")
        bot.upload_photo(path, final_caption)

    elif choice == '3':
        bot.login()
        path = input("Enter video path: ")
        caption = input("Enter caption: ")
        bot.upload_reel(path, caption)

    elif choice == '4':
        bot.login()
        path = input("Enter media path: ")
        is_video = input("Is this a video? (s/n): ").lower() == 'y'
        bot.upload_story(path, is_video=is_video)

    elif choice == '5':
        print("Categories:", hashtags_gen.list_categories())
        cat = input("Choose category: ")
        print(hashtags_gen.get_hashtags(cat))

    elif choice == '6':
        bot.login()
        print("For demo purposes, we will hardcode a schedule or run immediately.")
        # Example schedule
        # scheduler.schedule_golden_hour_post("C:/path/to/photo.jpg", "Golden hour magic!")
        
        print("Running scheduler loop... Press Ctrl+C to exit.")
        while True:
            scheduler.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    main()
