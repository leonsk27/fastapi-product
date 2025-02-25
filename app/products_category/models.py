
from datetime import datetime, timezone
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel, Column, DateTime

if TYPE_CHECKING:
    from app.products.models import Product

class ProductCategory(SQLModel, table=True):
    """
    ProductCategory model that represents a product category in the database.
    """
    __tablename__ = "product_category"
    id: Optional[int] = Field(default=None, primary_key=True, description="The primary key")
    name: str = Field(default=None, description="The name of the product category")
    description: Optional[str] = Field(default=None, description="The description of the product category")

    products: List["Product"] = Relationship(back_populates="category")

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