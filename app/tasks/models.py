
from datetime import datetime
from sqlmodel import Column, DateTime, Field
from typing import Optional
from app.models.base_model import BaseModel, get_current_time

class Task(BaseModel, table=True):
    """
    Task model that represents a task in the database.
    """
    # id: Optional[int] = Field(default=None, primary_key=True, description="The primary key")
    title: str = Field(default=None, description="The title of the task")
    description: Optional[str] = Field(default=None, description="The description of the task")
    completed: bool = Field(default=False, description="The completion status of the task")
    created_at: Optional[datetime] = Field(
        default_factory=get_current_time,
        sa_column=Column(DateTime(timezone=False), nullable=True),
        description="The timestamp when the data was created"
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=False), 
            onupdate=get_current_time, 
            nullable=True
        ),
        description="The timestamp when the data was last updated"
    )