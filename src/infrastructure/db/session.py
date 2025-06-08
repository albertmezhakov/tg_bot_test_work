from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.ext.asyncio import async_sessionmaker
from config import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
