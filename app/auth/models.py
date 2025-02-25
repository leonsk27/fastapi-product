from sqlmodel import SQLModel, Field, Column, DateTime
from datetime import datetime, timezone
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, description="The primary key")
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    is_verified: bool = Field(default=False)
    password_hash: str = Field(exclude=True)
    
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