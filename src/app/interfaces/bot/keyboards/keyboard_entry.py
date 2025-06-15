from __future__ import annotations

from typing import Callable, ClassVar

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from app.interfaces.bot.features.feature_entry import FeatureEntry


class KeyboardEntry:
    all_keyboards: ClassVar[list[KeyboardEntry]] = []

    def __init__(self, *, features: list[list[FeatureEntry]]):
        self.features = features
        self.all_keyboards.append(self)

    def as_inline_markup(
        self, suffix: str = "", should_add_suffix: Callable[[FeatureEntry], bool] = lambda f: True
    ) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        for row in self.features:
            buttons = []
            for feature in row:
                if not (feature.callback_action and feature.button):
                    raise ValueError(
                        f"Feature '{feature}' must have both `button` and `callback_action` for inline markup."
                    )

                callback_data = (
                    feature.callback_action + suffix
                    if suffix and should_add_suffix(feature)
                    else feature.callback_action
                )

                buttons.append(InlineKeyboardButton(text=feature.button, callback_data=callback_data))
            builder.row(*buttons)

        return builder.as_markup()

    def as_reply_markup(self) -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()

        for row in self.features:
            buttons = []
            for feature in row:
                if not feature.button:
                    raise ValueError(f"Feature '{feature}' must have `button` for reply markup.")
                buttons.append(KeyboardButton(text=feature.button))
            builder.row(*buttons)

        return builder.as_markup()
