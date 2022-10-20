from pydantic import BaseModel


class TodoItemBase(BaseModel):
  title: str
  description: str | None = None
  done: bool = False


class TodoItem(TodoItemBase):
  id: str
