from aiogram import types
from loader import dp
@dp.message_handler(hashtags='homework')
async def hashtags(msg:types.Message):
    await msg.answer('siz hashtag yubordingiz!')
