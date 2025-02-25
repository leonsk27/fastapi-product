from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional
import pytz
from app.config import Config

# Define la zona horaria -4
timezone_app = pytz.FixedOffset(Config.TIME_ZONE * 60)

def get_current_time():
    return datetime.now(timezone_app).replace(tzinfo=None)

class BaseModel(SQLModel):
    """
    Base model that includes common fields for all models.
    """
    id: Optional[int] = Field(default=None, primary_key=True, description="The primary key")
