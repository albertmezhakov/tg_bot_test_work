import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.interfaces.bot.handlers.init_handlers import setup_handlers
from app.interfaces.bot.lifecycle import router as lifecycle_router
from app.interfaces.bot.middlewares.authorization import AuthorizationMiddleware
from app.interfaces.bot.middlewares.dependency_injection import UserProfileServiceMiddleware
from config import settings
from infrastructure.redis.fsm import fsm_storage


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(
        token=settings.tg_bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage() if settings.environment.local_test else fsm_storage)

    dp.include_router(lifecycle_router)

    dp.include_router(setup_handlers())

    dp.message.middleware(UserProfileServiceMiddleware())
    dp.callback_query.middleware(UserProfileServiceMiddleware())

    dp.message.middleware(AuthorizationMiddleware())
    dp.callback_query.middleware(AuthorizationMiddleware())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
