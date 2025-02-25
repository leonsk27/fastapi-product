
from datetime import datetime, timezone
from sqlmodel import Column, DateTime, Field, SQLModel
from typing import Optional
class Task(SQLModel, table=True):
    '''
    Task model that represents a task in the database.
    '''
    id: Optional[int] = Field(default=None, primary_key=True, description="The primary key")
    title: str = Field(default=None, description="The title of the task")
    description: Optional[str] = Field(default=None, description="The description of the task")
    completed: bool = Field(default=False, description="The completion status of the task")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=True),
        description='The timestamp when the task was created'
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), 
            onupdate=lambda: datetime.now(timezone.utc), 
            nullable=True
        ),
        description='The timestamp when the task was last updated'
    )