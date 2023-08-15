import enum
from pydantic import BaseModel
from typing import Optional


class TaskStatus(enum.Enum):
    TO_DO = 'todo'
    IN_PROCESS = 'in process'
    DONE = 'done'


class Task(BaseModel):
    title: str
    description: Optional[str]
    status: TaskStatus = TaskStatus.TO_DO


class TaskOut(Task):
    id: int


# class TaskPut(BaseModel):
#     title: Optional[str]
#     description: Optional[str]
#     status: Optional[TaskStatus]


class TaskPut(Task):
    __annotations__ = {k: Optional[v] for k, v in Task.__annotations__.items()}