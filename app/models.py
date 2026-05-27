from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from datetime import datetime

from app.database import Base
from app.constants import AssetStatus


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)

    asset_code = Column(String, unique=True, nullable=False)

    asset_name = Column(String, nullable=False)

    asset_type = Column(String, nullable=False)

    assigned_to = Column(String, nullable=True)

    location = Column(String, nullable=True)

    purchase_date = Column(Date, nullable=False)

    maintenance_due = Column(Date, nullable=False)

    status = Column(String, default=AssetStatus.ACTIVE.value)

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    maintenance_logs = relationship(
        "MaintenanceLog",
        back_populates="asset",
        cascade="all, delete"
    )



class MaintenanceLog(Base):
    __tablename__ = "maintenance_logs"

    id = Column(Integer, primary_key=True, index=True)

    asset_id = Column(
        Integer,
        ForeignKey("assets.id"),
        nullable=False
    )

    issue = Column(String, nullable=False)

    maintenance_date = Column(Date, nullable=False)

    engineer_name = Column(String, nullable=False)

    remarks = Column(String, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    asset = relationship(
        "Asset",
        back_populates="maintenance_logs"
    )