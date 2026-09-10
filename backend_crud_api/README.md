# Task API - Containerized with Docker & PostgreSQL

A simple CRUD API for managing a to-do list, built with FastAPI.
This version replaces the SQLite database with a real **PostgreSQL database** running inside a **Docker container**.

## Why PostgreSQL and Docker?
Using Docker removes "works on my machine" issues. The PostgreSQL database is run in a throwaway container that behaves identically everywhere, and a mounted volume ensures data persistence across restarts. We use a `.env` file to keep secrets out of Git.

## Installation & Running

1. Clone the repository and navigate to this directory.
2. Copy the example environment variables:
   ```bash
   cp .env.example .env
   ```
3. Run the entire stack (API + Database) with one command:
   ```bash
   docker compose up
   ```

The API server will start on `http://localhost:3000`.

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | API description |
| GET | `/health` | Health check (verifies DB connection) |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{id}` | Get a specific task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Example Request

```bash
curl -i http://localhost:3000/tasks/1
```

## Interactive Documentation

FastAPI provides an automatic, interactive Swagger UI documentation page.
After starting the stack, visit: **[http://localhost:3000/docs](http://localhost:3000/docs)**
