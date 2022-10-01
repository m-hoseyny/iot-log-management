from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.device import Device
from app.schemas.device import DeviceCreate, DeviceUpdate

from app.schemas.device_credential import DeviceCredentialInDBBase
from app.crud import crud_device_credential

import uuid, random, string


class CRUDDevice(CRUDBase[Device, DeviceCreate, DeviceUpdate]):

    def create(self, db: Session, *, obj_in: DeviceCreate) -> Device:
        db_obj = Device(
            name=obj_in.name,
            type=obj_in.type,
            label=obj_in.label,
            customer_id=obj_in.customer_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        credential_id = uuid.uuid4()
        dc_obj = DeviceCredentialInDBBase(
            id=credential_id,
            credentials_id=credential_id.hex,
            credentials_type='access_token',
            credentials_value=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
            device_id=db_obj.id
        )
        crud_device_credential.device_credential.create(db=db, obj_in=dc_obj)
        print(db_obj.device_credential)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Device, obj_in: Union[DeviceUpdate, Dict[str, Any]]
    ) -> Device:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


device = CRUDDevice(Device)
