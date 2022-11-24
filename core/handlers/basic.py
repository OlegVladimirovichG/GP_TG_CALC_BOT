from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import get_reply_keyboard


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Hello {message.from_user.first_name}', reply_markup=get_reply_keyboard())
