from aiogram import Router

from . import fallback, profile, ping_pong, errors


def setup_handlers() -> Router:
    router = Router()
    router.include_router(profile.router)
    router.include_router(ping_pong.router)
    router.include_router(errors.router)
    router.include_router(fallback.router)
    return router
