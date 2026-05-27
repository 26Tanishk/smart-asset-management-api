from typing import List

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app import schemas

from app.services import asset_service



router = APIRouter(
    prefix="/assets",
    tags=["Maintenance"]
)


@router.post(
    "/{asset_id}/maintenance",
    response_model=schemas.MaintenanceResponse,
    status_code=201
)
def create_maintenance_log(
    asset_id: int,
    maintenance: schemas.MaintenanceCreate,
    db: Session = Depends(get_db)
):
    return asset_service.create_maintenance_service(
        db,
        asset_id,
        maintenance
    )



@router.get(
    "/{asset_id}/maintenance",
    response_model=List[
        schemas.MaintenanceResponse
    ]
)
def get_maintenance_logs(
    asset_id: int,
    db: Session = Depends(get_db)
):
    return (
        asset_service
        .get_maintenance_logs_service(
            db,
            asset_id
        )
    )