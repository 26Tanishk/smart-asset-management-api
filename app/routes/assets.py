from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app import crud
from app import schemas

from app.services import asset_service


router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)


@router.post(
    "/",
    response_model=schemas.AssetResponse,
    status_code=201
)
def create_asset(
    asset: schemas.AssetCreate,
    db: Session = Depends(get_db)
):
    return asset_service.create_asset_service(
        db,
        asset
    )


@router.get(
    "/",
    response_model=List[schemas.AssetResponse]
)
def get_assets(
    status: Optional[str] = None,
    asset_type: Optional[str] = None,
    assigned_to: Optional[str] = None,
    sort_by: Optional[str] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return crud.get_assets(
        db=db,
        status=status,
        asset_type=asset_type,
        assigned_to=assigned_to,
        sort_by=sort_by,
        page=page,
        limit=limit
    )


@router.get(
    "/overdue",
    response_model=List[schemas.AssetResponse]
)
def get_overdue_assets(
    db: Session = Depends(get_db)
):
    return crud.get_overdue_assets(db)


@router.get(
    "/active",
    response_model=List[schemas.AssetResponse]
)
def get_active_assets(
    db: Session = Depends(get_db)
):
    return crud.get_assets_by_status(
        db,
        "active"
    )


@router.get(
    "/under-maintenance",
    response_model=List[schemas.AssetResponse]
)
def get_under_maintenance_assets(
    db: Session = Depends(get_db)
):
    return crud.get_assets_by_status(
        db,
        "under_maintenance"
    )


@router.get(
    "/{asset_id}",
    response_model=schemas.AssetResponse
)
def get_asset_by_id(
    asset_id: int,
    db: Session = Depends(get_db)
):
    asset = crud.get_asset_by_id(
        db,
        asset_id
    )

    if not asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found."
        )

    return asset


@router.put(
    "/{asset_id}",
    response_model=schemas.AssetResponse
)
def update_asset(
    asset_id: int,
    asset_update: schemas.AssetUpdate,
    db: Session = Depends(get_db)
):
    return asset_service.update_asset_service(
        db,
        asset_id,
        asset_update
    )


@router.delete("/{asset_id}")
def delete_asset(
    asset_id: int,
    db: Session = Depends(get_db)
):
    return asset_service.delete_asset_service(
        db,
        asset_id
    )