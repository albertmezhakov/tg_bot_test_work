from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def _menu_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="Меню", callback_data="main_menu")
    return kb.as_markup()



def _open_menu_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="Нажми меня")
    kb.button(text="Рейтинг")
    kb.button(text="Мой профиль")
    return kb.as_markup()
