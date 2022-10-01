from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from starlette.status import HTTP_403_FORBIDDEN
from sqlalchemy.orm import Session
from app import crud, models
import uuid

from .deps import get_db

API_KEY_NAME = "access_token"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)

api_keys = [
    "akljnv13bvi2vfo0b0bw"
]  # This is encrypted in the database

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
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


async def api_key_auth(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
    api_key_cookie: str = Security(api_key_cookie),
    db: Session = Depends(get_db)
) -> models.DeviceCredential:
    api_key = get_api_key(api_key_query, api_key_header, api_key_cookie)
    device_id_hex, credential_id = api_key.split(':')
    device_id = uuid.uuid4(device_id_hex)
    device_credential = crud.device_credential.get_by_id(db=db, id=device_id)
    if device_credential.credentials_id == credential_id:
        return device_credential
    raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Device credential_id is not valid with device_id"
        )
