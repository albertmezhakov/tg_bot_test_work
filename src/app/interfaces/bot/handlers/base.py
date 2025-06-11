from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message

from app.interfaces.bot.features import features
from app.interfaces.bot.filters.text_ignore_case import TextInIgnoreCase
from config import settings

router = Router()


@router.message(TextInIgnoreCase(features.ping_pong.triggers))
async def ping_pong(message: Message):
    await message.answer("200 pong")


@router.message(TextInIgnoreCase(features.creator.triggers))
async def creator(message: Message):
    if message.from_user.id == settings.creator_id:
        await message.answer("*Master?*", parse_mode=ParseMode.MARKDOWN)


@router.message(TextInIgnoreCase(features.help.triggers))
async def cmd_help(message: Message):
    await message.answer("Бот для соревнования по тыканью по кнопке. Тыкай в кнопку и побеждай!")
