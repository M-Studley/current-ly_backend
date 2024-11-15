from typing import Sequence, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.notification import Notification
from schemas.notification import NotificationCreate, NotificationUpdate


class NotificationService:
    @staticmethod
    async def create_notification(session: AsyncSession, notification_data: NotificationCreate) -> Notification:
        """Create a new notification."""
        new_notification = Notification(**notification_data.model_dump())
        session.add(new_notification)
        await session.commit()
        await session.refresh(new_notification)
        return new_notification

    @staticmethod
    async def get_all_notifications(session: AsyncSession) -> Sequence[Notification]:
        """Retrieve all notifications."""
        result = await session.execute(select(Notification))
        return result.scalars().all()

    @staticmethod
    async def get_notifications_for_user(session: AsyncSession, user_id: int) -> Sequence[Notification]:
        """Retrieve all notifications for a specific user."""
        result = await session.execute(select(Notification).where(Notification.user_id == user_id))
        return result.scalars().all()

    @staticmethod
    async def get_notification_by_id(session: AsyncSession, notification_id: int) -> Optional[Notification]:
        """Retrieve a notification by its ID."""
        result = await session.execute(select(Notification).where(Notification.id == notification_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_notification(session: AsyncSession, notification_id: int, notification_data: NotificationUpdate) -> \
    Optional[Notification]:
        """Update an existing notification."""
        notification = await NotificationService.get_notification_by_id(session, notification_id)
        if not notification:
            return None

        for key, value in notification_data.dict(exclude_unset=True).items():
            setattr(notification, key, value)

        await session.commit()
        await session.refresh(notification)
        return notification

    @staticmethod
    async def delete_notification(session: AsyncSession, notification_id: int) -> bool:
        """Delete a notification by its ID."""
        notification = await NotificationService.get_notification_by_id(session, notification_id)
        if not notification:
            return False

        await session.delete(notification)
        await session.commit()
        return True
