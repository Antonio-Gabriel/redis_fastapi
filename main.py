from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.env import *
from src.services import *

from src.models.Task import Task

from starlette.requests import Request

app = FastAPI()
app.title = "Redis App"
app.description = "Create a simple todo using regis and fastapi"

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def say_hello():
    return {"message": "Redis todo with fastapi, developed by António Gabriel"}


@app.get("/tasks")
async def get_tasks():
    """Get all tasks from redis"""

    return get_tasks_service()


@app.post("/tasks")
async def create(task: Task):
    """Save an new task"""

    return task.save()


@app.put("/tasks/{pk}")
async def update(pk: str, request: Request):
    """Update the task name"""

    task = Task.get(pk)
    parsed_body = await request.json()
    task.name = int(parsed_body["name"])

    # return task.save()
    return task.name


@app.patch("/tasks/{pk}")
async def complete(pk: str, request: Request):
    """Mark if the task is done or undone"""

    task = Task.get(pk)
    parsed_body = await request.json()
    task.complete = int(parsed_body["complete"])

    return task.save()


@app.delete("/tasks/{pk}")
async def delete(pk: str):
    """Delete the task"""

    return Task.delete(pk)
