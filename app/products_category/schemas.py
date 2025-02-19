
from sqlmodel import Field, SQLModel

class ProductCategoryBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)

# Modelo para crear una nueva tarea (hereda de TaskBase)
class ProductCategoryCreate(ProductCategoryBase):
    pass

class ProductCategoryUpdate(ProductCategoryBase):
    pass
