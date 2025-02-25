
from fastapi import APIRouter, status

from app.db import SessionDep
from app.tasks.models import Task
from app.tasks import schemas
from app.tasks.service import TaskService

router = APIRouter()
service = TaskService()


# CREATE - Crear una nueva tarea
# ----------------------
@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: schemas.TaskCreate,
    session: SessionDep
    ):
    """
     Create a new task.
    """
    return service.create_task(task_data, session)
# GET ONE - Obtener una tarea por ID
# ----------------------
@router.get("/{task_id}", response_model=Task)
async def get_task(
    task_id: int,
    session: SessionDep
):
    """
    Get a task by ID.
    """
    return service.get_task(task_id,session)

# UPDATE - Actualizar una tarea existente
# ----------------------
@router.patch("/{task_id}", response_model=Task, status_code=status.HTTP_201_CREATED)
async def update_task(
    task_id: int,
    task_data: schemas.TaskUpdate,
    session: SessionDep
):
    """
    Update an existing task.
    """
    return service.update_task(task_id, task_data, session)

# GET ALL TASK - Obtener todas las tareas
# ----------------------
@router.get("/", response_model=list[Task])
async def get_tasks(
    session: SessionDep
):
    """
    Get all tasks.
    """
    return service.get_tasks(session)

# DELETE - Eliminar una tarea
# ----------------------
@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    session: SessionDep,
):
    """
    Delete a task by ID.    
    """
    return service.delete_task(task_id, session)