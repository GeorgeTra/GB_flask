"""Задание №7
Создать RESTful API для управления списком задач. Приложение должно
использовать FastAPI и поддерживать следующие функции:
○ Получение списка всех задач.
○ Получение информации о задаче по её ID.
○ Добавление новой задачи.
○ Обновление информации о задаче по её ID.
○ Удаление задачи по её ID.
Каждая задача должна содержать следующие поля: ID (целое число),
Название (строка), Описание (строка), Статус (строка): "todo", "in progress",
"done"."""


import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models import Task, TaskOut, TaskPut


app = FastAPI()

tasks: dict[int, Task] = {i: Task(title=f'task{i}', description=f'description task {i}') for i in range(5)}


@app.get('/tasks/{task_id}', response_model=TaskOut, tags=['Task'], summary='Get task by id')
async def task_get(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Not Found")
    return TaskOut(id=task_id, **tasks[task_id].dict())


@app.get('/tasks', response_model=list[TaskOut], tags=['Task'], summary='Get all tasks')
async def task_get_all():
    return [TaskOut(id=k, **v.dict()) for k, v in tasks.items()]


@app.post('/tasks', response_model=TaskOut, tags=['Task'], summary='Add new task')
async def task_post(task: Task):
    next_task_id = max(tasks.keys()) + 1
    tasks[next_task_id] = task
    return TaskOut(id=next_task_id, **tasks[next_task_id].dict())


@app.put('/tasks', response_model=TaskOut, tags=['Task'], summary='Update task by id')
async def task_put(task_id: int, task_update: TaskPut):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Not Found")

    task.title = task_update.title or task.title
    task.description = task_update.description or task.description
    task.status = task_update.status or task.status
    return TaskOut(id=task_id, **tasks[task_id].dict())


@app.delete('/tasks', tags=['Task'], summary='Delete task by id')
async def task_delete(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Not Found")
    tasks.pop(task_id)


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
