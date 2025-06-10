from aiogram import Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import ChatMemberUpdated, ErrorEvent
from loguru import logger

router = Router()


@router.errors()
async def bot_blocked_handler(event: ErrorEvent) -> None:
    exception = event.exception
    if isinstance(exception, TelegramBadRequest) and "bot was blocked by the user" in str(exception).lower():
        logger.info(event.message.from_user.id)
        logger.info(exception)


@router.my_chat_member()
async def handle_my_chat_member(event: ChatMemberUpdated):
    pass
