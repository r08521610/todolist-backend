from uuid import uuid4
from fastapi import FastAPI

from todolist_backend.model import TodoItemBase, TodoItem

app = FastAPI()

todos: dict[str, TodoItem] = {}


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.get("/todo")
async def get_todos(done: bool | None = None):
  if done is not None:
    return list(filter(lambda item: item['done'] == done, list(todos.values())))
  return list(todos.values())


@app.get('/todo/{todo_id}')
async def get_todo(todo_id: str):
  return todos.get(todo_id, None)


@app.post('/todo')
async def create_todo(todo: TodoItemBase):
  todo = {'id': str(uuid4()), **todo.dict()}
  todos[todo['id']] = todo
  return todo


@app.put('/todo/{todo_id}')
async def update_todo(todo_id: str, todo: TodoItemBase):
  if todo_id in todos:
    todo = todos[todo_id] | todo.dict()
    todos[todo_id] = todo
    return todo
  return None


@app.delete('/todo/{todo_id}')
async def delete_todo(todo_id: str):
  if todo_id in todos:
    del todos[todo_id]
    return True
  return False
