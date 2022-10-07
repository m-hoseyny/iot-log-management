from aioredis import Redis, AuthenticationError
from app.core.config import settings
from typing import AsyncIterator


REDIS_URI = settings.REDIS_URI


redis_client = Redis().from_url(REDIS_URI)

