from pydantic import BaseModel

class CategoryImage(BaseModel):
    id: int
    img: str

class Category(CategoryImage):
    title: str
    rules: str
    not_take: str | None = None
