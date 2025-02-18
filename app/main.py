# main.py
from fastapi import FastAPI, HTTPException, status
from app.models import Task, TaskCreate
app = FastAPI()
# Base de datos en memoria (lista de tareas)
tasks = []
# Obtener todas las tareas
@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks
# Obtener una tarea por ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")
# Crear una nueva tarea
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    new_task = Task(id=len(tasks) + 1, **task.dict())
    tasks.append(new_task)
    return new_task

# Actualizar una tarea existente
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskCreate):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = Task(id=task_id, **updated_task.dict())
            return tasks[index]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")

# Eliminar una tarea
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")