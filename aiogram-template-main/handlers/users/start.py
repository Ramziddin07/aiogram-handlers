from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

BLACKLIST=[]

@dp.message_handler(chat_id=BLACKLIST, text='/start')
async def bot_start(message: types.Message):
    text=f"Salom, {message.from_user.full_name}! Siz bloklangansz!"
    await message.answer(text)

@dp.message_handler(CommandStart(deep_link="mylifeblacksky"))
async def bot_start(message: types.Message):
    args = message.get_args()
    text=f"Salom, {message.from_user.full_name}!"
    text += f"Sizni {args } tavsiya qildi"
    await message.answer(text)


