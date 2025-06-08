from config.config import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
