from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.env import *
from src.services import *

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
    return get_tasks_service()
