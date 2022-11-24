import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config_reader import config
from aiogram.filters import Text


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
    await message.answer("""Привет, это бот-калькулятор. Он поможет Вам в работе с рациональными и комплексными числами!

Напишите /help чтобы посмотреть список доступных команд.""")


# Хэндлер на команду /test1
@dp.message(commands=["help"])
async def hello_msg(message: types.Message):
    await message.answer("""Выберете:
/calculator - выбрать тип калькулятора
/help - получить справку о командах бота""")


# Хэндлер на команду /calc
@dp.message(commands=["calc"])
async def rational_calc(message: types.Message):
    await message.answer("Калькулятор рациональных чисел")
    await message.answer("Введите выражение:")

# Хэндлер на команду /complex
@dp.message(commands=["complex"])
async def сomplex_calc(message: types.Message):
    await message.answer("Калькулятор комплексных чисел")
    await message.answer("Введите выражение:")


@dp.message(commands="calculator")
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Рациональный")],
        [types.KeyboardButton(text="Комплексный")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Тип калькулятора"
    )
    await message.answer("Выберете тип калькулятора:", reply_markup=keyboard)


@dp.message(Text(text="Рациональный"))
async def with_puree(message: types.Message):
    await message.reply("Выбран рациональный калькулятор!", reply_markup=types.ReplyKeyboardRemove())

@dp.message(lambda message: message.text == "Комплексный")
async def without_puree(message: types.Message):
    await message.reply("Выбран комплексный калькулятор!", reply_markup=types.ReplyKeyboardRemove())

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
