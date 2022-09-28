from datetime import datetime
from typing import Optional
import uuid
from pydantic import BaseModel, UUID4


# Shared properties
class DeviceCredentialBase(BaseModel):
    credentials_id: str
    credentials_type: str
    credentials_value: Optional[str] = 'unknwon'
    device_id: Optional[UUID4] = uuid.uuid4()

    created_at: datetime
    updated_at: datetime


# Properties to receive via API on creation
class DeviceCredentialCreate(DeviceCredentialBase):
    pass


# Properties to receive via API on update
class DeviceCredentialUpdate(DeviceCredentialBase):
    pass


class DeviceCredentialInDBBase(DeviceCredentialBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class DeviceCredential(DeviceCredentialInDBBase):
    pass


# Additional properties stored in DB
class DeviceInDB(DeviceCredentialInDBBase):
    pass
