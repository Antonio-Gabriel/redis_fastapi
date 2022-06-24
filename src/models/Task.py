from redis_om import HashModel

from src.config.redis_config import redis_db


class Task(HashModel):
    name: str
    complete: bool

    class Meta:
        database = redis_db
