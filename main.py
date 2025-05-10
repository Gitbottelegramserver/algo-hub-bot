import asyncio
import threading
import aiohttp
import os
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from app.handlers.start import router

from aiohttp import web

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

# Фейковый веб-сервер
async def fake_web_server():
    async def handle(request):
        return web.Response(text="OK")
    app = web.Application()
    app.router.add_get('/', handle)
    port = int(os.environ.get("PORT", 8080))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# 🔵 Heartbeat без текста
async def heartbeat():
    while True:
        await asyncio.sleep(300)  # просто ждёт 5 минут
#SelfPING
async def ping_self():
    import aiohttp
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://algo-hub-bot.onrender.com/") as resp:
                    print(f"Ping response: {resp.status}")
        except Exception as e:
            print(f"Ping error: {e}")
        await asyncio.sleep(600)  # раз в 10 минут

async def main():
    async def main():
    await asyncio.gather(
        start_web_server(),
        dp.start_polling(bot),
        ping_self()
    )

if __name__ == "__main__":
    asyncio.run(main())
