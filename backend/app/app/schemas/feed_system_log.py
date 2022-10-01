from datetime import datetime
from typing import Optional, Union
import uuid, time
from pydantic import BaseModel, Json, FiniteFloat


# Shared properties
class SystemLogFeed(BaseModel):
    sent_timestamp: FiniteFloat = time.time()
    device_id: uuid.UUID
    type: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "sent_timestamp": 1664522749.846137,
                "device_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "type": "temprature",
                "data": "{\"DataType\":\"TrackRadarList\",\"SamanehID\":\"template1\",\"TrackRadar\":{\"setting\":{\"CenterCoords\":[48,37],\"TR_Radius\":600,\"TR_Azimuth_xy\":0,\"TR_Azimuth_z\":0,\"TR_SectorWidth_xy\":100,\"TR_SectorWidth_z\":100}},\"RadarList\":[]}"
            }
        }
    


# Shared properties
class SystemLogFeedCreate(SystemLogFeed):
    data: Json

class SystemLogFeedOut(SystemLogFeed):
    message: str = 'Data added successfully'
    status: str = 'ok'
    pass
