from pydantic import BaseModel


class TodoItem(BaseModel):
  title: str
  description: str | None = None
  done: bool = False
