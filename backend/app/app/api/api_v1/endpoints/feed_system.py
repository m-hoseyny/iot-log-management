from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorCollection

from app import crud, models, schemas
from app.api.api_v1.deps import api_key, deps

router = APIRouter()


@router.post("/", response_model=schemas.SystemLogFeedOut)
async def ingest_system_log(
    *,
    collection: AsyncIOMotorCollection = Depends(deps.get_mongo_logs_collection),
    obj_in: schemas.SystemLogFeedCreate,
    device_credential=Depends(api_key.api_key_auth)
) -> Any:
    """
    Ingest System Log.
    """
    obj = crud.add_log_to_mongo(collection=collection, obj_in=obj_in)
    print(obj)
    return obj_in


