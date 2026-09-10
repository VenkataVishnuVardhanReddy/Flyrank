# Task API

A simple CRUD API for managing a to-do list, built with FastAPI.

## Installation & Running

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

The server will start on `http://localhost:8000`.

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

## Example Request

```bash
curl -i http://localhost:8000/tasks/1
```

**Output:**
```
HTTP/1.1 200 OK
date: Thu, 10 Sep 2026 08:40:00 GMT
server: uvicorn
content-length: 47
content-type: application/json

{"id":1,"title":"Buy groceries","done":false}
```

## Interactive Documentation

FastAPI provides an automatic, interactive Swagger UI documentation page.
After starting the server, visit: **[http://localhost:8000/docs](http://localhost:8000/docs)**
