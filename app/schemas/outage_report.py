from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OutageReportBase(BaseModel):
    reported_status: str  # 'initial', 'update', 'resolved'
    description: Optional[str]


class OutageReportCreate(OutageReportBase):
    outage_id: int
    user_id: int


class OutageReportOut(OutageReportBase):
    id: int
    outage_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class OutageReportUpdate(BaseModel):
    reported_status: Optional[str]
    description: Optional[str]

    class Config:
        from_attributes = True
