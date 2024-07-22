from loader import dp, bot
from aiogram.types import ContentType,Message
from pathlib import Path

download_path=Path().joinpath("downloads","categories")
download_path.mkdir(parents=True, exist_ok=True)

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message:Message):
    await message.document.download(destination=download_path)
    doc_id=message.document.file_id
    await message.reply("Siz hujjat yubordingiz!\n"
                        f"file_id={doc_id}")

@dp.message_handler(content_types='video')
async def photo_handler(message:Message):
    await message.photo[-1].download(destination=download_path)
    await message.reply("rasm qabul qilindi\n"
                        f"file_id={message.photo[1].file_id}")

@dp.message_handler(content_types='photo')
async def photo_handler(message:Message):
    await message.photo[-1].download(destination=download_path)
    await message.reply("rasm qabul qilindi\n"
                        f"file_id={message.photo[1].file_id}")

@dp.message_handler(content_types=ContentType.LOCATION)
async def any_handler(message:Message):
    await message.reply(f"{message.contact_type} qabul qilindi")


@dp.message_handler(content_types=ContentType.CONTACT)
async def any_handler(message: Message):
    await message.reply(f"{message.contact_type} Kantakt qabul qilindi")

@dp.message_handler(content_types=ContentType.AUDIO)
async def any_handler(message:Message):
    await message.reply(f"{message.contact_type} ovoz qabul qilindi")


@dp.message_handler(content_types=ContentType.STICKER)
async def any_handler(message: Message):
    await message.reply(f"stiker qabul qilindi")







