from sqlalchemy import DateTime, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase, AsyncAttrs):
    pass


class TimestampMixin(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    created_at = mapped_column(DateTime, nullable=False, server_default=func.now())
    updated_at = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )
