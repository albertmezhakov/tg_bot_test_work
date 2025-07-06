from aiogram import Router
from aiogram.types import CallbackQuery, Message

from app.domain.user_rating import UserRating
from app.interfaces.bot.features import features
from app.interfaces.bot.filters.callback_prefix import CallbackPrefixFilter
from app.interfaces.bot.filters.text_ignore_case import TextInIgnoreCase
from app.interfaces.bot.keyboards import keyboards
from app.use_cases.user_game_service import UserGameService

router = Router()


@router.message(TextInIgnoreCase(features.rating.triggers))
async def rating_cmd(message: Message, user_game_service: UserGameService):
    rating: UserRating | None = await user_game_service.get_rating(message.from_user.id)
    if rating is None:
        return
    await message.answer(
        f"Всего нажатий твоих: {rating.user_taps}\nВсего нажатий: {rating.total_taps}",
        reply_markup=keyboards.menu_kb.as_reply_markup(),
    )
    if rating.user_best is not None and rating.total_taps > 0:
        await message.answer(
            f"Лучший жмакер:\n{rating.user_best.name}[@{rating.user_best.username}]\n{rating.user_best.info}"
        )
        await message.answer_photo(rating.user_best.photo)


@router.message(TextInIgnoreCase(features.send_tap.triggers))
async def send_tap_btn(message: Message):
    await message.answer(
        "Нажатий за последнюю сессию: 0",
        reply_markup=keyboards.tap_kb.as_inline_markup(suffix=":0", should_add_suffix=lambda f: f is features.tap_btn),
    )


@router.callback_query(CallbackPrefixFilter(features.tap_btn.callback_action))
async def action_tap(callback: CallbackQuery, user_game_service: UserGameService):
    await user_game_service.register_tap(callback.from_user.id)
    session_taps = int(callback.data.split(":")[1]) + 1
    await callback.message.edit_text(
        f"Нажатий за последнюю сессию: {session_taps}",
        reply_markup=keyboards.tap_kb.as_inline_markup(
            suffix=f":{session_taps}", should_add_suffix=lambda f: f is features.tap_btn
        ),
    )
    await callback.answer()
