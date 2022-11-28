from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_CALC_TYPE = State()
    GET_OPERATION = State()
    GET_FIRST_NUM = State()
    GET_SECOND_NUM = State()
    GET_EXPRESSION = State()
    GET_FRST_POLY = State()
    GET_SECOND_POLY = State()
