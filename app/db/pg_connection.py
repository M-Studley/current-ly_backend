from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.config import Config
from app.models.base import Base


class PostgresConnection:
    def __init__(self):
        self.engine = create_async_engine(Config.PG_URL, echo=True)
        self.Session = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    async def init_db(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def close_db(self):
        await self.engine.dispose()

    async def get_async_session(self) -> AsyncSession:
        async with self.Session() as session:
            yield session


postgres_connection = PostgresConnection()
