from functools import partial

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from app.use_cases.healthcheck import healthcheck
from config import settings


def start_scheduler(bot: Bot) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()

    hour, minute = map(int, settings.schedule_healthcheck.split(":"))
    scheduler.add_job(partial(healthcheck, bot), CronTrigger(hour=hour, minute=minute), id="healthcheck")

    scheduler.start()
    return scheduler
