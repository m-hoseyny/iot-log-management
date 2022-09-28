from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.DeviceCredential])
def read_device_credentials(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve device_credentails.
    """
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    objs = crud.device_credential.get_multi(db, skip=skip, limit=limit)
    return objs


@router.post("/", response_model=schemas.DeviceCreate)
def create_device_credential(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.DeviceCredentialUpdate,
) -> Any:
    """
    Create new device_credential.
    """
    obj = crud.device.get(db, id=obj_in.id)
    if obj:
        raise HTTPException(
            status_code=400,
            detail="The device with this external_id already exists in the system.",
        )
    obj = crud.device_credential.create(db, obj_in=obj_in)
    return obj


@router.get("/{device_credential_id}", response_model=schemas.Device)
def read_device_credentials(
    device_credential_id: UUID,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific device by id.
    """
    obj = crud.device_credential.get(db, id=device_credential_id)
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return obj


@router.put("/{device_credential_id}", response_model=schemas.DeviceCredentialUpdate)
def update_device(
    *,
    db: Session = Depends(deps.get_db),
    device_credential_id: UUID,
    obj_in: schemas.DeviceCredential,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a device_credentials.
    """
    obj = crud.device_credential.get(db, id=device_credential_id)
    if not obj:
        raise HTTPException(
            status_code=404,
            detail="The device with this external_id does not exist in the system",
        )
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    obj = crud.device_credential.update(db, db_obj=obj, obj_in=obj_in)
    return obj
