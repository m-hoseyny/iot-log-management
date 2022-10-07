from app.models.device_credential import DeviceCredential
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi import Security, Depends, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN, HTTP_406_NOT_ACCEPTABLE
from app.db.redis import redis_client
from app import crud, models, schemas
import uuid, datetime, json

from .deps import get_db

API_KEY_NAME = "access_token"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # use token authentication

def get_api_key(
    api_key_query: str,
    api_key_header: str,
    api_key_cookie: str
):
    if api_key_query:
        return api_key_query
    elif api_key_header:
        return api_key_header
    elif api_key_cookie:
        return api_key_cookie
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="There is not API_KEY in sent request"
        )

def datetime_parser(dct):
    for k, v in dct.items():
        if isinstance(v, str) and v.endswith('+00:00'):
            try:
                dct[k] = datetime.datetime.fromisoformat(v)
            except:
                pass
    return dct


async def get_cache(credential_id):
    credentials = await redis_client.get(credential_id)

    if credentials:
        return json.loads(credentials, object_hook=datetime_parser)


async def set_cache(credential_id: str, data: dict):
    def serialize_dates(v):
        if isinstance(v, datetime.datetime):
            return v.isoformat()
        elif isinstance(v, uuid.UUID):
            print(str(v))
            return str(v)
        return v
    print(data)
    await redis_client.set(
        credential_id,
        json.dumps(data, default=serialize_dates),
    )
    return data

def validate_uuid(input):
    try:
        uuid.UUID(input)
        return True
    except:
        return False


async def get_credential_cache(credential_id_hex: str):
    cache_data = await get_cache(credential_id_hex)
    if cache_data:
        return cache_data
    db = next(get_db())
    device_credential = crud.device_credential.get_by_id(db=db, id=credential_id_hex)
    device_credential = schemas.DeviceCredential.from_orm(device_credential)
    dict_data = device_credential.dict()
    cache_data = await set_cache(credential_id_hex, dict_data)
    return cache_data


async def api_key_auth(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
    api_key_cookie: str = Security(api_key_cookie),
) -> models.DeviceCredential:
    api_key = get_api_key(api_key_query, api_key_header, api_key_cookie)
    if len(api_key.split(':')) != 2:
        raise HTTPException(
            status_code=HTTP_406_NOT_ACCEPTABLE, detail="access_token must be xxx:xxx format"
        )
    credential_id_hex, credentials_value = api_key.split(':')
    if not validate_uuid(credential_id_hex):
        raise HTTPException(
        status_code=HTTP_406_NOT_ACCEPTABLE, detail="in access_token, XXX:xxx, XXX must be UUID4"
        )
    credential_cache = await get_credential_cache(credential_id_hex)
    if credential_cache and credential_cache['credentials_value'] == credentials_value:
        return credential_cache
    raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="access_token is not valid (device_credential_value is not valid)"
        )
