from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from app.interfaces.bot.features import features
from app.interfaces.bot.filters.text_ignore_case import TextInIgnoreCase

router = Router()


@router.message(TextInIgnoreCase(features.cancel.triggers), StateFilter("*"))
async def cancel(message: Message, state: FSMContext):
    await message.answer("Принял, отбой, возвращаюсь в главное меню.")
    if await state.get_state() is not None:
        await state.clear()
    # await _menu_kb()


@router.callback_query(TextInIgnoreCase(features.cancel.callback_action), StateFilter("*"))
async def cancel_callback(cb: CallbackQuery, state: FSMContext) -> None:
    await cb.message.edit_text("Принял, отбой, возвращаюсь в главное меню.")
    if await state.get_state() is not None:
        await state.clear()
    # await _menu_kb()


def _menu_kb():
    # TODO: Вынести в keyboards.common
    kb = ReplyKeyboardBuilder()
    kb.button(text="Меню", callback_data="main_menu")
    return kb.as_markup()
