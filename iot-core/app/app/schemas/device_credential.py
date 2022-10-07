from datetime import datetime
from typing import Optional
import uuid
from pydantic import BaseModel


# Shared properties
class DeviceCredentialBase(BaseModel):
    id: uuid.UUID
    credentials_id: Optional[str]
    credentials_type: Optional[str]
    credentials_value: Optional[str]
    device_id: Optional[uuid.UUID]


# Properties to receive via API on creation
class DeviceCredentialCreate(DeviceCredentialBase):
    pass


# Properties to receive via API on update
class DeviceCredentialUpdate(DeviceCredentialBase):
    pass


class DeviceCredentialInDBBase(DeviceCredentialBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


# Additional properties to return via API
class DeviceCredential(DeviceCredentialInDBBase):
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


# Additional properties stored in DB
class DeviceInDB(DeviceCredentialInDBBase):
    pass
