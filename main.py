import asyncio
import aiohttp
import os
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from app.handlers.start import router
from aiohttp import web, ClientSession
import threading
from ping import ping_forever
from config import SELF_URL


# Запускаем пинг в отдельном потоке
threading.Thread(target=ping_forever, daemon=True).start()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

# Фейковый веб-сервер для Render
async def fake_web_server():
    async def handle(request):
        return web.Response(text="✅ Bot is alive!")
    app = web.Application()
    app.router.add_get("/", handle)
    port = int(os.environ.get("PORT", 8080))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# 🔁 Self-ping every 10 minutes

async def self_ping():
    while True:
        try:
            async with aiohttp.ClientSession(timeout=None) as session:
                await session.get(SELF_URL)
                print(f"🔄 Self-ping → {SELF_URL}")
        except Exception as e:
            print("⚠️ Self-ping error:", e)
        await asyncio.sleep(300)  # раз в 5 минут


# Опциональный heartbeat
async def heartbeat():
    while True:
        await asyncio.sleep(300)

# 🚀 Главная функция с ОТСТУПОМ!
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.gather(
        fake_web_server(),
        dp.start_polling(bot),
        heartbeat(),
        self_ping()
    )

if __name__ == "__main__":
    asyncio.run(main())




