from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OutageBase(BaseModel):
    service_type: str  # e.g., 'electricity', 'water' this may become an ENUM
    status: str  # e.g., 'ongoing', 'resolved' this may become an ENUM


class OutageCreate(OutageBase):
    location_id: int


class OutageOut(OutageBase):
    id: int
    location_id: int
    description: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class OutageUpdate(BaseModel):
    service_type: Optional[str]
    status: Optional[str]
    description: Optional[str]

    class Config:
        from_attributes = True
