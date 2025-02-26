
from fastapi import APIRouter, status, Depends

from app.core.db import SessionDep
from .models import Customer
from .schemas import CustomerCreate, CustomerUpdate
from .service import CustomerService
from app.auth.utils import get_current_user
from app.models.user import User

router = APIRouter()
service = CustomerService()


# CREATE - Crear una nueva tarea
# ----------------------
@router.post("/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(
    customer_data: CustomerCreate,
    session: SessionDep,
    current_user: User = Depends(get_current_user)
    ):
    return service.create_customer(customer_data, session)
# GET ONE - Obtener una tarea por ID
# ----------------------
@router.get("/{customer_id}", response_model=Customer)
async def get_customer(
    customer_id: int,
    session: SessionDep
):
    return service.get_customer(customer_id,session)

# UPDATE - Actualizar una tarea existente
# ----------------------
@router.patch("/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def update_customer(
    customer_id: int,
    customer_data: CustomerUpdate,
    session: SessionDep
):
    
    return service.update_customer(customer_id, customer_data, session)

# GET ALL TASK - Obtener todas las tareas
# ----------------------
@router.get("/", response_model=list[Customer])
async def get_customers(
    session: SessionDep,
    current_user: User = Depends(get_current_user)
):
    return service.get_customers(session)

# DELETE - Eliminar una tarea
# ----------------------
@router.delete("/{customer_id}")
async def delete_customer(
    customer_id: int,
    session: SessionDep,
):
    return service.delete_customer(customer_id, session)