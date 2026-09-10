from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    done: bool

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="The title of the task")

tasks = [
    Task(id=1, title="Buy groceries", done=False),
    Task(id=2, title="Read documentation", done=True),
    Task(id=3, title="Write code", done=False)
]

def get_next_id():
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def read_health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate):
    new_task = Task(id=get_next_id(), title=task_in.title, done=False)
    tasks.append(new_task)
    return new_task
