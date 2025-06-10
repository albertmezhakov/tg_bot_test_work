from aiogram.fsm.state import State, StatesGroup


class ProfileState(StatesGroup):
    name = State()
    info = State()
    photo = State()
