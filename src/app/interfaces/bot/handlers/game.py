from aiogram import Router
from aiogram.types import Message

from app.domain.user_rating import UserRating
from app.interfaces.bot.features import features
from app.interfaces.bot.filters.text_ignore_case import TextInIgnoreCase
from app.interfaces.bot.keybords.common import _menu_kb
from app.use_cases.user_game_service import UserGameService

router = Router()


@router.message(TextInIgnoreCase(features.rating.triggers))
async def rating(message: Message, user_game_service: UserGameService):
    rating: UserRating = await user_game_service.get_rating(message.from_user.id)
    await message.answer(f"Всего нажатий твоих: {rating.user_taps}\nВсего нажатий: {rating.total_taps}",
                         reply_markup=_menu_kb())
    if rating.user_best is not None and rating.total_taps > 0:
        await message.answer(
            f"Лучший жмакер:\n{rating.user_best.name}[@{rating.user_best.username}]\n{rating.user_best.info}")
        await message.answer_photo(rating.user_best.photo)
