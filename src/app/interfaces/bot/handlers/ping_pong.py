from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command(commands=["ping", "health", "healthcheck"]))
async def ping_pong(message: Message):
    print(10000)
    await message.answer("200 pong")
