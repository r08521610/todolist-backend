from typing import List
from uuid import uuid4
from fastapi import FastAPI

from todolist_backend.model import TodoItemBase, TodoItem

app = FastAPI()

todos: List[TodoItem] = []


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.get("/todo")
async def get_todos(done: bool | None = None):
  if done is not None:
    return list(filter(lambda item: item['done'] == done, todos))
  return todos


@app.get('/todo/{todo_id}')
async def get_todo(todo_id: str):
  print(todos, todo_id)
  return next((item for item in todos if item['id'] == todo_id), None)


@app.post('/todo')
async def create_todo(todo: TodoItemBase):
  todo = {'id': str(uuid4()), **todo.dict()}
  todos.append(todo)
  return todo
