from aiogram import Bot
from loguru import logger

from config import settings


async def healthcheck(bot: Bot):
    logger.info("Bot is alive")
    await notify_admin_on_bot_status(bot, settings.creator_id)


async def notify_admin_on_bot_status(bot: Bot, admin_id: int) -> None:
    await bot.send_message(admin_id, "Bot is up")
