from typing import Optional

from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    @staticmethod
    async def create_user(session: AsyncSession, user_data: UserCreate) -> User:
        """Create a new user."""
        new_user = User(**user_data.model_dump())
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user

    @staticmethod
    async def get_user_by_id(session: AsyncSession, user_id: int) -> Optional[User]:
        """Retrieve a user by their ID."""
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_all_users(session: AsyncSession) -> Sequence[User]:
        """Retrieve all users."""
        result = await session.execute(select(User))
        return result.scalars().all()

    @staticmethod
    async def update_user(session: AsyncSession, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """Update user details."""
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            for key, value in user_data.dict(exclude_unset=True).items():
                setattr(user, key, value)
            await session.commit()
            await session.refresh(user)
        return user

    @staticmethod
    async def delete_user(session: AsyncSession, user_id: int) -> bool:
        """Delete a user by their ID."""
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            await session.delete(user)
            await session.commit()
            return True
        return False
