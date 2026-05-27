from pydantic import BaseModel
from pydantic import Field
from pydantic import ConfigDict

from datetime import date
from datetime import datetime

from typing import Optional

from app.constants import AssetStatus


class AssetBase(BaseModel):
    asset_code: str

    asset_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    asset_type: str

    assigned_to: Optional[str] = None

    location: Optional[str] = None

    purchase_date: date

    maintenance_due: date

    status: AssetStatus = AssetStatus.ACTIVE


class AssetCreate(AssetBase):
    pass



class AssetUpdate(BaseModel):
    asset_name: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100
    )

    asset_type: Optional[str] = None

    assigned_to: Optional[str] = None

    location: Optional[str] = None

    maintenance_due: Optional[date] = None

    status: Optional[AssetStatus] = None



class AssetResponse(AssetBase):
    id: int

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)




class MaintenanceBase(BaseModel):
    issue: str = Field(
        ...,
        min_length=3,
        max_length=255
    )

    maintenance_date: date

    engineer_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    remarks: Optional[str] = None



class MaintenanceCreate(MaintenanceBase):
    pass



class MaintenanceResponse(MaintenanceBase):
    id: int

    asset_id: int

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)