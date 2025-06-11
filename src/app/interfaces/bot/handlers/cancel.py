from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.interfaces.bot.features import features
from app.interfaces.bot.filters.text_ignore_case import TextInIgnoreCase
from app.interfaces.bot.keyboards import keyboards

router = Router()


@router.message(TextInIgnoreCase(features.cancel.triggers), StateFilter("*"))
async def cancel(message: Message, state: FSMContext):
    await message.answer("Принял, отбой, возвращаюсь в главное меню.", reply_markup=keyboards.menu_kb.as_reply_markup())
    if await state.get_state() is not None:
        await state.clear()


@router.callback_query(F.text == features.cancel.callback_action, StateFilter("*"))
async def cancel_callback(cb: CallbackQuery, state: FSMContext) -> None:
    await cb.message.edit_text(
        "Принял, отбой, возвращаюсь в главное меню.", reply_markup=keyboards.menu_kb.as_reply_markup()
    )
    if await state.get_state() is not None:
        await state.clear()
