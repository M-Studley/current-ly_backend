from typing import Optional

from pydantic import BaseModel, Field


class LocationBase(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    address: Optional[str]
    city: Optional[str]
    district: Optional[str]
    building: Optional[str]


class LocationCreate(LocationBase):
    pass


class LocationOut(LocationBase):
    id: int

    class Config:
        from_attributes = True


class LocationUpdate(BaseModel):
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)
    address: Optional[str]
    city: Optional[str]
    district: Optional[str]
    building: Optional[str]

    class Config:
        from_attributes = True
