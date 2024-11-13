import json
import logging
from typing import Any, Optional

from redis.asyncio import Redis

logging.basicConfig(level=logging.INFO)


class RedisConnection:
    def __init__(self):
        self.redis: Redis | None = None

    async def connect(self, url) -> None:
        if self.redis is None:
            try:
                self.redis = await Redis.from_url(url)
                logging.info("Connected to Redis")
            except Exception as e:
                logging.error(f"Failed to connect to Redis: {e}")
                raise e

    async def disconnect(self):
        if self.redis is not None:
            try:
                await self.redis.close()
                logging.info("Disconnected from Redis")
            except Exception as e:
                logging.error(f"Error disconnecting from Redis: {e}")
                raise e
            finally:
                self.redis = None

    async def get(self, key: str) -> Any:
        if not self.redis:
            raise ConnectionError("Redis connection not established.")
        value = await self.redis.get(key)
        if value:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        return None

    async def set(self, key: str, value: Any):
        if not self.redis:
            raise ConnectionError("Redis connection not established.")
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        await self.redis.set(key, value)


redis_connection = RedisConnection()
