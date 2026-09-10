# Task API - SQLite Version

A simple CRUD API for managing a to-do list, built with FastAPI.
This version replaces the in-memory array with a real **SQLite database**.

## Why SQLite?
SQLite is a lightweight database that stores everything in a single file (`tasks.db`). 
It requires zero server setup, has no external dependencies, and perfectly demonstrates how data persists (survives restarts) without added complexity. 

## Installation & Running

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

The server will start on `http://localhost:8000`. The `tasks.db` database is created automatically upon startup.

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | API description |
| GET | `/health` | Health check |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{id}` | Get a specific task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Example SQL Query (Stage 4)

I manually opened `tasks.db` in DB Browser for SQLite and ran:
```sql
SELECT * FROM tasks WHERE done = 1;
```
It returned only the completed tasks, exactly as expected.

## Interactive Documentation

FastAPI provides an automatic, interactive Swagger UI documentation page.
After starting the server, visit: **[http://localhost:8000/docs](http://localhost:8000/docs)**
