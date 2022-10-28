from typing import Any, List

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, APIKeyHeader
from motor.motor_asyncio import AsyncIOMotorCollection

from app import crud, schemas
from app.api.api_v1.deps import api_key, deps

router = APIRouter()

auth_scheme = HTTPBearer()
auth_header1 = APIKeyHeader(name='X-SECRET-1', scheme_name='secret-header-1')
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
    obj = await crud.add_log_to_mongo(collection=collection, obj_in=obj_in, device_credential=device_credential)
    await crud.add_to_redis_for_logstash(obj_in=obj_in, device_credential=device_credential)
    return obj_in


