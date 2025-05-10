from dotenv import load_dotenv
import os
SELF_URL = os.getenv("SELF_URL", "https://algo-hub-bot.onrender.com")

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
