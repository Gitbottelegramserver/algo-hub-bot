import asyncio
import os
from aiogram import Bot, Dispatcher
from aiohttp import web
import aiohttp

from config import BOT_TOKEN
from app.handlers.start import router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

# 📡 AIOHTTP Web Server
async def handle_ping(request):
    return web.Response(text="OK")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    port = int(os.environ.get("PORT", 8080))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# 🔁 Self-ping every 10 minutes
async def self_ping():
    while True:
        try:
            url = os.getenv("SELF_URL", "https://algo-hub-bot.onrender.com")
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    print(f"Pinged {url} | Status: {resp.status}")
        except Exception as e:
            print(f"[Ping Error] {e}")
        await asyncio.sleep(600)

# 🔄 Run everything
async def main():
    await asyncio.gather(
        start_web_server(),
        dp.start_polling(bot),
        self_ping()
    )

if __name__ == "__main__":
    asyncio.run(main())
