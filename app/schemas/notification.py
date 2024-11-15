from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NotificationBase(BaseModel):
    message: str
    is_read: bool = False


class NotificationCreate(NotificationBase):
    user_id: int
    outage_id: Optional[int]


class NotificationOut(NotificationBase):
    id: int
    user_id: int
    outage_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True

class NotificationUpdate(BaseModel):
    message: Optional[str]
    is_read: Optional[bool]

    class Config:
        from_attributes = True
