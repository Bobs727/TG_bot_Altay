from main import bot, dp
from aiogram.types import Message
import os

ADMIN_ID = (os.getenv("ADMIN_ID"))

async def send_to_admin(dp):
    await bot.send_message(chat_id=ADMIN_ID, text="Здарова")

@dp.message_handler()
async def echo(message: Message):
    text = f"написал: {message.text}"
    await bot.send_message(chat_id=message.from_user.id, text=text)
    await message.answer(text=text)