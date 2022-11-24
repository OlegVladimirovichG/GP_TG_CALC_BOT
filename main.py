import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from core.handlers.basic import get_start, get_help
from core.settings import settings
from core.utils.commands import set_commands
from core.handlers import form
from core.utils.statesform import StepsForm


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, 'Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] -  %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(form.get_form, Command(commands='calc'))
    dp.message.register(form.get_calc_type, StepsForm.GET_CALC_TYPE)
    dp.message.register(form.get_operation, StepsForm.GET_OPERATION)
    dp.message.register(form.get_first_num, StepsForm.GET_FIRST_NUM)
    dp.message.register(form.get_second_num, StepsForm.GET_SECOND_NUM)
    dp.message.register(form.get_expression, StepsForm.GET_EXPRESSION)
    dp.message.register(get_start, Command(commands='start'))
    dp.message.register(get_help, Command(commands='help'))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
