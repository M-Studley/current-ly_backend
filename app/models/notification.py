from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, TimestampMixin


class Notification(Base, TimestampMixin):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    is_read = Column(Boolean, default=False)

    # Foreign Keys
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    outage_id = Column(Integer, ForeignKey("outages.id"), nullable=True)

    # Relationships
    user = relationship("User", back_populates="notifications")
    outage = relationship("Outage", backref="notifications")
