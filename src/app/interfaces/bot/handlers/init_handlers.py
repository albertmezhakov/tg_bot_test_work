from aiogram import Router

from . import base, cancel, fallback, game, profile


def setup_handlers() -> Router:
    router = Router()
    router.include_router(cancel.router)
    router.include_router(game.router)
    router.include_router(profile.router)
    router.include_router(base.router)
    # router.include_router(errors.router)
    router.include_router(fallback.router)
    return router
