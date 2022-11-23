import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config_reader import config


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
# Для записей с типом Secret* необходимо
# вызывать метод get_secret_value(),
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Написать приветствие")


# Хэндлер на команду /test1
@dp.message(commands=["help"])
async def cmd_test1(message: types.Message):
    await message.reply("Написать помощ")


# Хэндлер на команду /test2
@dp.message(commands=["calc"])
async def cmd_test2(message: types.Message):
    await message.reply("Тут у нас калькулятор рациональных чисел")


@dp.message(commands=["complex"])
async def cmd_test2(message: types.Message):
    await message.reply("Тут у нас калькулятор комплексных чисел")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
