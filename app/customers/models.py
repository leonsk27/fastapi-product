
from datetime import datetime, timezone
from sqlmodel import Column, DateTime, Field, SQLModel
from typing import Optional
from pydantic import EmailStr
class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, description="The primary key")
    name: str = Field(default=None)
    last_name: str | None = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr = Field(default=None)
    age: int = Field(default=None)
    
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=True),
        description="The timestamp when the data was created"
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), 
            onupdate=lambda: datetime.now(timezone.utc), 
            nullable=True
        ),
        description="The timestamp when the data was last updated"
    )