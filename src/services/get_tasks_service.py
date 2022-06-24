from src.models.Task import Task


def get_tasks_service():
    return Task.all_pks()
