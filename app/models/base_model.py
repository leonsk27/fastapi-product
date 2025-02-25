from sqlmodel import SQLModel, Field
from typing import Optional

class BaseModel(SQLModel):
    """
    Base model that includes common fields for all models.
    """
    id: Optional[int] = Field(default=None, primary_key=True, description="The primary key")
