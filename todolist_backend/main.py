from uuid import uuid4
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, get_db
from .models import Base, Todo
from .schemas import TodoItem

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.get("/todo")
async def get_todos(db: Session = Depends(get_db)):
  return db.query(Todo).all()


@app.get('/todo/{todo_id}')
async def get_todo(todo_id: str, db: Session = Depends(get_db)):
  return db.query(Todo).filter(Todo.id == todo_id).first()


@app.post('/todo')
async def create_todo(todo: TodoItem, db: Session = Depends(get_db)):
  todo = Todo(**todo.dict())
  db.add(todo)
  db.commit()
  db.refresh(todo)
  return todo
