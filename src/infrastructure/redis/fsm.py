from aiogram.fsm.storage.redis import RedisStorage

from infrastructure.redis.client import redis_client

fsm_storage = RedisStorage(redis_client)
