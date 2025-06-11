from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.interfaces.bot.features import features


def tap_kb():
    kb = InlineKeyboardBuilder()
    kb = InlineKeyboardBuilder()
    kb.row(
        InlineKeyboardButton(
            text=features.tap.button,
            callback_data=features.tap.callback_action
        )
    )
    kb.row(
        InlineKeyboardButton(
            text=features.to_menu.button,
            callback_data=features.to_menu.callback_action
        )
    )
    return kb.as_markup()
