# models.py
from pydantic import BaseModel
from typing import Optional

# Modelo de entrada (al crear o actualizar una tarea)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Modelo para crear una nueva tarea (hereda de TaskBase)
class TaskCreate(TaskBase):
    pass

# Modelo de respuesta (incluye el ID de la tarea)
class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
        
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int