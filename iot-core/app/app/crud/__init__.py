from .crud_user import user
from .crud_device import device
from .crud_device_credential import device_credential
from .crud_system_log_feed import add_log_to_mongo, add_to_redis_for_logstash

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
