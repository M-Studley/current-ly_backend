from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Outage(Base, TimestampMixin):
    __tablename__ = "outages"

    id = Column(Integer, primary_key=True, index=True)
    service_type = Column(String, nullable=False)  # e.g., 'electricity', 'water'
    status = Column(String, nullable=False)  # e.g., 'ongoing', 'resolved'
    description = Column(Text, nullable=True)

    # Foreign Keys
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)

    # Relationships
    location = relationship("Location", back_populates="outages")
    reports = relationship("OutageReport", back_populates="outage")
