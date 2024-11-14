from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Location(Base, TimestampMixin):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    district = Column(String, nullable=True)
    building = Column(String, nullable=True)

    # Relationships
    outages = relationship("Outage", back_populates="location")
