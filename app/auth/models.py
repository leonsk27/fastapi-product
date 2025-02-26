from sqlmodel import Field, Column, DateTime
from datetime import datetime
from typing import Optional
from app.models.base_model import BaseModel
from app.util.datetime import get_current_time

class User(BaseModel, table=True):
    
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    is_verified: bool = Field(default=False)
    password_hash: str = Field(exclude=True)
    
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
class UserRevokedToken(BaseModel, table=True):
    __tablename__ = "user_revoked_token"
    token: str = Field(index=True, unique=True)
    user_id: int = Field(index=True)
    revoked_at: Optional[datetime] = Field(
        default_factory=get_current_time,
        sa_column=Column(DateTime(timezone=False), nullable=True),
        description="The timestamp when the token was Revoked"
    )