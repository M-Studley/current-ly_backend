import pytest
from app.db.redis_connection import redis_connection
from app.config import Config

TEST_REDIS_URL = Config.TEST_REDIS_URL

@pytest.mark.asyncio
async def test_redis_connection():
    await redis_connection.connect()

    test_key = "test_key"
    test_value = "test_value"

    await redis_connection.set(test_key, test_value)

    result = await redis_connection.get(test_key)

    assert result == test_value

    await redis_connection.redis.delete(test_key)
    await redis_connection.disconnect()
