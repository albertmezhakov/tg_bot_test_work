from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Envs(Enum):
    local_test = "local_test"
    stage = "stage"
    prod = "prod"


class BotSettings(BaseSettings):
    tg_bot_token: str

    postgres_db: str | None
    postgres_user: str | None
    postgres_password: str | None
    postgres_host: str | None
    postgres_port: str | None

    fsm_redis_host: str | None
    fsm_redis_port: str | None
    fsm_redis_db: int | None
    fsm_redis_pass: str | None

    register_passphrase: str | None
    creator_id: int | None

    environment: Envs = Envs.local_test

    schedule_healthcheck: str = "7:00"  # !!!UTC timezone!!!

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:"
            f"{self.postgres_password}@{self.postgres_host}:"
            f"{self.postgres_port}/{self.postgres_db}"
        )


settings = BotSettings()
