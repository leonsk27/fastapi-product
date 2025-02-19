from typing import Optional
from sqlmodel import Field, SQLModel
from app.products_category.schemas import ProductCategoryRead

class ProductBase(SQLModel):
    title: str = Field(default=None)
    price: int = 0
    description: Optional[str] = None
    image: Optional[str] = None
    category_id: Optional[int] = None

# Modelo para crear una nueva tarea (hereda de TaskBase)
class ProductCreate(ProductBase):
    pass
  
class ProductUpdate(SQLModel):
    title: Optional[str] = None
    price: Optional[int] = None
    description: Optional[str] = None
    image: Optional[str] = None
    category_id: Optional[int] = None

class ProductRead(ProductBase):
    id: int
    category: Optional[ProductCategoryRead] = None  # Relación con la categoría