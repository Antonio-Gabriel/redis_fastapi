from src.models.Task import Task


def get_tasks_service():

    return [format_task_service_response(pk) for pk in Task.all_pks()]


def format_task_service_response(pk: str):
    task = Task.get(pk)

    return {"id": task.pk, "name": task.name, "complete": task.complete}
