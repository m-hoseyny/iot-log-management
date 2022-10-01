from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api.api_v1.deps import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Device])
def read_devices(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve devices.
    """
    # TODO: Check access current user to the device not superuser
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    objs = crud.device.get_multi(db, skip=skip, limit=limit)
    return objs


@router.post("/", response_model=schemas.Device)
def create_device(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.DeviceCreate,
) -> Any:
    """
    Create new device.
    """
    obj = crud.device.get(db, id=obj_in.id)
    # TODO: Check access current user to the device not superuser
    if obj:
        raise HTTPException(
            status_code=400,
            detail="The device with this id already exists in the system.",
        )
    obj = crud.device.create(db, obj_in=obj_in)
    return obj


@router.get("/{device_id}", response_model=schemas.Device)
def read_device_by_id(
    device_id: UUID,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific device by id.
    """
    obj = crud.device.get(db, id=device_id)
    # TODO: Check access current user to the device not superuser
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return obj


@router.put("/{device_id}", response_model=schemas.User)
def update_device(
    *,
    db: Session = Depends(deps.get_db),
    device_id: UUID,
    obj_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a device.
    """
    obj = crud.device.get(db, id=device_id)
    if not obj:
        raise HTTPException(
            status_code=404,
            detail="The device with this id does not exist in the system",
        )
    # TODO: Check access current user to the device not superuser
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    obj = crud.device.update(db, db_obj=obj, obj_in=obj_in)
    return obj
