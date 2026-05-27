from datetime import date

from sqlalchemy.orm import Session

from app import models
from app import schemas


def create_asset(
    db: Session,
    asset: schemas.AssetCreate
):
    db_asset = models.Asset(
        asset_code=asset.asset_code,
        asset_name=asset.asset_name,
        asset_type=asset.asset_type,
        assigned_to=asset.assigned_to,
        location=asset.location,
        purchase_date=asset.purchase_date,
        maintenance_due=asset.maintenance_due,
        status=asset.status.value
    )

    db.add(db_asset)

    db.commit()

    db.refresh(db_asset)

    return db_asset


def get_assets(
    db: Session,
    status: str = None,
    asset_type: str = None,
    assigned_to: str = None,
    sort_by: str = None,
    page: int = 1,
    limit: int = 10
):
    query = db.query(models.Asset)

    if status:
        query = query.filter(
            models.Asset.status == status
        )

    if asset_type:
        query = query.filter(
            models.Asset.asset_type == asset_type
        )

    if assigned_to:
        query = query.filter(
            models.Asset.assigned_to == assigned_to
        )

    allowed_sort_fields = {
        "purchase_date": models.Asset.purchase_date,
        "created_at": models.Asset.created_at,
        "asset_name": models.Asset.asset_name
    }

    if sort_by in allowed_sort_fields:
        query = query.order_by(
            allowed_sort_fields[sort_by]
        )

    offset = (page - 1) * limit

    query = query.offset(offset).limit(limit)

    return query.all()


def get_asset_by_id(
    db: Session,
    asset_id: int
):
    return (
        db.query(models.Asset)
        .filter(models.Asset.id == asset_id)
        .first()
    )


def get_asset_by_code(
    db: Session,
    asset_code: str
):
    return (
        db.query(models.Asset)
        .filter(models.Asset.asset_code == asset_code)
        .first()
    )


def update_asset(
    db: Session,
    db_asset: models.Asset,
    asset_update: schemas.AssetUpdate
):
    update_data = asset_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        if key == "status" and value:
            value = value.value

        setattr(db_asset, key, value)

    db.commit()

    db.refresh(db_asset)

    return db_asset


def delete_asset(
    db: Session,
    db_asset: models.Asset
):
    db.delete(db_asset)

    db.commit()


def create_maintenance_log(
    db: Session,
    asset_id: int,
    maintenance: schemas.MaintenanceCreate
):
    db_maintenance = models.MaintenanceLog(
        asset_id=asset_id,
        issue=maintenance.issue,
        maintenance_date=maintenance.maintenance_date,
        engineer_name=maintenance.engineer_name,
        remarks=maintenance.remarks
    )

    db.add(db_maintenance)

    db.commit()

    db.refresh(db_maintenance)

    return db_maintenance


def get_maintenance_logs(
    db: Session,
    asset_id: int
):
    return (
        db.query(models.MaintenanceLog)
        .filter(
            models.MaintenanceLog.asset_id == asset_id
        )
        .all()
    )


def get_overdue_assets(
    db: Session
):
    today = date.today()

    return (
        db.query(models.Asset)
        .filter(
            models.Asset.maintenance_due < today
        )
        .all()
    )


def get_assets_by_status(
    db: Session,
    status: str
):
    return (
        db.query(models.Asset)
        .filter(
            models.Asset.status == status
        )
        .all()
    )