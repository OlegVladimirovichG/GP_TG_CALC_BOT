from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core import views
from core.utils.statesform import StepsForm
from core.keyboards.reply import choose_calc, choose_operation
from core.utils.calc import init



async def get_form(message: Message, state: FSMContext):
    await message.answer(f'Выберите какие числа будем считать', reply_markup=choose_calc())
    await state.set_state(StepsForm.GET_CALC_TYPE)


async def get_calc_type(message: Message, state: FSMContext):
    if message.text == 'Рациональные':
        await state.update_data(calc_type='decimal')
        await message.answer(views.chosen_rational(), reply_markup=choose_operation())
        await state.set_state(StepsForm.GET_OPERATION)
    elif message.text == 'Комплексные':
        await state.update_data(calc_type='complex')
        await message.answer(views.chosen_complex(), reply_markup=choose_operation())
        await state.set_state(StepsForm.GET_OPERATION)
    elif message.text == 'Свободное выражение':
        await state.update_data(calc_type='free')
        await message.answer(views.chosen_freeform())
        await state.set_state(StepsForm.GET_EXPRESSION)
    else:
        await message.answer('Неправильный вид калькулятора ❌')


async def get_operation(message: Message, state: FSMContext):
    op = ''
    match message.text:
        case 'a + b':
            await state.update_data(operation='+')
            op = 'сложения'
        case 'a - b':
            await state.update_data(operation='-')
            op = 'вычитания'
        case 'a * b':
            await state.update_data(operation='*')
            op = 'умножения'
        case 'a / b':
            await state.update_data(operation='/')
            op = 'деления'
    await message.answer(views.got_operator(op))
    await state.set_state(StepsForm.GET_FIRST_NUM)



async def get_first_num(message: Message, state: FSMContext):
    check_input = message.text
    if check_input.isdigit():
        await state.update_data(first_num=message.text)
        await message.answer(f'Введите второе число:')
        await state.set_state(StepsForm.GET_SECOND_NUM)
    else:
        await message.answer(views.wrong_input())


async def get_second_num(message: Message, state: FSMContext):
    check_input = message.text
    if check_input.isdigit():
        await state.update_data(second_num=message.text)
        context_data = await state.get_data()
        await message.answer(f'Ответ: {context_data["first_num"]} {context_data["operation"]} '
                                f'{context_data["second_num"]} = {init(context_data)}')
        await message.answer(views.end_calc())
        await state.clear()
    else:
        await message.answer(views.wrong_input())


async def get_expression(message: Message, state: FSMContext):
    await state.update_data(operation='')
    await state.update_data(expression=message.text)
    context_data = await state.get_data()
    await message.answer(f'{init(context_data)}')
    await message.answer(views.end_calc())
    await state.clear()




