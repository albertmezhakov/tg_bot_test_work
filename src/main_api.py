from fastapi import FastAPI

from app.interfaces.api.routers import profile

app = FastAPI(
    title="Telegram Bot API",
    version="0.2.0",
    description="Telegram Bot API",
)

app.include_router(profile.router)
