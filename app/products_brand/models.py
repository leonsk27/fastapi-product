
from datetime import datetime, timezone
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Column, DateTime, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.products.models import Product
class ProductBrand(SQLModel, table=True):
    __tablename__ = "product_brand"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    description: str | None = Field(default=None)

    products: List["Product"] = Relationship(back_populates="brand")

    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=True)
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), 
            onupdate=lambda: datetime.now(timezone.utc), 
            nullable=True
        )
    )