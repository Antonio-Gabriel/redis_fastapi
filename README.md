# Todo app

Application developed for explore the resources of redisJson and redisCache using fastapi

## How to run the app

Create a virtualenv and run this command in your terminal

```bash
pip install -r requirements.txt
```

## Endpoints

The available routes for use are

### Tasks

- [GET] http://127.0.0.1:8000/tasks

- Response 200 (application/json)

  - Body

        {
            "id": "01G6AWS23CNW3B999HNM8DP63Z",
            "name": "Aprendendo redis na prática usando fastapi",
            "complete": false
        }

### Create todo

- [POST] http://127.0.0.1:8000/tasks

- Request (application/json)

  - Body

        {
            "name": "Learning about redisJson",
        }

- Response 200 (application/json)

  - Body

        {
            "id": "01G6AWS23CNW3B999HNM8DP63Z",
            "name": "Aprendendo redis na prática usando fastapi",
            "complete": false
        }

### Mark done or undone task

- [PATCH] http://127.0.0.1:8000/tasks/{pk}

- Request (application/json)

  - Body

        {
            "complete": 1,
        }

- Response 200 (application/json)

  - Body

        {
            "pk": "01G6AWS23CNW3B999HNM8DP63Z",
            "name": "Aprendendo redis na prática usando fastapi",
            "complete": true
        }
    
### Remove task

- [DELETE] http://127.0.0.1:8000/tasks/{pk}


## Feactures


- [x] Create tasks
- [x] Mark done and undone
- [x] Get tasks

## License
The redis_fastapi is licensed under the MIT license.