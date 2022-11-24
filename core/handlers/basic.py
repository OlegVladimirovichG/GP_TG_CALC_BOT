from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Привет {message.from_user.first_name} бла бла')


async def get_help(message: Message, bot: Bot):
    await message.answer(f'Тут помощь')
