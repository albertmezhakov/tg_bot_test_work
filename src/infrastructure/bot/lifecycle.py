import logging

from aiogram import Dispatcher, Router, Bot

from app.schedulers.apscheduler_runner import start_scheduler
from app.use_cases.healthcheck import notify_admin_on_bot_status
from app.use_cases.setup_bot_commands import setup_bot_commands
from config import settings

logger = logging.getLogger(__name__)

router = Router()


@router.startup()
async def on_startup(bot: Bot) -> None:
    logger.info("Bot is up")

    await notify_admin_on_bot_status(bot, settings.creator_id)
    await setup_bot_commands(bot)

    start_scheduler(bot)


@router.shutdown()
async def on_shutdown(dispatcher: Dispatcher) -> None:
    await dispatcher.storage.close()
