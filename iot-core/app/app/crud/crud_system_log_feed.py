from typing import Any, Dict, Optional, Union
from fastapi import Security, Depends, FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorCollection
import uuid, json
from app.schemas.feed_system_log import SystemLogFeed, SystemLogFeedCreate

from app.api.api_v1.deps import api_key
from app import models


async def add_log_to_mongo(
        collection: AsyncIOMotorCollection, 
        obj_in: SystemLogFeedCreate,
        device_credential : models.DeviceCredential) -> SystemLogFeed:
    obj_in = obj_in.dict()
    # obj_in['data'] = json.loads(obj_in['data'])
    obj = await collection.insert_one(obj_in)
    return obj





