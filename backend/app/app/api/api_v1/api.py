from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, utils, devices, device_credential

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])

api_router.include_router(devices.router, prefix="/devices", tags=["devices"])
api_router.include_router(device_credential.router, prefix="/device_credentials", tags=["device_credentials"])
