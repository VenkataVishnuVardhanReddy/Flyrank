from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing tasks.",
    version="1.0"
)

class Task(BaseModel):
    id: int
    title: str
    done: bool

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="The title of the task")

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    done: Optional[bool] = None

tasks = [
    Task(id=1, title="Buy groceries", done=False),
    Task(id=2, title="Read documentation", done=True),
    Task(id=3, title="Write code", done=False)
]

def get_next_id():
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1

@app.get("/", summary="Root Endpoint")
def read_root():
    """Returns basic information about the API."""
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health", summary="Health Check")
def read_health():
    """Returns the health status of the API."""
    return {"status": "ok"}

@app.get("/tasks", summary="List Tasks")
def get_tasks():
    """Returns a list of all tasks."""
    return tasks

@app.get("/tasks/{task_id}", summary="Get Task")
def get_task(task_id: int):
    """Returns a single task by ID."""
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.post("/tasks", status_code=status.HTTP_201_CREATED, summary="Create Task")
def create_task(task_in: TaskCreate):
    """Creates a new task."""
    new_task = Task(id=get_next_id(), title=task_in.title, done=False)
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", summary="Update Task")
def update_task(task_id: int, task_update: TaskUpdate):
    """Updates an existing task."""
    for i, task in enumerate(tasks):
        if task.id == task_id:
            if task_update.title is not None:
                task.title = task_update.title
            if task_update.done is not None:
                task.done = task_update.done
            tasks[i] = task
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Task")
def delete_task(task_id: int):
    """Deletes an existing task."""
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
