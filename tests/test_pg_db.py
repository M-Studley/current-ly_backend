import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.sql import text

from config import Config

TEST_PG_URL = Config.TEST_PG_URL

engine = create_async_engine(TEST_PG_URL, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@pytest.mark.asyncio
async def test_pg_connection():
    async with async_session() as session:
        result = await session.execute(text("SELECT 1"))

        assert result.scalar() == 1, f"Expected 1, but got {result.scalar()}"
