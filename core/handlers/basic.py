from aiogram import Bot
from aiogram.types import Message, ReplyKeyboardRemove
from core import views


async def get_start(message: Message, bot: Bot):
    await message.answer(views.welcome_message(message.from_user.first_name), reply_markup=ReplyKeyboardRemove())
    await message.answer(views.welcome_message2(message.from_user.first_name))


async def get_help(message: Message, bot: Bot):
    await message.answer(views.help_message())


async def get_any(message: Message, bot: Bot):
    await message.answer(views.wrong_value_message())


async def get_about(message: Message, bot: Bot):
    await message.answer(views.about_message())



