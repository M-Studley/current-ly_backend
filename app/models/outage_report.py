from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class OutageReport(Base, TimestampMixin):
    __tablename__ = "outage_reports"

    id = Column(Integer, primary_key=True, index=True)
    reported_status = Column(String, nullable=False)  # 'initial', 'update', 'resolved'
    description = Column(Text, nullable=True)

    # Foreign Keys
    outage_id = Column(Integer, ForeignKey("outages.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    outage = relationship("Outage", back_populates="reports")
    user = relationship("User", back_populates="reports")
