from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core import views
from core.utils.statesform import StepsForm
from core.utils.poly import poly_init
from core.settings import custom_log


async def get_poly(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await message.answer(views.start_poly())
    await message.answer(views.first_poly())
    await state.set_state(StepsForm.GET_FRST_POLY)


async def get_first_poly(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await state.update_data(first_poly=message.text)
    await message.answer(views.second_poly())
    await state.set_state(StepsForm.GET_SECOND_POLY)


async def get_second_poly(message: Message, state: FSMContext):
    custom_log(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.text)
    await state.update_data(second_poly=message.text)
    context_data = await state.get_data()
    await message.answer(f'{poly_init(context_data)}')
    await message.answer(views.end_poly())
    await state.clear()
