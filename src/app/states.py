from aiogram.fsm.state import StatesGroup, State

class ProfileState(StatesGroup):
    name = State()
    info = State()
    photo = State()