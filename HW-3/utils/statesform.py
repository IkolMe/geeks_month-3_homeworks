from aiogram.fsm.state import StatesGroup, State


class Questions(StatesGroup):
    GET_NAME = State()
    GET_LAST_NAME = State()
    GET_GENDER = State()
    GET_FAV_SHOW = State()
