# Instagram Automation Tool v2.0 (Photographer Edition) 📸

A powerful, Python-based automation tool designed specifically for photographers to manage their Instagram presence. Schedule posts, upload Reels/Stories, and grow your reach with smart hashtags.

## Features

- **📸 Photo & Video Upload**: Support for Posts, Reels, and Stories.
- **#️⃣ Smart Hashtags**: Auto-generate trending hashtags for Portraits, Landscapes, Street, and B&W photography.
- **📅 Smart Scheduler**: Schedule posts for "Golden Hour" or other high-engagement times.
- **🤖 Engagement Bot**: Automate likes and comments (use with caution).
- **🛡️ Safety First**: Built-in limits and delays to mimic human behavior.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/SaiBalusu-usf/instagram_bot.git
    cd instagram_bot
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Credentials**:
    - Rename `.env.example` to `.env`
    - Add your Instagram credentials:
      ```
      INSTAGRAM_USERNAME=your_username
      INSTAGRAM_PASSWORD=your_password
      ```

## Usage

Run the main script:
```bash
py main.py
```

### Menu Options
1.  **Login only**: Verify credentials.
2.  **Immediate Photo Upload**: Upload with auto-generated captions.
3.  **Immediate Reel Upload**: Upload video Reels.
4.  **Immediate Story Upload**: Post to your Story.
5.  **Generate Smart Hashtags**: Get a list of tags for manual use.
6.  **Start Scheduler**: Run the background automation loop.

## Disclaimer ⚠️

This tool uses the private Instagram API via `instagrapi`.
- **Use at your own risk.** Automated interaction can lead to account flags or bans.
- We recommend using this tool moderately and ideally with a 4G/5G mobile proxy.
- This project is for educational purposes.

## License

MIT
