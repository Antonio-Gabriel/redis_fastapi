from typing import Optional
from redis_om import HashModel

from src.config.redis_config import redis_db


class Task(HashModel):
    name: str
    complete: Optional[bool] = 0

    class Meta:
        database = redis_db
