import asyncio
import threading
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

async def main():
    asyncio.create_task(fake_web_server())  # Запускаем фейковый сервер
    asyncio.create_task(heartbeat())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
