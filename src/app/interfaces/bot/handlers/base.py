from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from config import settings

router = Router()


@router.message(Command(commands=["ping", "health", "healthcheck"]))
async def ping_pong(message: Message):
    await message.answer("200 pong")


@router.message(Command(commands=["creator"]))
async def creator(message: Message):
    if message.from_user.id == settings.creator_id:
        await message.answer("*Master?*", parse_mode=ParseMode.MARKDOWN)


@router.message(Command(commands=["help"]))
async def cmd_help(message: Message):
    await message.answer("Бот для соревнования по тыканью по кнопке. Тыкай в кнопку и побеждай!")
