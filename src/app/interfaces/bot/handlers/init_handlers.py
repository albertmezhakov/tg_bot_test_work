from aiogram import Router
import profile
import fallback


def setup_handlers() -> Router:
    router = Router()
    router.include_router(profile.router)
    router.include_router(fallback.router)
    return router
