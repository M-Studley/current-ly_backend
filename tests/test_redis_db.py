import pytest

from app.db.redis_connection import redis_connection
from config import Config


@pytest.mark.asyncio
async def test_redis_connection():
    # Attempt to connect to Redis using the provided URL
    await redis_connection.connect(Config.TEST_REDIS_URL)

    test_key = "test_key"
    test_value = "test_value"

    # Set the test key-value pair
    await redis_connection.set(test_key, test_value)

    # Get the value back and assert it matches the expected value
    result = await redis_connection.get(test_key)
    assert result.decode() == test_value, f"Expected value '{test_value}' but got '{result.decode()}'"

    # Optional cleanup - delete the test key after the test
    await redis_connection.redis.delete(test_key)
