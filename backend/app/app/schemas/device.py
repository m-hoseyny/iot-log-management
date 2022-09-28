from typing import Optional
import uuid
from pydantic import BaseModel


# Shared properties
class DeviceBase(BaseModel):
    name: str = None
    type: Optional[str] = 'unknwon'
    label: Optional[str] = 'unknwon'
    external_id: Optional[uuid.UUID] = uuid.uuid4()


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
    pass


# Additional properties stored in DB
class DeviceInDB(DeviceInDBBase):
    pass
