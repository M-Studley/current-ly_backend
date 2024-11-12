import pytest
from sqlalchemy.future import select
from app.db.pg_connection import postgres_connection as pg_conn
from app.models.base import Base
from app.config import Config
from sqlalchemy.ext.asyncio import create_async_engine

TEST_PG_URL = Config.TEST_PG_URL

# The fixture to create a test session with the test database
@pytest.fixture(scope="function")
async def test_db_session():
    # Create engine and connect to the test database
    engine = create_async_engine(TEST_PG_URL, echo=True, future=True)
    async with engine.begin() as conn:
        # Create the database schema for testing (tables, etc.)
        await conn.run_sync(Base.metadata.create_all)

    # Yield the session to be used in tests
    async with pg_conn.get_async_session() as session:
        yield session

    # Cleanup after test by dropping tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# Example of a test function using the test_db_session fixture
@pytest.mark.asyncio
async def test_db_initialization(test_db_session):
    async with test_db_session() as session:
        # Run a simple query to check the connection
        result = await session.execute(select(1))
        assert result.scalar() == 1  # Check if query returns 1

# Another example to check schema creation
@pytest.mark.asyncio
async def test_db_creation(test_db_session):
    async with test_db_session() as session:
        # Perform some database operation, like inserting data
        result = await session.execute(select(1))
        assert result.scalar() == 1  # Check if query returns 1
