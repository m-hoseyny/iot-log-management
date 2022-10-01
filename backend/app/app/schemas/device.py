from typing import Optional, Union, List
import uuid
from app.schemas.device_credential import DeviceCredentialInDBBase
from pydantic import BaseModel


# Shared properties
class DeviceBase(BaseModel):
    id: uuid.UUID
    name: str = None
    type: Optional[str] = 'unknwon'
    label: Optional[str] = 'unknwon'


# Properties to receive via API on creation
class DeviceCreate(DeviceBase):
    customer_id: Optional[uuid.UUID] = None


# Properties to receive via API on update
class DeviceUpdate(DeviceBase):
    pass


class DeviceInDBBase(DeviceBase):
    id: Optional[uuid.UUID] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Device(DeviceInDBBase):
    device_credential: Union[List[DeviceCredentialInDBBase], None]


# Additional properties stored in DB
class DeviceInDB(DeviceInDBBase):
    pass
