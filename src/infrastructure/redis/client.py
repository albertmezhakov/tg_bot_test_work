import redis.asyncio as redis

from config import settings

redis_client = redis.Redis(
    host=settings.fsm_redis_host,
    port=settings.fsm_redis_port,
    db=settings.fsm_redis_db,
    password=settings.fsm_redis_pass,
    decode_responses=True,
)
