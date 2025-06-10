from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands=["ping", "health", "healthcheck"]))
async def ping_pong(message: Message):
    print(10000)
    await message.answer("200 pong")
