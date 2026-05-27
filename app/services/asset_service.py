from fastapi import HTTPException
from sqlalchemy.orm import Session

from app import crud
from app import schemas

from app.constants import AssetStatus
from app.constants import ALLOWED_STATUS_TRANSITIONS


def create_asset_service(
    db: Session,
    asset: schemas.AssetCreate
):
    existing_asset = crud.get_asset_by_code(
        db,
        asset.asset_code
    )

    if existing_asset:
        raise HTTPException(
            status_code=400,
            detail="Asset code already exists."
        )

    if asset.maintenance_due < asset.purchase_date:
        raise HTTPException(
            status_code=400,
            detail=(
                "Maintenance due date cannot "
                "be earlier than purchase date."
            )
        )

    return crud.create_asset(db, asset)


def validate_status_transition(
    current_status: str,
    new_status: str
):
    allowed_transitions = (
        ALLOWED_STATUS_TRANSITIONS.get(
            current_status,
            []
        )
    )

    if new_status not in allowed_transitions:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Cannot transition asset "
                f"from '{current_status}' "
                f"to '{new_status}'."
            )
        )


def update_asset_service(
    db: Session,
    asset_id: int,
    asset_update: schemas.AssetUpdate
):
    db_asset = crud.get_asset_by_id(
        db,
        asset_id
    )

    if not db_asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found."
        )

    if (
        asset_update.status
        and asset_update.status.value
        != db_asset.status
    ):
        validate_status_transition(
            current_status=db_asset.status,
            new_status=asset_update.status.value
        )

    if (
        db_asset.status
        == AssetStatus.RETIRED.value
        and asset_update.assigned_to
    ):
        raise HTTPException(
            status_code=400,
            detail=(
                "Retired assets cannot be assigned."
            )
        )

    if (
        db_asset.status
        == AssetStatus.UNDER_MAINTENANCE.value
        and asset_update.assigned_to
    ):
        raise HTTPException(
            status_code=400,
            detail=(
                "Assets under maintenance "
                "cannot be reassigned."
            )
        )

    if (
        asset_update.maintenance_due
        and asset_update.maintenance_due
        < db_asset.purchase_date
    ):
        raise HTTPException(
            status_code=400,
            detail=(
                "Maintenance due date cannot "
                "be earlier than purchase date."
            )
        )

    return crud.update_asset(
        db,
        db_asset,
        asset_update
    )


def delete_asset_service(
    db: Session,
    asset_id: int
):
    db_asset = crud.get_asset_by_id(
        db,
        asset_id
    )

    if not db_asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found."
        )

    crud.delete_asset(db, db_asset)

    return {
        "message": (
            "Asset deleted successfully."
        )
    }


def create_maintenance_service(
    db: Session,
    asset_id: int,
    maintenance: schemas.MaintenanceCreate
):
    db_asset = crud.get_asset_by_id(
        db,
        asset_id
    )

    if not db_asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found."
        )

    if db_asset.status != AssetStatus.ACTIVE.value:
        raise HTTPException(
            status_code=400,
            detail=(
                "Only active assets can "
                "enter maintenance."
            )
        )

    maintenance_log = crud.create_maintenance_log(
        db,
        asset_id,
        maintenance
    )

    db_asset.status = (
        AssetStatus.UNDER_MAINTENANCE.value
    )

    db.commit()

    db.refresh(db_asset)

    return maintenance_log


def get_maintenance_logs_service(
    db: Session,
    asset_id: int
):
    db_asset = crud.get_asset_by_id(
        db,
        asset_id
    )

    if not db_asset:
        raise HTTPException(
            status_code=404,
            detail="Asset not found."
        )

    return crud.get_maintenance_logs(
        db,
        asset_id
    )