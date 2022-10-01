import motor.motor_asyncio
from app.core.config import settings

MONGO_DETAILS = settings.MONGO_SETTING_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

session = client.datalake
logs_collection = session.get_collection("logs_collection")