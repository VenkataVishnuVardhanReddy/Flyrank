from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
import psycopg
from psycopg.rows import dict_row
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Task API",
    description="A simple CRUD API for managing tasks, backed by PostgreSQL in Docker.",
    version="1.0"
)

def get_db_connection():
    db_url = os.environ.get("DATABASE_URL", "postgres://postgres:dev@localhost:5432/tasks")
    return psycopg.connect(db_url, row_factory=dict_row)

def init_db():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS tasks (
                        id SERIAL PRIMARY KEY,
                        title TEXT NOT NULL,
                        done BOOLEAN NOT NULL DEFAULT FALSE
                    )
                ''')
                cursor.execute('SELECT COUNT(*) AS count FROM tasks')
                row = cursor.fetchone()
                if row["count"] == 0:
                    cursor.execute("INSERT INTO tasks (title, done) VALUES (%s, %s)", ("Buy groceries", False))
                    cursor.execute("INSERT INTO tasks (title, done) VALUES (%s, %s)", ("Read documentation", True))
                    cursor.execute("INSERT INTO tasks (title, done) VALUES (%s, %s)", ("Write code", False))
            conn.commit()
    except Exception as e:
        print("Database not ready yet or connection failed:", e)

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

@app.get("/", summary="Root Endpoint")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health", summary="Health Check")
def read_health():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
        return {"status": "ok", "db": "connected"}
    except:
        return {"status": "ok", "db": "disconnected"}

@app.get("/tasks", response_model=List[Task], summary="List Tasks")
def get_tasks():
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM tasks')
            return cursor.fetchall()

@app.get("/tasks/{task_id}", response_model=Task, summary="Get Task")
def get_task(task_id: int):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
            row = cursor.fetchone()
            if row is None:
                raise HTTPException(status_code=404, detail='{"error": "Task not found"}')
            return row

@app.post("/tasks", status_code=status.HTTP_201_CREATED, response_model=Task, summary="Create Task")
def create_task(task_in: TaskCreate):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO tasks (title, done) VALUES (%s, %s) RETURNING *', (task_in.title, False))
            new_row = cursor.fetchone()
        conn.commit()
        return new_row

@app.put("/tasks/{task_id}", response_model=Task, summary="Update Task")
def update_task(task_id: int, task_update: TaskUpdate):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
            row = cursor.fetchone()
            if row is None:
                raise HTTPException(status_code=404, detail='{"error": "Task not found"}')
            
            new_title = task_update.title if task_update.title is not None else row["title"]
            new_done = task_update.done if task_update.done is not None else row["done"]
            
            cursor.execute('UPDATE tasks SET title = %s, done = %s WHERE id = %s RETURNING *', (new_title, new_done, task_id))
            updated_row = cursor.fetchone()
        conn.commit()
        return updated_row

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Task")
def delete_task(task_id: int):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM tasks WHERE id = %s RETURNING id', (task_id,))
            if cursor.fetchone() is None:
                raise HTTPException(status_code=404, detail='{"error": "Task not found"}')
        conn.commit()
        return
