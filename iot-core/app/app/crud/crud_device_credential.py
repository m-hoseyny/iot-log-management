from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.device_credential import DeviceCredential
from app.schemas.device_credential import DeviceCredentialCreate, DeviceCredentialUpdate


class CRUDDeviceCredential(CRUDBase[DeviceCredential, DeviceCredentialCreate, DeviceCredentialUpdate]):
    def get_by_id(self, db: Session, *, id: str) -> Optional[DeviceCredential]:
        return db.query(DeviceCredential).filter(DeviceCredential.id == id).first()

    def create(self, db: Session, *, obj_in: DeviceCredentialCreate) -> DeviceCredential:
        db_obj = DeviceCredential(
            id=obj_in.id,
            credentials_id=obj_in.credentials_id,
            credentials_type=obj_in.credentials_type,
            credentials_value=obj_in.credentials_value,
            device_id=obj_in.device_id
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: DeviceCredential, obj_in: Union[DeviceCredentialUpdate, Dict[str, Any]]
    ) -> DeviceCredential:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


device_credential = CRUDDeviceCredential(DeviceCredential)
