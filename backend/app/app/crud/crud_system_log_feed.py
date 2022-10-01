from typing import Any, Dict, Optional, Union
from fastapi import Security, Depends, FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorCollection
import uuid
from app.schemas.feed_system_log import SystemLogFeed, SystemLogFeedCreate

from app.api.api_v1.deps import api_key
from app import models


async def add_log_to_mongo(
        collection: AsyncIOMotorCollection, 
        obj_in: SystemLogFeedCreate,
        device_credential : models.DeviceCredential = Depends(api_key.api_key_auth)) -> SystemLogFeed:
    device = device_credential.device
    if device.external_device_id != uuid.uuid4(obj_in.device_external_id):
        raise HTTPException(status_code=403, detail='device external id is not compatibale with api_token')
    obj = await collection.insert_one(obj_in.dict())
    return obj





