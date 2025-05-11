import os
from dotenv import load_dotenv

load_dotenv()  # сначала загружаем .env


PORT = int(os.environ.get("PORT", "8080"))
BOT_TOKEN = os.getenv("BOT_TOKEN")
SELF_URL = os.getenv("SELF_URL", "https://algo-hub-bot.onrender.com")
