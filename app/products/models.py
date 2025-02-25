from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship, Column, DateTime, SQLModel
from datetime import datetime, timezone

if TYPE_CHECKING:
    from app.products_category.models import ProductCategory
    from app.products_brand.models import ProductBrand

class Product(SQLModel, table=True):
    '''
    Product model that represents a product in the database.
    '''
    id: Optional[int] = Field(default=None, primary_key=True, description="The primary key")
    title: str = Field(default=None)
    price: int = 0
    description: Optional[str] = Field(default=None)
    category: Optional[str] = Field(default=None)
    image: str = Field(default=None)

    category_id: Optional[int] = Field(default=None, foreign_key="product_category.id")
    category: Optional["ProductCategory"] = Relationship(back_populates="products")

    brand_id: Optional[int] = Field(default=None, foreign_key="product_brand.id")
    brand: Optional["ProductBrand"] = Relationship(back_populates="products")
    
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

