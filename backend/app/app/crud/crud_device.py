from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.device import Device
from app.schemas.device import DeviceCreate, DeviceUpdate


class CRUDDevice(CRUDBase[Device, DeviceCreate, DeviceUpdate]):
    def get_by_external_id(self, db: Session, *, external_id: str) -> Optional[Device]:
        return db.query(Device).filter(Device.external_id == external_id).first()

    def create(self, db: Session, *, obj_in: DeviceCreate) -> Device:
        db_obj = Device(
            name=obj_in.name,
            type=obj_in.type,
            label=obj_in.label,
            external_id=obj_in.external_id,
            customer_id=obj_in.customer_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
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
