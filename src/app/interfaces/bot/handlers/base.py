from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message

from app.interfaces.bot.features import features
from app.interfaces.bot.filters.text_ignore_case import TextInIgnoreCase
from app.interfaces.bot.keybords import keyboards
from config import settings

router = Router()


@router.message(TextInIgnoreCase(features.ping_pong.triggers))
async def ping_pong(message: Message):
    await message.answer("200 pong")


@router.message(TextInIgnoreCase(features.creator.triggers))
async def creator(message: Message):
    if message.from_user.id == settings.creator_id:
        await message.answer("*Master?*", parse_mode=ParseMode.MARKDOWN)


@router.message(TextInIgnoreCase(features.help_cmd.triggers))
async def cmd_help(message: Message):
    await message.answer("Бот для соревнования по тыканью по кнопке. Тыкай в кнопку и побеждай!")


@router.message(TextInIgnoreCase(features.start.triggers))
async def start(message: Message) -> None:
    await message.answer("Добро пожаловать в главное меню", reply_markup=keyboards.menu_kb.as_reply_markup())
