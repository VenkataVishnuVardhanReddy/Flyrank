from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
import sqlite3

app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing tasks.",
    version="1.0"
)

DB_FILE = "tasks.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL CHECK (done IN (0, 1))
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM tasks')
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO tasks (title, done) VALUES (?, ?)", [
            ("Buy groceries", 0),
            ("Read documentation", 1),
            ("Write code", 0)
        ])
    conn.commit()
    conn.close()

@app.on_event("startup")
def startup_event():
    init_db()

class Task(BaseModel):
    id: int
    title: str
    done: bool

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    done: Optional[bool] = None

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}
@app.get("/health")
def read_health():
    return {"status": "ok"}
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row["id"], "title": row["title"], "done": bool(row["done"])} for row in rows]

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail='{"error": "Task not found"}')
    return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}
@app.post("/tasks", status_code=status.HTTP_201_CREATED, response_model=Task)
def create_task(task_in: TaskCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, done) VALUES (?, ?)', (task_in.title, 0))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return {"id": task_id, "title": task_in.title, "done": False}
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    row = cursor.fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail='{"error": "Task not found"}')
    new_title = task_update.title if task_update.title is not None else row["title"]
    new_done = task_update.done if task_update.done is not None else bool(row["done"])
    cursor.execute('UPDATE tasks SET title = ?, done = ? WHERE id = ?', (new_title, int(new_done), task_id))
    conn.commit()
    conn.close()
    return {"id": task_id, "title": new_title, "done": new_done}

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    if cursor.fetchone() is None:
        conn.close()
        raise HTTPException(status_code=404, detail='{"error": "Task not found"}')
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return
