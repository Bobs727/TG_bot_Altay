from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
import os
import asyncio
load_dotenv()
BOT_TOKEN = (os.getenv("BOT_TOKEN"))

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)